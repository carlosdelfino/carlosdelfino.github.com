---
redirect_from: "/logicadeprogramacao/Macros_vs_Constantes_Arquitetura_AVR/"
title: Usar Macros ou Constantes, qual a melhor opção.
excerpt: Programar para microcontroladores se torna um desafio maior quando a densidade de informações a serem manipuladas (variaveis e constantes) se torna grande, então alguns valores em especiais aqueles que são constantes precisam ser bem alocados para que não se disperdice nenhum espaço.
tags: [Arduino, Curso, Arduino Mega, Arduino Due, Arduino Uno, Lógica, Programação, Algoritimos, Estrutura de Dados, Assembly, AVR, ATMega, ATTiny, ARM, Ementa, C, C++, C/C++, Variáveis, Constantes, Macros, Volateis, PROGMEN, Mémoria de Programa, Memória Flash, Mémoria RAM, SRAM, RAM, Optimização]
category: [logicadeprogramacao,nivel_2]
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

Uma das grandes dúvidas que são apresentadas quando se aprende a usar
variáveis, constantes e parametros, é quando usar um tipo de dado ou 
outro, porém mais ainda é quando usar uma variável ou constante.

As variáveis devem ser usadas quando se deseja manipula-las de forma a
alterar seu conteúdo, armazenando nas mesmas sempre novos valores com 
base em analises, tomadas de decisão, calculos ou leituras externas.

Já as constantes, deve ser utilizadas quando for necessário o armazenamento
de valores especificos imutáveis, como por exemplo o valor de um fator
de correção, um valor de composição de calculo como PI, por exemplo.

Há usos interessantes para posições de armazenamento em memória como o 
acesso a endereços de memória que representam dispositivos, para o programa/software
é uma posição imutável, ou seja, o software não irá altera-la de forma alguma
mas conforme o estado do dispositivo tal posição terá um valor. Isso
ocorre com posições de memória que representam a porta de entrada ou 
saída de um dispositivo que está acoplado ao endereço indicado, registradores
de controle também podem ser usados assim, seja a arquitetura AVR ou ARM
tal recurso é amplamente utilizado.

Não confunda os registradores de uso geral do processador, que auxiliam 
nas operações internas de manipulação de dados, com os registradores de 
dispositivos, como conversor Analógico Digital, Portas Seriais, entre 
diversos outros. Ambos são mapeados na memória RAM mesmo que sendo somente 
leitura.
{: notice-warning }

Veja que quando se utiliza as constantes para tais aplicações, acesso a 
dispositivos internos ao chip acomplados ao Microcontrolador, é preciso
sinalizar que tal constante é volátil, fica um certo antagonismo, já que
sendo constante como ele pode ser volátil? ou seja algo externo ao código
principal está alterando seu valor. Tal informação já se justifica pois 
sendo uma constante volátil ela muda de valor inesperado, fato que ocorre
já que a posição de mémoria assim definida é a representação do valor gerado
pelo equipamento.

Mas nosso foco aqui é se devemos usar uma Macro do Pré processador ou usar uma consante?
Vejamos então.

As Macros do pré processador nos permitem criar estruturas bastante interessantes
para que sejam substituidas até mesmo por códigos permitindo assim que
criemos até mesmo algo que possamos chamar de um dialeto. Mas o que isso tem a ver
com as variáveis?

Bem, como inicialmente não existia o conceito de constante na linguagem C, a melhor
forma de se ter um determinado dado imutável que poderia ser usado em uma 
formula ou tomada de decisão (estrutura lógica como IF), ou mesmo uma frase/string
que se repita no código em diversos locais, era usando uma macro de pré processamento,
tal macro vejo do meu ponto de vista é mais adequado para indicar situações que
intervenham na estrutura do código e sua compilação, para se entender tal
recurso é preciso estudar mais as diretivas de pré compilação. Porém as macros
se mostram muito úteis para criar representações textuais de valores que são complexos.

Um exemplo de uma representação textual de um valor é a constante PI, sem dúvida 
que é mais fácil do que digitar todas vezes que preciso o número `3.14159265359`
mas qual o impacto deu usar uma macro ou uma constante? bem do primeiro ponto de 
vista não há muito impacto.

## Analisando o código usando Macro de pre-preprocessamento

Fiz alguns testes usando o Arduino para demonstrar tal impacto, e não percebi 
diferença prática alguma no resutlado final, e isso pode ser facilmente constatado
analisando o código assembly gerado.
 
Veja abaixo um código em C/C++ do Arduino, usando macro:

