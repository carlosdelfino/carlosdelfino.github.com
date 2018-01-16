---
title: Desenvolvimento Automotivo - AUTOSAR - MCAL
layout: article
categories: [hellowordarm, nivel_2, automotive, AUTOSAR]
tags: [arm, autosar, mcal, mcu, abstraction, layer, microcontroller, microcontrolador, abstração, camada, ecu]
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
  feature: arm/autosar/autosar-mcal-software-300x144.png
  teaser: arm/autosar/autosar-mcal-software.png
  credit: EMBITEL
  creditlink: https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture
---

Este ano voltarei dando um maior foco nos estudos e compartilhamento de informações sobre o universo ligado a arquitetura ARM, neste primeiro artigo veremos um novo conceito muito importante para dar os primeiros passos  no campo ligado ao desenvolvimento Automotivo.

<!--more-->

Para iniciarmos nossos estudos sobre Microcontroladores e Framewors para uso Automotivo, precisamos aprender sobre a arquitetura dos atuais sistemas de software automotivos e para isso precisamos aprender primeiro o conceito indicado pela sigla MCAL que significa __*M*icro *C*ontroler *A*bstraction *L*ayer__ ou __*MC*U *A*bstration *L*ayer__, esta sigla faz parte do que será nosso campo de estudo e é definido por __*AUT*omotive *O*pen *S*ystem*AR*__ chitecture (AUTOSAR)_ que veremos no próximo post.

O *MCAL* pode ser definido como uma camada do Software Básico do AUTOSAR, uma camada que tem acesso a todos os dispositivos sejam internos ou externos ao microcontrolador que normalmente são mapeados para endereços de memória como é no caso do ARM e outros MCUs.

O MCAL como seu nome diz abstrai toda a arquitetura do microcontrolador e o método de acesso aos dispositivos de forma que as camadas de softwares mais altas não se preocupem com a arquitetura e detalhes do microcontrolador. As camadas superiores são normalmente as camada de ECU e a camada de serviços.

O MCAL é parte fundamental do AUTOSAR, é este módulo que habilita esta arquitetura de software ter as camadas básicas de software (BSW) a Camada de Aplicação (Application Layer) totalmente independentes da arquitetura do MCU e da plataforma de Hardware como um todo, e claro com o auxilio da Camada ECU que abstrai totalmente os detalhes de operação da MCAL.

Assim traz grande benefícios ao desenvolvimento de produtos reduzindo custo e tempo, além de uma elevação na abordagem de projeto do ECU (Electronic Control Unit) de codificação para configuração.

### Controladores de Dispositivos do módulo AUTOSAR MCAL

Abaixo apresento a lista obtida no site www.embitel.com dos diferentes Device Drivers (controladores de dispositivos/recursos) disponibilizado pelo AUTOSAR MCAL.

Veja na imagem a seguir a relação do MCAL e seus módulos com os dispositivos existentes no MCU, a imagem foi obtida no site da [Embitel](www.embitel.com).

![Autosar MCAL Software](/images/arm/autosar/autosar-mcal-software.png)

Como podem ver cada periférico interno do MCU possui um módulo de software responsável por seu gerenciamento, incluindo sua configuração e gestão dos processos de entrada e saída.

#### Microcontroller Drivers:

Os Drives de Microcontrolador são responsáveis por fornecer uma API para acessar recursos como Timers, Watchdog e a própria MCU de abstrata, veja abaixo 3 deles:

 * GPT Driver: GPT (General Purpose Timer) é um driver de dispositivo que o Timer interno do MCU, ele inicializa o GPT e executa a contagem do tempo.
 
  * WDG Driver: WDG (Watchdog) é o Driver que inicializa o Watchdog e preparada e seleciona os modos de uso.
 
  * MCU Driver: o Driver da MCU (Micro Controller Unit) ele ajuda a configurar o MCU, inicializar o Clock e ajuda a configurar os modos de uso de Energia.
  
Ao dar inicio a esta analise, que já conhece o universo ARM pode estar se perguntando como eu, qual a diferença do AUTOSAR para o CMSIS, e com o desenrolar deste estudo se tornaram mais clara as diferenças e dependências.
 
