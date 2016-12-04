---
redirect_from:  
   - "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-2/"
   - "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-2/"
title: "Primeiros Passos com o QEMU, Passo 2" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Intel, TBB,  Emulação, Virtualização, KVM, QEMU, VMware, VirtualBox, VBox, Hiper-V, Xen, GNU ARM Eclipse, Eclipse, Windows, RTOS, uOS, Embarcados ]
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
Começamos tudo instalando o MSYS2, vejo que para você foi um sucesso como foi 
para mim, então estamos neste segundo passo. 

<!--more-->

Mas, não adianta seguir se são teve sucesso no passo anterior. Seja honesto com 
você mesmo, faça cada passo e repita se necessário até ter sucesso.

Caso tenha chegado aqui antes de tentar o primeiro passo, retorne a ele para 
fazê-lo até que tudo dê certo. [Clique aqui](http://carlosdelfino.eti.br/emulacaoevirtualizacao/Primeiros_Passos_com_o_QEMU-passo-1/ "Clique Aqui").

## Clonando o Repositório QEMU

Agora vamos clonar o projeto do QEMU usando meu fork. Abaixo estão os comandos 
que devem ser executados, veja que a linha de comando 
abaixo o que vem antes do dólar ($) representa o diretório onde o comando deve 
ser digitado, portanto `~/qemu-delfino/build $` que dizer que você está dentro 
do diretório `build` que está dentro do diretório `qemu-delfino` e que está
dentro do diretório home do usuário `~`.

{% highlight bash %}
~/ $ git clone --depth=1 git@github.com:carlosdelfino/qemu.git qemu-delfino
~/ $ cd qemu-delfino
~/qemu-delfino/ $ git submodule update --init --depth=1
{% endhighlight %}

Usaremos por hora a versão de desenvolvimento, na terceira fase iremos adotar
um novo branch para trabalharmos com as alterações.

A diretiva `depth`diz ao git para baixar apenas o ultimo commit evitando 
baixar todo o repositório de forma desencessária.

Quando executar o comando para atualizar os submodules pode ocorrer alguns erros
e ela ser interrompida, não se preocupe, iremos cada módulo atualiza-lo novamente
de forma individual, e também poderão haver mudanças quando estiver lendo este
artigo.

<figure>
<iframe width="640" height="360" src="https://www.youtube.com/embed/JGFOdaVMd6k?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
<figcaption>Neste video é apresentado os resultados durante a execução dos comandos</figcaption>
</figure>

## Ajustando o PATH.

Coloque o python e o GCC que foi de instalar no path usando o seguinte comando 
no shell do Msys2, caso já tenha feito isso no passo anterior e não fechou a 
janela do terminal, deve pular estes comandos, a execução repetitiva deles, irá 
prejudicar o funcionamento do `PATH`, portanto certifique-se sempre que os comandos
estão acessíveis:

{% highlight bash %}
~/qemu-delfino/ $ PATH=$PATH:/c/Python27:/c/Python27/DLLs
~/qemu-delfino/ $ PATH=$PATH:/mingw64/bin/
~/qemu-delfino/ $ export PATH
{% endhighlight %}

Para verificar se o python e o gcc estão corretos digite os seguintes comandos:

{% highlight bash %}
~/qemu-delfino/ $ python --version
Python 2.7.12

~/qemu-delfino/ $ gcc --version
gcc.exe (Rev2, Built by MSYS2 project) 6.2.0
Copyright (C) 2016 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
{% endhighlight %}

## Próximo passo

Depois de tudo pronto vou rever todos os passos e adicionar detalhes sobre como 
obter cada biblioteca, para que serve cada uma e sua importância no projeto. 
Portanto, estes posts estarão em constante atualziação.

[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-3/)