<script src="http://pastebin.com/embed_js.php?i=RVS9XBdF"></script>

No códio temos na primeira linha a definição da macro
`#define CONST_MACRO 13"`, observe que o nome *CONST_MACRO* foi escolhido
para que represente bem nosso examplo, você pode usar o nome que desejar,
mas deixamos a sugestão que use sempre letras maiúsculas com palavras
separadas por traço baixo, assim é fácil indentificar que é uma constante/macro.

Nas demais linhas do código do Arduino estamos usando nada além do padrão,
na função `void setup()` inicializamos a serial a 9660, depois imprimimos
na serial o valor que representa `CONST_MACRO`.

Na função setup, fazemo um calculo simples, sendo que na linha 11, provocamos
o casting do valor 5 que é um inteiro para que seja obtido o resultado da 
divisão como sendo float, assim podemos ter acesso como fração, ou seja
ponto flutuante.

Em seguida imprimimos os valores e calculos de diversas formas.

Bem, tal código quando compilado irá gerar o seguinte resultado em Assembly, 
observe que cortei o arquivo para exibir apenas o que nos interessa.
 
<script src="http://pastebin.com/embed_js.php?i=JnYccFNt"></script>

Já na linha 12 do código em assembly temos:

`d4:   6d e0           ldi     r22, 0x0D       ; 13`

Este códigos são números em exadecimal, o primeiro `d4`, é a linha
de nosso códio assembly, em seguida temos `6d e0` que é o código que
diz a CPU para fazer uma carga imediata no registrador r22 do valor 
`0x0D` que é, nada mais nada menos, o valor decimal `13`, ou seja
ai está o ponto a macro foi convertida ao seu valor. A representação 
textual (mnemônico) de tal comando é `ldi r22, 0x0D`.

Vejamos outro ponto do código onde em C/c++ (linha 10 e 19), calculamos
inicialmente um valor inteiro da divisão `CONST_MACRO/5` que é armazenado
na variável `int var_int`, veja que usamos tal variável apenas uma única
vez no código na linha 19, portanto como o Arduino ao compilar o código
usa optimizaçõa máxima a váriavel deixa de existir, e assim temos o valor
obtido no cálculo sendo diretamente como parametro para a chamada da função
que imprime o valor na serial.

Veja isso nas linhas 42 até 48 do codigo assembly, o valor que está extamente 
sendo carregado no registrador `r22` na linha 44 (em assembly linha 118), 
representado pelos códigos: 

`118:   62 e0           ldi     r22, 0x02       ; 2` 

Ou seja o código `62 e0` é o codio hexadecimal para instrução `ldi r22, 0x02`
e o valor 0x02 é o resultado obtido no calculo `CONST_MACRO/5` ou seja 
`13/5`, como estamos lidando com um valores inteiros temos apenas a parte 
inteira do cálculo.

## Analisando o código usando constantes

Vejamos abaixo o códio para o arduino usando constante.

<script src="http://pastebin.com/embed_js.php?i=TZ1ZDZwh"></script>

E abaixo vemos o código assembly gerado.

<script src="http://pastebin.com/embed_js.php?i=EhX9y71e"></script>

Podemos ver que há pouco diferença no trato dos valores, 
com exceção das linhas 25 a 35 e 36 a 45 no código assembly logo 
acima, onde é usado o ponteiro (linhas 20 e 21 do código em C/C++), 
nesta linhas temos acesso ao valor que representa o ponteiro.

A vantagem em termos o valor de ponteiro sem dúvida é que podemos
optimizar muitas operações, mas ao nível de simplicidade de tais códigos
não é tão interessante, já que o próprio optimizador do GCC, nos
oculta diversas questões que teoricamente existem, mas na prática
desaparecem com tal optimização.

de qualquer forma fica o código para uma analise minusiosa de quem
quer dominar a programação do Arduino e partir para níveis mais altos
adotando o AVR e seus macetes como o caminho para um código de qualidade.
 

## Fontes
 
 * [http://www.cs.ust.hk/~dekai/library/ECKEL_Bruce/TICPP-2nd-ed-Vol-one/TICPP-2nd-ed-Vol-one-html/Chapter03.html#Heading134](http://www.cs.ust.hk/~dekai/library/ECKEL_Bruce/TICPP-2nd-ed-Vol-one/TICPP-2nd-ed-Vol-one-html/Chapter03.html#Heading134)
 * [http://www.tfinley.net/notes/cps104/floating.html](http://www.tfinley.net/notes/cps104/floating.html) 