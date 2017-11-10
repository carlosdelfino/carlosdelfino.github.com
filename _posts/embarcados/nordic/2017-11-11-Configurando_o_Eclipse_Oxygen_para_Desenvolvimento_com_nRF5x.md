---
title: Configurando o Eclipse Oxygen para Desenvolvimento com nRF5x
layout: article  
tags: [ARM, CORTEX-M, ARMV8-M, IoT, Embarcados, Hello World Arduino, nRF, nRF5x, nRF51, nRF52, SDK, Cortex-M0, Cortex-M0+, Cortex-M1, Cortex-M23, Cortex-M33, Cortex-M3, Cortex-M4, Cortex-M7, AMBA, multicore]
categories: [ARM, Cortex-M, nRF5x]
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
ads:
 show: true
image:
  teaser: arm/Cortex-M23-33-350x155.png
  feature: arm/emabarcados-inteligentes-usando-cortex-m.png
---
Este tutorial visa ajudar os iniciantes da língua portuguesa, como eu, com a família nRF5x e que escolheram usar o Eclipse como ferramenta de desenvolvimento.

O tutorial será muito simples e usaremos o Eclipse Oxygen e o GNU MCU Plugin (Antigo GNU ARM Eclipse Plugin), além do GCC 6.
<!--more-->

Também haverão tutoriais separados para cada etapa, neste será a configuração apenas do Eclipse para uso das Ferramentas e logo a seguir criarei outro mostrando como criar um projeto usando um dos exemplos, e finalmente um terceiro demonstrando como criar um projeto do zero.

**Instalando o GCC para ARM**
==========================

Para compilar seus Firmwares você irá precisar do GCC para ARM, a propria ARM está cuidando agora da versão mais indicada para uso com os microcontroladores da familia Cortex-M e Cortex-R, portanto vamos baixar do site da ARM o GCC  e instala-lo conforme o padrão, portanto basta executar o instalador e seguir até o fim sem mudar nenhum parâmetro de instalação.

Escolha a ultima versão conforme seu Sistema Operacioal no link a seguir https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads

Faça a instalação sem alterar nenhum parâmetro ou diretório.

Agora vá a linha ao prompt de comando e digite `arm-none-eabi-gcc --version` e veja se o resultado se assemelha ao apresentado abaixo, a versão deve ser igual ou superior:


    x:\nRF5_SDK\14.x.x\examples\peripheral\blinky\pca10028\s110\armgcc>arm-none-eabi-gcc --version
    arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors 6-2017-q2-update) 6.3.1 20170620 (release) [ARM/embedded-6-branch revision 249437]
    Copyright (C) 2016 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


Em seguida digite no windows o comando `where arm-none-eabi-gcc` e certifique-se que em seu path haja apenas uma instalação e seja a que você acabou de fazer, caso contrário vá nas configurações do windows e remova as demais versões.

    X:\nRF5_SDK\10.x.x\examples\peripheral\blinky\pca10028\s110\armgcc>where arm-none-eabi-gcc
    C:\Program Files (x86)\GNU Tools ARM Embedded\6 2017-q2-update\bin\arm-none-eabi-gcc.exe

**Ferramentas de apoio para compilação**
====================================

No windows é preciso que seja instalado algumas ferramentas de apoio, e o autor do GNU ARM/MCU Plugin para Eclipse já nos presenteou com um instalador com todas que precisamos, para tanto, visite o link https://github.com/gnu-mcu-eclipse/windows-build-tools/releases e baixe a versão mais atual.

Faça a instalação padrão e certifique-se que não haja outras ferramentas similares no path, como o make, rm, ls, cp. para isso basta usar o comando where com cada uma delas no prompt de comando, por exemplo `where make`.

    C:\nRF5_SDK\10.x.x\examples\peripheral\blinky\pca10028\s110\armgcc>where make
    C:\Program Files\GNU MCU Eclipse\Build Tools\2.9-20170629-1013\bin\bin\make.exe

**Instalando a ferramenta de auxilio para depuração (DEBUG)**
======================================================

jLink e OpenOCD são as ferramentas para auxiliar depuração e gravar Firmwares mais utilizadas no universo de microcontroladores, e par ao nRF não é diferente, porém para faciliar nossa vida é fornecido um pacote de ferramentas de linha de comando que na ultima versão já vem com o jLink, portanto você tendo a placa de testes do nRF5x você poderá facilmente usar estas ferramenta.

Basta visitar o link http://www.nordicsemi.com/eng/nordic/Products/nRF51822/nRF51-Tools/33444 e baixar a ultima versão.

