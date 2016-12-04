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
Neste passo, que ainda não é o final, chegamos finalmente ao objetivo que é 
compilar e instalar o qemu personalizado.

<!--more-->

Apesar de chamar o QEMU de personalizado, não fizemos alteração alguma em seu 
código para que faz jus a este apelido, porém é o caminho para os primeiros 
passos com o QEMU e sua personalização, sem conseguir compreender o seu contexto 
de compilação fica difícil partir para qualquer personalização.

Portanto agora podemos assim colocarmos o QEMU funcionando com algum exemplo 
partir para interferência em seu código buscando resultados mais diretos e 
relacionados ao nosso objetivo.

O primeiro passo será unir o trabalho de Livius ao QEMU original mantendo assim 
um controle das customizações para Cortex-M, facilitando que possamos criar 
nossas placas de prototipação virtuais. Como dissemos a primeira placa será o 
Arduino DUE e o Maple, depois partiremos para o AVR e finalmente testaremos o 
xtensa para ESP.

## Um ultimo passo antes de finalizar

é preciso fazer o update do diretório cdt.

git submodule --init cdt


## Compilando o QEMU

Execute os seguintes comandos para começar a preparar o ambiente. Já considero 
aqui que está sendo mantido as variáveis de compilação adotada no último passo, 
(estou escrevendo um posto, descrevendo todas as variáveis utilizas nestes passos)
portanto a partir deste ponto não irei mais repetir as tarefas anteriores, não 
se esqueça de atualizar o path para encontrar as ferramentas em `/mingw64/bin`.

Atualize a variável `CFLAGS`:

{% highlight bash %}
~/qemu-delfino/pixman $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include -m64 `sdl2-config --cflags `"
{% endhighlight %}

export CFLAGS="-O0 -g -pipe -mms-bitfields -mthreads -I/mingw64/include -m64 `sdl2-config --cflags `"

Finalmente podemos compilar o código com os seguintes comandos.

Fique atento a definição das variáveis, mesmo que já tenha definido antes, 
certifique todas estão corretas.

g

{% highlight bash %}
~/qemu-delfino/ $ cd ../build
~/qemu-delfino/build $ mkdir qemu
~/qemu-delfino/build $ cd qemu
{% endhighlight %}

{% highlight bash %}

 ../../configure \
          --prefix=/mingw64/qemu \
          --cross-prefix=x86_64-w64-mingw32- \
          --disable-docs \
          --disable-snappy \
          --target-list="x86_64-softmmu,arm-softmmu,aarch64-softmmu,xtensaeb-softmmu,xtensa-softmmu" \
          --enable-lzo \
          --enable-bzip2 \
          --enable-vnc \
          --enable-user \
          --enable-system \
          --enable-kvm \
          --enable-vhost-net \
          --extra-cflags="-m64" \
          --extra-ldflags="-m64"



         
~/qemu-delfino/build/qemu $ make
~/qemu-delfino/build/qemu $ make install
{% endhighlight %}

Como podem ver pela diretiva `target-list`, serão compiladas apenas as 
arquiteturas x86_64, ARM, xtensaeb e xtensa, futuramente estarei adicionando 
também AVR. em ARM e xtensa respetivamente uma Placa Arduino e um ESP-01 para 
testes.

### Possíveis targets para o QEMU

É possível usar os seguintes targets (plataformas) para emular:

 * [aarch64-softmmu](/qemu/softmmu/aarch64)
 * [alpha-softmmu](/qemu/softmmu/alpha)
 * [arm-softmmu](/qemu/softmmu/arm)
 * [cortexm-softmmu](/qemu/softmmu/cortexm)
 * [cris-softmmu](/qemu/softmmu/cris)
 * [i386-softmmu](/qemu/softmmu/i386)
 * [lm32-softmmu](/qemu/softmmu/lm32)
 * [m68k-softmmu](/qemu/softmmu/m68k)
 * [microblaze-softmmu](/qemu/softmmu/microblaze) 
 * [microblazeel-softmmu](/qemu/softmmu/microblazeel)
 * [mips-softmmu](/qemu/softmmu/mips)
 * [mips64-softmmu](/qemu/softmmu/mips64)
 * [mips64el-softmmu](/qemu/softmmu/mips64el)
 * [mipsel-softmmu](/qemu/softmmu/mipsel)
 * [moxie-softmmu](/qemu/softmmu/moxie)
 * [or32-softmmu](/qemu/softmmu/or32)
 * [ppc-softmmu](/qemu/softmmu/ppc)
 * [ppc64-softmmu](/qemu/softmmu/ppc64)
 * [ppcemb-softmmu](/qemu/softmmu/ppcemb)
 * [s390x-softmmu](/qemu/softmmu/s390x)
 * [sh4-softmmu](/qemu/softmmu/sh4)
 * [sh4eb-softmmu](/qemu/softmmu/sh4eb)
 * [sparc-softmmu](/qemu/softmmu/sparc)
 * [sparc64-softmmu](/qemu/softmmu/sparc64)
 * [tricore-softmmu](/qemu/softmmu/tricore)
 * [unicore32-softmmu](/qemu/softmmu/unicore32)
 * [x86_64-softmmu](/qemu/softmmu/x86_64)
 * [xtensa-softmmu](/qemu/softmmu/xtensa)
 * [xtensaeb-softmmu](/qemu/softmmu/xtensaeb)
                           



[Estamos trabalhando no passo 11.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-11)

## Sites das bibliotecas, frameworks e tudo usado neste projeto

 * http://gnuarmeclipse.github.io/qemu/
 * http://qemu.org/
 * https://carlosdelfino.eti.br/qemu
 * http://www.zlib.net/

### Outras fontes de referência

 * http://qemu-project.org/Hosts/Linux
 * http://qemu-project.org/Hosts/W32#Cross_builds
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
 * https://www.gnu.org/software/libc/download.html
 * [Getting confused when exploring Qemu source? gcc comes to rescue!](http://the-hydra.blogspot.com.br/2011/04/getting-confused-when-exploring-qemu.html) 
 * [How to build the QEMU binaries?](http://gnuarmeclipse.github.io/qemu/build-procedure/)
 * https://bbs.archlinux.org/viewtopic.php?id=191629

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
 * git://sourceware.org/git/glibc.git

