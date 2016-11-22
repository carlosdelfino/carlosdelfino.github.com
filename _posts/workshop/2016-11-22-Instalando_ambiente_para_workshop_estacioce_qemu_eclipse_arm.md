---
redirect_from: /workshop/estacio_ceara/20162/Instalando_ambiente_para_workshop_estacioce_qemu_eclipse_arm/
title: "Instalando ferramentas e preparando ambiente"
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop]
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

Abaixo estão os passos resumidos para cada instalação, detalhes serão discutidos durante o workshop.

Em todas as instalações evite espaços nos nomes dos diretórios, mesmo que o windows trate bem tal situação, algumas ferramentas podem não lidar bem com os espaço, sem falar no incoveniente de de termos que usar aspas para agregar nomes de caminhos.

## Instalando o GCC para ARM

Primeiro passo é baixar o GCC para ARM, o mesmo se chama GCC ARM None EABI e deve ser obtido para o [Windows 32bits Clicando Aqui](https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-eabi-5_4-2016q3-20160926-win32.exe). Faça a instalação do pacote na pasta: `C:\GNU_Tools_ARM_Embedded\5.4 2016q3`.

O instalador irá lhe perguntar se deseja abrir o shell do GCC, você deixa esta opção marcada, porém a opção para adicionar ao path o diretório do GCC deve ficar desmarcada evitando que seu path seja alterado e você tenha problemas caso precise usar mais uma versão de GCC.


Para confirmar se a instalação ocorreu corretamente, se o shell não abriu logo em seguida vá na pasta `bin` na pasta que você seleciou para instalação e execute o arquivo `gccvar.bat` e no novo shell digite `arm-none-eabi-gcc --version`, e a seguinte mensagem será apresentada:

```
arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors) 5.4.1 20160919 (release) [ARM/embedded-5-branch revision 240496]
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```


## Instalando o MSys2

Em seguida instale o MSys2 escolhendo a plataforma em dos links a seguir, [arquitetura 32-Bit](http://repo.msys2.org/distrib/i686/msys2-i686-20161025.exe) ou [arquitetura 64-Bit](http://repo.msys2.org/distrib/x86_64/msys2-x86_64-20161025.exe) conforme seu ambiente.

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

## Instalando o OpenOCD

O OpenOCD deve apenas ser instalado com o básico, para que que os participantes do Workshop o configurem durante as atividades do evento.

Com nos outros softwares você deve escolher o pacote conforme sua arquitetura, portanto para clique nos links a seguir para baixar para [arquitetura 32-bit](https://github.com/gnuarmeclipse/openocd/releases/download/gae-0.10.0-20161028/gnuarmeclipse-openocd-win32-0.10.0-201610281609-dev-setup.exe) e para [arquitetura 64-bit neste link](https://github.com/gnuarmeclipse/openocd/releases/download/gae-0.10.0-20161028/gnuarmeclipse-openocd-win64-0.10.0-201610281609-dev-setup.exe)

No meu ambiente de trabalho uso a pasta `C:\GNU_ARM_Eclipse\OpenOCD\0.10.0-201610281609-dev` para instalar o QEMU, veja que a subpasta muda conforme a versão instalada `0.10.0-201610281609-dev`, sendo esta instalação nesta versão, futuramente este diretório poderá ter outro nome, eu mantenho o histórico dos instaladores para que possa detectar **bugs**.

## Resumo para facilitar

Eu gravei tudo no [mega drive](https://mega.nz/#F!0hs0mT5R) para facilitar para que posssam baixar posteriormente os aquivos usados no Workshop.

[Também tem estes post que ajuda na instalação do MSys2](http://carlosdelfino.eti.br/emulacaoevirtualizacao/qemu/compilando/Primeiros_Passos_com_o_QEMU-passo-1/)

## Páginas Oficiais

 * https://launchpad.net/gcc-arm-embedded
 * http://msys2.github.io/
 * http://www.eclipse.org/downloads/eclipse-packages/
 * https://github.com/gnuarmeclipse/openocd/releases
 * http://gnuarmeclipse.github.io/install/
 * 
