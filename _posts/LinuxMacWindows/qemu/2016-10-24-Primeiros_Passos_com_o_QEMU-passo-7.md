---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-7/"
title: "Primeiros Passos com o QEMU, Passo 7" 
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

O GLib é uma biblioteca multiplataforma, é uma biblioteca de uso geral que disponibiliza vários tipos de dados, macros, funções para conversão de tipos, utilitários para manipulação de strings e de arquivos, um laço de eventos, além de outras implementações.

<!--more-->>

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

Digite o comando abaixo para se certificar que está tudo funcionando:

```sh
~/qemu-delfino/ $ python --version
Python 2.7.11
```

## Compilando a biblioteca zlib

```sh
~/qemu-delfino/ $ git submodule update --init zlib
```

```sh
~/qemu-delfino/ $ cd zlib
~/qemu-delfino/ $ make -f win32/Makefile.gcc \
                            PREFIX=x86_64-w64-mingw32- \
                            INCLUDE_PATH=/mingw64/include \
                            LIBRARY_PATH=/mingw64/lib \
                            BINARY_PATH=/mingw64/lib \
                            install
```

## Compilando a biblioteca glib

GLib não pode ser confundida com GLIBC.

GLib também era muito associada ao projeto GTK+ e confundida como uma biblioteca gráfica para evitar isso, foi separada do projeto na versão GTK+ 2, assim ela é agora independente.

## Compilando a Biblioteca Glib

Para compilar a Glib com sucesso é fundamental ter o Python 2.7 instalado, certifique-se disso como foi apresentado no primeiro passo e volte para continuarmos. 

Não use outra versão além do Python 2.7.


Veja que para compilá-la precisamos de passar diversas variáveis parametrizadas conforme nosso ambiente e as novas bibliotecas, assim comece digitando:

```sh
~/qemu-delfino/ $ export LIBFFI_CFLAGS='-I /mingw64/lib/libffi-3.99999/include'
~/qemu-delfino/ $ export LIBFFI_LIBS=-lffi
~/qemu-delfino/ $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/ $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include"
~/qemu-delfino/ $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/ $ export LDFLAGS="-L/mingw64/lib "
~/qemu-delfino/ $ export LINGUAS="en pt pt-br"
~/qemu-delfino/ $ export GNULIB_SRCDIR="~/qemu-delfino/build/gnulib"  
~/qemu-delfino/ $ export GNULIB_TOOL="~/qemu-delfino/build/gnulib-tool"
```

Vamos entender algumas coisas importantes, primeiro a versão escolhida, como ao compilar a nova biblioteca fizemos uma versão compilada localmente, mesmo que sem alterações, ela não é uma versão oficial, então ela usou a numeração 3.99999 para identificar esta versão. por isso o diretório informando na primeira variável para a biblioteca ficou sendo `/mingw64/lib/libffi-3.99999/include'`.

Agora vamos obter o glib em nosso repositório:

```sh
~/qemu-delfino/ $ git submodule update --init glib
```

E atualizar seus scripts de configuração:

```sh
~/qemu-delfino/glib $ cd glib
~/qemu-delfino/glib $ export GNULIB_SRCDIR=../gnulib 
~/qemu-delfino/glib $ export GNULIB_TOOL=../gnulib-tool 
~/qemu-delfino/glib $ ./autogen.sh
```

```sh
~/qemu-delfino/glib $ cd ../build
~/qemu-delfino/build/ $ mdkir glib
~/qemu-delfino/build/glib $ cd glib
~/qemu-delfino/build/glib $ ../../glib/configure \
            --prefix=/mingw64 \
            --with-pcre=internal \
            --disable-static \
            --enable-silent-rules \
            --with-libiconv=gnu \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target==x86_64-w64-mingw32 
            
~/qemu-delfino/build/glib $ make
~/qemu-delfino/build/glib $ make install
```



[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-8/)