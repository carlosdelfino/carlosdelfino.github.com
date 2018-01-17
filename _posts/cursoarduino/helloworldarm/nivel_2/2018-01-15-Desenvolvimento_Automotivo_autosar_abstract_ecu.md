---
title: Desenvolvimento Automotivo - AUTOSAR - Abstract ECU
layout: article
categories: [hellowordarm, nivel_2, automotive, AUTOSAR]
tags: [arm, autosar, mcal, mcu, abstraction, layer, microcontroller, microcontrolador, abstração, camada, serviços, service, ecu]
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

Vamos ver agora a camada de abstração da Unidade de Controle Eletrônico (ECU Abstraction Layer), esta camada é responsável por abstrair detalhes de uso dos dispositivos presentes no MCU e é uma camada intimamente ligada ao nicho automotivo.

<!--more-->

Para relembrar a arquitetura de software do AUTOSAR, veja a imagem abaixo, obtida na documentação da [AUTOSAR](http://www.autosar.com), que demonstra em um diagrama de blocos a relação das camadas e módulos de forma bem simplificada.

![Arquitetura em módulos e camadas do AUTOSAR](/images/arm/autosar/arquitetura_detalhes_autosar.jpg)

A ECU é composta por uma grande variedade de outras unidades de controle, normalmente especializadas em cada recurso do automóvel, desde o controle de velocidade, freios, bancos, portas e vidros, luminosidade externa e interna, entre diversos outros, no Brasil conhecida como Centralina Eletrônica. É aquele equipamento que vem nos carros de ultima geração e permite gerenciar o veículo desde sua potência até outros recursos já citados. 

A ECU ou Centralina, iremos chamar sempre de ECU é o nome técnico correto do equipamento, ele se tornou muito conhecido do publico quando se começou a vender equipamentos que se conectam pelo OBD2 ao computador ou microcontroladores comum permitindo interversões interessantes.

Na foto abaixo é apresentado uma ECU, imagem obtida no site https://www.prettymotors.com/ecu-reloaded/

![ECU ou Centralina](/images/arm/autosar/ecu_centralina.jpg)

A Camada de Abstração da ECU no AUTOSAR permite que a camada de serviço se torne independente do hardware que se encontra abaixo dela, não se limita ao microcontrolador, todo o hardware é abstraído seja interno ao MCU ou externo, portando abstraindo praticamente toda a ECU.

Quando não for possível a total abstração, a comunicação pode se dar via o canal oferecido pelos drivers de dispositivos complexos, não sendo usado nenhuma das camadas sendo usado o módulo de drivers complex, que veremos no próximo post.

## Fontes

* <http://www.ebay.com/gds/What-Is-an-ECU-/10000000177635225/g.html>

* <https://electronicsforu.com/technology-trends/tech-focus/microcontrollers-getting-better-better?utm_source=pushengage&utm_medium=push_notification&utm_campaign=pushengage>

* <https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture>

* <https://vector.com/vi_preevision-electric-electronic-architecture_en.html?gclid=Cj0KCQiAv_HSBRCkARIsAGaSsrCNTc3YCz2klh4jjvEuoYrwhVOUP6LdJZhD0LE9JvD9hJwFq4vi7qYaAhGtEALw_wcB>

* <https://www.autosar.org>

* <https://www.engineersgarage.com/articles/autosar-automotive-open-systems-architecture>