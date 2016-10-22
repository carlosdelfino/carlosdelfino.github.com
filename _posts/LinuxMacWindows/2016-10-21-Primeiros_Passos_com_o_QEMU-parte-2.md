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

Veja que você também precisa de diversas bibliotecas além das que por padrão já estão como sub-modulos do repositório, como a *pixman* e *dtc*, por isso eu já deixei tudo organizado como submódulo no projeto principal em meu repositório assim basta usar o comando `submodule` do git para baixar a versão correta e compilar.

Vejamos o que devemos fazer para cada biblioteca

### Compilando a Biblioteca libffi

Abaixo estão os comandos que devem ser executados, veja que a linha de comando abaixo o que vem antes do dolar ($) representa o diretório onde o comando deve ser digitado, portanto `build $` que dizer que você está dentro do diretório `build`

```bash
gitclone/qemu-delifno/ $ git submodule update --init libffi
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

não deverá ser apresentada nenhuma mensagem de erro qualquer dúvida me informe nos comentários abaixo.

### Compilando a biblioteca zlib

A biblioteca zlib é importante para lidar com arquivos compactados, assim dá poder ao  software de lidar com arquivos que foram compactados.

Veja que esta biblioteca não tem como ser compilada fora de seu diretório original, onde estão os fontes, portanto seja cuidadoso ao limpar o diretório se desejar refazer a compilação. Caso tenha problemas use o comando `git checkout TAG --force`, onde a palavra `TAG`deve ser substituída pela *TAG* da versão selecionada para trabalho.

Usaremos por hora a versão **1.2.8** portanto a *TAG* usada será ***v1.2.8***.

```sh
gitclone/qemu-delifno/ $ git submodule update --init zlib
gitclone/qemu-delfino/ $ cd zlib
gitclone/qemu-delfino/ $ git checkout v1.2.8
```
Agora use o comando abaixo para configurar a compilação:

```sh
    CROSS_PREFIX=x86_64-w64-mingw32- \
		PREFIX=/mingw64 
		./configure  
``` 

e para compilar e instalar digite o comando:

```sh
    make -f win32/Makefile.gcc install \
		CFLAGS="-pipe" \
        LDFLAGS="-v" \
        PREFIX="x86_64-w64-mingw32-" \
        INCLUDE_PATH="/mingw64/include" \
        LIBRARY_PATH="/mingw64/lib" \
        BINARY_PATH="/mingw64/bin" 
```
Pronto para usarmos vamos a próxima biblioteca.



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
 * 