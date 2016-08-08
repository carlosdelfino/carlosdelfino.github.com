---
title: "Diferenças entre BigEndian, Little Endian e Bit Endianness"
tags: [big Endian, Little Endian, Endianness, Bit Endianness, LSB, MSB, Binário, Byte, Bit, Númeração, endereçamento, manipulação de bits, manipulação e bytes, bit, byte, Little End in, Big End In"
---

Para o iniciante este conceito pode parecer bastante confuso, e até inútil, mas para quem deseja trabalhar com microcontroladores é fundamental seu entendimento. Big Endian ou Little Endian, qual o impacto na transmissão de dados de um sistema para outro, entre o módulo e o microcontrolador?

<!--more-->

O conceito de Big Endian e Little Endian, nomeado simplesmente de Endianess vem da transição dos computadores de médio porte para os microcomputadores, quando estes passaram a endereçar tantos os bits quantos os Bytes de forma diferente, mas tal problema é principalmente observado quando lidamos com os Bytes, já que tal problema pode acarretar o embaralhamento até de texto causando confusão, mas no caso de tratamento numérica pode se tornar a falência total do sistema.

O problema se deu inicio, como já foi dito quando os microcomputadores surgiram, já que estes optaram em trabalhar com o conceito de Little Endian, mas o que é este Endian? porque Big ou Little? bem Endian é um termo cunhado em uma história que faz alusão as disputas politicas e religiosas na Europa, e descrita em uma história de ficção escrita por [Jonathan Swift]({% post_url 2016-08-09-Jonathan_Swift %}) em uma sátira escrita em 1726, Conhecida em português como as Viagens de Gulliver, esta história dois grupos de cidadãos entram em guerra por não concordarem qual o lado certo se deve quebrar o ovo, do lado maior (Big End) ou do lado menor (Little End), com isso uma guerra civil se instala separando os grupos.

Na informática isso não foi muito diferente, não chegamos uma guerra civil por isso, mas tivemos os sistemas separados em "Big End in" e "Little End in" que define como os bits são transmitidos em algum sistemas, e em outros apenas quando lidamos com palavras (world/2 bytes, Dworld/4 bytes), seja o microprocessador 8 bits ou maior.

Nos tempos atuais, não temos muitos problemas relativos a tal modo de endereçamento porque quase todos os microprocessadores usam o Little Endian para endereçar seus dados, com exceção de alguns como o antigo PowerMAC que usava um PowerPC especial travado para BIG Endian. Os que não usam permitem o chaveamento entre os dois modos no que tange a manipulação dos bytes.

Outras arquiteturas que trabalham com Big Endian são, Motorola 68000 series (incluindo Freescale ColdFire), Xilinx Microblaze, SuperH, IBM z/Architecture, Atmel AVR32.

Mas então, oque é realmente Big Endian e Little Endian?

Como já dito nada mais é do que a forma que os bytes e bits são endereçados na memória, quando se trata de bytes o Big Endian endereça em uma palavra por exemplo do tipo 2 bytes, o primeiro byte como sendo o endereço menor, e a segunda palavra o endereço seguinte. Ja no Little Endian, o segundo Byte é endereçado primeiro, isso para quem está começando pode causar um certo desconforto, apesar que as linguagens abstraem para nós tal problema, mesmo no C, isso não é percebido, mas podemos vir a ter problemas quando lidamos com ponteiros, já que o primeiro endereço em um sistema Big Endian, não será a menor parte do número, ou seja a parte menos significante (MSB), mas sim a parte mais significante (LSB).




## Fontes

 * https://en.wikipedia.org/wiki/Endianness
 * https://en.wikipedia.org/wiki/Bit_numbering
 * https://support.microsoft.com/pt-br/kb/102025
 * http://infocenter.arm.com/help/topic/com.arm.doc.dui0552a/I1835.html