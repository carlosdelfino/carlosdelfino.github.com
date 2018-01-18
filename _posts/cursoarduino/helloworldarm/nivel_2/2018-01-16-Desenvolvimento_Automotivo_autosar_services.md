---
title: Desenvolvimento Automotivo - AUTOSAR - Service
layout: article
categories: [helloword,arm, nivel_2, automotive, autosar]
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
  feature: arm/autosar/arquitetura_detalhes_autosar-350-177.jpg
  teaser: arm/autosar/arquitetura_detalhes_autosar.jpg
  credit: EMBITEL
  creditlink: https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture
---

Foi apresentado no post anterior a Camada responsável por ajudar na abstração do microcontrolador e seus dispositivos internos ou externos para as camadas mais altas. E agora veremos a camada de Serviços que fica no ponto oposto a MCAL.

<!--more-->

A imagem abaixo demonstra bem o que é a MCAL, simplificando tudo que apresentamos sobre ela no post anterior. A imagem foi obtida no site da [Embitel](www.embitel.com).

![Autosar MCAL Software](/images/arm/autosar/autosar-mcal-software.png)

A seguir vamos visualizar uma imagem que apresenta uma representação mais completa do AUTOSAR e assim percebemos onde cada camada e módulo está e como se relacionam. A imagem foi obtido na documentação da AUTOSAR disponível na internet.

![Arquitetura em módulos e camadas do AUTOSAR](/images/arm/autosar/arquitetura_detalhes_autosar.jpg)

E como dito iremos estudar neste post a camada de serviços, esta camada juntamente com acamada de abstração do ECU e a MCAL além do módulo que fornece Drivers Complexos (Complex Drivers), formam os serviços básicos do AUTOSAR chamado de BSW (Basic Software), como é visto no diagrama de blocos acima, a camada de serviços tem praticamente os memos módulos que a MCAL, é a camada mais elevada estando oposta a camada MCAL e tendo como auxiliar na abstração dos recursos a camada de abstração do ECU que veremos no próximo post.

A camada de serviços atende boa parte das solicitações vindas externamente do BSW (Basic Software), sendo auxiliada pelo módulo Complex Driver e no caso das portas de I/O gerais, são acessadas diretamente na camada MCAL.

Os serviços relacionados a MCU são auxiliados com a camada ECU que solicita a camada MCAL, porém a camada de serviços tem acesso direto a MCU em alguns casos.

A título de qualificação listo as funcionalidades oferecidas pela camada de serviços:

* Funcionalidades de Sistema Operacional;
* Serviços de gerenciamento e comunicação da rede do Veiculo (Vehicle Network);
* Serviços de memória, gerenciamento da NVRAM;
* Serviços de diagnósticos (incluindo comunicação UDS, tratamento de faltas e erros de memória);
* Gerenciamento do estado da ECU, Gerenciamento de modo;
* Monitoramento do fluxo temporal e lógico do programa (gerenciamento Wdg);
 
A Camada de serviços atende basicamente as aplicações, ao ambiente de execução (RTE) e módulos básicos, tornado a aplicação independente do hardware do microcontrolador e da ECU.

## Fontes

* https://electronicsforu.com/technology-trends/tech-focus/microcontrollers-getting-better-better?utm_source=pushengage&utm_medium=push_notification&utm_campaign=pushengage

* https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture

* https://vector.com/vi_preevision-electric-electronic-architecture_en.html?gclid=Cj0KCQiAv_HSBRCkARIsAGaSsrCNTc3YCz2klh4jjvEuoYrwhVOUP6LdJZhD0LE9JvD9hJwFq4vi7qYaAhGtEALw_wcB

* https://www.autosar.org

* https://www.engineersgarage.com/articles/autosar-automotive-open-systems-architecture