---
redirect_from: "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-4/"
title: "Primeiros Passos com o QEMU, Passo 4" 
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
Agora vamos compilar a biblioteca zlib, responsável por nos fornecer a API para 
compactação e descompactação de dados, como usado no ZIP, BZIP e GZip.

<!--more-->

A biblioteca zlib é importante para lidar com arquivos compactados, ela é 
importante para o QEMU diretamente.

Veja que esta biblioteca não tem como ser compilada fora de seu diretório original, 
onde estão os fontes, portanto seja cuidadoso ao limpar o diretório se desejar 
refazer a compilação. Caso tenha problemas use o comando `git checkout TAG --force`, 
onde a palavra `TAG`deve ser substituída pela *TAG* da versão selecionada para 
trabalho.

### Compilando a biblioteca zlib

Usaremos por hora a versão **1.2.8** portanto a *TAG* usada será ***v1.2.8***.

{% highlight bash %}
~/qemu-delifno/ $ git submodule update --init zlib
~/qemu-delfino/ $ cd zlib
~/qemu-delfino/ $ git checkout v1.2.8
{% endhighlight %}

Se ainda não colocou os diretórios do python e do GCC que estamos usando no path, 
faça isso usando o seguinte comando no shell do Msys2:

{% highlight bash %}
~/qemu-delfino/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/qemu-delfino/ $ PATH=/mingw64/bin/:$PATH
~/qemu-delfino/ $ export PATH
{% endhighlight %}

Agora use o comando abaixo para configurar a compilação, veja que estou informando
através da variável de istema `CROSS_PREFIX` o prefixo do compilador que será usado
para a compilação, mesm compilando o sistema para rodar neste mesma maquina, opto
em colocar esta informação para evitar que possa ser usado outro compilador:

{% highlight bash %}
~/qemu-delifno/zlib $ CROSS_PREFIX=x86_64-w64-mingw32- \
        PREFIX=/mingw64 \
        ./configure  
{% endhighlight %} 

e para compilar e instalar digite o comando:

{% highlight bash %}
~/qemu-delifno/zlib $ make -f win32/Makefile.gcc \
        CFLAGS="-pipe" \
        LDFLAGS="-v" \
        INCLUDE_PATH="/mingw64/include" \
        LIBRARY_PATH="/mingw64/lib" \
        BINARY_PATH="/mingw64/bin" \
        prefix=/mingw64 \
        install
{% endhighlight %}

Pronto para usarmos, veja no video abaixo como foi o procedimento.

<figure>
	<iframe width="640" height="360" src="https://www.youtube.com/embed/MsYjIHO9Yko?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
	<figcaption>video apresentando o processo de compilação da  biblioteca zlib</figcaption>
</figure>

## Atualizações

### 29/outubro/2016

Veja que antes eu determinava o `CROSS_PREFIX` no momento que eu executava o 
**make** porém algumas instalações do **MSYS2** estão dando problemas, portanto
por hora não vamos usa-lo.



Vamos a próxima biblioteca, se tiver alguma dúvida poste 
nos comentários e tentarei ajudar.


[Clique aqui para o próxima passo.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-5/)



