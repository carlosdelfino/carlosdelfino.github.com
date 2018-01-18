---
title: Aprendendo a Programar para ARM com QEMU - O Início
excerpt: "A melhor coisa para quem quer começar a aaprender a programar é ter uma ambiente controlado e que não haja nenhum risco de perda, e não tive dúvida que usar o QEMU para emular os Microcontroladores ARM seriam uma excelente escolha." 
categories: [HelloWorld,ARM]
tags: [Arduino,  DUE, ARM, SAMD21, ATmel, BareMetal, Bare Metal, QEMU, Programação, Lógica, BootLoader, Programando sem ter um ARM]
layout: article
comments: true
share: true
ads:
 show: true
toc: true
feature:
 index: true
 category: true
tagcloud: true
coinbase:
  show: true
feature: 
  index: true
  category: true
---

Porém iniciei meus estudos do QEMU  para ARM faz um a dois meses e não 
estou tendo muito sucesso ainda. o QEMU tem muitas funcionalidades por 
serem implementadas a nível do core do microcontrolador e por exemplo
estou tendo dificuldades em usar instruções Thumb para Cortex-M3.

Claro considerando a data de hoje ainda tenho muito que aprender, seja 
no que se refere a Arquitetura ARM ou apenasdo QEMU. E isso vai fazer
com qeu adie mais um pouco a publicação de artigos sobre o uso do QEMU
com Microcontroladores ARM.

Irei postar em breve um pequeno artigo demostrando como usar o QEMU
conforme sugerido pelo artigo publicado no link [Hello world for bare metal ARM using QEMU](https://balau82.wordpress.com/2010/02/28/hello-world-for-bare-metal-arm-using-qemu/#comment-516),
fiz diversos testes e tive sucesso com este metodo, porém não funciona 
como alguns sugerem com a arquitetura Cortex-M3, ainda não descobri
o que estou errando, já fiz as correções do uso da instrução LDR e 
outros ajustes de parametros para adquar a nova arquiteutra, mas sem
sucesso.

Caso queiram apresentar sugestões por favor usem os comentários abaixo.