A instalação é muito simples e basta ser feita seguindo os parâmetros padrões e depois certificando que o path da instalação se encontra no *System Path*, para isso basta entrar na linha de comando e digitar o comando `where nrfjprog`:

    C:\Nordic\nRF5_SDK\10.x.x\examples\peripheral\blinky\pca10028\s110\armgcc>where nrfjprog
    C:\Program Files (x86)\Nordic Semiconductor\nrf5x\bin\nrfjprog.exe

Veja que esta ferramenta é desenvolvida pela Nordic para facilitar nossa vida, assim ela foi criada apenas para uso com a linha nRF51 e nRF52.

Em outro post entrarei em detalhes de como usa-lo.

**Instalando o Eclipse**
====================

Agora já podemos partir para instalação do Eclipse, que não tem segredo, vá ao site [www.eclipse.org](http://www.eclipse.org) e baixe a versão Eclipse Oxygen CDT, é a versão mais indicada para uso com o GNU MCU Plugin, mas não vejo problemas em vc usar outro Eclipse Oxygen já instalado, eu por exemplo estou usando o Eclipse para Web e JavaScript e adicionei o plugin CDT e não tive problemas, já faço isso a algum tempo, usar diversas linguagens e plugins no mesmo eclipse e nas últimas versões está cada vez mais estável, e na versão Oxygen não identifiquei nenhuma dificuldade ainda.


**Instalando o GNU MCU Plugin**
============================

Para instalar o GNU MCU Plugin também não há dificuldade alguma, apenas lembre-se de certificar que os diretórios onde se encontram os binários do GCC, Build Tools como explicado acima, estão corretamente no *System Path do Windows*..

*Lembrando que este tutorial é para windows,* mas aqueles que trabalham com o linux não terão dificuldade alguma em adaptar as explicações para sua versão de linux.

Você pode seguir as instruções disponíveis no site: https://gnu-mcu-eclipse.github.io, porém, para instalar de forma bem simples você vai ao menu do Eclipse, seleciona "Help" → "Eclipse Marketplace", pesquise por "GNU MCU Eclipse" e siga os passos padrões de instalação de plugin.

Para o nosso caso somente é necessário selecionar durante a instalação os seguintes recursos:

 - GNU ARM C/C++ Cross Compiler
 - GNU ARM C/C++ Packs
 - GNU ARM C/C++ J-link Debugging

Os demais são opcionais e podem ser evitados por hora.

Ao finalizar a instalação reinicialize o Eclipse, e logo em seguida vamos terminar a parametrização das ferramentas.

## Parametrizando o Eclipse para uso do Plugin e GCC

Para finalizar esta etapa de nosso tutorial vamos finalizar a configuração do plugin e parametriza-lo para que tenhamos sucesso em usa-lo com o SDK do nRF5x.

Iremos seguir a ordem das opções presentes na árvore de configuração. Visite o seguinte o menu do Eclipse, selecione "Windows" → "Preferences", então selecione na arvore de configurações a esquerda, "MCU", e então selecione "Global ARM Toolchain Paths", procure o path onde foi instalado e o selecione transferindo para a caixa de texto, é bem provável que o caminho seja `C:/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin`.

Agora faça o mesmo para "Global Build Tools Path", e pesquise o caminho transferindo para a caixa de texto, é bem provável também que tenha instalado em `C:\Program Files\GNU MCU Eclipse\Build Tools\2.9-20170629-1013\bin\bin`.

E finalmente configure o j-Link selecionando "Global SEGGER J-Link Paths", pesquise o caminho onde foi instalado, previamente `C:/Program Files (x86)/SEGGER/JLink_V620b/` e transfira para a caixa de texto do path, e na caixa de texto do comando (Executable) digite `JLinkGDBServerCL.exe`

Como pode ver pelos nomes de grupos de parâmetros, é uma configuração Global, portanto sempre que abrir o Eclipse não importa o Workspace ou projeto, ele irá usar estas configurações. Caso queira fazer testes com outras versões de cada ferramenta, você pode criar um conjunto de configuração para cada workspace, e no projeto você também pode intervir em tais parâmetros para personalizar por projeto.

## Ajustando parametros de compilação e indexão

O Ajuste de parâmetros de compilação e indexação é feito por projeto, portanto aguarde o próximo tutorial onde mostrarei como usar um dos exemplos do SDK e parametriza-lo corretamente.

Conclusão
=========

Como podem ver a configuração é bem simples, não há praticamente segredo algum. No próximo tutorial irei demonstrar os macetes para se criar o primeiro projeto no Eclipse usando um dos exemplos presentes no SDK.

Este tutorial foi inspirado no aprendizado obtido com o tutorial escrito por [Vitar Berg](https://devzone.nordicsemi.com/users/2871/vibe/), funcionário da Nordic: https://devzone.nordicsemi.com/tutorials/7/
