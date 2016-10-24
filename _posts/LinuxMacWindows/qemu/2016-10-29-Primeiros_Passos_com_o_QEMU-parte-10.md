---
title: "Primeiros Passos com o QEMU, parte 10" 
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

Vamos nesta parte compilar o QEMU propriamente, até agora estamos apenas preparando o ambiente para este momento.

<!--more-->

### Compilando o QEMU

Crie um diretório para trabalhar por exemplo eu criei uma pasta chamada "build" dentro da pasta onde fiz o clone do QEMU 

	$ cd qemu-delfino
	qemu-delfino $ mkdir build
	qemu-delfino $ cd build
    build $

Nesta pasta iremos criar também uma pasta para cada biblioteca que formos compilar para uso no QEMU, assim evitamos poluir o diretório dos fontes com arquivos compilados e caso algo dê errado e quiser começar do zero, basta apagar tal pasta e criar novamente sem ter que baixar todo o repositório mais uma vez.

Agora vamos configurar o ambiente para a compilação digite o seguinte comando abaixo:

	build $ PATH=$PATH:/mingw64/bin/  ../configure  \ 
		--prefix=/mingw64/qemu
		--source-path=.. \
		--cross-prefix=x86_64-w64-mingw32- \
		--target-list="gnuarmeclipse-softmmu" \

O comando irá configura a compilação no diretório corrente usando como compilador o gcc que tenha o prefixo *x86_64-w64-mingw32*, eu também atualizei a variável de ambiente `PATH` para que use o caminho /mingw64/bin para encontrar as ferramentas prefixadas. E finalmente informei que desejo compilar apenas o QEMU para uso com o **GNU ARM Eclipse**, que é a versão gerada pelo Livius.

Em seguida, execute o comando *make*, este levará um tempo razoável para compilar tudo que é preciso. Caso tenha problemas poste nos comentário os detalhes de seu ambiente para termos corrigir.

















-----------------------------------------------

## Sites das bibliotecas, frameworks e tudo usado neste projeto

 * http://gnuarmeclipse.github.io/qemu/
 * http://qemu.org/
 * https://carlosdelfino.eti.br/qemu
 * http://www.zlib.net/

## Repositórios relacionados

 * git@github.com:qemu/qemu.git
 * git@github.com:gnuarmeclipse/qemu.git
 * git@github.com:beckus/qemu_stm32.git
 * git@github.com:carlosdelfino/qemu.git
 * git@github.com:madler/zlib.git
 * git@github.com:libffi/libffi.git
 * git://git.savannah.gnu.org/gnulib.git
 * git://git.savannah.gnu.org/gettext.git
 * git://git.savannah.gnu.org/libiconv.git
 * git://git.gnome.org/gtk+

## Outras fontes de referência

 * http://preshing.com/20141119/how-to-build-a-gcc-cross-compiler/
 * http://pt.stackoverflow.com
 * http://gcc.gnu.org 