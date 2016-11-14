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

Agora iremos obter uma biblioteca muito importante para as duas seguintes, 
ela é base para LibIconv e GetText. Iremos também compilar já a Libiconv.

<!--more-->

Vejamos então como proceder com a GnuLib e a Libiconv

### Preparando a biblitoeca GnuLib

GNULib não precisa ser compilada basta baixaremos apenas como um módulo do meu 
repositório como já informei.

Iremos usar um commit importante para o sucesso de nosso trabalho ele
está no commit de hash 6f9206d 
 

{% highlight bash %}
~/qemu-delifno/ $ git submodule update --init gnulib
~/qemu-delifno/ $ cd gnulib
~/qemu-delifno/ $ git checkout 6f9206d --force
{% endhighlight %}

Abaixo está o video do procedimento adotado relativo aos comandos acima:
<figure>
<iframe width="640" height="360" src="https://www.youtube.com/embed/EcNWMiW0wRM?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
<figcaption>Preparando o GNULib</figcaption>
</figure>

Agora podemos já trabalhar com a próxima biblioteca.

Certifique-se novamente que o python e o GCC estejam acessiveis pelo `PATH`, se
preciso faça isso usando o seguinte comando:


### Compilando a Biblioteca libiconv

A instalação do libiconv é bem simples, é importante fazemos a instalação dela 
antes e compilar o gettext.

Primeiro atualizamos o módulo que já deixamos pré pronto e fazemos o checkout 
da versão v1.9.2.

{% highlight bash %}
~/qemu-delifno/ $ git submodule update --init libiconv
~/qemu-delifno/ $ cd libiconv
~/qemu-delifno/libiconv/ $ git checkout v1.9.2
{% endhighlight %}

Defina o valor das variáveis LC_ALL e LANG como abaixo.

{% highlight bash %}
~/qemu-delifno/libiconv/ $ export LC_ALL="C"
~/qemu-delifno/libiconv/ $ export LANG="pt-BR.UTF8"
{% endhighlight %}

Criamos o diretório onde vamos compilar a biblioteca como padrão que adotei e 
configuramos o Makefile com os parâmetros de nosso ambiente:

{% highlight bash %}
~/qemu-delifno/ $ cd ../build
~/qemu-delifno/build $ mkdir libiconv
~/qemu-delifno/build $ cd libiconv
~/qemu-delifno/build/libiconv $ cd libiconv
~/qemu-delifno/build/libiconv $ ../../libiconv/configure \
                --prefix /mingw64 \
                --build=x86_64-w64-mingw32 \
                --disable-docs \
                CC="x86_64-w64-mingw32-gcc" \
                CXX="x86_64-w64-mingw32-g++" \
                LD="x86_64-w64-mingw32-ld" \
                NM="x86_64-w64-mingw32-nm" \
                AR="x86_64-w64-mingw32-ar" \
                RANLIB="x86_64-w64-mingw32-ranlib"
{% endhighlight %}

E finalmente executamos a compilação e instalação.

{% highlight bash %}
~/qemu-delifno/build/libiconv $ make
~/qemu-delifno/build/libiconv $ make install
{% endhighlight %}

Pronto, tendo alguma dúvida ou dificuldade use os comentários abaixo.



[Clique aqui para a próxima etapa.](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-6/)