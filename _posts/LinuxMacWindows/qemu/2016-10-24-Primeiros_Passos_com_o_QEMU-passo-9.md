---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-9/"
title: "Primeiros Passos com o QEMU, Passo 9" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, SDL, Games, Hardware, OpenGL, DirectX, Mouse, Keyboard, Video, Simple Direct Media Layar, Joystick ]
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

SDL de Simple DirectMedia Layer no inglês, é uma biblioteca cross-plataforma 
que permite o desenvolvimento de aplicações que acessam diretamente o hardware 
como áudio keyboard, mouse, joystick e gráficos via OpenGL ou Direct3D.

<!--more-->
	
Este biblioteca é muito usada por softwares para exibição de vídeos, emuladores como o QEMU e jogos populares.

Para compilar o SDL pode se obter o fonte de diversas formas, nos usaremos o nosso submódulo em nosso repositório, porém o oficial se encontra em um repositório baseado no Mercurial, uma ferramenta de controle de versão similar ao GIT `hg clone http://hg.libsdl.org/SDL`.

Para obter em nosso repositório use o comando:

```sh
~/qemu-delfino/ $ git submodule update --init SDL
~/qemu-delfino/ $ cd SDL
~/qemu-delfino/SDL $ git checkout  release-2.0.5
{% endhighlight %}


Execute os seguintes comandos para começar a preparar o ambiente.



Agora vamos preparar as variáveis de ambinte para nossa compilação.

{% highlight bash %}
~/qemu-delfino/build/glib $ export LIBFFI_CFLAGS=`pkg-config.exe libffi --cflags`
~/qemu-delfino/build/glib $ export LIBFFI_LIBS=`pkg-config.exe libffi --libs`
~/qemu-delfino/build/glib $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/build/glib $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include -m64"
~/qemu-delfino/build/glib $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/build/glib $ export LDFLAGS="-L/mingw64/lib "
~/qemu-delfino/build/glib $ export LINGUAS="en pt pt_BR"
~/qemu-delfino/build/glib $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/build/glib $ export GNULIB_TOOL="~/qemu-delfino/gnulib/gnulib-tool"
~/qemu-delfino/build/glib $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include" 
~/qemu-delfino/SDL $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/SDL $ export GLIB_LIBS="-lglib-2.0"
{% endhighlight %}

{% highlight bash %} 
~/qemu-delfino/SDL $ ./autogen.sh
{% endhighlight %}

Durante o processo se vier a ter problemas com a falta da biblioteca será necessário baixar o pacote OpenGL development headers e descompacte na pasta /mingw64:
    http://www.libsdl.org/extras/win32/common/opengl-devel.tar.gz

e repita o processo.

Fique atento a definição das variáveis, mesmo que já tenha definido antes, certifique todas estão corretas.

{% highlight bash %}
~/qemu-delfino/SDL $ cd ../build
~/qemu-delfino/build $ mkdir sdl
~/qemu-delfino/build $ cd sdl
~/qemu-delfino/build/sdl $ ../../sdl/configure \
            --prefix=/mingw64 \
            --exec-prefix=/mingw64 \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target=x86_64-w64-mingw32 
~/qemu-delfino/build/sdl $ make
~/qemu-delfino/build/sdl $ make install
{% endhighlight %}

[Pronto podemos partir agora para o próximo passo.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-10/)