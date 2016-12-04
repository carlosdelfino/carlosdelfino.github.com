---
layout: article
title: "Lançados novos Microcontroladores para IoT - Parte 2/2"
date: "2016-10-26 09:14:56 -0300"
tags: [ARM, CORTEX-M, ARMV8-M, IoT, Embarcados, Hello World Arduino, TrustZone, Cortex-M0, Cortex-M0+, Cortex-M1, Cortex-M23, Cortex-M33,
Cortex-M3, Cortex-M4, Cortex-M7, AMBA]
categories: [ARM, Cortex-M, IoT]
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

Continuamos neste parte dando mais detalhes sobre os dois novos microcontroladores
da família Cortex-M.

<!--more-->

## O Cortex-M23

O microcontroladores que adotarem o modelo Cortex-M23 serão fabricados para 
atender a demanda de microcontroladores de pequeno tamanho, baixo consumo de 
energia, e alta eficiência em código, sem deixar de lado a segurança provida 
pela tecnologia TrustZone.

<figure>
<img src="/images/arm/Cortex-M23-400x270.png" alt="Cortex-M23"/>
<figcaption>Cortex-M23</figcaption>
</figure>

Nos outros microcontroladores Cortex-M era necessário ter pelo dois núcleos para 
se atingir estados de segurança separados, assim cada processador executava um
perfil de código, o código confiável era executado em um processador e o outro 
executando o código inseguro, tendo assim uma separação fisica e honerosa para 
o microcontrolador.

No Cortex-M23 com o uso do TrustZone há dois estados de segurança, mesmo que 
tenhamos apenas um core no microcontrolador:

 * Estado seguro - que pode pode acessar tanto recursos seguros 
   como não seguros (sejam eles: mémorias, periféricos e etc)
 * Estado Não seguro - que somente acessa recursos nãos seguros

A transição de execução do código e dados nos dois estados é policiado pelo 
hardware minimizando o overhead de troca entre estados e garantindo o determinismo.

Um fato interessante no Cortex-M23 é o fato dele adotar a arquitetura Von-Neumann
com um pipeline de dois estágios, mantendo a compatibilidade com o ISA do 
Cortex-M0+. Aceitando todas as instruções 16 bits já oferecidas no Cortex-M0+,
adicionando algumas instruções 32 bits que trazem ganho de eficência em especial 
em operações condicionais, acesso mutiamente exclusivo e operações de divisão por 
hardware, movimentação imediata. Sendo assim todo conjunto de instruções ARMv6-M, 
usadas no Cortex-M0 e Cortex-M0+ são compátiveis podendo o codígo ser migrado 
diretamente do processador anterior para o novo.

Quem é familiarizado com o Cortex-M0+ como por exemplo quem usa o Arduino Zero 
Pro. Poderá migrar seus códigos diretamente para outro Arduino que venha a usar 
o Cortex-M23 sem perceber diferenças no funcionamento, porém com aumento de 
desempenho. Sendo melhor aproveitado pelos fabricantes do Arduino.

No que tange a depuração e rastreio de dados no microcontrolador foi adotado de 
forma opcional o Embedded Trace Macrocell além do Micro Trace Buffer (MTB) que
é disponível no Cortex-M0+. Estas opções dá ao projetista a escolha de mais 
funcionalidades de rastreamento ou um custo mais efetivo.

O novo modelo de proteção de memória, Memory Protection Unity (MPU) foi baseado
no PMSAv8 que foi adicionado de forma opcional, permitindo proteger até 16 
regiões para cada estado de segurança do processador.

Em sistemas multitarefa, durante a troca de contextos as regiões podem ser 
reprogramadas para cada tarefa.

<figure>
<img src="/images/arm/PMSA-Regionsx420x90.png" alt="Regiões de memória protegida no PMSAv7 e PMSAv8"/>
<figcaption>Regiões de memória protegida no PMSAv7 e PMSAv8</figcaption>
</figure>

