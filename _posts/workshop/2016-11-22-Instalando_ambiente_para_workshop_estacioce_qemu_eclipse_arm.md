---
title: "Instalando ferramentas e preparando ambiente"
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi]
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

O objetivo deste post é registrar os passos para preparar o ambiente para o Workshop de uso QEMU, Eclipse e ARM na estácio do Ceará.

<!--more-->

Primeiro passo é baixar o GCC para ARM, o mesmo se chama GCC ARM None EABI. e deve ser obtido para o [Windows 32bits Clicando Aqui](https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-eabi-5_4-2016q3-20160926-win32.exe). faça a instalação do pacote na pasta: `C:\GNU_Tools_ARM_Embedded\5.4 2016q3`.

## Instalando o MSys2

Em seguida instale o MSys2 escolha a plataforma [32-Bit](http://repo.msys2.org/distrib/i686/msys2-i686-20161025.exe) ou [64-Bit](http://repo.msys2.org/distrib/x86_64/msys2-x86_64-20161025.exe) (em um dos links) conforme seu ambiente.

Instale o MSys2 no diretório `c:\msys` para arquitetura 32-bit ou `c:\msys64`para arquitetura 64-bit.

Em seguida abra o shell executando o script `msys2_shell.cmd` que será encontrado na pasta onde foi instalado o MSys2 e execute os seguintes comandos, se a tela ao finalizar o comando, não se preocupe é normal, feche normalmente mesmo com alerta, e abra novamente e execute o próximo.

{% highlight sh %}
pacman -Suy pacman
pacman -Suy
pacman -Suy
{% endhighlight %}

O primeiro comando atualiza o próprio Pacman, o segundo atualiza todo o sistema, o terceiro é apenas para se ter certeza que tudo foi realmente atualizado, execute-o até que a mensagem lhe deixe claro que tudo está atualizado. Lembre-se se algum deles terminar e não voltar ao prompt (você perceberá depois que ele parar lhe dar mensagens de andamento dos processos), você pode fechar a janela e abrir de novo, normalmente isso irá acontecer apenas no primeiro comando e no máximo no segundo.

## Instalando o Eclipse

O eclipse pode ser instalado de duas formas, em ambas o java 1.8 ou maior deve estar instalado e preferencialmente no path.

Você pode baixar o instalador do Eclipse, através do instalador você terá que fazer o processo máquina por máquina, use os links a seguir para a arquitetura que for suas máquinas:

 * [Instalador 32-bit](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/neon/R1/eclipse-inst-win32.exe)
 * [Instalador 64-bit](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/neon/R1/eclipse-inst-win64.exe)
 
Seja qual instalador que tenha escolhido quando executa-lo será questionado o pacote que deseja instalar, escolha o pacote de nome **"Eclipse IDE for C/C++ Developers"**, este pacote deve ser instalado como é oferecido neste pacote nada mais.

Você tem a opção de baixar este pacote manualmente e apenas descompacta-lo, portanto isso facilita a instalação para mais de uma máquina podendo inclusive customizar a instalação de alguma forma para usar em todas as máquinas, mas aqui iremos usar apenas o básico, portanto escolha a arquitetura de seus ambiente e baixe o arquivo.

 * [Pacote para 32-bit](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/neon/1a/eclipse-cpp-neon-1a-win32.zip)
 * [Pacote para 64-bit](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/neon/1a/eclipse-cpp-neon-1a-win32-x86_64.zip)

Ao finalizar a instalação basta executar o arquivo `eclipse.exe`.

Veja que em ambos os métodos você terá que informar um diretório que será o espaço de trabalho para fazer o primeiro teste, use o que ele oferecer como sugestões evitando surpresas posteriores.

Finalmente vá no menu _"Help"_ e escolha a opção _"Check for Updates"_ e siga o processo até finalizar, normalmente ele irá informar que não há atualizações, mas se ouver, basta aceitar os contratos de licença e as chaves de verificação e finalizar a atualização aguardando a mensagem que completado.



## Resumo para facilitar

Eu gravei tudo no mega drive para facilitar para que posssam baixar posteriormente os aquivos usados no Workshop.

[Também tem estes post que ajuda na instalação do MSys2](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-1/)

## Páginas Oficiais

 * https://launchpad.net/gcc-arm-embedded
 * http://msys2.github.io/
 * http://www.eclipse.org/downloads/eclipse-packages/
 * http://gnuarmeclipse.github.io/install/
 * 
