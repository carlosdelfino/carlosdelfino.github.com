---
redirect_from: "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-4/"
title: "Primeiros Passos com o QEMU, parte 4" 
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
Vamos agora compilar a biblioteca zlib, responsável por nos fornecer a API para compactação e descompactação de dados, como usado no ZIP, BZIP e GZip.

### Compilando a biblioteca zlib

A biblioteca zlib é importante para lidar com arquivos compactados, ela é importante para o QEMU diretamente.

Veja que esta biblioteca não tem como ser compilada fora de seu diretório original, onde estão os fontes, portanto seja cuidadoso ao limpar o diretório se desejar refazer a compilação. Caso tenha problemas use o comando `git checkout TAG --force`, onde a palavra `TAG`deve ser substituída pela *TAG* da versão selecionada para trabalho.

Usaremos por hora a versão **1.2.8** portanto a *TAG* usada será ***v1.2.8***.

```sh
~/qemu-delifno/ $ git submodule update --init zlib
~/qemu-delfino/ $ cd zlib
~/qemu-delfino/ $ git checkout v1.2.8
```
Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

Agora use o comando abaixo para configurar a compilação:

```sh
~/qemu-delifno/zlib $ CROSS_PREFIX=x86_64-w64-mingw32- \
		PREFIX=/mingw64 
		./configure  
``` 

e para compilar e instalar digite o comando:

```sh
~/qemu-delifno/zlib $ make -f win32/Makefile.gcc install \
		CFLAGS="-pipe" \
        LDFLAGS="-v" \
        INCLUDE_PATH="/mingw64/include" \
        LIBRARY_PATH="/mingw64/lib" \
        BINARY_PATH="/mingw64/bin" \
        PREFIX="x86_64-w64-mingw32-" \
		prefix=/mingw64 \
		install
```
Pronto para usarmos vamos a próxima biblioteca, se tiver alguma dúvida poste nos comentários e tentarei ajudar.


[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-5/)



