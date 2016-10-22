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

### Compilando a Biblioteca gettext

```bash
gitclone/qemu-delifno/ $ git submodule update --init gettext
gitclone/qemu-delfino/ $ cd gettext
gitclone/qemu-delfino/gettext $ ./autogen.sh
gitclone/qemu-delfino/gettext $ cd ../build 
gitclone/qemu-delfino/build $ mkdir gettext
gitclone/qemu-delfino/build $ cd gettext
gitclone/qemu-delfino/build/gettext $
gitclone/qemu-delfino/build/gettext $ make
gitclone/qemu-delfino/build/gettext $ make install
```



### Compilando o QEMU

Crie um diretório para trabalhar por exemplo eu criei uma pasta chamada "build" dentro da pasta onde fiz o clone do QEMU 

	$ cd qemu-delfino
	qemu-delfino $ mkdir build
	qemu-delfino $ cd build
    build $

Nesta pasta iremos criar também uma pasta para cada biblioteca que formos compilar para uso no QEMU, assim evitamos poluir o diretório dos fontes com arquivos compilados e caso algo dê errado e quiser começar do zero, basta apagar tal pasta e criar novamente sem ter que baixar todo o repositório mais uma vez.

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
 * git://git.gnome.org/gtk+
 * git@github.com:libffi/libffi.git
 * it://git.savannah.gnu.org/gettext.git
 * git://git.savannah.gnu.org/libiconv.git