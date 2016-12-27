---
redirect_from:  
   - "/emula%C3%A7%C3%A3o%20e%20virtualiza%C3%A7%C3%A3o/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-1/"
   - "emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-parte-1/"
title: "Primeiros Passos com o QEMU, Passo 1" 
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
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Penso que o maior desafio para um programador C ou C++ é ter todos os ambientes 
que precisa disponíveis em sua máquina para compilar e testar seus programas, 
entenda todos os ambientes como múltiplos sistemas operacionais, múltiplas 
configurações e empacotamentos. Vamos ver então como fazer isso com o QEMU.

<!--more-->

Bem eu escolhi o Fork do Liviu Ionescu para trabalhar com o QEMU, seu fork foi 
criado para permitir emular embarcados e microcontroladores baseados em Cortex-M, 
e gostei de seu trabalho. Com isso, desejo ampliá-lo para o Arduino DUE o que se 
tornou para mim um desafio, em especial para rodar seu Sistema Operacional em 
Tempo Real - RTOS para Cortex-M chamado &Mu;OS.

Minha intenção é gerar apenas o QEMU para trabalhar com a família Cortex, seja 
A ou M, e talvez R, a família Cortex-A eu vou focar no Cortex-A53 a Família 
Cortex-M eu irei focar no que precisar e principalmente no que faltar no trabalho 
do Liviu Ionesco. Se vier a trabalhar com o Cortex-R inicialmente pretendo focar 
no Cortex-R52. Para saber porque, me consulte através dos comentários.

Conforme eu ampliar meu domínio sobre o QEMU principalmente em seu desenvolvimento, 
pretendo agregar o que tenho visto de melhor em outros Forks, inclusive AVR e
xTensa, por hora estarei trabalhando também com:

 * O origingal http://www.qemu.org
 * Fork do Liviu Ionesco: gnuarmeclipse.livius.net/qemu
 * Fork do Beckus para Cortex-M: git@github.com:beckus/qemu_stm32.git
 * Path AVR de Michael Rolnik e Richard Henderson: https://lists.nongnu.org/archive/html/qemu-devel/2016-09/msg03962.html

Os procesadores intel e emulação de pc serão usadas para testes com o Linux.

Estarei dividindo as publicações sobre este trabalho em partes, conforme eu for 
tendo sucesso na geração de material, portanto não sei quantas partes terei, mas 
a primeira será introdutória e como gerar o QEMU para o Windows diretamente dom o
fonte usando o MSYS2.

## O que é exatamente o QEMU

Bem, conforme o site do QEMU temos:

> QEMU is a FAST! processor emulator using dynamic translation to achieve good emulation speed.

Em tradução livre:

> QEMU é um emulador de processador RÁPIDO! que usa tradução dinâmica para atingir boa velocidade de emulação.

O QEMU tem dois modos de operação, um onde emula um sistema completo, como um 
computador, sendo todos os dispositivos de entrada e saída, acesso a memória. 
Neste modo podemos rodar um sistema operacional por completo dentro de outro 
sistema, por exemplo rodar o Linux dentro do Windows.

No segundo modo, o QEMU funciona em modo de emulação, ele emula apenas o processador, 
sendo usado para rodar uma aplicação como o Wine que permite executar aplicativos 
Windows dentro do Linux.

O QEMU é muito interessante tanto pela sua simplicidade de operação, um simples 
comando com varias diretivas que permitem carrarmos imagens e simularmos HD para 
armazenarmos dados, além de bastante dinâmico é bem rápido.

O principal uso que darei ao QEMU é fazer testes unitários e de sistema usando 
ambiente como o Trevis para testar códigos em diversos ambientes, já que o Trevis 
roda especificamente Linux, eu preciso do QEMU para simular um Cortex-M como o 
usado no Arduino DUE ou mesmo um Cortex-A como usado no NanoPI, em especial 
estarei usando imediatamente com o "Contador de Ciclistas"

## Algumas dicas de sucesso para estes passos.

Primeiro você deve seguir atentamente cada orientação dada nestes passos. A 
cada parte do processo você deve observar se o passo anterior não influência no 
atual, evitando assim que um erro vá causar um problema no final da compilação 
em um passo a frente.

As variáveis exportadas são o maior causador de problemas, procure ter cuidado 
ao definir as variáveis e veja se não há alguma dependência com alguma variável 
definida anteriormente.

