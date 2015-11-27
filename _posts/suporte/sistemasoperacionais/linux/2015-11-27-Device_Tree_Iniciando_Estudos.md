---
title: "Device Tree - Iniciando Estudos" 
tags: [Linux, Device, Tree, Device Tree, Sistemas Operacionais, Boot]
category: [Sistemas Operacionais, Linux, Boot]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Buscando ampliar meus conhecimentos sobre o uso do Linux em Sistemas Embarcados, 
encontrei um artigo na Communidade ARM (listado na seção fontes abaixo) que fala sobre Device Tree, 
Então partir em busca de mais conhecimento.

<!--more-->

Abaixo estou apresentando a tradução livre do conteúdo do site www.devicetree.org, onde é 
descrito este recurso que auxilia o processo de boot do Linux descrevendo textualmente a estrutura
do host. As traduções estão intercaladas com meu texto em forma de citação.

    "Device Tree" é uma estrutura de dados para descrever o hardware, ao invés de codificar cada detalhe 
    do dispositivo no sistema operacional, muitos aspectos do hardware podem ser descritos em uma estrutura
    de dados que é passada para o sistema operacional durante o momento do boot. O device tree é usado por 
    ambos, Pelo Firmware Aberto, e pelo  "Flattened Device Tree".

O objetivo deste meu estudo não é me tornar um especialista no tópico, porém comprender o formato do arquivo
e como ele é utilizado no processo de boot, e assim poder contribuir com explicações e esclarecimentos para
os demais colegas que possam estar buscando soluções.

[Mais informações sobre o arquivo descritor e como cria-lo, podem ser obtidos clicando aqui.](http://www.devicetree.org/Device_Tree_Usage)

    A estrutura de dados por si mesmo é uma simples arvore nomeada por nós e propriedades. Cada nó contem 
    propriedades e nós filhos. Propiedades são simplesmente pares de nomes-valor. A estrutura pode conter 
    algum tipo de dado.

    Porém, para que seja útil, os dados do device tree devem ser organizados em uma estrutura que o sistema
    operacional possa entende-lo. Um "bindings" é uma estrutura de de como os disposítivos é descrito no device tree.
    "Bindings" para uma coleção de dispositivos são bem estabelecidas e documentadas. Você pode ler sobre isso
    nas seguintes documentações 
    ["POWER.ORG™ STANDARD FOR EMBEDDED POWER ARCHITECTURE™ PLATFORM REQUIREMENTS (EPAPR)"](https://www.power.org/documentation/epapr-version-1-1/)
    e na norma IEEE 1275 (OpenFirmware).

Bem, por hora não irei detalhar mais informações, já que para nós isso é mais que suficiente para entendermos
do que se trata tal arquivo, e como ele impacta o fucnionamento do Kernel do Linux.

Abaixo segue as fontes sugeridas para um estudo mais aprofundado:

  * Lista de discussão sobre DeviceTree: devicetree-discuss@lists.ozlabs.org
  * [OpenFirmware](http://playground.sun.com/1275/home.html) - este link está fora do ar.
  * [ePAPR](http://www.power.org/resources/downloads/Power_ePAPR_APPROVED_v1.0.pdf)
  * [Documentação e implementações do OpenBIOS Source para Open Firmware](OpenBIOS)
  * [Linux Kernel device tree bindings: dts-bindings](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=Documentation/powerpc/dts-bindings;h=6096c2cc88a90bfac0b1f0c319689e788817f54a;hb=326ba5010a5429a5a528b268b36a5900d4ab0eba)
  * [Device Tree on ARM Linux kernel work](https://wiki.ubuntu.com/KernelTeam/ARMDeviceTrees)
  * [FreeBSD Device Tree support](http://wiki.freebsd.org/FlattenedDeviceTree)
