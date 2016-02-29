---
layout: article
title: RC Switch ou VirtualWire qual devo usar?
tags: [Arduino, Uno, Virtual Wire, RC Switch, Automação, Residencial, Domôtica, Sensores, Adaptacao, RC, Controle Remoto, drones, vants, carrinhos, automático, IoT, Internet das Coisas, Internet of Thinks, RF22, RF24, NRF24, NRF905, RF95, ASK, Serial, manchers, biphase, TCP, Mesh, Datagrama]
categories: [HelloWorldArduino, Nivel 2]
excerpt: Qual biblioteca usar? muitos dizem que a RC Switch é a melhor, outros dizem que é a Virtual Wire, porém poucos justificam sua escolha com parametros reais, o que você me diz de sua escolha? use o campo comentários abaixo para apresentar seu argumento.
comments: true
share: true
toc: true
ads:
 show: true
feature:
 index: true
 category: true
tagcloud: true
coinbase:
  show: true
---

## A Biblioteca RC Switch

Esta biblioteca foi criada com um proposito bastante especifico, que é interagir
com dispositivos de automação residencial que controlam lampadas e outros eltrodomesticos.

A RC Switch pode vir a fazer as mesmas tarefas que a Virtual Wire, porém foi criada
com este proposito especifico, possuem em seu código o algoritmo para controlar lamapdas
e interruptores dotados deste recurso. Veja no sub título abaixo sugestões de modelos de
interruptores e tomadas controladas com 433Mhz.

## A Biblioteca Virtual Wire

A Biblioca Virtual Wire foi criada para se criar o conceito de modem, ou seja um
sistema de comunicação bidirecional ou não entre dois pontos, simulando a presença
de uma interconexão física, proém através de rádio.

Pode parecer uma desvantagem a biblioteca Virtual Wire não vir com o algoritimo 
para comunicação com RC Switch como propõe a outra biblitoeca, porém sua simplicidade
a torna eficiente quando a comunicação será feita entre dois pontos controlados por 
Arduino, e também para construção de pequenas redes IoT.

A Biblioteca Virtual Wire também foi substituida pela biblioteca [Radio Head](http://www.airspayce.com/mikem/arduino/RadioHead/)
que é dotada novos algoritmos como construção de redes Mesh que é muito mais útil
para uso com IoT.

Além disso a Biblioteca Radio Head vem amparada com dezenas de protocolos muito 
úteis para uso com IoT.

## Equipamentos compátiveis com 433Mhz e a Biblioteca RC Switch

 * [Proteam HO1853 - Set Remote Sockets](http://www.amazon.co.uk/Proteam-HO1853-Set-Remote-Sockets/dp/B0029Z9YUQ)
 * [Rolson Tools 60027 2pc Remote Controlled Socket](http://www.amazon.co.uk/Rolson-60027-Remote-Controlled-Socket/dp/B001B4RE4O)
 * [Wireless AU Plug-in Socket w/ Remote Controller / 220V 10A - White](http://www.dx.com/p/wireless-au-plug-in-socket-w-remote-controller-220v-10a-white-347807#.VFkt9VOS1xU)
 * [1000W Dual Remote Control Electrical Switches (AC 125V / 2-Flat-1-Round-Pin Plug)](http://www.dx.com/p/1000w-dual-remote-control-electrical-switches-ac-220v-eu-plug-126226#.VFkt8FOS1xU)
 * [DIY SQ-084 AC 200~245V 4-Channel Digital Remote Control Switch w/ Wiring Diagrams](http://www.dx.com/p/diy-sq-084-ac-200-245v-4-channel-digital-remote-control-switch-w-wiring-diagrams-309443#.VFkuG1OS1xU)

## Projetos que usam a biblioteca RC-Switch

Os projetos abaixo são projetos que usam a biblioteca RC-Switch de alguma forma

 * [funkcontrol-over-net](https://code.google.com/p/funkcontrol-over-net/)
   webserver e webinterface totalmente plug-and-play para controlar lampadas e 
   outros eletrodomésticos, pode ser usado com o Arduino e Shield Ethernet. 
 * [homecontrol4.me](http://www.homecontrol4.me/)
   Automatize sua casa, usando seu Smartphone.
 * [OpenplacOS](http://openplacos.github.io/openplacos/)
   OpenplacOS é um projeto de código aberto criado para ser aplicado em automação
   residencial, Aquariofilia residencial e de Jardins, roda sobre Linux.
 * [OpenPyro](http://blog.openpyro.com/)
   O Sistema OpenPyro 
 * [APDuino](http://apduino.com/)
   Permite conectar objetos inteligentes.
   
