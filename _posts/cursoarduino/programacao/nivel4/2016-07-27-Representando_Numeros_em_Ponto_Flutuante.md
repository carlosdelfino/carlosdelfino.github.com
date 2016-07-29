---
redirect_from: 
 - "/logicadeprogramacao/Representando_Numeros_em_Ponto_Flutuante/"
 - "/logicadeprogramacao/nivel_4/Representando_Numeros_em_Ponto_Flutuante/"
title: Representação de Números em Ponto Flutuante
tags: [Arduino, Curso, Arduino Mega, Arduino Due, Arduino Uno, Lógica, Programação, Algoritimos, Estrutura de Dados, Assembly, AVR, ATMega, ATTiny, ARM, Ementa, C, C++, C/C++, Variáveis, Constantes, Macros, Volateis, PROGMEN, Mémoria de Programa, Memória Flash, Mémoria RAM, SRAM, RAM, Optimização, Ponto Flutuante, Fração, Denominador, Divisor, IEEE, IEEE 754]
category: [logicadeprogramacao, nivel_4]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
image:
  teaser: logica_programacao/fluxograma_planejamento-300x199.jpg
  feature: logica_programacao/algoritmo-jogo-900x673.png
  credit: Carlos Delfino 
  creditlink: 
tagcloud: true
coinbase:
 show: true
---
Como o ponto flutuante é representado em binário? existem padrões que normatizam tais representações? Como lidar com tais números em Assembly?

<!--more-->

Eu escrevi este artigo em 2014, porém na época o utilizei apenas na apostila para o curso do Arduino, quando fosse preciso entrar em detalhes sobre a representação de frações com precisão adequada a aplicações de engenharia ou científicas. Abaixo darei mais detalhes sobre ponto flutuante, e indicarei os sites na seção fontes onde obtive informações para a escrita.

Ponto flutuante é uma forma de representar números fracionados muito pequenos ou muito grandes, como sabemos o computador somente é capaz de lidar com 0, 1 e combinações destes como bytes, word, double word, e assim representar caracteres e números inteiros, mas como representar adequadamente o conjunto dos números reais?

Com isso foi criado uma forma de armazenar uma representação binária dos números reais sem que se perdesse grande quantidade de precisão, mas mesmo assim ainda há perdas, e para a computação cientifica e engenharia em geral, a notação sugerida pelo IEEE nos atende perfeitamente, ela é chamada de IEEE 754.

#### Mas o que realmente são números de ponto flutuante?

Como já dito números de pontos flutuante são todos os números existente no conjunto dos números reais, em especial aqueles que são muito pequenos com grandes quantidades de casa decimais, como por exemplo o número PI e os muito grandes onde de tão grande algumas partes de sua representação de menor valor podem ser descartadas.

Mas isso não significa que números como 10453.1 não possam ser representados por ponto flutuante, claro que pode, mesmo o impacto do arredondamento não sendo muito grande, pode se usar números de ponto flutuante para armazenar tais valores, mas o ideal é que se utilize para números de maior expressão onde seu arredondamento deve ser cauteloso.

Mas mesmo números de ponto flutuante não são tão precisos, números como 0.1 podem ter diferentes do que 10/100.

É preciso muita cautela ao se comparar números de ponto flutuante por isso, já que eles podem ser aproximados, e graficamente não ser exatamente o que está armazenado na memória do computador. devido ao arredondamento necessário para sua exibição.

#### Como são exibidos.

Os números de ponto flutuante são exibidos normalmente através de notação de engenharia, como é utilizado para representar unidades de medida como Km, Kg entre outras, portanto o número 1000 seria 1 * 10^3 o número de Euler (2.7182818284590452353602874713527) poderia ser representado 2718281.8284590452353602874713527 * 10^-6, evitando assim perder precisão.

#### Como os números são armazenados na memória.

Como vimos o número de Euler, é um número infinitamente grande e não há como ser armazenado na memória do computador sem que se perca precisão, e para tal, o uso de ponto flutuante pode variar como "Simples" (Float), "Duplo" (Double), entre outras conforme a plataforma escolhida e até mesmo a linguagem, mas vamos focar aqui na Linguagem C, e em especial na arquitetura (plataforma) AVR e ARM.

Em ambas apenas temos o ponto flutuante simples ou duplo, onde um utiliza 32 bits e o outro 64 bits para armazenar o número. porém na plataforma AVR devido a limitações de hardware mesmo a notação double (dupla) usa apenas 32 bits, sendo portanto da mesma precisão.

Como podemos ver no gráfico abaixo os 32 bits são divididos em 3 seções, a primeira de apenas um bit, indica qual o sinal do número, a segunda seção de 

#### Analisando Pontos Flutuantes
Podemos usar ferramentas para analisar a construção binária de um ponto flutuante, e o site a seguir é uma excelente opção para aprender mais sobre a composição deste número conforme o padrão IEEE754 http://babbage.cs.qc.cuny.edu/IEEE-754/index.xhtml

![Representação Ponto Flutuante](\images\programacao\Representacao_IEEE754_Ponto_Flutuante.png)

#### Quais os Limites de representação do Ponto Flutuante

![Limites Ponto Flutuante](\images\programacao\Limites_Ponto_Flutuante.png)


## Fontes:

* http://www.ntu.edu.sg/home/ehchua/programming/java/datarepresentation.html
* http://www.tfinley.net/notes/cps104/floating.html
* http://en.wikipedia.org/wiki/Floating_point
* http://kipirvine.com/asm/workbook/floating_tut.htm
* https://www.cs.duke.edu/~raw/cps104/TWFNotes/floating.html
* http://people.ece.cornell.edu/land/courses/ece4760/Math/Floating_point/
* http://voidware.com/binarycalculators.htm
* http://steve.hollasch.net/cgindex/coding/ieeefloat.html
* http://www.ntu.edu.sg/home/ehchua/programming/java/DataRepresentation.html
* http://www.mathsisfun.com/numbers/e-eulers-number.html


Artigo antigo removido: 2014-12-09-Representando_Numeros_em_Ponto_Flutuante