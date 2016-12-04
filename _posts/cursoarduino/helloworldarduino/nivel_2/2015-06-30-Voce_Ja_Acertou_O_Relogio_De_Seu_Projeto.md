---
title: "Você já acertou o relógio de seu projeto com o Arduino?" 
tags: [Relógio Atomico, TAI, UTC, TU1, Relógio de Quartzo, Relógio Mecanico, Relógio]
category: [HelloWorldArduino, Nivel 2]
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
  feature: redes_protocolos/tcpipstackprotocol-1024x505.png
  teaser: redes_protocolos/protocolstacks-500x469.jpg
tagcloud: true
coinbase:
 show: true
--- 

Um segundo a mais no tempo de seu dia, isso afeta sua aplicação Arduino?

<!--more-->

Se de alguma forma você trabalha com o tempo real, ou seja com pelo menos 
horas e minutos sincronizados com o mundo externo, seja via um RTC ou seja 
via uma conexão de rede ou mesmo através de um módulo GPRS/GSM ou um GPS 
você precisa avaliar até onde esta alteração no tempo que ocorre hoje afeta 
sua aplicação.

A mudança se faz necessária porque na prática o planeta terra não gasta 
exatamente 24 horas para girar em torno de si mesma (seu próprio eixo), 
portanto de tempos em tempos é preciso que seja feito um pequeno ajuste de 
tempo.

Em todo o mundo há servidores que contabilizam o tempo com base em um relógio 
atómico que tem segundos precisos que sempre são contatos uniformemente 
(conhecido como relógio UTC, no Brasil trabalhamos com UTC-3 ou seja a hora 
contabilizada por UTC menos 3 horas), porém também há com base em observações 
astronômicas um relógio natural da terra, que varia a duração de seus segundos 
com base na rotação da terra, já que esta não é uma rotação uniforme.

Se houvesse este ajuste, com o passar do tempo, os relógios UTC (seja como 
forem construídos, mecânicos ou digitais por mais precisos que sejam) estariam 
marcando o meio dia antes do sol chegar ao meio do céu, e portanto as horas da 
noite passariam a contabilizar ainda dia, como ocorre em alguns países quando 
acionam o horário de verão, mas claro isso levaria muitos anos para acontecer.

Por tanto é importante prever em seu sistema esta correção caso ele não seja 
automaticamente ajustado com uma fonte externa. 

Se seu projeto com o Arduino​ usa GSM/GPRS, GPS ou se conecta a internet a um 
servidor NTP para ajustar a hora, é bem provável que você não terá que se 
preocupar com isso, porém se você usa um chip RTC para dar apoio a 
contabilização de horas este precisará receber um ajuste no passar desta noite 
do dia 30 de junho para 1 de julho.