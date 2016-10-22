---
title: "Primeiros Passos com o QEMU, parte 3" 
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

<!--more-->
Agora vamos configurar o ambiente para a compilação digite o seguinte comando abaixo:

	build $ PATH=$PATH:/mingw64/bin/  ../configure  \ 
		--prefix=/mingw64/qemu
		--source-path=.. \
		--cross-prefix=x86_64-w64-mingw32- \
		--target-list="gnuarmeclipse-softmmu" \

O comando irá configura a compilação no diretório corrente usando como compilador o gcc que tenha o prefixo *x86_64-w64-mingw32*, eu também atualizei a variável de ambiente `PATH` para que use o caminho /mingw64/bin para encontrar as ferramentas prefixadas. E finalmente informei que desejo compilar apenas o QEMU para uso com o **GNU ARM Eclipse**, que é a versão gerada pelo Livius.

Em seguida, execute o comando *make*, este levará um tempo razoável para compilar tudo que é preciso. Caso tenha problemas poste nos comentário os detalhes de seu ambiente para termos corrigir.

Veremos na terceira parte como instalar este novo QEMU.