Não crie diretórios usando nomes com espaços, caracteres especiais e muito menos 
com caminhos muito extensos, isso pode se virar contra você na hora de buscar 
soluções para problemas.


# Instale o Python 2.7.

O QEMU e algumas ferramentas usaram o Python, podemos optar em usar o python do
MSYS2, mas é melhor instalar o pacote do Python para windows comum. Também não
esqueça que você deve instalar o Python 2.7. Nem mais nem menos.

## Instalando o Msys2

O primeiro passo é instalar o MSYS2 em seu computador, baixe a ferramenta do 
link: https://msys2.github.io/, escolha o pacote conforme sua plataforma.

Depois de instalado entre no shell do MSYS2, execute a seguinte sequência de 
comandos para atualizá-lo, em cada comando reinicialize o shell.

{% highlight bash %}
~ $ pacman -Sy pacman
~ $ pacman -Syu
~ $ pacman -Su
{% endhighlight %}

Você verá algumas mensagens, informando que estão sendo baixados e instalados 
alguns pacotes,  e ficará claro que tudo deu certo ou algo deu errado, neste 
último caso entre em contato comigo pelos comentários.

vamos precisar do ToolChain completo para compilar em C/C++ para 64Bits, assim 
vou escolher instalar o pacote `git`, `mingw-w64-x86_64-toolchain`, 
`mingw64/mingw-w64-x86_64-glib2`, entre outros e todas as dependências.

Veja que estou usando os pacotes para plataforma 64bits x86 `x86_64`, se deseja 
instalar para 32bits substitua nos nomes dos pacotes o `X86_64`por `i686`.

Digite o comando

{% highlight bash %}
~ $ pacman -S git autoconf automake-wrapper \
        patch \
        groff \
        gperf \
        wget \
        texinfo \
        gettext \
        pkg-config \
        msys/liblzma \
        msys/libtool \
        msys/bison \
        msys/ncurses-devel \
        msys/mercurial \
        msys/perl \
        msys/perl-Encode-Locale \
        msys/perl-Locale-Gettext \
        msys/libutil-linux-devel \
        msys/util-linux \
        msys/mingw-w64-cross-binutils \
        mingw64/mingw-w64-x86_64-emacs \
        mingw64/mingw-w64-x86_64-diffutils \
        mingw64/mingw-w64-x86_64-libtool \
        mingw64/mingw-w64-x86_64-glib2 \
        mingw64/mingw-w64-x86_64-ncurses \
        mingw-w64-x86_64-toolchain 
{% endhighlight %}

E receberá uma mensagem similar a esta abaixo:

{% highlight bash %}
	:: Há 16 membros no grupo mingw-w64-x86_64-toolchain:
	:: Repositório mingw64
	   1) mingw-w64-x86_64-binutils  2) mingw-w64-x86_64-crt-git  3) mingw-w64-x86_64-gcc
	   4) mingw-w64-x86_64-gcc-ada  5) mingw-w64-x86_64-gcc-fortran  6) mingw-w64-x86_64-gcc-libgfortran
	   7) mingw-w64-x86_64-gcc-libs  8) mingw-w64-x86_64-gcc-objc  9) mingw-w64-x86_64-gdb
	   10) mingw-w64-x86_64-headers-git  11) mingw-w64-x86_64-libmangle-git
	   12) mingw-w64-x86_64-libwinpthread-git  13) mingw-w64-x86_64-make  14) mingw-w64-x86_64-pkg-config
	   15) mingw-w64-x86_64-tools-git  16) mingw-w64-x86_64-winpthreads-git

	Digite uma seleção (padrão=todos):
{% endhighlight %}

Então apenas tecle enter e logo a seguir receberá a lista do que será instalado 
no meu caso apresentou a seguinte lista:

