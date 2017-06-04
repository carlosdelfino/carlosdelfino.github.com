---
date: "2017-05-30 09:16:18 -0300"
title: "Singleton - Padrões de Projeto em JavaScript"
tags: [JavaScript, Programar, Programação, ECMA, ECMAScript, WEB, WWW, Node.js, JQuery, módulos, CommonJS, ECMAScript 6, ES6, Padrões de Projeto, Criaçonal, Singleton, Prototype, Classes]
categories: [programacao, javascript, padroes_de_projeto]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
ads:
 show: true
tagcloud: true
coinbase:
 show: true
---
Este post estreia uma série de posts sobre padrões de projeto na linguagem JavaScript, estes posts são baseados diretamente no livro "Mastering JavaScript Design Patterns", escrito por Simon Timms e publicado pela Packt Publishing, entre outros especializados no assunto.

<!--more-->

## Consolidando alguns conceitos
Bem, para começarmos a falar de Padrões de projeto com a linguagem JavaScript, alguns conceitos ligados a Programação Orientada a Objetos precisam estar bem compreendidos. Portanto, vou dar inicio a este post explicando bem o conceito de prototype e como usa-lo para se ter sucesso em especial com o *"Padrão de Projetos"* **Singleton**.

Além disso, é importante salientarmos que iremos nos basear no ECMAScript 6 (ES6) para expressarmos nossos códigos no JavaScript, portanto é fundamental que se compreenda bem os novos conceitos, em espcial quando ao uso do `var` e `let` para decarlação de variáveis.

Apesar de nossos projetos estarem sendo migrados para TypeScript não iremos por hora abordar tal linguagem.

### Declarando Variáveis.

Bem, vamos começar esclarecendo a diferença entre 'let' e 'var', usaremos os conceitos conforme apresentado no livro "Learning ECMAscript 6" compilado por "Narayan Prusty" e publicado por "Packt publishing".

Até então o JavaScript não tinha nenhum mecanismos para definir o escopo de uma variável, sendo portanto as variáveis visiveis em toda a aplicação, sendo portanto todas globais, não importando onde elas eram declaradas.

Com o advento da especificação ES6, surgiu uma nova palavra chave para declarar variáveis, `let`, com esta nova palavra chave foi mantida a compatibilidade da linguagem com os códigos antigos que já tinha seus algoritmos baseados na declaração de variáveis com a palavra chave `var`.

Quando se usa `var` o JavaScript declara uma variável e anexa ela ao contexto global, sendo assim sua visiblidade é para todo o código, não importanto quando interno seja sua delcaração em algum bloco de código dentro de seu algoritmo.

Isso interfere bastante na funcionalidade em padrões de projeto como o Singleton, já que a variável que armazena a instância única da classe criada pode sofrer intervenções de outras partes do código, causando um mal funcionamento ou mesmo a quebra de seu código.

portanto, toda variável declarada por meio da palavra chave `let` é visivel em seu contexto e blocos inferiores.

### Prototype

Como muitos sabem, mas poucos usam, o javaScript e uma lingaugem orientada a objetos.

Possui 5 tipos primitivos:
* Undefined
* Null
* Boolean
* String
* Number

Dos 5 apenas 3 são objetos propriamente, Boolean, String e Number, estes são fácilmente encapsulados e desencapsulados de seu formato primitivo e diferem apenas pelas iniciais maísculas e mínusculas.


Por exemplo quando conecatenando String, comparando logicamente valores Booleanos, efetuando operações matematicas.

A criação de objetos em JavaScript é muito simples, você pode faze-la de duas formas, ou através do operador `new` ou usando um par de chaves `{}`, usando a notação JSON.

veja que vc não está declarando uma classe, mas estanciando um objeto que é declado em linha de código.

Assim, este objeto cada vez que é declarado, mesmo suas funções são novas entidades de código, tendo seu espaço de memória reservado, porém ainda se encontra o problema das declarações de váriaveis com a apalvra reservada `var`, pois estas variáveis estão anexadas ao contexto global.

Já as campos do objeto, estão anexadas a ele diretamente e não há o conceito de campo estática, já que este formato não existe a classe. Mas veremos a frente como isso foi contornado na Linguagem.

Internamente as funções e blocos de código, se pode definri variáveis usando a valavra reservada `let`que irá contextualizar a visiblidade da variável conforme ela é criada.

### `this`, seu uso.

A delcaração `this` é realmente um enigma a ser compreendido no JavaScript, e pode vir a causar bastante confusão para o iniciante, tivemos muitos transtorno no aprendizado da lingaugen, aplicando o conhecimento que foi adquirdo no Java e posteriormetne no C/C++.

