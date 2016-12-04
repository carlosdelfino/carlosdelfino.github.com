---
title: "Alocação e Desalocação de Mémoria em Microcontroladores" 
tags: [Alocação, Desalocação, Malloc, Free, Memoria, Stack, Heap, FiFo, Pipeline]
category: [logicadeprogramacao, Nivel_2]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
  teaser: logica_programacao/fluxograma_planejamento-300x199.jpg
  feature: logica_programacao/algoritmo-jogo-900x673.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Programar hoje em dia para microcontroladores sem dúvida se tornou muito fácil
mas chega uma hora ue se você não cuida bem de sua memória tudo se perde, e não
falo de sua mémoria pessoal, falo da mémoria do microcontrolador.

<!--more--> 

Muitos não percebem até que se deparam com problemas que a memória de um 
microcontrolador é as vezes menos que um milhonésio do que temos em um computador, 
isso mesmo se você tem 1Gb (e é pouco) em seu computador pode considerar que 
terá menos que este valor dividido por um milhão em seu microcontrolador, assim 
um Arduino Mega terá apenas 256KB para o programa e 8Kb para dados, o que é muito
menos. Já o Arduino DUE que usa um ARM tem o dobro de memória para programas
512KB e 10 vezes mais para dados 96KB.

Mas de qualquer forma esta memória é suficiente para muitas aplicações para este
modelo de microcontrolador.

E como gerir melhor esta mémoria?

A linguagem C tem o recurso de alocar e desalocar memória conforme o necessário.
Este recurso até agora foi usado de forma automática, isso se dá quando usamos
variáveis locais em especial, elas serão alocadas e desalocadas conforme se 
entra e sai das funções. Mas isso pode ser pesado quando se precisa de tempo.

Então podemos alocar os espaços conforme a necessidade durante a execução de 
seu código.

Eu particularmente gosto muito de usar variáveis locais dentro de blocos, 
definindo um escopo mais interno para tais mémorias, dentro das funções onde
são usadas, assim elas somente serão criadas quando realmente necessárias.

Outro fator complicador é o uso de Arrays, alocar um Array logo no inicio da 
função ou como global irá fazer com que este espaço de memória esteja sempre
separado para uso, o que pode ser um desperdicio, mas alocar em tempo de execução
pode trazer surpresas desagradáveis. Como o problema que infrentei com arrays
grandes eum projeto de georeferenciamento com o Arduino Mega, na época não 
existia o Ardduino Due, e eu precisava economizar muita memórria pois lidava com
muitos dados simultaneamente.

O Arduino então trava de tempo em tempo, e o problema estava no fato dele não 
conseguir memória continua para o array.

Sim este é um dos problemas de alocação e desalocação constante. A memória
do microcontrolador tende a ficar fragmentada cheia de buracos livres, porém
não há um espaço continuo para criar uma alocação conforme o tipo desejado
então apesar de no total haver memória, na prática ela não utilizável.

O Alocador de memória é construido de forma a tentar ótimizar ao máximo a aloação
tentando reorganizar o heap assim a memória não fica cheia de buracos, mas isso
é complicado.

<figure>
<img src="/images/programacao/ccplusplus/malloc-std.png"></img>
<figcaption>Visão Geral da Mémoria de um microcontrolador programador com C</figcaption>
</figure>
Vamos ver como a função Malloc funciona no Arduino Mega e UNO:



