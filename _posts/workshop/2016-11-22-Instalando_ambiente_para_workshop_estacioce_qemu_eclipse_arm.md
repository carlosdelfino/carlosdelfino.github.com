---
title: "Instalando ferramentas e preparando ambiente"
categories: [workshop,estacio_ceara,2016_2]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi]
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

O objetivo deste post é registrar os passos para preparar o ambiente para o Workshop de uso QEMU, Eclipse e ARM na estácio do Ceará.

<!--more-->

Primeiro passo é baixar o GCC para ARM, o mesmo se chama GCC ARM None EABI. e deve ser obtido para o [Windows 32bits Clicando Aqui](https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-eabi-5_4-2016q3-20160926-win32.exe). faça a instalação do pacote na pasta: `C:\GNU_Tools_ARM_Embedded\5.4 2016q3`.

Em seguida instale o MSys2 escolha a plataforma [32-Bit](http://repo.msys2.org/distrib/i686/msys2-i686-20161025.exe) ou [64-Bit](http://repo.msys2.org/distrib/x86_64/msys2-x86_64-20161025.exe) (em um dos links) conforme seu ambiente.

Instale o MSys2 no diretório `c:\msys` para arquitetura 32-bit ou `c:\msys64`para arquitetura 64-bit.

Em seguida abra o shell executando o script `msys2_shell.cmd` que será encontrado na pasta onde foi instalado o MSys2 e execute os seguintes comandos, se a tela ao finalizar o comando, não se preocupe é normal, feche normalmente mesmo com alerta, e abra novamente e execute o próximo.

## Resumo para facilitar

Eu gravei tudo no mega drive para facilitar para que posssam baixar posteriormente os aquivos usados no Workshop.

[Também tem estes post que ajuda na instalação do MSys2](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-1/)

## Páginas Oficiais

 * https://launchpad.net/gcc-arm-embedded
 * http://gnuarmeclipse.github.io/install/
 * http://msys2.github.io/
