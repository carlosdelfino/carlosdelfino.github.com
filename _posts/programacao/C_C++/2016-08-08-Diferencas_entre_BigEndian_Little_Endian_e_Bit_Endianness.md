---
title: "Diferenças entre BigEndian, Little Endian e Bit Endianness"
tags: [big Endian, Little Endian, Endianness, Bit Endianness, LSB, MSB, Binário, Byte, Bit, Numeração, endereçamento, manipulação de bits, manipulação e bytes, bit, byte, Little End in, Big End In]
categories: [programacao, cplusplus]
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
math: true
---

Para o iniciante este conceito pode parecer bastante confuso, e até inútil, mas para quem deseja trabalhar com microcontroladores é fundamental seu entendimento. Big Endian ou Little Endian, qual o impacto na transmissão de dados de um sistema para outro, entre o módulo e o microcontrolador?

<!--more-->

O conceito de Big Endian e Little Endian, nomeado simplesmente de Endianess vem da transição dos computadores de médio porte para os microcomputadores, quando estes passaram a endereçar tantos os bits quantos os Bytes de forma diferente, mas tal problema é principalmente observado quando lidamos com os Bytes, já que tal problema pode acarretar o embaralhamento até de texto causando confusão, mas no caso de tratamento numérica pode se tornar a falência total do sistema.

O problema se deu inicio, como já foi dito quando os microcomputadores surgiram, já que estes optaram em trabalhar com o conceito de Little Endian, mas o que é este Endian? porque Big ou Little? bem Endian é um termo cunhado em uma história que faz alusão as disputas politicas e religiosas na Europa, e descrita em uma história de ficção escrita por [Jonathan Swift]({% post_url 2016-08-08-Jonathan_Swift %}) em uma sátira escrita em 1726, Conhecida em português como as Viagens de Gulliver, esta história dois grupos de cidadãos entram em guerra por não concordarem qual o lado certo se deve quebrar o ovo, do lado maior (Big End) ou do lado menor (Little End), com isso uma guerra civil se instala separando os grupos.

Na informática isso não foi muito diferente, não chegamos uma guerra civil por isso, mas tivemos os sistemas separados em "Big End in" e "Little End in" que define como os bits são transmitidos em algum sistemas, e em outros apenas quando lidamos com palavras (World/2 bytes, DWorld/4 bytes), seja o microprocessador 8 bits ou maior.

Nos tempos atuais, não temos muitos problemas relativos a tal modo de endereçamento porque quase todos os microprocessadores usam o Little Endian para endereçar seus dados, com exceção de alguns como o antigo PowerMAC que usava um PowerPC especial travado para BIG Endian. Os que não usam permitem o chaveamento entre os dois modos no que tange a manipulação dos bytes.

Outras arquiteturas que trabalham com Big Endian são, Motorola 68000 series (incluindo Freescale ColdFire), Xilinx Microblaze, SuperH, IBM z/Architecture, Atmel AVR32 e o Intel 8051 com atenção para instrução `LCALL` que endereça usando Little Endian.

Mas então, oque é realmente Big Endian e Little Endian?

Como já dito nada mais é do que a forma que os bytes e bits são endereçados na memória, quando se trata de bytes o Big Endian endereça em uma palavra por exemplo do tipo 2 bytes, o primeiro byte como sendo o endereço menor, e a segunda palavra o endereço seguinte. Ja no Little Endian, o segundo Byte é endereçado primeiro, isso para quem está começando pode causar um certo desconforto, apesar que as linguagens abstraem para nós tal problema, mesmo no C, isso não é percebido, mas podemos vir a ter problemas quando lidamos com ponteiros, já que o primeiro endereço em um sistema Big Endian, não será a menor parte do número, ou seja a parte menos significante (MSB), mas sim a parte mais significante (LSB).

Vejamos abaixo para entendemos primeiro o conceito de LSB  e MSB, que trata a importância do bit ou byte na composição numérica.

**LSB** representa a parte menos significativa do número ou seja a parte mais a direita..

Já o **MSB** representa a parte mais significativa, ou seja a parte mais a esquerda do número.

Agora podemos entender melhor o conceito Little Endian e Big Endian, vejamos primeiro a nível de bits do que se trata.

Para o **Little Endian**  a representação numérica em bits, onde o algoritmo de conversão numérico  que a maioria de nós está acostumado pode ser facilmente representado na fórmula:

$$
\sum_{i=0}^{N-1} b_i \cdot 2^i
$$

Temos então a seguinte ordenação dos bits para a representação do número 180 em Little Endian, onde o bit menos significativo é tratado como sendo o bit 0 e o bit 7 é o bit mais significativo.

<figure>
<img src="/images/programcao/ccplusplus/LSB-0-bit-numbering-300px-Lsb0.svg.png" />
<figcaption>Representação gráfica do Little Endian</figcaption>
</figure>

Para o **Big Endian** os bits mantem sua disposição, porém sua ordem de transmissão inverte, ou seja são endereçados do MSB como sendo o primeiro bit, e o LSB como sendo o último bit, portanto a fórmula de conversão passa a ser:

$$
\sum_{i=0}^{N-1} b_i \cdot 2^{(N - 1 - i)}
$$

<figure>
<img src="/images/programcao/ccplusplus/LSB-0-bit-numbering-300px-Lsb0.svg.png" />
<figcaption>Representação gráfica do Little Endian</figcaption>
</figure>

Em se tratando de bits o conceito **Endianess** afeta mais o hardware no que tange o endereçamento de memória, transferência de dados em barramentos, principalmente nos seriais, e operações de manipulação de bits, já que principalmente se formos usarmos mascaras do tipo bitwise é preciso saber exatamente a ordem dos bits para não haver enganos fatais.

