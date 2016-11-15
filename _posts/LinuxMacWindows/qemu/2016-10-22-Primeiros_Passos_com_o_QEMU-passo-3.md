---
redirect_from: "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-3/"
title: "Primeiros Passos com o QEMU, Passo 3" 
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

Vamos neste passo, compilar nossa primeira biblioteca a LIBFFI responsável por 
permitir que haja interações entre funções em uma linguagem com outra, isso é 
expresso pelo seu nome FFI - Foreing Function Interface.

<!--more-->

Antes de continuarmos gostaria de esclarecer minha escolha em apresentar tais 
passos em detrimento de usar um script pronto, inclusive o projeto do Livius 
tem um excelente script. A escolha é puramente didatica, pois o aluno seguindo
estes passos tem a oportunidade de interagir com o processo completo de construção
de uma aplicação e sua compilação sem usar a IDE, interagindo com cada comando
e tendo a oportunidade de se aprofundar no proposito de cada um deles.

## Para que a Biblioteca libFFI

A biblioteca FFI é importante para integração do QEMU com outras linguagens, 
para quem é do Java, vai perceber uma certa semelhando com o propósito do JNI.

Tal biblioteca permite interagir por exemplo a linguagem Python com a maquina 
virtual, permitindo desenvolver softwares que interajam com outros aplicativos
que rodem internamente ao emulador.

Para conhecer mais sobre a biblioteca libFFI visite o site 
[https://sourceware.org/libffi/](https://sourceware.org/libffi/).

A LibFFI está tambem no GitHub e pode ser acessada pelo link 
[https://github.com/libffi/libffi](https://github.com/libffi/libffi)

## Compilando a Biblioteca libffi

O comando abaixo irá atualizar o submodulo criado para que seja usado o respositório
e branch correto. Estude um pouco do git para comprender melhor como funciona
os submódulos.

{% highlight bash %}
~/qemu-delifno/ $ git submodule update  --init libffi
~/qemu-delfino/ $ cd libffi
~/qemu-delfino/libffi $ git checkout v3.2.1
{% endhighlight %}

Se ainda não colocou o o python e o GCC que estamos usando no path, faça isso 
usando o seguinte comando no shell do Msys2:

{% highlight bash %}
~/qemu-delfino/ $ PATH=$PATH:/c/Python27:/c/Python27/DLLs
~/qemu-delfino/ $ PATH=$PATH:/mingw64/bin/
~/qemu-delfino/ $ export PATH
{% endhighlight %}

Abaixo definimos que o compilador C será x86\_64-w64-mingw32-gcc e o compilador 
C++ será x86\_64-w64-mingw32-g++

{% highlight bash %}
~/qemu-delfino/ $ export CC=x86_64-w64-mingw32-gcc 
~/qemu-delfino/ $ export CXX=x86_64-w64-mingw32-g++
{% endhighlight %}
				
Agora vamos compilar o projeto. Irei descrever cada conjunto de comandos 
detalhadamente, mas não farei isso em todos os passos, pois pode ficar repetitivo.

{% highlight bash %}
~/qemu-delifno/ $ mkdir build
{% endhighlight %}

A pasta `build` será nossa pasta de trabalho, quase todas as compilações
serão feitas nela, portanto se algo der errado basta remove-la e começar de novo.

Dentro desta pasta serão criadas uma pasta para cada projeto quando for o caso.

Abaixo executo o autogen.sh que irá atualizra algumas informações de compilação.
Uteis para uso no comando `configure`.

{% highlight bash %}
~/qemu-delifno/libffi $ ./autogen.sh
{% endhighlight %}

Em seguida devemos mudar de diretório para o  de trabalho, e criaremos uma 
subpasta chamada `libffi` onde iremos rodar os comandos de compilação.

{% highlight bash %}
~/qemu-delifno/libffi $ cd ..
~/qemu-delifno/ $ cd build
~/qemu-delifno/build $ mkdir libffi
~/qemu-delifno/build $ cd libffi
{% endhighlight %}

E a seguir o comando configure, que  irá fazer a checagem de dependências e 
parametrização do arquivo `Makefile` que será usado pelo comando `make` para 
gerar nossa biblioteca.

{% highlight bash %}
~/qemu-delifno/build/libffi $ ../../libffi/configure \
                    --prefix /mingw64 \
                    --build=x86_64-w64-mingw32 \
                    --with-gnu-ld
{% endhighlight %}

No comando `configure` acima faremos a configuração da compilação. A diretiva 
`--prefix` informa que a instalação será feita na pasta `/mingw64`, você pode 
mudar isso caso queira criar uma pasta especial para o QEMU, por exemplo 
`/mingw64/qemu`, mas pode haver efeitos colatarais com relação a carga de 
bibliotecas dinamicas, por hora vamos deixar como está.

Além disso, desabilitei também através da diretiva `--diable-docs` a geração 
de documentos, assim economizamos tempo e problemas com a instalação da 
ferramenta `makeinfo`.

Finalmente podemos compilar e instalar com os dois comandos a seguir:

{% highlight bash %}
~/qemu-delfino/build/libffi $ make
~/qemu-delfino/build/libffi $ make install
{% endhighlight %}

Não deverá ser apresentada nenhuma mensagem de erro.

Para finalizar adicone o diretório `/mingw64/lib/pkgconfig` a variável
`PKG_CONFIG_PATH` para que seja usado pela ferramenta **pkg-config**, apartir
de agora, faça isso sempre que for compilar algum pacote.

{% highlight bash %}
~/qemu-delfino/ $ PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/mingw64/lib/pkgconfig
~/qemu-delfino/ $ export PKG_CONFIG_PATH
{% endhighlight %}

A seguir o video do processo sendo executado por mim.

<figure>
<iframe width="640" height="360" src="https://www.youtube.com/embed/RJu2h9xOAcI?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
<figcaption>video apresentando o processo de compilação da  biblioteca libFFI</figcaption>
</figure>
Qualquer dúvida me informe nos comentários abaixo.

## Atualizações

### 12 de Novembro, 

Adotei a versão 3.2.1 identificada pela tag v3.2.1.

Adotei a opção para usar o LD como gnu-ld.


[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-4/)