{% highlight bash %}
    atenção: mingw-w64-x86_64-binutils-2.27-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-crt-git-5.0.0.4745.d2384c2-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-libgfortran-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-gcc-libs-6.2.0-2 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-headers-git-5.0.0.4747.0f8f626-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-libwinpthread-git-5.0.0.4741.2c8939a-1 está atualizado -- reinstalando
    atenção: mingw-w64-x86_64-winpthreads-git-5.0.0.4741.2c8939a-1 está atualizado -- reinstalando
    resolvendo dependências...
    procurando por pacotes conflitantes...
    atenção: dependência cíclica detectada:
    atenção: mingw-w64-x86_64-gcc-libgfortran será instalado antes de sua dependência mingw-w64-x86_64-gcc-libs
    
    Pacotes (32) mingw-w64-x86_64-ca-certificates-20150426-2  mingw-w64-x86_64-expat-2.2.0-1
	     mingw-w64-x86_64-gdbm-1.12-1  mingw-w64-x86_64-gettext-0.19.7-1
	     mingw-w64-x86_64-libffi-3.2.1-4  mingw-w64-x86_64-libsystre-1.0.1-2
	     mingw-w64-x86_64-libtasn1-4.9-1  mingw-w64-x86_64-libtre-git-r122.c2f5d13-4
	     mingw-w64-x86_64-ncurses-6.0.20161001-1  mingw-w64-x86_64-openssl-1.0.2.j-1
	     mingw-w64-x86_64-p11-kit-0.23.2-2  mingw-w64-x86_64-python2-2.7.12-1
	     mingw-w64-x86_64-readline-6.3.008-1  mingw-w64-x86_64-tcl-8.6.6-1
	     mingw-w64-x86_64-termcap-1.3.1-2  mingw-w64-x86_64-tk-8.6.6-1
	     mingw-w64-x86_64-binutils-2.27-2  mingw-w64-x86_64-crt-git-5.0.0.4745.d2384c2-1
	     mingw-w64-x86_64-gcc-6.2.0-2  mingw-w64-x86_64-gcc-ada-6.2.0-2
	     mingw-w64-x86_64-gcc-fortran-6.2.0-2  mingw-w64-x86_64-gcc-libgfortran-6.2.0-2
	     mingw-w64-x86_64-gcc-libs-6.2.0-2  mingw-w64-x86_64-gcc-objc-6.2.0-2
	     mingw-w64-x86_64-gdb-7.12-1  mingw-w64-x86_64-headers-git-5.0.0.4747.0f8f626-1
	     mingw-w64-x86_64-libmangle-git-5.0.0.4669.7de6266-1
	     mingw-w64-x86_64-libwinpthread-git-5.0.0.4741.2c8939a-1
	     mingw-w64-x86_64-make-4.1.2351.a80a8b8-1  mingw-w64-x86_64-pkg-config-0.29.1-2
	     mingw-w64-x86_64-tools-git-5.0.0.4669.7de6266-1
	     mingw-w64-x86_64-winpthreads-git-5.0.0.4741.2c8939a-1
    
    Tamanho total download:65,27 MiB
    Tamanho total instalado:  670,52 MiB
    Alteração no tamanho:   322,45 MiB
    
    :: Continuar a instalação? [S/n]
{% endhighlight %}    

Basta teclar [enter] novamente e esperar o termino da instalação:

