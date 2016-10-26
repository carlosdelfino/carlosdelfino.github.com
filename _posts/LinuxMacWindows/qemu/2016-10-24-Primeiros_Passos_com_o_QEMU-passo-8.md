---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-8/"
title: "Primeiros Passos com o QEMU, Passo 8" 
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

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

## Compilando o pkg-config

Como para compilar o pkg-config precisamos do glib e vice versa, iremos compila-lo agora e em seguida iremos compilar o glib novamente para atualiza-lo com pkg-config.

```sh
~/qemu-delfino/ $  git submodules update --init pkg-config
~/qemu-delfino/pkg-config/ $  cd pkg-config
~/qemu-delfino/pkg-config/ $  git checkout pkg-config-0.29.1
~/qemu-delfino/pkg-config/ $  ./autogen.sh --no-configure 
```


```sh
~/qemu-delfino/pkg-config/ $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/pkg-config/ $ export GLIB_LIBS="-lglib-2.0"
~/qemu-delfino/pkg-config/ $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
~/qemu-delfino/pkg-config/ $ export GLIB_LIBS=""
~/qemu-delfino/pkg-config/ $ ./configure -prefix=/mingw64 \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target==x86_64-w64-mingw32 
make
make install
```

Agora precisamos recompilar a glib para usarmos o novo pkg-config.

## Recompilando a glib


volte ao diretório de compilação e limpe o diretório

```sh
~/qemu-delfino/pkg-config $ cd ../build/glib
~/qemu-delfino/build/glib make distclean
```

Certifique-se que as variáveis abaixo já foram exportadas:

```sh
~/qemu-delfino/build/glib $ export LIBFFI_CFLAGS='-I /mingw64/lib/libffi-3.99999/include'
~/qemu-delfino/build/glib $ export LIBFFI_LIBS=-lffi
~/qemu-delfino/build/glib $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/build/glib $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include"
~/qemu-delfino/build/glib $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/build/glib $ export LDFLAGS="-L/mingw64/lib "
~/qemu-delfino/build/glib $ export LINGUAS="en pt pt-br"
~/qemu-delfino/build/glib $ export GNULIB_SRCDIR="~/qemu-delfino/build/gnulib"  
~/qemu-delfino/build/glib $ export GNULIB_TOOL="~/qemu-delfino/build/gnulib-tool"
~/qemu-delfino/build/glib $ export GNULIB_SRCDIR=../gnulib 
~/qemu-delfino/build/glib $ export GNULIB_TOOL=../gnulib-tool 
~/qemu-delfino/build/glib $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
~/qemu-delfino/build/glib $ export GLIB_LIBS=""
```

```sh
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

[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-9/)