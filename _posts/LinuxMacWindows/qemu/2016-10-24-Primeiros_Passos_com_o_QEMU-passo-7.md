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

<!--more-->

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

{% highlight bash %}
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
{% endhighlight %}

Digite o comando abaixo para se certificar que está tudo funcionando:

{% highlight bash %}
~/qemu-delfino/ $ python --version
Python 2.7.11
{% endhighlight %}

## Compilando a biblioteca glib

GLib não pode ser confundida com GLIBC.

GLib também era muito associada ao projeto GTK+ e confundida como uma biblioteca 
gráfica para evitar isso, foi separada do projeto na versão GTK+ 2, assim ela é 
agora independente.

## Compilando a Biblioteca Glib

Para compilar a Glib com sucesso é fundamental ter o Python 2.7 instalado, 
certifique-se disso como foi apresentado no primeiro passo e volte para continuarmos. 

Não use outra versão além do Python 2.7.


Veja que para compilá-la precisamos de passar diversas variáveis parametrizadas 
conforme nosso ambiente e as novas bibliotecas, assim comece digitando:

{% highlight bash %}
~/qemu-delfino/ $ export LIBFFI_CFLAGS=`pkg-config.exe libffi --cflags`
~/qemu-delfino/ $ export LIBFFI_LIBS=`pkg-config.exe libffi --libs`
~/qemu-delfino/ $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/ $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include"
~/qemu-delfino/ $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/ $ export LDFLAGS="-L/mingw64/lib "
~/qemu-delfino/ $ export LINGUAS="en pt pt_BR"
~/qemu-delfino/ $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/ $ export GNULIB_TOOL="~/qemu-delfino/gnulib/gnulib-tool"
~/qemu-delfino/ $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
{% endhighlight %}

Vamos entender algumas coisas importantes, primeiro a versão escolhida, como ao 
compilar a nova biblioteca fizemos uma versão compilada localmente, mesmo que sem 
alterações, ela não é uma versão oficial, então ela usou a numeração 3.99999 para 
identificar esta versão. por isso o diretório informando na primeira variável 
para a biblioteca ficou sendo `/mingw64/lib/libffi-3.99999/include'`.

Agora vamos obter o glib em nosso repositório:

{% highlight bash %}
~/qemu-delfino/ $ git submodule update --init glib
~/qemu-delfino/ $ cd glib
~/qemu-delfino/glib/ $ git checkout 2.51.0
{% endhighlight %}

E atualizar seus scripts de configuração:

{% highlight bash %}
~/qemu-delfino/glib $ cd glib
~/qemu-delfino/glib $ export GNULIB_SRCDIR=~/qemu-delfino/gnulib 
~/qemu-delfino/glib $ export GNULIB_TOOL=~/qemu-delfino/gnulib/gnulib-tool 
~/qemu-delfino/glib $ ./autogen.sh \
            --prefix=/mingw64 \
            --with-pcre=internal \
            --with-libiconv=gnu \
            --with-gnu-ld \
            --with-threads=win32 \
            --disable-static \
            --disable-gtk-doc \
            --disable-selinux  \
            --disable-man \
            --enable-silent-rules \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target==x86_64-w64-mingw32 
{% endhighlight %}

{% highlight bash %}
~/qemu-delfino/glib $ make
~/qemu-delfino/glib $ make install
{% endhighlight %}



[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-8/)