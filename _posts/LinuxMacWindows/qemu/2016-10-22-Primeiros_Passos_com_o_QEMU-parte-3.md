---
title: "Primeiros Passos com o QEMU, parte 3" 
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

Vamos compilar nossa primeira biblioteca a LIBFFI responsável por permiti que haja interações entre funções em uma linguagem com outra, por seu nome FFI - Foreing Function Interface.

<!--more-->

### Compilando a Biblioteca libffi

Abaixo estão os comandos que devem ser executados, veja que a linha de comando abaixo o que vem antes do dólar ($) representa o diretório onde o comando deve ser digitado, portanto `build $` que dizer que você está dentro do diretório `build`

```sh
gitclone/qemu-delifno/ $ git submodule update --init libffi
```

Coloque o python e o GCC que estamos usando no path usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

abora vamos compilar o projeto.

```sh
gitclone/qemu-delifno/libffi $ ./autogen.sh
gitclone/qemu-delifno/libffi $ cd ..
gitclone/qemu-delifno/ $ mkdir build
gitclone/qemu-delifno/build $ mkdir libffi
gitclone/qemu-delifno/build $ cd libffi
gitclone/qemu-delifno/build/libffi $ ../../libffi/configure --prefix \
					/mingw64 --build=x86_64-w64-mingw32 \
					CC=x86_64-w64-mingw32-gcc \
					CXX=x86_64-w64-mingw32-g++ \
					--disable-docs
```

No quarto comando acima faremos a configuração da compilação, a diretiva `--prefix` informa que a instalação será feita na pasta `/mingw64`, você pode mudar isso caso queira criar uma pasta especial para o QEMU, por exemplo `/mingw64-qemu`.

Além desabilitei também através da diretiva `--diable-docs` a geração de documentos, assim economizamos tempo e problemas com a instalação da ferramenta `makeinfo`.

Finalmente podemos compilar e instalar com os dois comandos a seguir:

```bash
gitclone/qemu-delfino/build/libffi $ make
gitclone/qemu-delfino/build/libffi $ make install
```

Não deverá ser apresentada nenhuma mensagem de erro qualquer dúvida me informe nos comentários abaixo.

[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-4/)

