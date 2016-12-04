---
redirect_from: "/logicadeprogramacao/nivel_3/Usando_Instrucao_RJMP_Para_Substituir_NOP/"
title: "Usando Instrução RJMP Para Substituir NOP"
tags: [Otimização de Código, Assembly, Instrução, NOP, RJMP, Relative Jump, No Operation, AVR, AVR8 AVR32, ATmega, ATtiny]
category: [logicadeprogramacao, assembly]
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
  feature: logica_programacao/language_stack-250x182.gif
  teaser: logica_programacao/language_stack-250x182.gif
  credit: Carlos Delfino
  creditlink: http://carlosdelfino.eti.br
tagcloud: true
coinbase:
 show: true
---
Alguns instruções podem vir a ser usadas de forma a simular outras mesmo que fugindo totalmente de seu uso padrão, como neste caso onde RJMP substitui duas instruções NOP quando se deseja reduzir o tamanho de um código!"

<!--more-->

Nada melhor que pequenos macetes para se ter um programa eficiente e pequeno.

Este artigo foi escrito para o Assemby da arquitetura AVR8 que é usada nos microcontroladores ATmega e ATtiny.

## A Instrução *NOP*

Usamos muitas vezes a instrução "NOP", uma instrução que é utilizada para sincronizar o códio pedindo ao processador que não execute nada durante um ciclo de clock. Este sincronismo pode ser usado para aguardar alguma mudança de estado externo ao processador com tempo pré estabelecido, ou mesmo para temporizar envio de informações para o mundo externo.

A instrução "NOP" tem o tamanho de dois bytes, e pode inclusive ser usada para alinhar o código dentro da mémoria, de forma que grupos de instruções (funções) tenham um tamanho pre-definido. Isso se faz necessário em algumas estruturas de código, em especial para alocação de dados na memória de programa.

A instrução "NOP" é executada exatamente em um ciclo de clock nos processadores RISC em especial nos de arquitetura ARM. Com isso é muito fácil saber seu tempo de execução desde que se sáiba exatamente o clock usado.

Funções como "delay()" e "microdelay()" utilizam a instrução "NOP" em um Loop pré calculado, onde a instrução é executada repetidamente conforme a frequência do clock para obter o tempo de espera  desejada do processador até que se passe o número de milessegundos informado. Mas observe, isso somente ocorre em softwares que são do tipo *Baremetal* e ou que não são controlados por um RTOS, por exemplo.

Para um melhor entendimento do que pretendemos mostrar aqui, é preciso compreender que quando o processador encontra uma instrução "NOP", ele executa simplesmente a operação pc = pc + 1, ou seja soma uma unidade ao "Program Counter".

## Instrução RJMP

Mas ver como funciona a *"RJMP"* e como podemos usa-la para melhorar o tamanho de nosso código quando precisamos executar muitas instruções "NOP", mas não tanto quanto para um delay de um milisegundos. Em um controlador AVR como o ATMega328 usado no Arduino, a frequência de padrão usada é de 16Mhz (16000000) para o clock, o que precisariamos um loop que leva-se a executar um pouco menos que 16000 (dezeseis mil) instruções de um ciclo.

Mas suponha que precisemos neste microcontrolador aguarda apenas 0,5uS (meio microssegundos), portanto seria suficiente apenas 8 instruções de um ciclo. Com isso poderiamos escrever o código usando o "NOP" 8 vezes. Mas isso, irá aumentar em 8 linhas nosso código, claro isso é muito pouco em um código de 2KB, mas suponha que falte espaço e que vc esteja usando um microcontrolador como o ATtiny24 que exatamente esta quantidade de mémoria RAM, portanto é crucial economizar cada byte, ou melhor cada Word, já que cada instrução consome 2 bytes.

Diante disso, temos um macete onde usamos uma estrução perfeitamente previsível e que irá consumir um certo número de ciclos independente da instrução anterior ou posterior, esta instrução se chama RJMP (Relative Jump).

Esta instrução é usada para saltar da posição atual em seu código para outra sem identificar o ponto de retorno, somando um valor relativo para a nova referência. Tal instrução é muito útil para acesso a labels em seu código Assembly e por ser relativa a posição atul pode acessar qualquer parte de um código de até 2KB a frente ou para traz no código.  

Seu funcionamento é bem simples, quando é executada esta instrução pega o valor do PC e somado a posição relativa desejada, se para frente é somado também mais 1 ao valor.

Portanto se usarmos "RJMP" como abaixo:

```
rjmp .+0
```

teremos exatamente o processador gastando dois ciclos de instruções para fazer a operação PC = PC + 0 + 1;

Assim ela será equivalente a usarmos dois *NOP*, e não irá de forma alguma mudar seu comportamento não importa qual instrução seja usada antes ou depois. Além disso esta instrução não interfere no registrador de estado (SREG).

Sendo assim, onde precisavamos de 8 intruções "NOP", podemos usar apenas 4 instruções "RJMP .+0".

A instrução RJMP tem o seguinte código binário (OP-Code):

```
1100 kkkk kkkk kkkk kkkk ---- 40KK KKKK
```

onde a parte representada por k é substituida pela representação binária (K para byte) do valor a ser somado ou subtraido ao CP.

## Fontes

 * [AVR Assembler Instructions - NOP - No OPeration](http://www.atmel.com/webdoc/avrassembler/avrassembler.wb_NOP.html)
 * [AVR Assembler Instructions - RJMP- Relative Jump](http://www.atmel.com/webdoc/avrassembler/avrassembler.wb_RJMP.html)