No JavaScript podemos criar as funções (mensagens do objeto), veja em JavaScript não temos metodos, apenas funções, em qualquer parte do códigoe  em seguida atribuila a umo campo do objeto e assim usa-la como um membro do ojbeto, o que nos dá muita dinamicidade para estender objetos, mas isso é bastante perigoso, veremos isso nesta série.

Quando usamos `this` ele faz referencia ao objeto onde a função está sendo executada, e não criada, por exemplo:

Eu tenho a função x() criada na console de seu naevagdor, conforme abaixo:

``` JavaScript
> var x = function(){
   console.log(this);
}
```

Esta função quando executada na console, irá ter `this` fazendo referência ao objeto  `window` que é o contexto global e quem possuie o controle, ou seja é o dnbo da função quando sendo executada.

Agora, criando um objeto `o`:

``` JavaScript
var o = {};
```

e posteriormente, adicionar o  conteúdo de `x` que é uma função:

``` JavaScript
o.x = x;
```

Ao executar a função `o.x`, `this` já será uma referência ao objeto `o` e não mais o objeto `window`, assim será `this` igual a `o` e não mais a `window`;

Para minizar o desconforto de uso do `this`, caso venha ter, é preciso práticar seu uso exasltivamente, criando senários onde você transfere a propriedade( o dono, o senhorio) de funções entre objetos.

Uma forma de perceber isso é havendo um atributo `nome`, referênciada por `this.nome` em uma função quando definida em um objeto qualquer, ao dar esta função ao senhorio de outro objeto, ou seja permitir que outro objeto seja o prorprietário dela, este novo objeto pode não ter o atributo, e como tal situação não irá gerar um erro na maioria dos usos, retornando apenas como `undefined`, o erro pode ser detectado tarde de mais.

### protipando

Um último conceito que precisamos dominar antes de continuar com padrões de projeto em JavaScript é a prototipação de objetos, que é feita através do uso do campo `prototype` presente na definição de objetos, ou seja na classe do objeto.

Quando definimos um objeto, usando a notação de classe, por exemplo:

``` JavaScript
var MinhaClasse = function(){
   // aqui vc define propriedades, atributos
   // e funções, mensagens.
}
```

A Classe acimna é a definição de um objeto do tipo MinhaClasse, ele não tem nenhuma campo/propriedade/atributo e nenhuma função/mensagem.

Atenção: usaremos o termo atributo apartir de agora para identificar os campos ou propriedades de uma classe, e o termo mensagem para identificar funções e métodos da classe.
{ .notice }

Para usar a classe acima, precisamos instância-la em um objeto, da seguinte forma:

``` JavaScript
var objetoMinhaClasse =  new MinhaClasse();
```

Mas não temos nenhum atributo ou mensagem para esta classe, então nosso objeto não faz nada.

Podemos ampliar (não vou usar o termo extender aqui, em outro post veremos a diferença entre ampliar uma classe, e extender a classe), adiiconando novas atributos e novas mensagens a então criada classe.

Assim:

``` JavaScript
MinhaClasse.prototype.nome = "";
MinhaClasse.prototype.mostreNome = function(){
   this.nome;
}
```

Fazendo testes com o objeto criado, você verá que ele automáticamente possui os novos atributos adicionados, e mensagens. Em cada instância da classe o objeto possui seu proprio `this`, mas compartilha a implementação, não ocupando memória extra quanto a implemntação das mensagens.

o atributo `prototype` é um array que contém as propriedades adicioando a classe, sejam elas novas funções ou campos.

### Outra forma de criar objetos

No ECMAScript 5 foi adicionado uma nova sintaxe para se criar objetos, ela usa a seguinte função presente na classe `Objeto`:

```JavaScript
Object.create(prototype[, propriedades do objeto]);
```

As *propriedades do objeto* informado como segundo parametro opcionalmente, é um objeto JSON, que descreve cada atributo ou mensagem do objeto, definindo se ele pode ser:

* _writable_: ou seja o campo é alterável;
* _configurable_: se ele pode ser removido e reconfigurado futuramente;
* _enumerable_: se será listado, quando acessando a lista de propriedades(campos) do objeto;
* _value_: valor padrão do objeto, usado quando craido.

Esta é uma forma muito eficaz de extender uma classe já existente, basta informar o prototipo e assim instância-lo com novos atributos e mensagens, podendo inclusivo sobreescrever os existentes.

### Novidades no ECMAscript 6

No ECMAScript 6, ou simplesmente ES6, que também é conhecido como *Harmony*, foram definidos novos instrumentos para trabalhar com Classes e Módulos, deixando a linguagem mais familiar para quem vem de linguagens como Java e C++, e até mesmo PHP. E claro, dando mais poder para manipular objetos e classes.

