---
title: "GCC Explorer - Um Compilador Interativo"
tags: [C, C++, Compilador, GCC Explorer, GCC, Navegador, Tempo Real, Aprendizado, ARM, Parallella, Epiphany, ARM64, AVR, x86, PowerPC]
category: [programacao, CCplusplus]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
flattr:
 show: true
---
 

Qualquer pessoa que se interessa pela programação assembly deve definitivamente
conhece a incrível ferramenta chamada "GCC Explorer", uma ferramenta open 
source de inspeção assembly. A ferramenta roda em seu navegador e permite
a inspeção de código assembly conforme você escreve seu código em C. Comparado
ao "hacking" de usar na linha de comando de seu terminal o comando "objdump"
esta ferramenta é um grande ganho de produtividade.

<!--more-->

A habilidade de obter instantaneamente (1 segundo) a avaliação da qualidade de
seu código, especialmente quando você trabalha com pequenas plataformas como
por exemplo microcontroladores ou embarcados, e assim precisa de um código bem 
otimizado, sem falar na oportunidade de aprendizado onde se pode aprender 
codificação Assembly por comparação com o código C.

No site da ["Parallella"](http://gcc.parallella.org) é possível usar o "GCC 
Explorer" para as plataformas:

 * Epiphany
 * ARM
 * x86
 
No site original [GCC Explorer](http://gcc.godbolt.org) é possível usar as 
seguintes plataformas:

 * ARM
 * ARM64
 * PowerPC
 * x86 (diversos sabores GCC)
 * e também AVR, 
 
Porém não achei ainda como usar códigos do Arduino, o que seria muito bom para
estudantes e pesquisadores.


Basta você copiar e colocar seus blocos de códigos ou carregar os arquivos de
exemplos no site original ou funções no caso do site da Parallella que usa a
biblioteca PAL.

Quando usando o compilador Epiphany fica recomendado usar os parâmetros 
`-02 -mfp-mode=round-nearest` para obter melhores resultados.

**Texto Traduzido livremente e adaptado do site da www.parallella.org, conforme
fontes abaixo**

## Fontes:

 * [GCC Explorer: An interactive compiler that runs in your browser](https://www.parallella.org/2015/08/07/curious-about-assembly-programming-check-this-out/)
 * [GCC Explorer on GitHub](https://github.com/mattgodbolt/gcc-explorer)