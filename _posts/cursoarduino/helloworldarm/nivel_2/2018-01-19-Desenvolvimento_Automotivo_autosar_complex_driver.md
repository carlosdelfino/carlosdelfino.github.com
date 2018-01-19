---
title: Desenvolvimento Automotivo - AUTOSAR - Complex Driver
layout: article
categories: [helloword,arm, nivel_2, automotive, autosar]
tags: [arm, autosar, mcal, mcu, abstraction, layer, microcontroller, microcontrolador, abstração, camada, serviços, service, complex, complex driver, driver]
comments: true
share: true
ads:
 show: true
toc: true
feature:
 index: true
 category: true
tagcloud: true
image:
  feature: arm/autosar/ecu_centralina-360x210.jpg
  teaser: arm/autosar/ecu_centralina.jpg
  credit: EMBITEL
  creditlink: https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture
---

O módulo "Complex Driver" tenta resolver problemas que não podem ser atingidos por uma abstração mais generica, além de facilitar a migração.

<!--more-->

Vimos que no BSW (Basic SoftWare), temos diversas camadas compostas por diversos módulos, apresentados sua relação no digrama de blocos abaixo.

![Arquitetura em módulos e camadas do AUTOSAR](/images/arm/autosar/arquitetura_detalhes_autosar.jpg)

O Módulo "Complex Driver" é um módulo quen ão pertende a nenhuma das camadas do BSW por tratar questõess que estas camadas não consegue lidar, como drivers/handlers que não foram migrados ainda, ou denível de complexidade que não permite sua implementação a nível tão abstrato.

ESte módulo deve de qualquer forma seguir orientações de interface definidos pelo AUTOSAR.

Uma característica importante a ser implementada no módulo "Complex Driver" são característica relativas a RTOS que exigem um tempo de resposta predeterminada, observando parametros deterministicos de execução.

São inclusos por exemplo serviços de injeção eletrônica, ou ECUs  que demandam drivers que ainda não foram implementados de forma abstrata como exigido o AUTOSAR.

## Fontes

* <http://www.ebay.com/gds/What-Is-an-ECU-/10000000177635225/g.html>

* <https://electronicsforu.com/technology-trends/tech-focus/microcontrollers-getting-better-better?utm_source=pushengage&utm_medium=push_notification&utm_campaign=pushengage>

* <https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture>

* <https://vector.com/vi_preevision-electric-electronic-architecture_en.html?gclid=Cj0KCQiAv_HSBRCkARIsAGaSsrCNTc3YCz2klh4jjvEuoYrwhVOUP6LdJZhD0LE9JvD9hJwFq4vi7qYaAhGtEALw_wcB>

* <https://www.autosar.org>

* <https://www.engineersgarage.com/articles/autosar-automotive-open-systems-architecture>