Por hora, veremos simplesmente a sintaxe usada para criar uma classe que está exposta abaixo;

``` JavaScript
class ECG extend BioSignal{
   constructor(name){
      super(name);
      ...
   }

   consolidar(){
      ...
      super.consolidar();
      ...
   }
}
```

Vamos deixar para um post futuro o uso de módulos e exportação, importação de funções e Classes.

## O Padrão de projeto

E porque estamos vendo estes conceitos? Nosso objetivo aqui é estudar padrões de projeto com a Lingaugem JavaScript e suas variações como o TypeScript, mas aqui nesta série de posts veremos apenas a lingaugem JavaScript em especial com foco no ECMAscript 6. Portanto precisamos consolida-los de forma a domina-los e usa-los da melhor forma.

O Padrão de projeto é um conjunto de práticas de condificação, onde blocos de códigos tem funcionalidadees bastante específicas e atendem a necessidades arquiteturais de códigos para qualquer sistema.

Os padrões de projeto são blocos de código reaproveitáveis em objetos de forma a  otimizar sua aplicação, mas como também dar maior legibilidade e compreenção do código, estrutuando e auxiliando na modularização do código.

Os padrões de projeto inicialmente foram catalogados por um grupo de Engenheiros de Softwares conhecidos como Gang of Four, para [mais detalhes leia o artigo sobre o livro clicando aqui]({% post_url programacao/padroesdeprojetos/2017-05-29-Gang_of_Four_o_livro_padroes_de_projetos %}), e desde então tem sido ampliados, e hoje temos publicações diversas com nichos e niveis arquiteturais diferenciados.

### Singleton

Finalmente, vamos então tratar do nosso primeiro padrão de projeto, o objetivo primário para se dar início a estea série de artigos.

O que me levou a escrever esta série, é principalmente porque eu renasci como programador na programação *OO* já pensando em padrões de projetos, no meu primeiro sistema desenvolvido nesta nova fase, o ALF para o Mestrado do Professor Aminadabe, eu já comecei a pensar em padrões de projeto, claro que nos primeiros códigos nem tinha ideia que isso se chamava padrão de projeto e que já existia algo consolidado sobre o assunto, eu chamava minhas padronizações de gerentes, e depois fui descobrindo outras, até que nos meus estudos me deparei com o conceito e me aprofundei, mas ainda não tive contato com os padrões como foram definidos pela Gangue dos Quatro.

E bem mais tarde, na atualidade (2017), quando iniciei a programar com NativeScript, senti muita falta de usar Padrões de Projetos, e o primeiro que tive demanda foi o Singleton, este padrão me fez muita falta, e o que me surpreendeu é que na comunidade Brasileira de NativeScript, até até o momento que eu iniciei esta série, ninguém soube me explicar o que eu estava errando ao tentar criar o padrão *Singleton* com o JavaScript, e alguns chegaram a dizer que eu não estava errado e sim podeia ser um bug do _Engine_ usado pelo NativeScript para interpretar o JavaScript, isso me deixou bastante curioso.

Então fui em busca de padrões de projeto com JavaScript, quando achei este livro ["Mastering JavaScript Design Patterns", escrito por Simon Timms e publicado pela Packt Publishing](), e nele além de me demonstrar o padrão de projeto como deve ser escrito, me apresentou os conceitos necessários a serem utilizados, o que está resumido acima.

O padrãode projeto *Singleton* vista construir uma estrutura de código que seja única em toda a aplicação, não permitindo que o objeto definido de forma a ser um Singleton,  seja instânciado indiscriminadamente.

Bem, porque não indiscriminadamente, e não unicamente, sendo um singleton, leva a tender que seja único!

A questão é que há a possiblidade de certos objetos poderem ser instânciados uma única vez em toda a aplicação, ou casos que sua instancia é controlada conforme contextos, por exemplo, sendo limitados a recursos ou outros fatores. Senbdo assim você pode ter singletons que são instanciados duas, três, ou quatro vezes de formas independentes, porém indexadas, sendo acessados por nomes ou indices numéricos.

No caso da aplicação onde eu estou desenvolvendo e precisei   usar o Singleton, quando demandei uma instância de uma classe que representa o usuário logado e outra que representava as configurações do sistema (não restringindo a elas), no caso do usuário a existência de uma instância indica que o usuário ,que manipulava a aplicação, havia feito login com sucesso. E não poderia haver mais de um objeto usuário em toda a aplicação com as mesmas credênciais, e toda as vezes que este fosse solicitado deveria ser retornado o mesmo objeto. Portanto não só é preciso o uso do Singleton, como também do Registry.

