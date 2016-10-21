---
title: "Primeiros Passos com o QEMU, parte 1" 
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
Acho que o maior desafio para um programador C ou C++ é ter todos os ambientes que precisa disponíveis em sua maquina para testar seus programas, entenda todos os ambientes como múltiplos sistemas operacionais, e múltiplas configurações, empacotamentos. Vamos ver então como fazer isso com o QEMU.

<!--more-->

Bem eu escolhi o Fork do Liviu Ionescu para trabalhar com o QEMU, seu fork foi criado para permitir emular embarcados e microcontroladores baseados em Cortex-M, e gostei de seu trabalho, e desejo amplia-lo para o Arduino DUE o que se tornou para mim um desafio, em especial para rodar seu Sistema Operacional em Tempo Real - RTOS para Cortex-M chamado &Mu;OS.

Minha intenção é gerar apenas o QEMU para trabalhar com a família Cortex, seja A ou M, e talvez R, a família Cortex-A eu vou focar no Cortex-A53 a Família Cortex-M eu irei focar no que precisar e principalmente no que faltar no que o Lonesco estiver trabalhando. Se vier a trabalhar com o Cortex-R inicialmente pretendo focar no Cortex-R52. Para saber porque me consulte através dos comentários.

Conforme eu ampliar meu domínio sobre o QEMU principalmente em seu desenvolvimento, pretendo agregar o que tenho visto de melhor em outros Forks, por hora estarei trabalhando também com:

 * O origingal http://www.qemu.org
 * e o Fork do Beckus git@github.com:beckus/qemu_stm32.git

Estarei dividindo as publicações sobre este trabalho em partes, conforme eu for tendo sucesso na geração de material, portanto não sei quantas partes terei, mas a primeira será introdutória e como gerar o QEMU para o Windows diretamente do fonte usando o MSYS2.

## O que é exatamente o QEMU

Bem, conforme o site do QEMU temos:

> QEMU is a FAST! processor emulator using dynamic translation to achieve good emulation speed.

Em tradução livre:

> QEMU é um emulador de processador RÁPIDO! que usa tradução dinâmica para atingir boa velocidade de emulação.

O QEMU tem dois modos de operação, um onde emula um sistema completo, como um computador, sendo todos os dipostivos de entrada e saída, acesso a memória. Neste modo podemos rodar um sistema operacional por completo dentro de outro sistema, por exemplo rodar o Linux dentro do Windows.

No segundo modo, o QEMU funciona em modo de emulação, ele emula apenas o processador, sendo usado para rodar uma aplicação como o Wine que permite executar aplicativos Windows dentro do Linux.

O QEMU é muito interessante tanto pela sua simplicidade de operação, um simples comando com varias diretivas que permitem carrarmos imagens e simularmos HD para armazenarmos dados, além de bastante dinâmico é bem rápido.

O principal uso que darei ao QEMU é fazer testes unitários e de sistema usando ambiente como o Trevis para testar códigos em diversos ambientes, já que o Trevis roda especificamente Linux, eu preciso do QEMU para simular um Cortex-M como o usado no Arduino DUE ou mesmo um Cortex-A como usado no NanoPI, em especial estarei usando imediatamente com o "Contador de Ciclistas"

## Compilando meu primeiro QEMU

Você não precisa compilar seu QEMU na internet você irá encontrar versões prontas para windows e Linux, tanto do QEMU original como Forks como o disponibilizado pelo Liviu Ionesco.

Para compilar seu QEMU você precisa baixar o Fonte original ou um FORK, eu irei usar como referência meu fork que é baseado no trabalho do Livius, que pode ser encontrado link http://gnuarmeclipse.github.io/qemu/.

O primeiro passo é instalar o MSYS em seu computador, baixe a ferramenta do link: https://msys2.github.io/, escolha o pacote conforme sua plataforma.

Depois de instalado entre no shell do MSYS2, execute a seguinte sequência de comandos para atualiza-lo, em cada comando reinicialize o shell.


    $ pacman -Sy pacman
	$ pacman -Syu
	$ pacman -Su

Você verá algumas mensagens, informando que estão sendo baixados e instalados alguns pacotes,  e ficará claro que tudo deu certo ou algo deu errado, neste ultimo caso entre em contato comigo pelos comentários abaixo.

    $ pacman -Ss pkg-config
    mingw32/mingw-w64-i686-pkg-config 0.29.1-2 (mingw-w64-i686-toolchain)
    	A system for managing library compile/link flags (mingw-w64)
    mingw64/mingw-w64-x86_64-pkg-config 0.29.1-2 (mingw-w64-x86_64-toolchain)
    	A system for managing library compile/link flags (mingw-w64)
    msys/pkg-config 0.29.1-1 (base-devel) [instalado]
   		A system for managing library compile/link flags
    
O comando acima listou o que temos disponível para instalar o `pkg-config` escolhi este pacote exatamente para facilitar a escolha do que iremos instalar, veja que nosso foco é compilar o GCC, e no meu caso estou usando uma plataforma 64bits, portanto vou precisar do ToolChain completo para compilar em C/C++ para 64Bits, assim vou escolher instalar o pacote `git`, `mingw-w64-x86_64-toolchain`, `mingw64/mingw-w64-x86_64-glib2` e todas as dependências

Digite o comando

	$ pacman -S git autoconf automake-wrapper\
		msys/libtool \
		mingw64/mingw-w64-x86_64-libtool \
		mingw64/mingw-w64-x86_64-glib2 \
		mingw-w64-x86_64-toolchain 

