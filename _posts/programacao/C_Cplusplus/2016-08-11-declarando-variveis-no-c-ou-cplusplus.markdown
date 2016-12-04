---
layout: article
title: "Declarando Variáveis no C ou C++"
date: "2016-08-11 07:40:49 -0300"
tags: [declaração, inicialização, variáveis, C, C++, Blocos, Global, Local, Estática, Constante]
categories: [programacao, ccplusplus]
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
  teaser: programacao/ccplusplus/programacao-660x300.png
  feature: programacao/ccplusplus/programacao-660x300.png
---
Vamos falar um pouco sobre variáveis no C e C++, parece um assunto já esgotado, mas não é, não só porque há sempre novos profissionais adotando a linguagem, como também porque ainda há profissionais que não se preocupam com a clareza de seu código.

<!--more-->

## Detalações de Variáveis no C e C++ de forma geral

Vamos começar falando da prática de se declarar variávies, depois falremos um pouco do contexto delas, o que veremos aqui é valido para o C, mas se aplica também o C++.

Quando declaramos uma variável no C, podemos fazer a declaração de multiplas variáveis em uma unica linha, o que pode parecer uma economia de espaço e até uma prática profissional, mas nem sempre é, isso pode ser visto como desleixo, já que se as variáveis não forem agrupadas adequamente poderão perder qualidade no comentários que as descrevem em detalhes.

Vejamos o código abaixo:

{% highlight C %}
 double lat_i,long_i,lat_f,long_f,fator_variavel; // cordenadas iniciais e finais e fator de conversão variável.
{%endhighlight %}

Bem coloquei um comentário bem resumido, mas já o suficiente para perceber que a variável `fator_variavel`, não deveria estar junto com as variáveis correspondentes as coordenadas, mesmo sendo todas do tipo `double` o ideal seria:

{% highlight C %}
 double lat_i,long_i,lat_f,long_f // cordenadas iniciais e finais, sendo ponto A e ponto B
 double fator_variavel; // fator de conversão variável, será selecionado como método de conversão de coordenadas
{%endhighlight %}

Não fica bem mais claro desta forma? Assim as variáveis que representam coordenadas tem sua linha de declaração e descrião através de seu próprio comentário, e a linha seguinte está com a declaração do fator e seua descrição.

Tal prática não afeta em nada a qualidade do código final, caso a empresa esteja usando um sistema de métricas supervisonado, poderá impactar na qualidade do código escrito e gerar pontos para você.

Vejamos outro exemplo de declarçaão que devemos evitar.

Neste caso temos variáveis do mesmo tipo, mas usos completamente diferentes, veja:

{% highlight C %}
 double lat, long, *buffer_coord
{% endhighlight %}

No primeiro instante não vemos problema, duas variáveis do tipo `double`, mas a terceira é um poneiro de mémoria para um tipo `double`, caimos no mesmo problema anterior, se tivessemos decumentado o par inicial o ponteiro irão destoar e não puoderiam ser claramente descrito, procure separar claramente este tipo de variável.

{% highlight C %}
double lat, long;  // Par de conrdenadas obitidas do GPS
double *buffer_coord; // Bufer de armazenamento das coordenadas, armazena um par de coordenadas
                      // o primeiro double é latitude, o segundo longitude
{% endhighlight %}

Como pode ver o ponteiro agora está bem descrito, indicando que quando for alocado irá armazenar algo semelhante a um array de coordenadas.

Vejamos um caos mais delicado com as mesmas variáveis que pode causar muito mais confusão.

{% highlight C %}
 double* buffer_coord, lat, long;
{% endhighlight %}

É muito comum vermos este tipo de declaração, o que leva a entender que todas as variáveis são ponteiros, correto?

Mas não está correto, apenas a primeira variável é um ponteiro `buffer_coord`, as outras são variáveis comuns, o que leva a muito mau entendido, claro quando compilar iremos ver erros, mas até lá é tempo perdido.

mas uma vez o ideal é usar uma linha para cada aplicação da variável como já sugerido:

{% highlight C %}
double *buffer_coord; // Bufer de armazenamento das coordenadas, armazena um par de coordenadas
                      // o primeiro double é latitude, o segundo longitude
double lat, long;  // Par de conrdenadas obitidas do GPS
{% endhighlight %}

Assim fica bem melhor não é?

Depois farei um artigo falando sobre o contexto de variáveis, globais, estáticas, locais, e etc.
