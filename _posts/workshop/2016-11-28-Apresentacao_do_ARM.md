---
title:  Apresentação da ARM
date: 2016-11-29 01:10:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, Apresentação]
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

Do que se trata o nome ARM? é uma empresa um produto ou apenas um nome fantasia?

<!--more-->

<figure>
<img src="/images/arm/arm-cortex-a15-350x200.png/images/arm/arm-cortex-a15-350x200.png"></img>
</figure>

ARM é o nome da empresa que dá origem a série de processadores mais utilizaod no mundo para dispositivos móveis, é bem provável que seu celular tenha um processaador baseado na Arquitetura definida pela ARM.

E porque dizer definido pela ARM, e não produzido?

A ARM é um empresa que apenas detem a propriedade intelectual da arquitetura para se produzir os processadores e recursos que envolvem seu funcionamento, incluindo alguns dispositivos auxiliares como acontece nos microcontroladores.

A Empresa ARM portanto, juntamente com fabricantes define como uma determinada família de processadores deve funcionar e ser construido, sendo a detentora da tecnologia, e licensiando a mesma para todos os fabricantes que se mostram qualificados a produzir os chips com este processadores e seus periféricos e interces de comunicação.

A Empresa ARM atua em conjunto com grandes fabricantes de celulares, tablets, computadores e outros dispositivos microcontrolados, e também fabricantes apenas de chip.

A ARM produz especificações arquiteturais de processadores desde dos mais simples processadores para uso em microcontroladores que concorrem com os microcontroladores 8-bits já conhecidos de nosso mercado brasileiro, porém usa sempre arquitetura 32bit ou superior, como no caso dos processadores para uso em celulares, tablets e até mesmo servidores, neste último compostos por dezena ou até mesmo centenas de núcleos que permitem umd esempenho extremo e baixissimo consumo de energia..

As Famílias de processadores se dividem em 3, os que são destinados a Aplicações como servidores, celulares e tablets, são empoderados pelos processadores da família Cortex-A; os destinado ao uso em sistemas de alto risco e que demandam tempo de resposta imediato como sistemas Real Time usado em Freios ABS, Carros Autonomos, Industria onde há vidas humanas em riscos e equipamentos hospitalares, são estes os microcontroladores da família Cortex-R; e finalmente nosso foco, os processadores da Família Cortex-M destinados a microcontroladores, como o usado no Arduino DUE, Arduino Zero, Mapple entre outros.

Todos os precessadores ARM são no mínimo 32bit e 64bit, sendo este ultimo usado apenas na arquitetura para processadores da familia Cortex-A, usados para aplicações.

Há também o conseito arquitetural, ou seja cada familia usa uma arquitura ou algumas arquiteturas.

Temos 3 principais arquiteturas muito usadas, são a arquitetura ARMv6, ARMv7 e ARMv8, cada uma delas agrupadas conforme a família que a usa, portanto os Cortex-A usam a arquitetura ARMv7-A e ARMv8-A, os processadores Cortex-M como o Cortex-M0, Cortex-M0+ usam a arquitetura ARMv6-M, Os processadores Cortex-M3 e Cortex-M4 tema de nosso workshop, usa a Arquitetura ARMv7-M, e os novos dois processadores focados no mercado IoT o Cortex-M23 e Cortex-M33 usam a arquitura ARMv8-M.

Não entraremos aqui nos detalhes de cada arquitura e os procesadores ARM, apenas os usaremos em nosso workshop.

Abaixo está um gráfico de como os processadores foram distribuidos e suas aplicações, este gráfico não apresenta ainda os processadores Cortex-M33, Cortex-M23 e Cortex-A53 (este usado no NanoPi):

<figure>
<img src="/images/arm/processadores-arm-performance-vs-aplicacao.png"></img>
<figcapture></figcapture>
</figure>
