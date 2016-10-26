---
layout: post
title: "Lançados novos Microcontroladores para IoT - Parte 2/2"
date: "2016-10-26 09:14:56 -0300"
tags: [ARM, CORTEX-M, ARMV8-M, IoT, Embarcados, Hello World Arduino, TrustZone, Cortex-M0, CortexM0+, Cortex-M1, Cortex-M23, Cortex-M33,
Cortex-M3, Cortex-M4 e Cortex-M7]
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

Continuaremos aqui vendo em mais detalhes os dois novos microcontroladores da família
Cortex-M.

<!--more-->

## O Cortex-M23

O microcontroladores que foram Cortex-M23 serão fabricados para atender a demanda
de microcontroladores de pequeno tamanho, baixo consumo de energia, e alta eficiência
em código, sem deixar de lado a segurança provida pela tecnologia TrustZone.

<figure>
<img src="/images/arm/Cortex-M23-400x270.png" alt="Cortex-M23"/>
<figcaption>Cortex-M23</figcaption>
</figure>

Nos outros microcontroladores Cortex-M era necessário ter pelo dois núcleos para 
se atingir estados de segurança separados, separando assim cada processador um 
executando o código confiável, e o outro executando o código inseguro, tendo assim
uma separação fisica e honerosa para o microcontrolador.

No Cortex-M23 com o uso do TrustZone há dois estados de segurança:

 * Estado seguro - que pode ser acessado que pode acessar tanto recursos seguros 
   como não seguros (mémorias, periféricos e etc)
 * Estado Não seguro - que somente acessa recursos nãos seguros

A trasição de execução do código e dados nos dois estados é policiado pelo hardware
minimizando o overhead de troca entre estados e garantindo o determinismo.]

Um fato interessante no Cortex-M23 é o fato dele adotar a arquitetura Von-Neumann
com um pipeline de dois estágios, mantendo a compátibilidade com o ISA do Cortex-M0+,
aceitando todas as instruções 16 bits por ele usadas. Adicionando algumas instruções
32 bits que trazem ganho de eficência em especial em operações condicionais, acesso 
muamente exclusivo e operações de divisão por hardware, movimentação imediata. Sendo
assim todo conjunto de instruções ARMv6-M, usadas no Cortex-M0 e Cortex-M0+ são 
compátiveis podendo o codígo ser migrado diretamente de um processador para o outro.

Quem é familiarizado com o Cortex-M0+ como or exemplo quem usa o Arduino Zero Pro.
Poderá migrar seus códigos diretamente para outro ARduino que use o Cortex-M23 sem
perceber diferenças no funcionamento. Mais ainda para os fabricantes do Arduino.

No que tange a depuração e rastreio de dados no microcontrolador foi adotado de 
forma opcional o Embedded Trace Macrocell além do Micro Trace Buffer (MTB) que
é disponível no Cortex-M0+. Estas opções dá ao projetista a escolha de mais 
funcionalidades de rastreamento ou um custo mais efetivo.

O novo modelo de proteção de memória, Memory Protection Unity (MPU) foi baseado
no PMSAv8 que foi adicionado de forma opcional, permitindo proteger até 16 regiões
para cada estado de segurança do processador.

Em sistemas multitarefa, durante a troca de tarefas as regiões podem ser reprogramadas
para cada tarefa.

<figure>
<img src="/images/arm/PMSA-Regionsx420x90.png" alt="Regiões de memória protegida no PMSAv7 e PMSAv8"/>
<figcaption>Regiões de memória protegida no PMSAv7 e PMSAv8</figcaption>
</figure>


## Cortex-M33

<figure>
<img src="/images/arm/Cortex-M33-455x328.png" alt="Cortex-M33"/>
<figcaption>Cortex-M33</figcaption>
</figure>
 
## Fontes

Fontes de referência sobre Cortex-M

 * [http://www.arm.com/products/processors/instruction-set-architectures/armv8-m-architecture.php](http://www.arm.com/products/processors/instruction-set-architectures/armv8-m-architecture.php)
 * [https://community.arm.com/groups/processors/blog/2016/10/25/cortex-m23-and-cortex-m33-security-foundation-for-billions-of-devices](https://community.arm.com/groups/processors/blog/2016/10/25/cortex-m23-and-cortex-m33-security-foundation-for-billions-of-devices)

Para quem deseja avançar no uso do Cortex-M 23 e cortex-M vai uma lista de links interessantes:

 * [ARMv8-M Architecture Reference Manual - beta](http://infocenter.arm.com/help/topic/com.arm.doc.ddi0553a.b/index.html)
 * [ARMv8-M architecture: what’s new for developers - YouTube](https://www.youtube.com/embed/V5zr5mPjAvU?rel=0&autoplay=1)
 * [ARM Compiler Software Development Guide : Chapter 8 Building Secure and Non-secure Images Using ARMv8-M Security Extensi…](http://infocenter.arm.com/help/topic/com.arm.doc.dui0773e/pge1446115999905.html)
 * [ARMv8-M Security Extensions: Requirements on Development Tools - ARM Information Center](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ecm0359818/index.html)
 * [The Next Steps in the Evolution of Embedded Processors for the Smart Connected Era](https://community.arm.com/docs/DOC-11532)
 * [Enhanced Security and Energy Efficiency of Microcontrollers and SoCs](https://community.arm.com/docs/DOC-11533)
 * [ARMv8-M document on developer.arm.com](https://developer.arm.com/products/architecture/m-profile/docs)

