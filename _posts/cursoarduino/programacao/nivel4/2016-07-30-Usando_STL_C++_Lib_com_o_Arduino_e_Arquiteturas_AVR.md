---
title: "Usando STL C++ Lib com o Arduino e Arquiteturas AVR"
tags: [Arduino, Curso, Shields, Modulos, Arduino Mega, Arduino Due, Arduino Uno, Lógica, Programação, FIFO, Algoritimos, Estrutura de Dados, Assembly, AVR, ATMega, ATTiny, ARM, STL, C++, Library, Biblioteca Padrão de Templates, Standart Template Library, SGI]
category: [cursoarduino, nivel_4]
layout: article
share: true
toc: true
comments: true
feature:
  category: true
ads: 
 show: true
image:
  teaser: logica_programacao/fluxograma_planejamento-300x199.jpg
  feature: logica_programacao/fluxograma_planejamento-300x199.jpg
  credit: Carlos Delfino 
  creditlink: 
---
Diante do amadurecimento de projetos e a demanda de bibliotecas mais avançadas para lidar com coleções de dados e comunicação mais complexa via rede, me deparei com a necessiadde de uso de containers como Vetores e Maps, porém o GCC para AVR não possui a biblioteca padrão de templates que nos permite tal uso.

<!--more-->

Diante disso me vi com a necessidade de encontrar uma alternativa, ao pesquisar a internet achei um desenvolvedor que está mantendo um projeto com base na implementação da SGI do STL, esta implementação conforme seus argumentos tem um consumo de memória muito eficiente, sendo que a outra opção mais próxima tem tem um consumo 70% maior.

Com base na introdução apresentada no site http://www.sgi.com/tech/stl/stl_introduction.html e o trabalho de [Andy Brown](http://andybrown.me.uk/2011/01/15/the-standard-template-library-stl-for-avr-with-c-streams/) que adaptou a versão SGI STL para AVR,  apresento o inicio do trabalho com uma nova biblioteca e a construção da mesmma para uso com o Arduino, já que Andy Brown, sugere que esta biblioteca seja depositada dentro da pasta do core, o que não acredito ser uma boa prática, então estarei adaptando a mesma para uso externo como uma Biblioteca do Arduino.