Vejamos agora como é tratado o conceito **endianess** quando se trata de bytes, o que afeta mais a manipulação do dado na memória quando é representado com mais de dois bytes, por exemplo números inteiros e short int em maquinas 32 bits.

As imagem abaixo representam dois números inteiros armazenado na memória de um microcontrolador qualquer que seja do tipo **Little Endian**, a primeira representa um número de 16bits ou seja um Word, o segundo um número de 32 bits, Double Word (DWord).

<figure>
<img src="/images/programcao/ccplusplus/Big_Endian_Byte-Word.png" />
<figcaption>Representação gráfica do Little Endian para um Word</figcaption>
</figure>

<figure>
<img src="/images/programcao/ccplusplus/Big_Endian_Byte-DWord.png" />
<figcaption>Representação gráfica do Little Endian para um DWord</figcaption>
</figure>

Como pode ver o byte mais significativo é armazenado no endereço mais baixo da memória, sendo então acessado primeiramente, e o byte menos significativo é armazenando posteriormente. Na representação o endereço de memória começa a contar em `a`.

Vejamos agora como o mesmo número fica representado em um sistema Little Endian. Temos a seguir os mesmos números usados na representação anterior, porém agora utilizado o mecanismo Little Endian para armazená-lo.

<figure>
<img src="/images/programcao/ccplusplus/Little_Endian_Byte-Word.png" />
<figcaption>Representação gráfica do Little Endian para um Word</figcaption>
</figure>

<figure>
<figcaption>Representação gráfica do Little Endian para um DWord</figcaption>
<img src="/images/programcao/ccplusplus/Little_Endian_Byte-DWord.png" />
</figure>

Ouve épocas que tal conflito quando se transferindo dados entre computadores que usavam sistemas diferentes (chamdos bytesex), ou seja transmitindo de um sistema Little Endian para um sistema Big Endian a string **UNIX**, foi identificado como ***NUXI Problem***, ou seja o "problema **NUXI**", devido a inversão da String "UNIX".

Como pode ver a cada par de bytes, haveria uma inversão, de dos dois bytes, causando um certo transtorno.

## Um exemplo do formato Little Endian em C

Abaixo estão dois códigos que demonstra como um número inteiro é armazenado na mémoria, o primeiro um número de 16 bits, um típico inteiro, o outro um número de de 32 bits, ou seja um típico inteiro longo.

Neste exemplo mostramos como um inteiro de 2 bytes (16bits) é armazenado na memória em um formato Little Endian:
```
#include <stdint.h>
#include <stdio.h>
#include <string.h>

struct DWORD
   {
      uint8_t a0;
      uint8_t a1; 
   } ;

    
int main(void)
{
	struct DWORD dw;  
 
	dw.a0 = 0xDF;
	dw.a1 = 0xEA;  
    
	printf("Endereço 0: %#X\nEndereço 1: %#X\n: %#X\n", dw.a0, dw.a1);

	uint32_t dw1;
 	memcpy(&dw1, &dw,4);
	//dw1 = 2;

	printf("   Endereços   1 0\n");
	printf("-------------------\n");
	printf("Valor Word: %#hX\n", dw1);

    return 0;
}
```
<figure>
<figcaption>Resultado para um Word</figcaption>
<img src="/images/programcao/ccplusplus/exemplo_little_endian_c_word" />
</figure>

--------

A seguir um outro exemplo para um inteiro longo de 4 bytes (32 bits), apresentando como é armazenado na memória em um formato Little Endian. Observe as pequenas diferenças no código:
```
#include <stdint.h>
#include <stdio.h>
#include <string.h>

struct DWORD
   {
      uint8_t a0;
      uint8_t a1;
      uint8_t a2;
      uint8_t a3;
   } ;

    
int main(void)
{
	struct DWORD dw;  
 
	dw.a0 = 0xDF;
	dw.a1 = 0xEA; 
	dw.a2 = 0xAB;
	dw.a3 = 0xCF; 
    
	printf("Endereço 0: %#X\nEndereço 1: %#X\nEndereço 2: %#X\nEndereço 3: %#X\n", dw.a0, dw.a1, dw.a2, dw.a3);

	uint32_t dw1;
 	memcpy(&dw1, &dw,4);
	//dw1 = 2;

	printf("   Endereços   3 2 1 0\n");
	printf("-------------------\n");
	printf("Valor DWord: %#lX\n", dw1);

    return 0;
}
```
<figure>
<figcaption>Resultado para um DWord</figcaption>
<img src="/images/programcao/ccplusplus/exemplo_little_endian_c_dword" />
</figure>

## Outras formas de representação

Há outras formas de representação **Endianess** formas que misturam convenientemente os dois formatos acima, porém não entraremos em detalhes aqui como são apresentadas e utilizadas.


## Fontes

 * [https://en.wikipedia.org/wiki/Endianness](https://en.wikipedia.org/wiki/Endianness)
 * [https://en.wikipedia.org/wiki/Bit_numbering](https://en.wikipedia.org/wiki/Bit_numbering)
 * [https://support.microsoft.com/pt-br/kb/102025](https://support.microsoft.com/pt-br/kb/102025)
 * [http://infocenter.arm.com/help/topic/com.arm.doc.dui0552a/I1835.html](http://infocenter.arm.com/help/topic/com.arm.doc.dui0552a/I1835.html)
 * [http://david.carybros.com/html/endian_faq.html](http://david.carybros.com/html/endian_faq.html)
 * [https://www.ietf.org/rfc/ien/ien137.txt](https://www.ietf.org/rfc/ien/ien137.txt)