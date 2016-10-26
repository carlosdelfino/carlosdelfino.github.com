---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-5/"
title: "Primeiros Passos com o QEMU, Passo 5" 
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
  teaser: programacao/ccplusplus/programacao-660x300.png
  feature: programacao/ccplusplus/programacao-660x300.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

Agora iremos obter uma biblioteca muito importante para as duas seguintes, ela é base para LibIconv e GetText. Iremos também compilar já a Libiconv.

### Compilando a biblitoeca GnuLib

GNULib não precisa ser compilada basta baixaremos apenas como um módulo do meu repositório como já informei.
 

```bash
~/qemu-delifno/ $ git submodule update --init gnulib
```

Agora podemos já trabalhar com a próxima biblioteca.

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

### Compilando a Biblioteca libiconv

A instalação do libiconv é bem simples, é importante fazemos a instalação dela antes e compilar o gettext.

Primeiro atualizamos o módulo que já deixamos pré pronto e fazemos o checkout da versão v1.9.2.

```sh
~/qemu-delifno/ $ git submodule update --init libiconv
~/qemu-delifno/ $ cd libiconv
~/qemu-delifno/libiconv/ $ git checkout v1.9.2
```

Criamos o diretório onde vamos compilar a biblioteca como padrão que adotei e configuramos o Makefile com os parâmetros de nosso ambiente:

```sh
~/qemu-delifno/ $ cd ../build
~/qemu-delifno/build $ mkdir libiconv
~/qemu-delifno/build $ cd libiconv
~/qemu-delifno/build/libiconv $ cd libiconv
~/qemu-delifno/build/libiconv $ ../../libiconv/configure \
				--prefix /mingw64 \
				--build=x86_64-w64-mingw32 \
				--disable-docs \
				CC=x86_64-w64-mingw32-gcc \
				CXX=x86_64-w64-mingw32-g++ 
```

E finalmente executamos a compilação e instalação.

```sh
~/qemu-delifno/build/libiconv $ make
~/qemu-delifno/build/libiconv $ make install
```

Pronto, tendo alguma dúvida ou dificuldade use os comentários abaixo.



[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-6/)