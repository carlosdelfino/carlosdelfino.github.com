---
title: "Primeiros Passos com o QEMU, parte 2" 
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
Começamos tudo instalando o MSYS2, vejo que para você, foi um sucesso, como foi para mim, então estamos neste segundo passo. Mas, não adianta seguir se são teve sucesso no passo anterior.

<!--more-->

Caso tenha chegado aqui antes de tentar o primeiro passo, retorne a ele para fazê-lo até que tudo dê certo. [Clique aqui](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/Primeiros_Passos_com_o_QEMU-parte-1/ "Clique Aqui").

Agora vamos clonar o projeto do QEMU usando meu fork:

	git clone git@github.com:carlosdelfino/qemu.git qemu-delfino

Veja que você também precisa as bibliotecas *pixman* e *dtc* estejam instaladas, caso não as tenha, use um dos seguintes comandos para instalar as que faltam.

	git submodule update --init pixman
	git submodule update --init dtc

Bem, agora finalmente podemos dar um passo em direção a compilação do QEMU.

Crie um diretório para trabalhar por exemplo eu criei uma pasta chamada "build" dentro da pasta onde fiz o clone do QEMU 

	$ cd qemu-delfino
	qemu-delfino $ mkdir build
	qemu-delfino $ cd build
    build $

Agora vamos configurar o ambiente para a compilação digite o seguinte comando abaixo:

	build $ PATH=$PATH:/mingw64/bin/  ../configure  \
		--source-path=.. \
		--cross-prefix=x86_64-w64-mingw32- \
		--target-list="gnuarmeclipse-softmmu" \

O comando irá configura a compilação no diretório corrente usando como compilador o gcc que tenha o prefixo *x86_64-w64-mingw32*, eu também atualizei a variável de ambiente `PATH` para que use o caminho /mingw64/bin para encontrar as ferramentas prefixadas. E finalmente informei que desejo compilar apenas o QEMU para uso com o **GNU ARM Eclipse**, que é a versão gerada pelo Livius.

Em seguida, execute o comando *make*, este levará um tempo razoável para compilar tudo que é preciso. Caso tenha problemas poste nos comentário os detalhes de seu ambiente para termos corrigir.

Veremos na terceira parte como instalar este novo QEMU.

-----------------------------------------------

## Sites dos repositórios

 * http://gnuarmeclipse.github.io/qemu/
 * http://qemu.org/
 * https://carlosdelfino.eti.br/qemu

## Repositórios relacionados

 * git@github.com:qemu/qemu.git
 * git@github.com:gnuarmeclipse/qemu.git
 * git@github.com:beckus/qemu_stm32.git
 * git@github.com:carlosdelfino/qemu.git