e receberá uma mensagem similar a esta abaixo:

	:: Há 16 membros no grupo mingw-w64-x86_64-toolchain:
	:: Repositório mingw64
	   1) mingw-w64-x86_64-binutils  2) mingw-w64-x86_64-crt-git  3) mingw-w64-x86_64-gcc
	   4) mingw-w64-x86_64-gcc-ada  5) mingw-w64-x86_64-gcc-fortran  6) mingw-w64-x86_64-gcc-libgfortran
	   7) mingw-w64-x86_64-gcc-libs  8) mingw-w64-x86_64-gcc-objc  9) mingw-w64-x86_64-gdb
	   10) mingw-w64-x86_64-headers-git  11) mingw-w64-x86_64-libmangle-git
	   12) mingw-w64-x86_64-libwinpthread-git  13) mingw-w64-x86_64-make  14) mingw-w64-x86_64-pkg-config
	   15) mingw-w64-x86_64-tools-git  16) mingw-w64-x86_64-winpthreads-git

	Digite uma seleção (padrão=todos):

Então apenas tecle enter e logo a seguir receberá a lista do que será instalado no meu caso apresentou a seguinte lista:

    atenção: mingw-w64-x86_64-binutils-2.27-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-crt-git-5.0.0.4745.d2384c2-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-libgfortran-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-libs-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-headers-git-5.0.0.4747.0f8f626-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-libwinpthread-git-5.0.0.4741.2c8939a-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-winpthreads-git-5.0.0.4741.2c8939a-1 está atualizado -- reinstalando
    resolvendo dependências...
    procurando por pacotes conflitantes...
    atenção: dependência cíclica detectada:
    atenção: mingw-w64-x86_64-gcc-libgfortran será instalado antes de sua dependência mingw-w64-x86_64-gcc-libs
    
    Pacotes (32) mingw-w64-x86_64-ca-certificates-20150426-2  mingw-w64-x86_64-expat-2.2.0-1
	     mingw-w64-x86_64-gdbm-1.12-1  mingw-w64-x86_64-gettext-0.19.7-1
	     mingw-w64-x86_64-libffi-3.2.1-4  mingw-w64-x86_64-libsystre-1.0.1-2
	     mingw-w64-x86_64-libtasn1-4.9-1  mingw-w64-x86_64-libtre-git-r122.c2f5d13-4
	     mingw-w64-x86_64-ncurses-6.0.20161001-1  mingw-w64-x86_64-openssl-1.0.2.j-1
	     mingw-w64-x86_64-p11-kit-0.23.2-2  mingw-w64-x86_64-python2-2.7.12-1
	     mingw-w64-x86_64-readline-6.3.008-1  mingw-w64-x86_64-tcl-8.6.6-1
	     mingw-w64-x86_64-termcap-1.3.1-2  mingw-w64-x86_64-tk-8.6.6-1
	     mingw-w64-x86_64-binutils-2.27-2  mingw-w64-x86_64-crt-git-5.0.0.4745.d2384c2-1
	     mingw-w64-x86_64-gcc-6.2.0-2  mingw-w64-x86_64-gcc-ada-6.2.0-2
	     mingw-w64-x86_64-gcc-fortran-6.2.0-2  mingw-w64-x86_64-gcc-libgfortran-6.2.0-2
	     mingw-w64-x86_64-gcc-libs-6.2.0-2  mingw-w64-x86_64-gcc-objc-6.2.0-2
	     mingw-w64-x86_64-gdb-7.12-1  mingw-w64-x86_64-headers-git-5.0.0.4747.0f8f626-1
	     mingw-w64-x86_64-libmangle-git-5.0.0.4669.7de6266-1
	     mingw-w64-x86_64-libwinpthread-git-5.0.0.4741.2c8939a-1
	     mingw-w64-x86_64-make-4.1.2351.a80a8b8-1  mingw-w64-x86_64-pkg-config-0.29.1-2
	     mingw-w64-x86_64-tools-git-5.0.0.4669.7de6266-1
	     mingw-w64-x86_64-winpthreads-git-5.0.0.4741.2c8939a-1
    
    Tamanho total download:65,27 MiB
    Tamanho total instalado:  670,52 MiB
    Alteração no tamanho:   322,45 MiB
    
    :: Continuar a instalação? [S/n]
    

Basta teclar [enter] novamente e esperar o termino da instalação:

**ATENÇÃO:** Se receber uma mensagem informando algo relativo a diretório `/mingw32` ou /mingw64` basta criar este diretório no raiz. a mensagem é similar a apresentada abaixo:

	erro: falha em submeter a transação (arquivos conflitantes)
	mingw-w64-i686-libiconv: /mingw32 existe no sistema de arquivos


Repita então o processo de instalação depois de criado os diretórios.

Claro quando ele te consultar sobre quais pacotes deseja instalar, você poderá selecionar instalar um deles, e repetir o processo, ou mesmo repetir o processo fazendo referência direta a cada pacote, só deve tomar cuidado para não esquecer nada, você vai precisar nó minimo dos pacotes que instalam:

 * ncurses
 * readline
 * termcap
 * binutils
 * gcc
 * gcc-libs
 * gdb
 * make
 * tols-git
 * winpthreads-git
 * python2
 * pkg-config
 * expat
 * gettext
 * libffi
 * libtre-git
 * libsystre
 * tcl
 * tk
 * glib2
 * autoconf
 * e muitos outros

Aprenda o máximo que puder sobre a ferramenta `pacman`, ela sera sua ferramenta para lhe ajudar a instalar tudo que precisa no MSYS2.

Pronto estamos preparados para começar a compilação do QEMU, [veja como fazê-lo na segunda parte deste tutorial](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/Primeiros_Passos_com_o_QEMU-parte-2/).