O texto abaixo é a tradução livre da [Introdução ao STL da SGI](http://www.sgi.com/tech/stl/stl_introduction.html), e pela explicação sobre o STL da SGI introduz muito bem o que é o STL e seu beneficio, em caso de dúvida no final da página você poderá apresenta-la assim amadureço o texto de forma a amadurecer eventuais pontos que tenha ficado pouco claro.

## Introdução à Biblioteca Padrão de Template

A Biblioteca Padrão de Template, ou STL da seu nome em inglês "Standart Template Library", é uma biblioteca do C++ para classes de containers, algortimos e interators; ela prové a maioria dos algorimos basicos e struturas de dados para ciência de computador. O STL é uma biblioteca generica, de forma que seus componentnes são fortemente parametrizados: a maioria dos componentes do STL são templates. Você precisa se grantir que entende bem o que são templates no C++ antes de usar STL, para isso aomenos leia antes o artigo [O que é um Template em C++]({% post_url 2016-07-31-O_que_e_um_Template em_C++.md %}).


## Containers e algoritmos

Como muitas bibliotecas de classes, o STL inclue classes de containers: Classe no qual o proposito é conter outro objetos. o STL inclue como vector, list, deque, set, multiset, map, multimap, hash_set, hash_multiset, hash_map e hash_multimap. cada uma destas classes é um template, e pode ser instanciado para conter algum tipo de objeto, você pode, por exemplo, usar um vector<int> da mesma forma que você usa um array no C, exceto que o vetor elimina a necessidade de gerenciamento da memória dinâmica manualmente.

```
      vector<int> v(3);            // Declare a vector of 3 elements.
      v[0] = 7;
      v[1] = v[0] + 3;
      v[2] = v[0] + v[1];          // v[0] == 7, v[1] == 10, v[2] == 17  
```

O STL também inclui uma larga coleção de algoritmos que manipulam os dados armazenados em containers, você pode reverter a ordem de elementos em um vetor, por exemplo, usando o algoritmo `reverse`.

```
      reverse(v.begin(), v.end()); // v[0] == 17, v[1] == 10, v[2] == 7
```

Há dois pontos importantes sobre esta chamada ao `reverse`. Primeiro, ele é uma função global, não é uma função membro de uma classe. Segundo, ele recebe dois argumentos ao invez de um: ele opera sobre uma faixa de elementos, ao invez de um container. Neste caso particular a faixa deve cobrir o container `v` como um todo.

a razão para isso é que, como outros algortimos em STL, ele é desacoplado de outras classes containers. Este significa que `reverse` pode ser usado não apenas com a reversão de elementos em vetores, mas também reverter elementos em listas, e cada elemento em um array em C. O seguinte programa também é valido.

```
      double A[6] = { 1.2, 1.3, 1.4, 1.5, 1.6, 1.7 };
      reverse(A, A + 6);
      for (int i = 0; i < 6; ++i)
        cout << "A[" << i << "] = " << A[i];
```

O exemplo usado como faixa, é exatamente como o exemplo que reverte o vetor: o primeiro argumento para reveter é o ponteiro para o inicio da faixa, e o segundo ergumento aponta para um elemento após o ultimo elemento da faixa. Esta faixa é denominada como `A, A + 6`; a assimetrica notação é uma lembrança que os dois pontos são diferentes, que o primeiro é o inicio da faixa e o segundo é um após o fim da faixa.

## Iterators

No exemplo de reversão do Array C, o argumento para `reverse`são claramente do tipo `double*`. Quais são os argumentos para `reverse`se você está revertendo um `vector`, ou mesmo um `list`? Isto é, o que exatamente faz `reverse` declarar seus argumento como são, e o que exatamente faz `v.begin()` e `v.end()` retornar?.

A resposta é que os argumentos para `reverse` são `interators`, que são uma generalização dos ponteiros. Ponteiros são por si mesmo interators, por isso é que é possível reverter os elementos de um array em C. De forma similar, `vector`delcara um tipo `iterator` interno e um `const_iterator`. No exemplo acima, o tipo retornado por `v.begin()^ e `v.end()` é `vector<int>::iterator`. Há também alguns Iterators,  tais como `istream_iterator` e òstream_iterator`, que não são associados a nenhum container.

Iterators são um mecanismo que torna possível desacoplar algoritmos dos containers: algortimos são templates, e são parametrizados para o tipo do iterator, porém não são restritos a um tiplo simples de container. Considere, por exemplo, como escrever um algoritmo que executa uma pesquisa linear atrav´pes de um faixa. Este é o algrotimo de busca STL.

```
      template <class InputIterator, class T>
      InputIterator find(InputIterator first, InputIterator last, const T& value) {
          while (first != last && *first != value) ++first;
          return first;
      }
```
O `find` espera três argumentos: dois iterators que define a faixa, e um valor para ser pesquisado dentro da faixa. Ele examina cada iterator na faixa [first, last], partindo do início  até o fim, e parando quando ele encontra um iterator que aponta para o valor ou quando ele chega ao final da faixa.

`first` e `last` são declarados  como do tipo `InputIterator`, e `InputIterator` é um parametro do tipo template. Isto é, não há na verdade algum tipo chamado `inputIterator`: quando você chama `find`, o compilador substitui o atual tipo do argumento pelo o tipo formal dos parametros `InputIterator` e `T`. se os dois primeiros argumentos para o `find` são do tipo `int*` e o terceiro é do tipo `int`, então é como se você tivesse chamado a função:

```
      int* find(int* first, int* last, const int& value) {
          while (first != last && *first != value) ++first;
          return first;
      }
```	  

## Conceitos e Modelagem

Uma pergunta muito importante a ser feita sobre qual a função do template, não exatamente sobre algortimos do STL, é qual o conjunto de tipos que pode ser corretamente substituito para um parametro formal do template. Esclarecendo, por exemplo, `int*`ou `double*`pode ser substituido por parametros formais do tipo `InputIterator` do `find` . Igualmente, `int` ou `double` não pode: `find` usa a expressão `*first`, e o operador de referência do ponteiro não faz sentido para um objeto do tipo `int` ou do tipo `double`. A resposta simples, então , é que `find` define de forma implicita um conjunto de requerimentos nos tipos, e que ele pode ser instanciado com algum tipo que satisfaz estes requisitos. Portanto, o tipo é substituido por `InputStream` que fornece certos tipos de operações: deve ser possível comparar dois objetos conforme a igualdade de seu tipo, deve ser possível incrementar um objeto deste tipo, deve ser possível fazer referência pelo ponteiro de um objeto do tipo obtido pleo objeto que ele aponta, e assim por diante.

`find` não é o unico algortimo do STL que tem tal conjunto de requisitos; os argumentos do `for_each` e do `count`, e outros algortimos, devem satisfazer os mesmos requisitos. Estes requisitos são suficientemente importantes para que nos demos então um nome: nos chamaos tais conjuntos de requisitos de "Conceito", e nos chamamos este conceito em particular de **Input Iterator** porque `int*` fornece todo as operações que são especificadas pelos requisitos do **Input Iterator**.

**Conceitos** não parte da linguagem C++; eles são uma forma de declarar um conceito em um programa, ou declarar que um tipo particular é um modelo de um conceito. Mesmo assim, conceios são uma parte extremamente importante do STL. Usando conceitos torna possível escrevre programas que claramente separam interfaces de implementação: o autor do algorimo `find` somente tem de considerar a interface especificada pelo conceito **Input Iterator**. ao invez de da implementação  de cada tipo possível conforme cada conceito. Similarmente, se você deseja usar `find`, você precisa somente se assegurar que os argumentos que você passa para ele são do modelo **Input Iterator**. Esta é a razão que `find` e `reverse` podem ser usada com `list`s, `vector`s, arrays em C, e muitos outros tipos: programando em termos de **conceitos**, ao invez de termos de tipos especificos torna possível reutilizar o componente de software e então combinar componentes conjuntamente.


# Refinamentos

**Input Iterator** é, de fato, um fraco conceito: isto é, ele impõem alguns requisitos. Um **Input Iterator** deve suportar um subconjunto da aritimética de ponteiros (ele deve ser possível incrementar um **Input Iterator** usando o perador ++ prefixado ou pósfixado), mas não precisa suportar todos os peradroes de aritimética de ponteiros. Isto é suficiente para o `find`, mas alguns outros algortimos requerem que seus argumentos satisfaça requisitos adicionais. `reverse`, por exemplo, deve ser apto a decrementar seus argumentos também e incrementa-los; ele usa a expressão `--last`. Em termos de conceito, nos dizemos que os argumentos do `reverse` devem ser modelos de um **Bidirectional Iterator** ao invez de um **Input Iterator**.

O conceito **Bidirectional Iterator** é muito similar ao conceito **Input Iterator**: ele simplesmente impõem alguns requisitos adicionais. Os tipos que são modelos do **Bidirectional Iterator** são um subconjunto dos tipos que são modelos para o **Input Iterator**: cada tipo que é um modelo do **Bidirectional Iterator** é também um modelo do **Iterator**. `int*`, por exemplo, é ambo um modelo para **Bidirectional Iterator** e um modelo para **Input Iterator**, mas `istream_iterator`, é somente um modelo de `input iterator`: ele não atende os requisitos mais rigorosos do **Bidirectional Iterator**.

Nos descrevemos a relalação entre Input Iterator e Bidirectional Iterator dizendo que **Bidirectional Iterator** é um refinamento de **Input Iterator**. Refinamentos de conceitos é muito parecido com erança de classes em C++; a principal razão para nós usarmos uma palavra diferente, ao invez de simplesmente dizer que é uma "erança", é enfatizar que o refinamento se aplica a conceitos ao invez de se aplicar ao tipo em questão.

Há atualmente três outros conceitos de interator em adição aos dois que nos temos já discutidos aqui: Os cinco interators são **Output Iterator**, **Input Iterator**, **Forward Iterator**, **Bidirectional Iterator**, e **Rando Access Iterator**; **Forward Iterator** é o refinamento do *Input Iterator**, **Bidirectional Iterator** é um refinamento de **Forward Iterator**, e **Random Access Iterator** é um refinamento de **Bidirectional Iterator**. (**Output Iterator** é relacionado a outros 4 conceitos, mas ele não é parte da hieraquia de refinamentos: ele não é um refinamento de nenhum dos outros conceitos de iterator, e nenhum dos outros conceitos de interator são refinamentos dele). Na página [Iterator Overview](http://www.sgi.com/tech/stl/Iterators.html) há mais informações sobre iterator em geral.

Classes Containers, como iterators, são organizadas em uma hieraquia de conceitos. Todos os conteiners são modelos de conceitos de Conteiners; Conceitos mais refinados, tais como uma **Sequence** e um **Associative Container**, descreve tipos especificos de conteiners.

## Outras partes do STL

Se você entendeu algortimos, iterators e conteriners, então você entendeu práticamente tudo que há para se conhecer sobre STL. O STL , porém, inclui varios outros tipos de componentes.

Primeiro, o STL inclui varios utilitários: conceitos muito básicos e funções que são usadas em diferentes partes da biblioteca. O conceito **Assignable**, por exemplo, descreve tipos que ~tem operadores de atribuição e construtores de cópia; na maioria das classes STL são modelos de **Assignable**, e a maioria dos algortimos exigem que seus argumentos sejam modelos de **Assignable**.

Segundo, o STL inclue alguns mecanismos de baixo nível para alocação de desalocação de memória. **Allocators** são muito especializados, e você pode seguramente ignorar para alguns todos os propositos.

Finalmente, o STL inclue uma grande coleção de objetos de função, também conhecidos como **functors**. Exatamente como iterators são generalizações de ponteiros. objetos de função são generalizações de funções: um objeto de função é qualquer coisa que você possa chamar usando um sintaxe ordinária de função. Há vários conceitos diferentes relacionados a objetos de função, incluindo **Unary function** (um objeto de função que recebe apenas um parametro, por exemplo, os que são chamados  como `f(x)`) e **Binary Function** (um objeto de função que recebe dois argumentos, por exemplo os que são chamados como `f(x, y)). Objetos de função  são uma parte importante da programação com genericos (Generic Programming) porque eles são abstrações não apenas sobre tipos de objetos, mas também sobre operações que estão sendo executadas.
 
