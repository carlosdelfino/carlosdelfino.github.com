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

A biblioteca zlib é importante para lidar com arquivos compactados, ela é importante para o QEMU diretamente.

Veja que esta biblioteca não tem como ser compilada fora de seu diretório original, onde estão os fontes, portanto seja cuidadoso ao limpar o diretório se desejar refazer a compilação. Caso tenha problemas use o comando `git checkout TAG --force`, onde a palavra `TAG`deve ser substituída pela *TAG* da versão selecionada para trabalho.

Usaremos por hora a versão **1.2.8** portanto a *TAG* usada será ***v1.2.8***.

```sh
gitclone/qemu-delifno/ $ git submodule update --init zlib
gitclone/qemu-delfino/ $ cd zlib
gitclone/qemu-delfino/ $ git checkout v1.2.8
```
Agora use o comando abaixo para configurar a compilação:

```sh
gitclone/qemu-delifno/zlib $ CROSS_PREFIX=x86_64-w64-mingw32- \
		PREFIX=/mingw64 
		./configure  
``` 

e para compilar e instalar digite o comando:

```sh
gitclone/qemu-delifno/zlib $ make -f win32/Makefile.gcc install \
		CFLAGS="-pipe" \
        LDFLAGS="-v" \
        INCLUDE_PATH="/mingw64/include" \
        LIBRARY_PATH="/mingw64/lib" \
        BINARY_PATH="/mingw64/bin" \
        PREFIX="x86_64-w64-mingw32-" \
		prefix=/mingw64 \
		install
```
Pronto para usarmos vamos a próxima biblioteca.

### Compilando a biblitoeca GnuLib

GNULib é importante para a biblioteca GetText e libiconv.

```bash
gitclone/qemu-delifno/ $ git submodule update --init gnulib
```



### Compilando a Biblioteca libiconv

A instalação do libiconv é bem simples, é importante fazemos a instalação dela antes e compilar o gettext.

Primeiro atualizamos o módulo que já deixamos pré pronto e fazemos o checkout da versão v1.9.2.

```sh
gitclone/qemu-delifno/ $ git submodule update --init libiconv
gitclone/qemu-delifno/ $ cd libiconv
gitclone/qemu-delifno/libiconv/ $ git checkout v1.9.2
```

Criamos o diretório onde vamos compilar a biblioteca como padrão que adotei e configuramos o Makefile com os parâmetros de nosso ambiente:

```sh
gitclone/qemu-delifno/ $ cd ../build
gitclone/qemu-delifno/build $ mkdir libiconv
gitclone/qemu-delifno/build $ cd libiconv
gitclone/qemu-delifno/build/libiconv $ cd libiconv
gitclone/qemu-delifno/build/libiconv $ ../../libiconv/configure \
				--prefix /mingw64 \
				--build=x86_64-w64-mingw32 \
				--disable-docs \
				CC=x86_64-w64-mingw32-gcc \
				CXX=x86_64-w64-mingw32-g++ 
```

E finalmente executamos a compilação e a instalação.

```sh
gitclone/qemu-delifno/build/libiconv $ make
gitclone/qemu-delifno/build/libiconv $ make install
```

### Compilando a Biblioteca gettext

Gettext para ser compilado na versão 0.19.8.1 precisa de uma versão especifica do GNULib, portanto iremos primeiro atualizar nosso repositório pra esta versão com o seguinte comando:

```sh
gitclone/qemu-delfino/ $ cd gnulib
gitclone/qemu-delfino/gnulib/ $ git checkout 6f9206d --force
```

Agora podemos prosseguir com o gettext, como ele já está como submódulo, basta atualizá-lo com os seguintes comandos:

```sh
gitclone/qemu-delifno/ $ git submodule update --init gettext
gitclone/qemu-delfino/ $ cd gettext
gitclone/qemu-delfino/gettext $  git checkout v0.19.8.1
```

precisamos atualizar as configurações antes de executá-las para criar o `Makefile` e então compilar o projeto no diretório de trabalho.

```sh
gitclone/qemu-delfino/gettext $  GNULIB_SRCDIR=../gnulib \
            GNULIB_TOOL=../gnulib-tool \
            ./autogen.sh
```


```sh
~/qemu-delfino/gettext $ cd ../build 
~/qemu-delfino/build/ $ mkdir gettext
~/qemu-delfino/build/ $ cd gettext
~/qemu-delfino/build/gettext $  ../../gettext/configure \
		--host=x86_64-w64-mingw32 \
		--prefix=/mingw64 \
		--with-gnu-ld \
		--without-bzip2 \
		--without-xz \
		--without-emacs \
		--without-lispdir \
		--without-cvs \
		--disable-java \
		--disable-native-java \
		--disable-c++ \
		--disable-libasprintf \
		--disable-openmp \
		--disable-csharp \
		--enable-threads=win32 \
		--enable-relocatable \
		--build=x86_64-w64-mingw32
```
E finalmente podemos compilar o gettext.

```sh
~/qemu-delfino/build/gettext $ make
~/qemu-delfino/build/gettext $ make install
```





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