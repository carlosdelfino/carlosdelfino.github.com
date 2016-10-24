---
title: "Primeiros Passos com o QEMU, parte 3" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, ]
categories: [Emulação e Virtualização]
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

### Compilando a Biblioteca gettext

Gettext para ser compilado na versão 0.19.8.1 precisa de uma versão especifica do GNULib, portanto iremos primeiro atualizar nosso repositório pra esta versão com o seguinte comando:

```sh
gitclone/qemu-delfino/ $ cd gnulib
gitclone/qemu-delfino/gnulib/ $ git checkout 6f9206d --force
```

Agora podemos prosseguir com o gettext, como ele já está como submódulo, basta atualizá-lo com os seguintes comandos:

```sh
gitclone/qemu-delifno/ $ git submodule update --init gettext
gitclone/qemu-delfino/ $ cd gettext
gitclone/qemu-delfino/gettext $  git checkout v0.19.8.1
```

precisamos atualizar as configurações antes de executá-las para criar o `Makefile` e então compilar o projeto no diretório de trabalho.

```sh
gitclone/qemu-delfino/gettext $  GNULIB_SRCDIR=../gnulib \
            GNULIB_TOOL=../gnulib-tool \
            ./autogen.sh
```


```sh
~/qemu-delfino/gettext $ cd ../build 
~/qemu-delfino/build/ $ mkdir gettext
~/qemu-delfino/build/ $ cd gettext
~/qemu-delfino/build/gettext $  ../../gettext/configure \
        --host=x86_64-w64-mingw32 \
        --build=x86_64-w64-mingw32 \
        --prefix=/mingw64 \
        --with-gnu-ld \
        --without-bzip2 \
        --without-xz \
        --without-emacs \
        --without-lispdir \
        --without-cvs \
        --disable-doc \
        --disable-java \
        --disable-native-java \
        --disable-c++ \
        --disable-libasprintf \
        --disable-openmp \
        --disable-csharp \
        --enable-threads=win32 \
        --enable-relocatable
```
E finalmente podemos compilar o gettext.

```sh
~/qemu-delfino/build/gettext $ make
~/qemu-delfino/build/gettext $ make install
```






