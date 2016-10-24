---
title: "Primeiros Passos com o QEMU, parte 7" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, ]
categories: [Emulação e Virtualização, QEMU, Compilando]
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

O GLib é uma biblioteca multiplataforma, é uma biblioteca de uso geral que disponibiliza vários tipos de dados, macros, funções para conversão de tipos, utilitários para manipulação de strings e de arquivos, um laço de eventos, além de outras implementações.

<!--more-->>

GLib não pode ser confundida com GLIBC.

GLib também era muito associada ao projeto GTK+ e confundida como uma biblioteca gráfica para evitar isso, foi separada do projeto na versão GTK+ 2, assim ela é agora independente.

## Compilando a Biblioteca Glib

Para compilar a Glib com sucesso é fundamental ter o Python 2.7 instalado, certifique-se disso como foi apresentado no primeiro passo e volte para continuarmos. 

Não use outra versão além do Python 2.7.

Coloque o python e o GCC que estamos usando no path usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH= /mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

Digite o comando abaixo para se certificar que está tudo funcionando:

```sh
~/qemu-delfino/ $ python --version
Python 2.7.11
```
Veja que para compilá-la precisamos de passar diversas variáveis parametrizadas conforme nosso ambiente e as novas bibliotecas, assim comece digitando:

```sh
~/qemu-delfino/ $ export LIBFFI_CFLAGS='-I /mingw64/lib/libffi-3.99999/include'
~/qemu-delfino/ $ export LIBFFI_LIBS=-lffi
~/qemu-delfino/ $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/ $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads"
~/qemu-delfino/ $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
```

Vamos entender algumas coisas importantes, primeiro a versão escolhida, como ao compilar a nova biblioteca fizemos uma versão compilada localmente, mesmo que sem alterações, ela não é uma versão oficial, então ela usou a numeração 3.99999 para identificar esta versão. por isso o diretório informando na primeira variável para a biblioteca ficou sendo `/mingw64/lib/libffi-3.99999/include'`.

Agora vamos obter o glib em nosso repositóiro:

```sh
~/qemu-delfino/ $ git submodule update --init glib
```

E atualizar seus scripts de configuração:

```sh
~/qemu-delfino/ $ cd glib
~/qemu-delfino/ $ GNULIB_SRCDIR=../gnulib \
            GNULIB_TOOL=../gnulib-tool \
            ./autogen.sh
```

```sh
~/qemu-delfino/glib $ configure -prefix=/c/mingw-builds/mingw64 -with-pcre=internal -disable-static -disable-gtk-doc -enable-silent-rules -build=x86_64-w64-mingw32
make
make install
```