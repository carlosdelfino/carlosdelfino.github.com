---
title: "Depurando com Arrays" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, GDB, Array, Depuração, Variável]
categories: [programacao, depuracao]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: embarcados/nanopi-m3-03-1024x445.png
 teaser: embarcados/nanopi-m3-03-300x174.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

Qual programa não usa um Array, quase todos não é? e como então fazer para depurar um programa em C ou C++ usando o GDB e imprimir adequadamente o conteúdo de Arrays?

<!--more-->

É muito simples imprimir o conteúdo de arrays no GDB. Antes de tudo é preciso lembrar que as variáveis que armazenam um Array são ponteiros, portanto deverá tratá-los assim ou lembrar de indicar que são Arrays.

É preciso também conhecer o tamanho do Array para não se perder dados ou imprimir lixo a mais.

Veja a pequena parte de um programa em C:

```C
int main(){
   int *a;
   int b[3] = {1,2,3};
   a = b;

   int *c[3] = {a, b, 0};
   int **d = c;
   return 0;
 }
```

Ao depurar este programa, no momento que desejar ver o conteúdo da variável `a` você deve lembrar que ela é um ponteiro e sendo um array que tem 3 posições, portanto use o comando `print` da seguinte forma:

```C
(gdb) print *a@3
 $4 = {1, 2, 3}
```

Você pode também fazer um casting durante a depuração:

```C
(gdb) print (int [3]) *a
 $8 = {1, 2, 3} 
```

## fonte:

http://the-hydra.blogspot.com.br/2011/01/gdb-trick-for-printing-array-content.html