#### Memory Drivers

 * FLS Driver: Driver FLS (Flash), este Driver inicializa a memória flash e gerecia a Leitura/Escrita para ela.
 
#### Communication Drivers

Os módulos responsáveis pela comunicação são capazes de lidar com o dispositivo físico e seus protocolos de comunicação.

 * SPI Handler/Driver, Driver ou Handler é responsável pela inicialização do clock e das funções seriais relacionadas, além de gerenciar as configurações dos Buffers de entrada e saída relativos.
 
 * [LIN Driver](/autosar/mcal/lin) (Local Interconnected network) é responsável por por inicializar o recursos relativos ao LIN e gerir os processos de Entrada e Saída.

 * [CAN Driver](/autosar/mcal/can) (Controller Area Network) como o LIN é responsável pelos processos de configuração e entrada e saída dos periféricos internos do MCU relativos ao CAN e seu protocolo.
 
 * [FlexRay Driver](/autosar/mcal/flexray) é um controlador de dispositivo que inicializa o FlexRay e gerencia todo o o processo de entrada e saída.

 * Ethernet Driver, é um controlador do dispositivo Ethernet que inicializa e gerencia todo o processo de entrada e saida Ethernet.
 
#### I/O Drivers

 * ICU Driver (Input Capture Unit) é um controlador de dispositivo que usando o Timer interno do MCU mede formas de onda PWM, e também é responsável por todo o processo de inicialização do ICU.
 
 * PWM Driver (Pulse Width Modulation) é um controlador de dispositivo que usando o Timer Interno do MCU gera formas de onda PWM e gerencia toda sua configuração.
 
 * ADC Driver (Analog Digital Converter) é um controlador de dispositivo para ADC interno ao MCU, responsável pela inicialização do ADC, parada e inicio da conversão AD, configuração dos buffers de conversão e leitura dos resultados AD.
 
 * DIO Driver (Digital Input/Output) é um controlador de dispositivo que controla a sinalização das portas de entrada e saída digital.
 
 * PORT Driver é o controlador que gerencia as portas do MCU configurando como entrada e saida e o gerenciamento das configurações e compartilhamento das funções das portas do MCU, lembrando que uma porta é ocmposta por conjuntos de pinos cada pino pode assumir uma função conforme sua configuração e anexação a um dispositivo interno como porta serial, spi, i2c, pwm, adc e etc..
 
## Conclusão

Vimos neste post a camada de software que contém controladores que adaptam e ajudam a abstrair o hardware do MCU para as camadas mais elevadas, este conjunto de softwares controladores são módulos responsáveis por cada tipo de periféricos. 

Esta camada atende a demanda da camada de abstração do ECU que é a camada responsável pela real abstração de cada dispositivo,  e assim atendem a necessidade da camada de serviços, veremos detalhes sobre esta camada no próximo post, estas camadas compõem a BSW, que possuem além destas camadas o módulo de drivers complexos.

Veja podemos perceber a BWS em camadas ou em uma matrix camada funcionalidade, já que em cada camada há um módulo de software especializado que se compõem com o módulo da camada inferior, sendo assim na camda de serviços temos um módulo que se comunica com outro módulo da camada de abstração ECU que por sua vez se conecta a camada de controladores de dispositivos (MCAL) que finalmente transmite ou recebo do MCU.




## Fontes

* https://electronicsforu.com/technology-trends/tech-focus/microcontrollers-getting-better-better?utm_source=pushengage&utm_medium=push_notification&utm_campaign=pushengage

* https://www.embitel.com/blog/embedded-blog/what-is-autosar-mcal-software-architecture

* https://vector.com/vi_preevision-electric-electronic-architecture_en.html?gclid=Cj0KCQiAv_HSBRCkARIsAGaSsrCNTc3YCz2klh4jjvEuoYrwhVOUP6LdJZhD0LE9JvD9hJwFq4vi7qYaAhGtEALw_wcB

* https://www.autosar.org

* https://www.engineersgarage.com/articles/autosar-automotive-open-systems-architecture