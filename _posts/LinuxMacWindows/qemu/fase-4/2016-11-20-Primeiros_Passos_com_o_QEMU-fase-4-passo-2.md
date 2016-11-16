---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-11/"
title: "Primeiros Passos com o QEMU, Passo 12" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS]
categories: [EmulacaoEVirtualizacao, QEMU, Compilando, dtc, device tree compiler]
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
EStamos quase no final, vamos agora compilar a libssh2.

<!--more-->

 git submodule update --init libssh2
 git checkout libssh2-1.8.0



{% highlight bash %}
~/qemu-delfino/ $ export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/mingw64/lib/pkgconfig 
~/qemu-delfino/pixman $ export LIBFFI_CFLAGS=`pkg-config.exe libffi --cflags`
~/qemu-delfino/pixman $ export LIBFFI_LIBS=`pkg-config.exe libffi --libs`
~/qemu-delfino/pixman $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/pixman $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/pixman $ export LDFLAGS="-L/mingw64/lib "
~/qemu-delfino/pixman $ export LINGUAS="en pt pt_BR"
~/qemu-delfino/pixman $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/pixman $ export GNULIB_TOOL="~/qemu-delfino/gnulib/gnulib-tool"
~/qemu-delfino/pixman $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include" 
~/qemu-delfino/pixman $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/pixman $ export GLIB_LIBS="-lglib-2.0" 
{% endhighlight %}

 
{% highlight bash %}
~/qemu-delfino/ $ cd ../build
~/qemu-delfino/build $ mkdir libsshs
~/qemu-delfino/build $ cd libssh2
{% endhighlight %}

Oserve que para compilar o libssh2 a variável cflags é configurada com outros
parametros, portanto sendo temporariamente alterada conforme abaixo:

{% highlight bash %}
~/qemu-delfino/build/libsshs $ CFLAGS=" -O0 -g -pipe -Wall -mthreads  -m64 " \
                                    ../../libssh2/configure \
                                              --disable-static  \
                                              --with-gnu-ld \
                                              --prefix=/mingw64 \
                                              --build=x86_64-w64-mingw32 \
                                              --host=x86_64-w64-mingw32 \
                                              --target=x86_64-w64-mingw32

         
~/qemu-delfino/build/qemu $ make
~/qemu-delfino/build/qemu $ make install
{% endhighlight %}