Sendo assim criei a classe `LoggedUser` que somente poderia ser instânciada uma única vez e seria gerida por uma outra classe Factory, responsável por sua construção e associação a outros objetos. Mas não é de responsabilidade desta classe controlar quantos usuários estariam logados, mas quais estariam ativos, mas a classe `LoggedUser`, sim iria controlar tal situação conforme parametrização do sistema, o que não vem ao caso, neste momento.

Abaixo apresento o que o livro me sugere como solução para uso do *Singleton*, que só pode ser instanciado uma única vez em toda a aplicação. O Código está reescrito com minha [assinatura de codificação]({% post_url programacao/2017-05-31-assinatura_de_programacao %}).

``` JavaScript
var A2Manager = {};
(function (A2Manager){
   let LoggedUser = (function(){
      function LoggedUser(){
         this.user = null;
         if(!LoggedUser._instance){
            LoggedUser._instance = this;
         }
         return LoggedUser._instance;
      };
      LoggedUser.prototype.login = function(login, password){
         this.user = new User(login,password);
         console.log("Fazer o Login");
      };
      LoggedUser.prototype.logout = function(login){
         console.log("Fazer o logout");
         this.user = null;
      };
      LoggedUser.getInstance = function(){
         if(!LoggedUser._instance){
            LoggedUser._instance = new LoggedUser();
         }
         return LoggedUser._instance;
      };
      LoggedUser._instance = null;
      return LoggedUser;
   })();
   A2Manager.LoggedUser = LoggedUser;
})(A2Manager);
```

Vamos então analisar algumas partes deste código. }Eu vou tentar ser bem detalhado neste primeiro exemplo para ajudar quem está começando com o JavaScript, e etnder esta forma de programar, para os veteranos alguams explicações podem ser efandonhas, mas realmente são necessárias.

Antes quero lembrar que este código pode ser testado no console JavaScript de seu navegador ou no console do NodeJS. caso tenha problemas em um deles, por favor anote detalhes do erro, se possível copie a tela e me envie relatando passo a passo o que fez, para eu tentar descobrir como lhe ajudar.

Na Primeira linha já declaro um objeto chamdo A2Manger, que usarei como uma forma de modularizar minha aplicação, o objetivo aqui é criar um conseito de pacotes ou módulos que irão conter os grupos de Classes.

Para que este código execute com sucesso no NodeJs é importante que o objeto já exista, há uma diferença entre a console dos navegadores e do NodeJS quando a referências de variáveis. Não entraremos em detalhes neste artigo sobre isso..

Continuando, a segunda linha inicio uma função anonima que irá receber como parametro o nosso objeto que representa o módulo que irá agrupar nossas classes criadas.

já na terceira linha, declaro uma variável privada que será usada para construir nossa classe LoggedUser, portando já dei o mesmo nome a esta variável. cotinuo criando uma função anonima responsável pela declaraçãod da classe que será retornado no final desta segudna função anonima.

Jà na quarta linha até a decima linha, inicio a declar a classe LoggedUser escrevendo sua função construtora que deve ter o nome da classe em questão, no caso LoggedUser, esta classe ao ser construida não recebe nenhum parâmetro.

Uma pecularidade do JavaScript é que devido ao fato de não poder ser criado um Construtor privado ou protegido para a classe, precisamos proteger nosso algoritmo para que outros programadores, ou nós mesmos não esqueçamos e usemos o construtor, ao inez do *[Factory Method]()* para instanciar nossa classe, quebrando assim nosso código, então no caso do JavaScript poderemos usar o construtor normalmente para ter acesso ao singleton, devido ao fato do construtor retornar a representação do objeto. é o que ocorre então na linha 9:

```
   return LoggedUser._instance;
```

Então nesta linha uso esta capacidade de retornar um valor mesmo sendo um construtor, para retornar a instancia da classe, que se não existia antes foi criada nas linhas 6 a 8. Veja que na linha 7 uso `this`, para fazer referencia ao objeto em questão, isso é possível como em qualquer outra lingaugem para acesso ao objeto criado, ele já existe neste ponto.

Das linhas 11 até 18, uso o prototypo da classe para expandila-la (lembre-se não estou extendendo a classe, mas expandido, adicionando seus métodos).

E nas linhas 19 até 24, tenho um *Factory Method* responsável pela criação do singleton, veja que o Singleton tem uma parceria intima com o *Factory Method*  que usa o conceito *Lazy*

Aguarde, continuo.
{ .notice }

## Classe User do exemplo acima

Para ajudar aos iniciantes, a classe user está descrita abaixo.

var User = (function(){
   User.prototype.login = null;
   User.prototype.password = null;
	function User(login,password){
      this.password = password;
      this.login = login;
   };
	return User;
})();
