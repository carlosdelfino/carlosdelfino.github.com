---
redirect_from:  "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-2/"
title: "Primeiros Passos com o QEMU, parte 2" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS ]
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
Começamos tudo instalando o MSYS2, vejo que para você foi um sucesso como foi para mim, então estamos neste segundo passo. 

<!--more-->

Mas, não adianta seguir se são teve sucesso no passo anterior. Seja honesto com você mesmo, faça cada passo até ter sucesso.

Caso tenha chegado aqui antes de tentar o primeiro passo, retorne a ele para fazê-lo até que tudo dê certo. [Clique aqui](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/Primeiros_Passos_com_o_QEMU-parte-1/ "Clique Aqui").

Agora vamos clonar o projeto do QEMU usando meu fork:

```sh
~/ $ git clone git@github.com:carlosdelfino/qemu.git qemu-delfino
~/ $ git submodule update --init
```

Coloque o python e o GCC que estamos usando no path usando o seguinte comando no shell do Msys2:

```sh
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
```

Veja que você também precisa de diversas bibliotecas além das que por padrão já estão como sub-módulos do repositório, como a *pixman* e *dtc*, por isso eu já deixei tudo organizado como submódulo no projeto principal em meu repositório assim basta usar o comando `submodule` do git para baixar a versão correta e compilar.

A obtenção deste repositório é importante pois nele configurei como módulos todas as bibliotecas que iremos precisar para ter sucesso na compilação do QEMU.

veremos nos próximos passos como obter cada uma delas e como compilá-las.

Depois de tudo pronto vou rever todos os passos e adicionar detalhes sobre como obter cada biblioteca, para que serve e sua importância no projeto.

[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-3/)