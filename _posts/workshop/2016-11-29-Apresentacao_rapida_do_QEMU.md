---
title: Apresentação rápida do QEMU
date: 2016-11-29 02:20:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, pranejamento]
layout: article-workshop-estacio-2016-1
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
coinbase:
 show: true
---

QEMU um emulador de alto desempenho para criação de hardware virtual.

<!--more-->

> A physicist, an engineer, and a computer scientist were discussing the nature of God. “Surely a Physicist,” said the physicist, “because early in the Creation, God made Light; and you know, Maxwell's equations, the dual nature of electromagnetic waves, the relativistic consequences...” “An Engineer!,” said the engineer, “because before making Light, God split the Chaos into Land and Water; it takes a hell of an engineer to handle that big amount of mud, and orderly separation of solids from liquids...” The computer scientist shouted: “And the Chaos, where do you think it was coming from, hmm?”
—Anonymous

Não que eu queira dizer que o QEMU seja um caos, pelo contrário, ele é sem dúvida uma excelente opção quando se precisa lidar com diversos modelos de máquinas diferentes. Sua capacidade de emular tanto o processador como o hardware nos permite criar uma infidade de modelos de máquinas sem um gasto excessívo com novos equipamentos.

O QEMU além de emular maquinas ele também virtualiza sobre o hardware existentes novas instâncias de um sistema operacional,  e quando emulando hardware premite até mesmo aplicativos bare-metal quando por exemplo com microcontroladores e até sobre processadores ARM ou outros.

O Desempenho do QEMU é excelente, e quase equivalente ao desempenho do hardware nativo que faz o papel de host, isso se deve a estratégia de tradução dinâmica das instruções Assembly de uma arquitura (ISA) para outra diretamente.

Porém desenvolver um novo hardware para o QEMU não é tão simples assim além do domínio da arquitetura do processador envolvido, é preciso compreender bem como se programar para o QEMU e criar novos **Targets**, a programação do QEMU é feita em C, e utiliza amplamente o recurso de macros de pré processamento, mas o mais interessante é que temos grandes profissionais dispostos a fazer tal trabalho e até mesmo nos orientar como chegarmos a um nível para que possamos contribuir.

O maior exemplo para um bom trabalho para emulação de hardware é o trabalho desenvolvido pelo Engenheiro Senior de Software Liviu Iunesco, esponsável pela criação do **TArget** que permite rodar emuladores de placas de prototipação da STMicroeletrônics, as placas Discovery tanto para Cortex-M3 como para Cortex-M4.

Tais **targets** emulados ainda não são capazes de ter 100% de funcionalidade, mas hoje já temos as principais instruções ARM para Cortex-M3 e Cortex-M4 sendo interpretadas, e também já temos a caminho novos hardwares funcionais, hoje apenas os LEDS (4 coloridos) funcionam.

Em particular estou comprometido em desenolver a porta serial, emuladores para comunicação via rede, além de pesquissar sobre o uso de Multicores ARM Cortex-M e Cortex-R, além do uso do xTensa para ESP 8266, um longo caminho, que pode levar tempo dependendo da dedicação e envolvimento da comunidade  amigos brasileiros no projeto.

Neste Workshop iremos usar portando o QEMU para descobrirmos como darmos nosso sprimeiros passos e compreender como programar efetivamente e usando recursos profissionasi para Cortex-M3 e Cortex-M4.

O QEMU também poderá ser usado para programar para AVR, estou responsável para agregar o Código de um **TArget** AVR para que possa também ser usado no QEMU com o plugin AVR para Eclipse.

Hoje oque mais tem atrasado para o desenvolvimento com o QEMU é a compilação da biblioteca SDL pois esta tem apresentado problemas em meu ambiente, mas assim que resolver tal problema, integrarei o AVR e posteriormente irei unir esforços com o Livius Iunesco para produzir novos recursos para o Cortex-M.

