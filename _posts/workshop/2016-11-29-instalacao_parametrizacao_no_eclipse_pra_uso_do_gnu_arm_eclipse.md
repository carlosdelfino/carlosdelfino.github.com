---
title: "Instalação e Parametrização no Eclipse para uso do GNU ARM Eclipse"
date: 2016-11-29 02:20:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, Instalação, Parametrização]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

Como instalar o plugin _**GNU ARM Eclipse**_, as parametrizações necessárias para uso dele com o QEMU e OpenOCD.

<!--more-->

Iremos agora instalar o Plugin _*"GNU ARM Eclipse"*_ Criado por Livius Iunesco, um Engenheiro de Software Sénior, especializado em instrumentação aeronáutica. Ele tem diversos projetos de software relacionados a arquitetura ARM e é uma excelente fonte de conhecimento, Ele é muito aberto ao dialogo e a troca de conhecimento neste contexto e seus projetos são opensource. 

Sou colaborar em seu projeto em especial na parte de tradução e testes do uOS, um Sistema Operacional para aplicações em Tempo Real com embarcados, este projeto é minha continuidade do DuinOS.

## Instalando o GNU ARM Eclipse

Veja para nosso Workshop não haverá tempo para se baixar todos os Plugins necessários da Internet, portanto foram deixados em cada maquina uma cópia de instalação no desktop ou na pasta downloads, veja como proceder então para instalar este plugin é muito simples apesar de ser vários plugins, todos em um mesmo pacote.

No Windows, abra o Menu, _"Help"_, _"Install New Software"_, irá aparecer uma nova janela e poderá instalar novos softwares fácilmente pesquisando na caixa _"type filter text"_, ou informando um caminho para o pacote local ou na internet, este será baixado e apresentado na caixa abaixo para ser selecioando.

Então como faremos a instalação local, clique no botão _"Add"_, assim, será apresentado uma nova janela, pedindo o nome do pacote que será usado e o caminho para o novo pacote, em seguida clique no botão, _"Arquive"_, selecione o pacote que será usado, provalmente estará na pasta *"Downloads"* do perfil de usuário que está usando ou no seu Desktop. Clique finalmente em OK e será apresentar a lista de pacotes disponíveis neste arquivo.

Nesta lista você pode até selecionar todos os pacotes, mas iremos usar apenas os seguntes pacotes neste Workshop:

 * GNU ARM C/C++ Cross Compiler
 * GNU ARM C/C++Documentation (Placeholder)
 * GNU ARM C/C++ Generic Cortex-M Project Template
 * GNU ARM C/C++ J-Link Debugging
 * GNU ARM C/C++ OpenOCD Debugging
 * GNU ARM C/C++ Packs (Experimental)
 * GNU ARM C/C++ QEMU Debugging
 * GNU ARM C/C++ STM32Fx Project Templates
 
Ao clicar em OK, será apresentada a lista que selecionou, e confirme clicando em "Next", a próxima tela lhe perguntará se aceita os termos da licença que é baseada na *"Eclipse Foundation Sofware User Agreement", e então poderá clicar em *"Finish"*, o Eclipse cuidará de tudo para você.

No final da instalação será perguntado se você aceitar instalar alguns softwares que não estão assinados pelo Eclipse, isso é normal, pois nem todo plugin é homologado, mas este é de fonte confiável e pode instalar sem problemas. Para maior garantia sempre baixe o pacote direto da fonte, fizemos desta forma para agilizar durante o Workshop.

Reinicialize o Eclipse e o Plugin estará instalado. Se você seguir todos os passos que dei não terá nenhum problema.
