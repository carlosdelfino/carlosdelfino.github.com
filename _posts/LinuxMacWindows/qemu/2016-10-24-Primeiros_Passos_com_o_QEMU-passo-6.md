---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-6/"
title: "Primeiros Passos com o QEMU, Passo 6" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, ]
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

Bem, fiz todos os testes necessários para se ter sucesso com o GetText, segui alguns caminhos não foram bons e isso é um aprendizado muito valioso, pois permite entendermos como tudo é feito e como deve realmente ser feito.

### Compilando a Biblioteca gettext

O Gettext é uma biblioteca muito útil para internacionalização da aplicação, com ela podemos ter as mensagens de nossa aplicação traduzidas para diversos idiomas de uma forma bem fácil e simples.

Gettext para ser compilado na versão 0.19.8.1 precisa de uma versão específica do GNULib, portanto iremos primeiro atualizar nosso repositório pra esta versão com o seguinte comando:

```sh
~/qemu-delfino/ $ cd gnulib
~/qemu-delfino/gnulib/ $ git checkout 6f9206d --force
```

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

Agora podemos prosseguir com o gettext, como ele já está como submódulo, basta atualizá-lo com os seguintes comandos:

```sh
~/qemu-delifno/ $ git submodule update --init gettext
~/qemu-delfino/ $ cd gettext
~/qemu-delfino/gettext $  git checkout v0.19.8.1
```

precisamos atualizar as configurações antes de executá-las para criar o `Makefile` e então compilar o projeto no diretório de trabalho.

```sh
~/qemu-delfino/gettext $  GNULIB_SRCDIR=../gnulib \
            GNULIB_TOOL=../gnulib-tool \
            ./autogen.sh
```


```sh
~/qemu-delfino/gettext $ cd ../build 
~/qemu-delfino/build/ $ mkdir gettext
~/qemu-delfino/build/ $ cd gettext
~/qemu-delfino/build/gettext $  ../../gettext/gettext-runtime/configure \
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

Pronto já temos agora o Gettext instalado, o LibIconv, GnuLib e Zlib, agora o próximo a ser compilado é GLib.

Como sempre se tiver alguma dúvida poste abaixo nos comentários.

[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-7/)