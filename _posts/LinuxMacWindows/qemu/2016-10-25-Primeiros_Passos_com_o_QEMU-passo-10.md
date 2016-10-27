---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-10/"
title: "Primeiros Passos com o QEMU, Passo 10" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, pixman, xTensa, AVR]
categories: [EmulacaoEVirtualizacao, QEMU, Compilando]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
  teaser: programacao/ccplusplus/programacao-660x300.png
  feature: programacao/ccplusplus/programacao-660x300.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

Pixman é importante para o QEMU para manipular de pixels em imagens, fornecendo recursos para composição e rasterização de trapezoides. 

<!--more-->

O Pixman é importante apenas para versões do qemu acima de 1.3.

Para obter em nosso repositório use o comando:

```sh
git submodule update --init pixman
```


Execute os seguintes comandos para começar a preparar o ambiente.

```sh
cd pixman
./autogen.sh
```
 

Agora vamos preparar as variáveis de ambiente para nossa compilação.

```sh
~/qemu-delfino/pixman $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/pixman $ export GNULIB_TOOL="~/qemu-delfino/gnulib-tool"
~/qemu-delfino/pixman $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/pixman $ export GLIB_LIBS="-lglib-2.0"
~/qemu-delfino/pixman $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
~/qemu-delfino/pixman $ export GLIB_LIBS=""
~/qemu-delfino/pixman $ export LIBFFI_CFLAGS='-I /mingw64/lib/libffi-3.99999/include'
~/qemu-delfino/pixman $ export LIBFFI_LIBS=-lffi
```

Fique atento a definição das variáveis, mesmo que já tenha definido antes, certifique todas estão corretas.

```sh
~/qemu-delfino/pixman $ cd ../build
~/qemu-delfino/build $ mkdir pixman
~/qemu-delfino/build $ cd pixman
~/qemu-delfino/build/pixman $ ../../glib/configure \
            --prefix=/mingw64 \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target=x86_64-w64-mingw32 
~/qemu-delfino/build/pixman $ make
~/qemu-delfino/build/pixman $ make install
```



[Estamos trabalhando no passo 11.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-11)