A arquitetura de proteção de memória do Cortex-M23 adota um estílo de comparação
de limites para definir a região de memória, em oposição ao estilo anterior com 
tamanho baseado na potência de dois e esquema de alinhamento por tamanho. Esta
nova melhoria simplifica o desenvolvimento de software, e em alguns casos, reduz 
a perda de memória por demandas que não se encaixam perfeitamene no tamanho 
equivalente na potência de 2.

As instruções do Cortex-M23 foram extendida sem que se perdesse sua caracterisca
relativa a baixissimo consumo de energia, ampliando o perfil ARMv6-M e adotando
algumas instruções do ARMv7-M, com exceção das instruções relativas ao TrustZone. 

Instruções para carga e amazenamento de dados de forma exclusiva do ARMv7-M foram
adicionadas pra melhorar a consitência da arquitetura do Cortex-M23 em sistemas
multicore onde semaforos entre processadores pode ser manipulados com o mesmo 
mecanismo. Além disso, foi melhorado o suporte a atomicidade para linguagem
C11/C++11, as instruções load-acquire e store-release são incluidas do ARMv8-A 
(versão Thumb 32), incluindo uma variação de acesso exclusivo para estas instruções.

## Cortex-M33

O Cortex-M33 é uma implementação completa do ARMv8-M, além do TrustZone tem 
também uma extenção para manipulação de sinais digitais, DSP. Este processador
tem diversas possibilidades de configuração, permitindo aos  coprocessadores,
através de usa interface especializada para soluções que demandam grande 
procesamento computacional.

O Cortex-M33 é uma excelente escolha entre Performance, consumo de energia, 
segurança e produtividade para sistemas embarcados relacionados a IoT e SoCs 
complexos.


<figure>
<img src="/images/arm/Cortex-M33-455x328.png" alt="Cortex-M33"/>
<figcaption>Cortex-M33</figcaption>
</figure>
 
O Cortex-M33 tem um pipeline de 3 estágios com o objetivo de manter seu consumo 
de energia baixo, muitas instruções são executadas em apenas dois estágios, já 
outras demandam os 3 estágios para completarem.

O NVIC pode ser configurado para suportar até 480 interrupções externas com até
256 níveis de prioridades.

<figure>
<img src="/images/arm/Cortex-M33-Arquitetura-800x846.png" alt="Arquitetura em Blocos do Cortex-M33"/>
<figcaption>Arquitetura em Blocos do Cortex-M33</figcaption>
</figure>

 * [MPU Memory Protection Unit](/arm/tecnologias/MPU)
 * [DSP Digital Signal processing](/arm/tecnologias/DSP)
 * [FPU Floating Point Unit](/arm/tecnologias/FPU)
 * [SP Single Precision](/arm/tecnologias/SP)
 * [ETM Embedded Trace Macrocell](/arm/tecnologias/ETM)
 * [MTB Micro Trace Buffer](/arm/tecnologias/MTB)
 * [BPU Break Point unit](/arm/tecnologias/BPU)
 * [DWT Data Watch and Trace Unit](/arm/tecnologias/DWT)
 * [ITM Instrumentation Trace Macrocell](/arm/tecnologias/ITM)
 * [NVIC Nested Vectored Interrupt Controller](/arm/tecnologias/NVIC)
 * [WIC Wake-up Interrupt Controller](/arm/tecnologias/WIC)
 * [AHB Advanced High Performance Bus](/arm/tecnologias/AHB)
 * [AMBA Advanced Microcontroller Bus Architecture](/arm/tecnologias/AMBA)
</ul>

Com o TrustZone o Cortex-M33 tem dois estados de segurança, mais dois estados
ortogonais, como podem ser visto na figura abaixo. Abrindo assim um novo horizonte
para novas aplicações e modelos de uso. o Firmware pode ser protegido de diversas 
formas, um supervisor de código pode ser colocado no estado seguro que pode ser 
usado para recuprar o sistema após um ataque ou uma operação não desejada, Enquanto
o lado não seguro é mantido disponível como antes para uso como milhões de outros 
programadores já o fazem nos atuais microcontroladores Cortex-M.

