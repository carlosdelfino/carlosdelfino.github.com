---
title: "Hello World ARM Cortex-M4 usando o QEMU"
date: 2016-11-29 03:30:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, programação, Hello World Cortex-M4, Hello World ARM]
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

Veremos agora como escrever um primeiro código apenas para piscar o LED em uma placa que utiliza o Cortex-M4.

<!--more-->

O código que iremos escrever será para uma placa que utiliza o microcontrolador da família [STM32F407xx](/arm/cortex-m3/stm/STM32F407XX), que é um [ARM](/arm) [Cortex-M4](/arm/cortex-m4), a palca é um modelo [STM32F4-Discovery](/arm/cortex-m4/stm/STM32F4-Discovery) da [STMicroeletronics](/arm/cortex-m4/STM/) e usa exatamene o processador [STM32F407VG](/arm/cortex-m3/stm/STM32F407XX/STM32F407VG).

## Criando o Projeto no Eclipse

Abra o Eclipse e em seguida a janela para criar um novo projeto, selecione o projeto do tipo _"C++ Project"_, clique em "Next", na janela seguinte selecione na arvore _"Project type:"_,  na pasta _"Executable"_, o template _"STM32F4xx C/C++ Project"_, na parte direita em _"Toolchains:"_ selecione _"Cross ARM GCC"_, clique em *"Next"*. na próxima janela deixe as opções selecionadas com o padrão forneceido, apenas mude a opção _"Use system calls"_ para _"Semihosting (POSIX system calls via host)"_, clique em *"Next"*, deixe na nova tela todas as pastas sugeridas como estão, continue com *"Next"*, na próxima janela deixe também como o padrão, e prossiga com *Next*, confirme que nesta tela o diretório informado é o correto para a instalação do GNU ARM GCC que definimos na instalação do plugin para nosso workshop, esta configuração foi préviamente feita durante a instalado [conforme este tutorial (clique no link)](workshop/estacio_ceara/2016_2/instalando_o-ambiente_base_ferramentas_e_preparando_o_ambiente_de_desenvolvimento_-_estacio_do_ceara/); Agora basta clicar em _"Finish"_.

Um projeto será criado com o template para processadores da família [STM32F407xx](/arm/cortex-m3/stm/STM32F407XX), se ainda não tiver um template na lista a seguir, siga para o artigo [Como Instalar os Templates](/workshop/estacio_ceara/2016_2/Como_Instalar_os_Templates_para_Nosso_Workshop/).

