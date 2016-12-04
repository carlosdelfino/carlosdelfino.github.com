---
title: "Formas de Gravar o Arduino!"
excerpt: ""
tags: [Gravar, Boot, Loader, Boot Loader, Arduino, AVR]
category: [HelloWorldArduino, Nivel 3]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
image:
  feature: helloworldarduino/bluetooth/Bluetooth_bb-1800x1113.png
  teaser: helloworldarduino/bluetooth/logo_bluetooth-320x320.jpg
  credit: Carlos Delfino
  creditlink: http://carlosdelfino.eti.br
tagcloud: true
coinbase:
 show: true
--- 

A família ATmega e ATtiny tem diversos modos para gravação de sua 
memória de programa (Flash) e EEPROM.

O Arduino se beneficia de algumas desses modos, uma vez que nem 
todos são viáveis com o MCU montado em um circuito, além de se 
destacar por poder se tornar também um gravador de baixo custo, 
e que pode inclusive ser usado para outros MCUs como o PIC.

Veremos em outros posts como utilizar cada uma das formas possíveis 
com ou sem o Arduino, conforme listado abaixo:

### Métodos de Gravação:

 * HVSP - Neste método é utilizado uma conexão serial por pinos 
   específicos e uma tensão de +12V no pino de Reset.
 * HVPP - Já neste formato o processo de gravação usa 4 pinos de 
   dados, mais alguns de controle que variam entre o ATmega e 
   ATtiny, sendo também aplicado +12V no Reste.
 * ICSP - In-Circuit Serial Programming -  neste modo permite 
   gravar o circuito diretamente mesmo estando montado no circuito, 
   podendo usar tanto a conexão SPI ou USART para comunicação.’

### Alguns Gravadores mais Populares
 * AVR Dragon
 * Linha STK da ATMel
 * USBlast
 * Arduino (Arduino ISP)
 * USBtinyISP
 * DAPA Cable - Direct AVR Parallel Access
 * HV Rescue Shield 2 da Mighty Ohm

A maioria deles é possível usar o AVRDude para efetuar a gravação de seu código
