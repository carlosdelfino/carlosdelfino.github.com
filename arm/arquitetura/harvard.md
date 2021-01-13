---
permalink: /arm/arquitetura/havard/
title: Arquitetura Harvard
tags: [ARM, Tecnologias, Memoria, Proteção, Unidade, Arquitetura, Cortex-A, Cortex-R, Cortex-M, Harvard]
layout: glossarylist
categories: [ARM, arquitetura]
share: true  
toc: true
comments: true
feature:
 category: true
 index: false
tagcloud: true
ads:
 show: true
image:
 feature: arm/Cortex-M33-Arquitetura-800x846.png
 teaser: arm/logo-ARM-370x205.png
---

O nome Aquitetura Harvard vem do computador baseado em relês Harvard Mark I. 

<!--more-->

A caracteristica mais óbvia da Arquitetura Harvard é que ele tem sinalização fiscamente separada e armazenamento de código e dados em memórias separadas também. Assim é possível acessar a memória de programa e a memória de dados simultaneamente. Tipicamente, a memória de código (ou programa)  é somente leitura e a memória de dados é ready-write (leitura e escrita). Portanto, é impossível o conteúdo do programa ser modificado por si mesmo. (há alternativas para tal questão).

A Arquitetura Harvard é bastante usada em microcontroladores que tem códigos fixos no estilo baremetal que são gravados em memória não volatil pelo desenvolvedor e raramente são alterados após colocados em produção, as memórias usadas em microcontroladores são tipicamente memórias do tipo flash, podem ser regravadas um grande número de vezes fácilmente, mas para que o próprio programa seja capaz de faze-lo é preciso que se coloqueo processador em um modo de execução típico para tal atualização. Normalmente isso acontece logo após o reset, o que permite a precarga de um código chamado BootLoader.

## Fontes:

* https://en.wikipedia.org/wiki/Harvard_architecture
