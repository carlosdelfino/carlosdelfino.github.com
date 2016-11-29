---
redirect_from: /workshop/estacio_ceara/2016_2/Apresentacao_rapida_do_QEMU/
title: Apresentação rápida do QEMU
date: 2016-11-29 02:20:00 -0300
categories: [III-SiConect]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, pranejamento, SS&#x1d09;conect]
layout: article-workshop-estacio-2016-1
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
coinbase:
 show: true
---

QEMU um emulador de alto desempenho para criação de hardware virtual.

<!--more-->

![QEMU](/images/QEMU/Qemu-logo.png)

> A physicist, an engineer, and a computer scientist were discussing the nature of God. “Surely a Physicist,” said the physicist, “because early in the Creation, God made Light; and you know, Maxwell's equations, the dual nature of electromagnetic waves, the relativistic consequences...” “An Engineer!,” said the engineer, “because before making Light, God split the Chaos into Land and Water; it takes a hell of an engineer to handle that big amount of mud, and orderly separation of solids from liquids...” The computer scientist shouted: “And the Chaos, where do you think it was coming from, hmm?”
—Anonymous

Não que eu queira dizer que o QEMU seja um caos, pelo contrário, ele é sem dúvida uma excelente opção quando se precisa lidar com diversos modelos de máquinas diferentes. Sua capacidade de emular tanto o processador como o hardware nos permite criar uma infidade de modelos de máquinas sem um gasto excessívo com novos equipamentos.

O QEMU além de emular maquinas ele também virtualiza sobre o hardware existentes novas instâncias de um sistema operacional,  e quando emulando hardware premite até mesmo aplicativos bare-metal quando por exemplo com microcontroladores e até sobre processadores ARM ou outros.

O Desempenho do QEMU é excelente, e quase equivalente ao desempenho do hardware nativo que faz o papel de host, isso se deve a estratégia de tradução dinâmica das instruções Assembly de uma arquitura (ISA) para outra diretamente.

Porém desenvolver um novo hardware para o QEMU não é tão simples assim além do domínio da arquitetura do processador envolvido, é preciso compreender bem como se programar para o QEMU e criar novos **Targets**, a programação do QEMU é feita em C, e utiliza amplamente o recurso de macros de pré processamento, mas o mais interessante é que temos grandes profissionais dispostos a fazer tal trabalho e até mesmo nos orientar como chegarmos a um nível para que possamos contribuir.

O maior exemplo para um bom trabalho para emulação de hardware é o trabalho desenvolvido pelo Engenheiro Senior de Software Liviu Ionesco, esponsável pela criação do **TArget** que permite rodar emuladores de placas de prototipação da STMicroeletrônics, as placas Discovery tanto para Cortex-M3 como para Cortex-M4.

Tais **targets** emulados ainda não são capazes de ter 100% de funcionalidade, mas hoje já temos as principais instruções ARM para Cortex-M3 e Cortex-M4 sendo interpretadas, e também já temos a caminho novos hardwares funcionais, hoje apenas os LEDS (4 coloridos) funcionam.

Em particular estou comprometido em desenolver a porta serial, emuladores para comunicação via rede, além de pesquissar sobre o uso de Multicores ARM Cortex-M e Cortex-R, além do uso do xTensa para ESP 8266, um longo caminho, que pode levar tempo dependendo da dedicação e envolvimento da comunidade  amigos brasileiros no projeto.

Neste Workshop iremos usar portando o QEMU para descobrirmos como darmos nosso sprimeiros passos e compreender como programar efetivamente e usando recursos profissionasi para Cortex-M3 e Cortex-M4.

O QEMU também poderá ser usado para programar para AVR, estou responsável para agregar o Código de um **TArget** AVR para que possa também ser usado no QEMU com o plugin AVR para Eclipse.

Hoje oque mais tem atrasado para o desenvolvimento com o QEMU é a compilação da biblioteca SDL pois esta tem apresentado problemas em meu ambiente, mas assim que resolver tal problema, integrarei o AVR e posteriormente irei unir esforços com o Liviu Ionesco para produzir novos recursos para o Cortex-M.

## Modos de Operação