**ATENÇÃO:** Se receber uma mensagem informando algo relativo a diretório `/mingw32` 
ou /mingw64` basta criar este diretório no raiz. a mensagem é similar a apresentada 
abaixo:

{% highlight bash %}
	erro: falha em submeter a transação (arquivos conflitantes)
	mingw-w64-i686-libiconv: /mingw32 existe no sistema de arquivos
{% endhighlight %}

Repita então o processo de instalação depois de criado os diretórios.

Alguns comandos serão regerados pelo processo, mas não se preocupe, apenas instale
como sugerido.

Claro quando ele te consultar sobre quais pacotes deseja instalar, você poderá 
selecionar instalar um deles, e repetir o processo, ou mesmo repetir o processo 
fazendo referência direta a cada pacote, só deve tomar cuidado para não esquecer 
nada, você vai precisar nó minimo dos pacotes que instalam:

 * ncurses
 * readline
 * termcap
 * binutils
 * gcc
 * gcc-libs
 * gdb
 * make
 * tols-git
 * winpthreads-git
 * python2 
 * expat 
 * libtre-git
 * libsystre 
 * glib2
 * autoconf
 * bison
 * e muitos outros

Aprenda o máximo que puder sobre a ferramenta `pacman`, ela sera sua ferramenta 
para lhe ajudar a instalar tudo que precisa no MSYS2.

<figure>
<iframe width="640" height="360" src="https://www.youtube.com/embed/ebUf_m8fRZ4?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>	
<figcaption>Video apresentando cada commando digitado neste video</figcaption>
</figure>

## Acerte o PATH

Fique atento ao `PATH` configurado, procure observar se os comandos que estão 
sendo executados são na versão esperada e para o **target** desejado. 
Principalmente para o Toolchain do GCC e Python. Procure usar o `PATH` a baixo 
a não ser quando orientado do contrário:

{% highlight bash %}
~/qemu-delfino/ $ PATH=$PATH:/c/Python27:/c/Python27/DLLs
~/qemu-delfino/ $ PATH=$PATH:/mingw64/bin/
~/qemu-delfino/ $ export PATH
{% endhighlight %}

Caso venha receber mensagens se queixando que o LC_ALL não está setado, basta
digitar o comando abaixo durante a seção de compilação. Para maiores informações
relativas a problemas com variáveis de [Internacionalização (I18N) e Localização
(L10N) clique aqui](http://pubs.opengroup.org/onlinepubs/7908799/xbd/envvar.html)
e também [nesse outro link](https://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html#The-LANGUAGE-variable).

{% highlight bash %}
~/qemu-delfino/ $ export LC_ALL="C"
{% endhighlight %}

Fique atento as redefinições de variáveis, de um passo para outro uma variável 
que define diretivas de compilação podem mudar, ou mesmo serem apagadas.

Fique atento com o diretório onde o comando deve ser executado, comandos como 
`git`, `hg`, `autogen.sh`, `autoreconf`, `configure`, `make` outros ligados ao 
GCC, devem ser executados exatamente no diretório indicado, se não será fatal.

Procure fazer sempre backup da pasta antes de fazer qualquer alteração em sua 
estrutura, e evite alterar arquivos a não ser que seja explicitamente indicado.

Fique atento toda as dicas estão sendo feitas considerando que tem uma maquina 
Windows com 64 Bits e rodando o Mingw, a pasta de instalação dos binários gerados 
será também sempre `/mingw64` e serão sempre usados no mínimo as diretivas abaixo 
no `configure`, comando que prepara o arquivo com os parametros de compilação,
 a não ser quando informado o contrário:

{% highlight bash %}
../../glib/configure \
            --prefix=/mingw64 \
            --build=x86_64-w64-mingw32 \
            --host=x86_64-w64-mingw32 \
            --target=x86_64-w64-mingw32
{% endhighlight %}

Em caso de dúvida use os comentários de cada passo para esclarecer sua dúvida.

## Começando a preparara para compilar meu primeiro QEMU

Você não precisa compilar seu QEMU, na internet você irá encontrar versões prontas 
para windows e Linux, tanto do QEMU original como Forks como o disponibilizado 
pelo Liviu Ionesco.

Para compilar seu QEMU você precisa baixar o Fonte original ou um FORK, eu irei 
usar como referência para o meu fork que é baseado no trabalho do Liviu e no 
fonte original, que pode ser encontrado link http://gnuarmeclipse.github.io/qemu/.

## Atualizações

### 05 de Novembro de 2016

Adiconado os pacotes:

 * msys/libutil-linux-devel
 * msys/util-linux 

Ambos os pacotes foram adicionados para permitir ampliar a compilação do QEMU.

### 03 de Novembro de 2016

Adicionado o pacote `msys/mingw-w64-cross-binutils`, o comando `x86_64-w64-mingw32-ar`
não estava presente no ambiente e é adiconado com este pacote.

Outras correções.

### 29 de Outubro de 2016

Se você já leu este post alguma vez, deve ter percebido que mudei algumas coisas.
hoje dia 29 de outubro de 2016, já é a quarta ou quinta vez que compilo algumas
parte deste projeto numa tentativa de melhorar o processo.

Por exemplo adicionei a instalação de pacotes o Gettext, mesmo que ele seja 
recompilado em nossos passos, optei em insta-lo para que todas as biblitoecas 
sejam atualizadas já com ele, não adianta eu compila-lo já no promeiro passo, 
mas com certeza irei reordenar os passos para que possamos compilar o Gettext
o quanto antes possível e assim usar a nossa versão atualizada.

Isso não atrabalha o nosso projeto, mas para gosta de compilar todos os binários
como eu gosto, isso é importante pois temos um código bem enchuto e tunado para
o nosso computador.

Nesta ordenação de prioridades já estou ajustando o nossos submódulos, isso
não impacta em desempeho, mas espelha as prioridades de disponibilidade.

## Próximo passo

Pronto estamos preparados para começar a compilação do QEMU (começar!), 
[veja como fazê-lo na segunda parte deste tutorial](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-2/).