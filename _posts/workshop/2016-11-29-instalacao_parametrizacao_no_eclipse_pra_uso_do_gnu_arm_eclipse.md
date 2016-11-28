---
title: "Instalação e Parametrização no Eclipse para uso do GNU ARM Eclipse"
date: 2016-11-29 02:20:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, Instalação, Parametrização]
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

Como instalar o plugin _**GNU ARM Eclipse**_, as parametrizações necessárias para uso dele com o QEMU e OpenOCD.

<!--more-->

Iremos agora instalar o Plugin _*"GNU ARM Eclipse"*_ Criado por Liviu Ionesco, um Engenheiro de Software Sénior, especializado em instrumentação aeronáutica. Ele tem diversos projetos de software relacionados a arquitetura ARM e é uma excelente fonte de conhecimento, Ele é muito aberto ao dialogo e a troca de conhecimento neste contexto e seus projetos são opensource. 

Sou colaborar em seu projeto em especial na parte de tradução e testes do uOS, um Sistema Operacional para aplicações em Tempo Real com embarcados, este projeto é minha continuidade do DuinOS.

## Instalando o GNU ARM Eclipse

Veja para nosso Workshop não haverá tempo para se baixar todos os Plugins necessários da Internet, portanto foram deixados em cada maquina uma cópia de instalação no desktop ou na pasta downloads, veja como proceder então para instalar este plugin é muito simples apesar de ser vários plugins, todos em um mesmo pacote.

No Windows, abra o Menu, _"Help"_, _"Install New Software"_, irá aparecer uma nova janela e poderá instalar novos softwares fácilmente pesquisando na caixa _"type filter text"_, ou informando um caminho para o pacote local ou na internet, este será baixado e apresentado na caixa abaixo para ser selecioando.

Então como faremos a instalação local, clique no botão _"Add"_, assim, será apresentado uma nova janela, pedindo o nome do pacote que será usado e o caminho para o novo pacote, em seguida clique no botão, _"Arquive"_, selecione o pacote que será usado, provalmente estará na pasta *"Downloads"* do perfil de usuário que está usando ou no seu Desktop. Clique finalmente em OK e será apresentar a lista de pacotes disponíveis neste arquivo.

Nesta lista você pode até selecionar todos os pacotes, mas iremos usar apenas os seguntes pacotes neste Workshop:

 * GNU ARM C/C++ Cross Compiler
 * GNU ARM C/C++ Documentation (Placeholder)
 * GNU ARM C/C++ Generic Cortex-M Project Template
 * GNU ARM C/C++ Packs (Experimental)
 * GNU ARM C/C++ QEMU Debugging
 * GNU ARM C/C++ STM32Fx Project Templates
 
Ao clicar em OK, será apresentada a lista que selecionou, e confirme clicando em "Next", a próxima tela lhe perguntará se aceita os termos da licença que é baseada na *"Eclipse Foundation Sofware User Agreement", e então poderá clicar em *"Finish"*, o Eclipse cuidará de tudo para você.

No final da instalação será perguntado se você aceitar instalar alguns softwares que não estão assinados pelo Eclipse, isso é normal, pois nem todo plugin é homologado, mas este é de fonte confiável e pode instalar sem problemas. Para maior garantia sempre baixe o pacote direto da fonte, fizemos desta forma para agilizar durante o Workshop.

Reinicialize o Eclipse e o Plugin estará instalado. Se você seguir todos os passos que dei não terá nenhum problema.

## Parametrização e Inicial do Eclipse

Neste ponto é fundamental que o GCC para ARM já esteja instalado, no caso esta instalação já foi feita pois é simples e não necessita muitos detalhes, mas caso queira ver como foi o processo sugiro que leia o artigo [Instalando o ambiente base, ferramentas e preparando o ambiente de desenvolvimento](/workshop/estacio_ceara/2016_2/Instalando_ambiente_para_workshop_estacioce_qemu_eclipse_arm/)

Se você tem seguido as orientações que estou apresentando neste workshop não terá nenhuma surpresa, mas se não segui, você pode ter surpresas aqui, discutiremos isso no Workshop ao vivo.

Entre na janela de preferências do Eclipse, siga a arvore de parametros pelo caminho _"C/C++"_, _"Build"_, _"Global Tools Paths"_, será apresentado a tela para informar o caminho para as ferramentas que irão auxiliar na construção dos códigos, e a pasta onde foi instalado o GNU GCC (o Toolchain"

Ao lado da caixa para instalar o _"Build tools folder"_, clique no botão _"Browser..."_ e selecione na pasta onde foi instalado o Msys2, a pasta que estão os binários que nos ajudaram a compilar nossos nossos softwares `usr\bin`. Seu path ficará provalmente da seguinte forma: `c:\msys64\usr\bin`.

Deixe as demais opções conforme o padrão, _"GNU Tools for ARM Embedded Processors"_ e vamos agora indicar em qual pasta está o GNU GCC para ARM que já foi também instalado no processo apresentado no artigo sugerido acima. Clique no botão _"Browser..."_ ao lado da caixa de texto que permite informar o _"Toolchain folder"_. Click em _"Apply"_ e feche a janela clicando no botão _"Ok"_.

## Parametrizando para uso com o QEMU

Na tela de configuração do Eclipse siga a arvore de parametros e vá até _"Run/Debug"_, _"QEMU"_, na janela informe o PATH onde o QEMU foi instalado, caso o Eclipse já tenha encontrado confirme ser o diretório usada durante a nossa instalação.

![Parametrização do QEMU no Eclipse](/images/workshop/estaciodoceara/siconect/2016-2/configurando-qemu-gnu-arm-eclipse.png)
