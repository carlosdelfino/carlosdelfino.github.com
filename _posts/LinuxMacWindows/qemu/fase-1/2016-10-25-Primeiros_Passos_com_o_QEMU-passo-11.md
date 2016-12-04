---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-11/"
title: "Primeiros Passos com o QEMU, Passo 11" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS]
categories: [EmulacaoEVirtualizacao, QEMU, Compilando]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: embarcados/nanopi-m3-03-1024x445.png
 teaser: embarcados/nanopi-m3-03-300x174.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Neste passo, que ainda não é o final, chegamos finalmente ao objetivo que é compilar e instalar o qemu personalizado.

<!--more-->

Apesar de chamar o QEMU de personalizado, não fizemos alteração alguma em seu código para que faz jus a este apelido, porém é o caminho para os primeiros passos com o QEMU e sua personalização, sem conseguir compreender o seu contexto de compilação fica difícil partir para qualquer personalização.

Portanto agora podemos assim colocarmos o QEMU funcionando com algum exemplo partir para interferência em seu código buscando resultados mais diretos e relacionados ao nosso objetivo.

O primeiro passo será unir o trabalho de Liviu ao QEMU original mantendo assim um controle das customizações para Cortex-M, facilitando que possamos criar nossas placas de prototipação virtuais. Como dissemos a primeira placa será o Arduino DUE e o Maple, depois partiremos para o AVR e finalmente testaremos o xtensa para ESP.

## Compilando o QEMU

Execute os seguintes comandos para começar a preparar o ambiente. Já considero aqui que está sendo mantido as variáveis de compilação adotada no último passo, portanto a partir deste ponto não irei mais repetir as tarefas anteriores, não se esqueça de atualizar o path para encontrar as ferramentas em `/mingw64/bin`.


```sh
cd ~/qemu-delfino
./autogen.sh
```

Atualize a variável `CFLAGS`:

```sh
~/qemu-delfino/ $ export CFLAGS=`sdl2-config --cflags --libs`
```

Finalmente podemos compilar o código com os seguintes comandos.

Fique atento a definição das variáveis, mesmo que já tenha definido antes, certifique todas estão corretas.

```sh
~/qemu-delfino/ $ cd ../build
~/qemu-delfino/build $ mkdir qemu
~/qemu-delfino/build $ cd qemu
~/qemu-delfino/build/qemu $  ../../configure \
         --prefix=/mingw64 \
         --cross-prefix=x86_64-w64-mingw32- \
         --disable-docs \
         --disable-bzip2 \
         --disable-lzo \
         --disable-snappy \
         --target-list="x86_64-softmmu,arm-softmmu,xtensaeb-softmmu,xtensa-softmmu"

~/qemu-delfino/build/qemu $ make
~/qemu-delfino/build/qemu $ make install
```
Como podem ver pela diretiva `target-list`, serão compiladas apenas as arquiteturas x86_64, ARM, xtensaeb e xtensa, futuramente estarei adicionando também AVR. em ARM e xtensa respetivamente uma Placa Arduino e um ESP-01 para testes.


[Estamos trabalhando no passo 11.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-11)

## Sites das bibliotecas, frameworks e tudo usado neste projeto

 * http://gnuarmeclipse.github.io/qemu/
 * http://qemu.org/
 * https://carlosdelfino.eti.br/qemu
 * http://www.zlib.net/

### Outras fontes de referência

 * http://preshing.com/20141119/how-to-build-a-gcc-cross-compiler/
 * http://pt.stackoverflow.com
 * http://gcc.gnu.org 
 * https://www.gnu.org/software/autoconf/manual/autoconf-2.65/html_node/Specifying-Target-Triplets.html
 * https://www.betaarchive.com/forum/viewtopic.php?t=28834
 * https://en.wikibooks.org/wiki/QEMU/MinGW
 * https://www.libsdl.org/extras/win32/mingw32/README.txt
 * https://www.betaarchive.com/forum/viewtopic.php?t=28834
 * https://en.wikibooks.org/wiki/QEMU/MinGW
 * https://wiki.libsdl.org/Installation
 * http://qemu-project.org/Hosts/W32#Cross_builds

## Repositórios relacionados

 * git@github.com:qemu/qemu.git
 * git@github.com:gnuarmeclipse/qemu.git
 * git@github.com:beckus/qemu_stm32.git
 * git@github.com:carlosdelfino/qemu.git
 * git@github.com:carlosdelfino/sdl.git
 * git@github.com:madler/zlib.git
 * git@github.com:libffi/libffi.git
 * git://git.savannah.gnu.org/gnulib.git
 * git://git.savannah.gnu.org/gettext.git
 * git://git.savannah.gnu.org/libiconv.git
 * git://git.gnome.org/gtk+
 * git://git.gnome.org/glib
 * git://anongit.freedesktop.org/pkg-config