O QEMU Possuem dois modos de operação:

 * Emulação total do sistema, onde um sistema completo seja um PC ou um módulo como [RaspeberryPI](/raspberrypi) ou [NanoPI](/nanopi), incluindo todos os seus recursos e periféricos são emulados pode ser usado para uso com um sistema operacional igual ou diferente do hospeiro ou mesmo programação bare-metal seja qual for o processador escolhido.
 * Emulação em modo usuário, neste modo o QEMU executa um processo, um aplicativo por exemplo um editor de texto ou outra aplicação que você possa ter sido compilado em uma CPU na CPU do HOST não importando a diferença, por exemplo ele pode ser usado para rodar o [WINE](http://www.winehq.org) para ARM no Linux que está sobre um INTEL Core I7, para testes, depuração (cross-debug) ou até produção.

## Sistemas oficialmente emulados

### Emulação completa

 * PC (x86 or x86_64 processor)
 * ISA PC (old style PC without PCI bus)
 * PREP (PowerPC processor)
 * G3 Beige PowerMac (PowerPC processor)
 * Mac99 PowerMac (PowerPC processor, in progress)
 * Sun4m/Sun4c/Sun4d (32-bit Sparc processor)
 * Sun4u/Sun4v (64-bit Sparc processor, in progress)
 * Malta board (32-bit and 64-bit MIPS processors)
 * MIPS Magnum (64-bit MIPS processor)
 * ARM Integrator/CP (ARM)
 * ARM Versatile baseboard (ARM)
 * ARM RealView Emulation/Platform baseboard (ARM)
 * Spitz, Akita, Borzoi, Terrier and Tosa PDAs (PXA270 processor)
 * Luminary Micro LM3S811EVB (ARM Cortex-M3)
 * Luminary Micro LM3S6965EVB (ARM Cortex-M3)
 * Freescale MCF5208EVB (ColdFire V2).
 * Arnewsh MCF5206 evaluation board (ColdFire V2).
 * Palm Tungsten|E PDA (OMAP310 processor)
 * N800 and N810 tablets (OMAP2420 processor)
 * MusicPal (MV88W8618 ARM processor)
 * Gumstix "Connex" and "Verdex" motherboards (PXA255/270).
 * Siemens SX1 smartphone (OMAP310 processor)
 * AXIS-Devboard88 (CRISv32 ETRAX-FS).
 * Petalogix Spartan 3aDSP1800 MMU ref design (MicroBlaze).
 * Avnet LX60/LX110/LX200 boards (Xtensa)

### Emulação em modo usuário

Para emulação em modo usuário, as CPUs suportadas são: x86 (32 ou 64bit), Power PC (32 ou 64bit), ARM, MIPS (32 bit somente), Sparc (32 e 64bit), Alpha, ColdFire (m68k), CRISv32 e MicroBlaze.

## Forks do QEMU (Não oficiais)

### ARM Cortex-M

#### Versão Beckus

É um Fork do QEMU 2.1.3 criada por [Andre Beckus](https://github.com/beckus) para adicionar recursos para Cortex-M3 e CortexM1 (para FPGA)

Módulos de prototipação:

 * [Olimex STM32-P103 development board](https://github.com/beckus/qemu_stm32/blob/stm32/hw/arm/stm32_p103.c)
 * [Olimex Olimexino STM32 Maple Development Board](https://github.com/beckus/qemu_stm32/blob/stm32/hw/arm/stm32_maple.c)
 
Códigos de exemplo podem ser obitidos no link [https://github.com/beckus/stm32_p103_demos](https://github.com/beckus/stm32_p103_demos)

Maiores informações visite o link [https://beckus.github.io/qemu_stm32/](https://beckus.github.io/qemu_stm32/)

#### Pebble QEMU

É um Fork do QEMU 2.1.1 para emular o Pebble Smartwatch.

![Pebble Smartwatch](/images/pebble/pebble_classic_smartwatch-black.jpg)

Maiores informações em [https://github.com/pebble/qemu](https://github.com/pebble/qemu) e [https://developer.pebble.com/](https://developer.pebble.com/)

#### GNU ARM Eclipse QEMU

O QEMU para uso com o GNU ARM Eclipse foi desenvolvido pelo Enenheiro de sofware Liviu Ionesco, que iniciou o trabalho em 2003 onde lançou o primeiro release do QEMU para ARM, em seguida em 2006 lançançou a primeira versão do plugin que tem sido melhorado e ampliado em cada novo release.

O QENU para ARM produzido pelo Liviu Ionesco, já tem um módulo de prototipação da STMicroeletrônics que permite a execução de softwares para Cortex-M3 e Cortex-M4, porém os perifericos ainda não estão amplamente desenvolvidos.

Para mais informações entre no site: [http://gnuarmeclipse.github.io/qemu/](http://gnuarmeclipse.github.io/qemu/)

### Quem usa o QEMU como apoio e como usar

#### Mathlab

https://www.mathworks.com/help/supportpkg/armcortexm/ug/build-and-run-executable-on-arm-cortex-m-processors.html?requestedDomain=www.mathworks.com

#### Zephyr 

https://wiki.zephyrproject.org/view/ARM_Cortex-M3_Emulation_(QEMU

#### Linaro

https://www.linaro.org/blog/core-dump/arm-trustzone-qemu/

### Cortex-A

#### QEMU ARM TrustZone

Para testes do ARM TrustZone qu é responsável por segurança de código em processsadores ARM, apesar de desenvolvido para o Cortex-A, está sendo adotado no Cortex-M com arquitetura ARMv8-M.

[![QEMU TrustZone](/images/QEMU/trustzone/qemu-trusted.jpg)](https://www.linaro.org/blog/core-dump/arm-trustzone-qemu/)

Foi produzido pela equipe da Linaro

![Linaro](/images/linaro/linaro-log.png)

https://www.linaro.org/blog/core-dump/testing-qemu-arm-trustzone/

### AVR (ATMega e ATtiny)
