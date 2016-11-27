---
title: "Como Instalar os Templates para Nosso Workshop"
date: 2016-11-29 03:10:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, templates, keyl, stm32f3,stm32f4,stmicroeletronics]
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

Para usar o Plugin GNU ARM Eclipse o ideal é que seja baixado os templates de cada microprocessador.

<!--more-->

Os Templates são layouts e exemplos de códigos, e também possuem manuais e biblioteca de funções para compilação de códigos de forma otimizada para o microcontrolador escolhido, além de permitir que nos concentramos no nosso algortimo sem nos procuparmos com detalhes do hardware já que é usado o [framework CMSIS](/arm/cortex-m/CMSIS) que abstrai os detalhes do hardware da programação que é nosso  objetivo.

A Instalação dos pacotes de templates para microcontroladores e para módulos de prototipação deve normalmente ser feita diretamente pelo Eclipse, através da interface gerenciamento de pacotes que é acessível clicando no icone _"Make the C++ Packs Perspective Visible"_ fazendo a atualização dos cabeçalhos e poseteriormente o download de cada template.

Os templates, além da bibliteca de funções defindas pelo Framework CMSIS, é também feito o Download dos datasheets, em pdf, de cada processador e Módulos, com isso temos muitas informações úteis ao desenvolvimento naquela plataforma.

Já na tela de gerenciamento (Perspectiva) dos pacotes CMSIS, basta clicar no icone atualizar, mas como já teremos um pacote preprocessador para ajudar no download faremos apenas a título de prática, já que tal pacote tem mais de 500Mbs de dados úteis.



