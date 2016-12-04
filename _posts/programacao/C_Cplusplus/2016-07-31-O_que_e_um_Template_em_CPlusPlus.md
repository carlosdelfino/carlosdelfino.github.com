---
title: "O que é um Template em C++"
tags: [Arduino, Curso, Shields, Modulos, Arduino Mega, Arduino Due, Arduino Uno, Lógica, Programação, FIFO, Algoritimos, Estrutura de Dados, Assembly, AVR, ATMega, ATTiny, ARM, STL, C++, Library, Biblioteca Padrão de Templates, Standart Template Library, SGI]
category: [cursoarduino, nivel_4]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
ads: 
 show: true
image:
   teaser: pensamentos/pensamento2-400x200.jpg
   feature: pensamentos/pensamento2-400x200.jpg
---

Templates um recurso amplamente utilizado em C++, sendo um dos grandes diferenciais da lingaugem. Veremos um pouco de sua história e como pode ser útil até mesmo no desenvolvimento de sistemas embarcados, e quais os mitos envolvidos que faz muitos desenvolvedores evita-lo.

<!--more-->

Como muitos sabém o C++ teve sua primeira versão desenvolvida em 1985 por [Bjarne Stroustru]({% post_url perfil/2016-08-01-Bjarne_Stroustru %}), e durante 25 anos ele a desenvolveu junto a ISO.

Bem, eu nasci na programação faz algum tempo, porém sempre passei a certa distância do C e C++ então nas linguagens que programava, como Clipper, Dataflex, e posteriormente o Java, não tive contato algum com algo que pudesse explicar bem o que era o template, sempre ouvi dizer que era um problema, que tornava o código pessado, e isso se deve ao fato que para muitos templates são dificeis de se implementar e entender, os compiladores são muito vagos em suas mensagens de erros, e houve uma época que o código gerado era muito redundante. E sinceramente hoje vejo que foi apenas uma fase do C++, onde os compiladores não conseguiam gerar um código muito otimizado, sem contar o preconceito de alguns com o recurso.

Para quem programa em Java, poderia dizer que Templates é similar a Generics, e na verdade o Generics do java foi inspirado neste conceito, e sua função é como o nome sugere criar código genérico.

Dentro do universo de Templates não temos o conceito de herança, mas sim refinamentos, já que lidamos com conceitos de algortimos, conceitos de funções, como já foi comentado no artigo ["Usando STL C++ LIB com o Arduino e Arquiteturas AVR"]({% post_url cursoarduino/programacao/nivel4/2016-07-30-Usando_STL_CPlusPlus_Lib_com_o_Arduino_e_Arquiteturas_AVR %}), o refinamento de um conceito trata da melhoria de seu algoritmo para que o algortimo anterior possa continuar com suas funcionalidades e atender novos requisitos, sem que insira incompátibilidade e possíveis bugs.

Os fatos envolvidos na construção de um template determinando requisitos para seu uso, como por exemplo que haja um certo número de parametros e estes parametros herdem de classes ou interfaces especificas.

O uso de template é muito restrito, e não se aplica a aplicações finais, pelo a não ser que seja necessário criar uma classe genérica, algo como um conteiner de classes de sua aplicação o que já torna esta classe mais especializada, mesmo que seja generica dentro de seu contexto, o ideal para se usar Templates é quando se cria classes genericas para uso em qualquer aplicação ou num contexto bastante amplo de uso, de forma que possa ser compartilhado com outros colegas.

Templates hoje são amplamente usado devido a biblioteca STL também explicada no post citado logo acima, graças ao templates é possível a criação de algoritmos genericos para operadores como no caso de usarmos o operador unário `++` em classes, ou mesmo o uso de pares `[` e `]` para acesso tanto em array do C como da mesma forma vetores, listas e mapas do C++ que são definidos no STL, e claro funções especiais como funções genericas para manipulação dos tipos de containers citados.

Abaixo podemos ver a sintaxe usada para definir um template para uma função simples:

```
   template <class InputIterator, class T>
      InputIterator find(InputIterator first, InputIterator last, const T& value) {
          while (first != last && *first != value) ++first;
          return first;
      }
```

Apasar do exemplo simples, já suficiênte para bugar a mente de um iniciante, veja eu definio com a diretiva `template` que a função a ser definida `find` é um template e que esta espera uma classe que chamaará `InputIterator` e outra classe que chamará `T`, mas é ai que se precisa ter muito cuidado, pois não se existe estas classes, são apenas nomes para que os parametros sejam generalizados, e assim tais classes sejam referenciadas onde elas devem ser usadas, com isso a classe que será identificada como InputIterator, será na verddade a realização da classe informada quando tal função for chamada, assim se tal função for chamada com parametros do tipo `int`ela irá ser a classe equivalente ao tipo `int`, e isso obriga que o retorno seja do mesmo tipo, e o segundo parametro também, perceberam como este tipo de estrutura de código ajuda a amarrar sem perder a generalização.

Desde que seja possível efetuar as oprações ali sugeridas pela função `find` tudo correrá bem, e com os compiladores atuais, tal código será otimizado tanto para melhoria de desempenho como para melhoria de seu tamanho, evitando códigos redudantes, basta usar as chaves corretas para compilação.

Na sitaxe para se definir um template também é permitido usar a palavra chave `typename`, quando Stroustru criou o C++ ele não queria criar uma nova palavra chave, e reutilizou class, porem isso trouxe uma complexidade em certos casos, não etraremos em detalhes aqui, mas veja que de qualquer forma fica bem mais claro quando substituimos a diretiva `class` para `typename`:

```
   template <typename InputIterator, typename T>
      InputIterator find(InputIterator first, InputIterator last, const T& value) {
          while (first != last && *first != value) ++first;
          return first;
      }
```

Portanto, fica claro que `InputIterator` é o nome para um local onde haverá substituição do tipo para o que será informado quando a função for chamada, e assim também para `T`.

Quem usa **Generics** em java, pode ficar tentando a perguntar como usar templates com curinga `?`, já de imediato digo que não é necessário, todo template é um curinga como no Generics do java, e se eu quiser limitar a um determinado grupo de classes pertencentes a uma determinada hierarquia? bem neste caso é bem mais complexo e varia bastante o código necessário entre o C11 e C14, portanto não vou entrar nesta questão aqui, realmente isso daria um novo post, quem sábe no futuro?

E qual o problema relativo a queixa de códigos ficarem maiores com o uso de Templates do C++, isso é verdade? Veremos isso na publicação "[O mito que impede o uso de templates em sistemas embarcados]({% post_url cursoarduino/programacao/nivel4/2016-07-31-O_Mito_que_Impede_o_Uso_de_Templates_Em_Sistemas_Embarcados %}).

------

## Fontes: 

* https://en.wikipedia.org/wiki/Standard_Template_Library
* http://www.cplusplus.com/info/history/
* https://blog.feabhas.com/2014/05/an-introduction-to-c-templates/
* http://www.codeproject.com/Articles/257589/An-Idiots-Guide-to-Cplusplus-Templates-Part-1
* http://www.cprogramming.com/tutorial/templates.html
* http://www.stroustrup.com/hopl2.pdf
