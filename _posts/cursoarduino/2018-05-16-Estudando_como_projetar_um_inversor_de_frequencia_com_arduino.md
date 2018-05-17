---
title: Estudando como projetar um inversor de frequência com Arduino
tags: [arduino, projeto, inversor de frequencia, rpm, ibjt, fet, mosfet, scr, triac, diodos, pwm, spwm, rotor, estator, bobinas, brushes, escovas, carvao]
categories: [cursoarduino, potencia]
layout: article
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
   teaser: basicaodaeletronica/motores/motor-eletrico-estator-rotor-partes.jpg
   feature: basicaodaeletronica/motores/squirrel-motor.jpg
math: true
---

Estou fazendo um estudo com o objetivo de construir um modelo didático de inversor de frequência para uso monofásico, bifásico e trifásico, de forma que possa ser adaptado para uso em pequenos motores de baixa potência.

<!--more-->

Bem para começarmos é importanter entendermos como funciona um motor comum projetado para ser alimentado com corrente AC. No momento deste estudo não irei entrar em muitos detalhes sobreo funcionamento do motor, [para mais detalhes clique aqui e verá um artigo muito bom sobre como funciona motores AC em detalhes](https://www.citisystems.com.br/motor-eletrico/), é importante apenas sabermos que o motor é composto com a imagem abaixo apresenta, por um *Rotor* que possui um conjunto de bonbinas que são interligadas conforme o tipo de alimentação, estas bobinas são ligadas por um conjunto de escovas (Brushes) que conforme o *Rotor* gira interfere no campo magnético das bobinas, este campo magnético também recebe influência contrária de outro campo magnético gerado por um conjunto de bonbinas que fica dispostas no *estator*

![Partes de um motor AC, obtido no site https://www.citisystems.com.br/motor-eletrico/](/images/basicaodaeletronica/motores/motor-eletrico-estator-rotor-partes.jpg)

Também é importante entender como a velocidade do motor AC é definda, no motor de corrente continua sua velocidade máxima é definida na fabricação para uma determinada tensão ideal, ou seja, se ele é projetoado para ter uma rotação de 1000rpm a 12 volts, quando for alimentado nesta tensão terá 100% da velocidade, mas se for alimentado com 6V terá em torno de 50% da velocidade. Mas o motor de corrente alternada (AC) sua velocidade é controlada pela frequência da alternancia da corrente, assim um motor de 3600rpm a 60hz terá sua velocidade máxima quando alimentado na tensão no qual foi prejetado para funcionar mais a frequência de alternancia da corrente em 60Hz, reduzindo assim a frequência se terá uma velocidade menor, e aumentando a frequência teremos até certo limite uma velocidade maior. Porém se aumentarmos a tensão poderemos ter um rompimento da camada de isolação do motor.

Eu ainda não pesquisei sobre o impacto do inversor de frequência em motores AC que precisam de capacitores para partida, mas conforme o andar deste projeto irei fazer testes com diversos tipos de motores. Sugestões de *_leitura_* são bem vindas.

Como podem ver a cada visita neste artigo estarei trazendo novos restualdos dos estudos, complementando ou corrigindo alguma informação aqui fornecida, seja por novas descobertas ou por sugestões dos leitores.

Nos meus estudos estarei usando os motores AC do tipo Squirrel, este motores tem os rotores compostos por bobinas de cobre ou aluminio curtocircuitadas, assim não precisam de buchas para reversão dos contatos tendo uma maior durabilidade. Abaixo a imagem obtida no site www.citisystems.com.br mostra como é o rotor deste tipo de motor.

![Rotor do motor AC do tipo Squirrel, obtido no site https://www.nrcan.gc.ca/energy/products/reference/15433](/images/basicaodaeletronica/motores/squirrel-motor.jpg)


## PWM

Até este estudo, eu apenas conhecia um tipo de PWM e mesmo nesta nova categoria o chamava apenas de PWM, porém o PWM podem ser classificados como PWM comum e SPWM.

O SPWM é quando o PWM tem o comportamento com o intuito de induzir no circuito uma onda senoite, e é o que será usado para simular ondas senoites com nosso inversor. Veremos mais detalhes a frente.

A geração do PWM se faz necessário porque no inversor de frequência, não importa a fonte de alimentação, trabalha sobre a tensão continua, e com ela gera de forma sincronizada os pulsos no formato SPWM para excitar o motor, seja ele mono, bi ou trifásico.

Na imagem abaixo é mostrado o circuito padrão de um inversor de frequência típico para uso trifásico que pode ser adaptado para circuitos bi e monofásico. Observe que o circuito retifica o sinal transformando a corrente em continua, filtra e finalmente o driver final que com base no SPWM simula a onda senoidal na frequêncial desejada desejada.

![Circuito retificador, filtro e Driver IBJT do motor, obtido no site https://www.nrcan.gc.ca/energy/products/reference/15433](/images/basicaodaeletronica/motores/ponte-retificadora-vfd.jpg)

## VFD

VFD é o tipo de dispositivo que iremos estudar e criar aqui neste estudo usando o Arduino, o significado do acronimo é *Variable Frequênce Drivers* ou seja *Controlador por Variação de Frequência*.

O VFD que iremos estudar é baseado em IBJT, particularmente nunca usei este componente em meus projetos, mas irei apresentar mais informações a parte para explicar seu funcionamento e mostrar como pode ser simulado com outros componentes.

Controladores anteriormente usavam SCRs e Thyristores, estes são *Inversores de Corrente* ou *Controladores por Variação de Voltagem*, por exemplo Dimmer normalmente apresentado para uso com o Arduino é um controlador por variação de tensão, já que com base na variação da tensão ele corta a onda conforme a tensão que se deseja simular.

Tentarei neste estudos coletar as informações para criar um inversor de frequência versátil que usando o arduino e um processo de parametrização (futuramente pode ser automático) se adaptará conforme o tipo de motor, independente da forma que é alimentado.

## Formas de alimentação do motor

Como já falamos o motor pode ser alimentado de três formas distintas mesmo em Corrente Alternada (AC), muitos só devem ter ouvido falar em 110V ou 220V, vejamos as 3 formas que iremos lidar neste projeto, o texto foi adaptado de https://www.citisystems.com.br/motor-eletrico/:

* Distribuição monofásica envolve uma distribuição de tensão senoidal (alternada) em 110V ou 220V (como em regiões praianas) sendo utilizado em residências pequenas.

* Distribuição bifásica envolve uma distribuição em 2 padrões de tensão senoidal em 110V cada, defasados entre si em 120° sendo muito utilizado para energia comercial e residencial.

* A Distribuição trifásica contém três padrões de tensão alternados simultâneos senoidal, tipicamente defasados em 120° um com o outro. Com operação trifásica é possível alcançar maior eficiência de energia e suavidade na operação sendo que a energia trifásica é mais tipicamente aplicada motores elétricos industriais ou de alta potência.

## Velocidades típicas dos motores

A velocidade do motor é medida em RPM, Rotações por Minuto, os motores do tipo Inducção e Síncronos tem a velocidade controlada por inversores de frequência ou atráves de redutores de velocidade mecânicos, sendo muitos deles especificados sobre uma certa carga, portanto caso a carga seja menor, ele poderá rodar em uma velocidade superior.

O Inversor de Frequência pode ser capaz de monitorar a carga sobre o motor através da corrente esperada na velocidade desejada.

Uma informação itneressante para entender o funcionamento dos motores é apresentada pela fómula abaixo, o motor AC tem sua velocidade definida pelo número de espiras em seu estator.

$$
Velocidade Sincrona = \frac{120 * Frequência em Hz}{Número de polos}
$$

* 2 Polos -> 3600 rpm
* 4 Polos -> 1800 rpm
* 6 Polos -> 1200 rpm
* 8 polos ->  900 rpm

## IBJT




## Fontes

* [https://pt.wikipedia.org/wiki/Motor_elétrico](https://pt.wikipedia.org/wiki/Motor_elétrico)
* [https://www.citisystems.com.br/motor-eletrico/](https://www.citisystems.com.br/motor-eletrico/)
* [https://www.nrcan.gc.ca/energy/products/reference/15433](https://www.nrcan.gc.ca/energy/products/reference/15433)