<figure>
<img src="/images/arm/TrustZone-ARMv8-280x460.png" alt="Arquitetura em Blocos do Cortex-M33"/>
<figcaption>Arquitetura em Blocos do Cortex-M33</figcaption>
</figure>

<ul>
 * Secure state
 * Non-secure state
 * Quatro stacks e quatro registradores para ponteiros de stack
 * Hardware stack-limit checking
 * Suporte para MPU programável como a Uidade de Atribuição de segurança (SAU - Security Attribution Unit
 * Interface para sistema de indicação de segurança
 * Visibility of secure code from non-secure (NS) domain restricted to predefined entry points
 * Exception hardware automatically saves and clears secure register state when switching to non-secure
 * Extensive banking of interrupt or exception control, SysTick
 * Memory protection unit for each of the secure and non-secure side

O Cortex-M33 tem uma interface para coprocessador fortemente acoplada com um barramento 
para instruções e outro para dados, o que permite a transferência simultânea para
até 8 coprocessadores.

O MPU no Cortex-M33 funciona como no Cortex-M23, usando também a arquitetura PMSAv8.

Uma extenção especial de 85 instruções pode ser usada com o Cortex-M33 para 
processamento de sinais digitais (DSP). Um conjunto de 16 novos registradores 
de 64bits podem ser também adicioandos para processamento de ponto flutuante 
conforme o padrão IEEE754-2008 e mais 45 instruções para manipulação destes 
pontos flutuantes, baseado no IEEE754-2008, o uso deste coprocessador (FPU) 
aumenta em 10 vezes a velocidade de manipulação de ponto flutante no Cortex-33, 
e é mantido em um domínio de energia separado, para que possa ser desativado 
quando não está sendo usado.


## Fontes

Fontes de referência sobre Cortex-M

 * [http://www.arm.com/products/processors/instruction-set-architectures/armv8-m-architecture.php](http://www.arm.com/products/processors/instruction-set-architectures/armv8-m-architecture.php)
 * [https://community.arm.com/groups/processors/blog/2016/10/25/cortex-m23-and-cortex-m33-security-foundation-for-billions-of-devices](https://community.arm.com/groups/processors/blog/2016/10/25/cortex-m23-and-cortex-m33-security-foundation-for-billions-of-devices)
 * [https://community.arm.com/groups/processors/blog/2016/10/25/five-key-features-of-the-arm-cortex-m23-processor](https://community.arm.com/groups/processors/blog/2016/10/25/five-key-features-of-the-arm-cortex-m23-processor)
 * [https://developer.arm.com/products/processors/cortex-m/introduction-to-arm-cortex-m23-and-cortex-m33](https://developer.arm.com/products/processors/cortex-m/introduction-to-arm-cortex-m23-and-cortex-m33)
 
Para quem deseja avançar no uso do Cortex-M 23 e cortex-M vai uma lista de links interessantes:

 * [ARMv8-M Architecture Reference Manual - beta](http://infocenter.arm.com/help/topic/com.arm.doc.ddi0553a.b/index.html)
 * [ARMv8-M architecture: what’s new for developers - YouTube](https://www.youtube.com/embed/V5zr5mPjAvU?rel=0&autoplay=1)
 * [ARM Compiler Software Development Guide : Chapter 8 Building Secure and Non-secure Images Using ARMv8-M Security Extensi…](http://infocenter.arm.com/help/topic/com.arm.doc.dui0773e/pge1446115999905.html)
 * [ARMv8-M Security Extensions: Requirements on Development Tools - ARM Information Center](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ecm0359818/index.html)
 * [The Next Steps in the Evolution of Embedded Processors for the Smart Connected Era](https://community.arm.com/docs/DOC-11532)
 * [Enhanced Security and Energy Efficiency of Microcontrollers and SoCs](https://community.arm.com/docs/DOC-11533)
 * [ARMv8-M document on developer.arm.com](https://developer.arm.com/products/architecture/m-profile/docs)

