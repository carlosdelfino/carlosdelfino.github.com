---
layout: post
title: "Lançados novos Microcontroladores para IoT - Parte 1/2"
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
  feature: arm/ARMv6-7-8-M-800x500.png
---
Esta semana do dia 26 de outubro de 2016 foi lançado dois novos 
microcontroladores ARM da Família Cortex-M com foco exclusivo em IoT.

<!--more-->

## o Lançamento da Família Cortex-M

A família cortex-M nasceu em 19 de outubro de 2004, quando a ARM revolucionou o
mercado trazendo um conceito de chips 32bit para o nicho de microcontroladores,
até então todos se gabavam, e até hoje alguns ainda insistem em viver no passado
com o argumento que não precisam mais de 8 bits para desenvolver suas soluções.
Sem dúvida muitas soluções se resolvem com menos de 8 bits, porém não é só de bits
que se trata este novo conceito de processadores para microcontroladores.

A adoção dos microcontroladores ARM desde então foi rápida e sem traumas, já
que a ARM manteve compátibilidade entre as familias usando subconjuntos de 
instruções, facilitando assim a migração dos programadores ARM de outros nichos
sem traumas para o nicho de microcontroladores.

Desde então a família de microcontroladores tem crescido, sendo composta hoje 
pelos microcontroladores Cortex-M0, CortexM0+, Cortex-M1, Cortex-M23, Cortex-M33,
Cortex-M3, Cortex-M4 e Cortex-M7.

Cada um destes microcontroladores busca atender um nicho dentro do mercado de 
microcontroladores, trazendo sempre a arquiteutra Risc de 32 bits como sendo 
sua base, e o conjunto de instruções ARM Thumb de 16bits, porém capaz de tratar
dados e transferi-los em blocos de 32 bits, com exceção dos novos
Cortex-M33 e Cortex-M23 que são também com instruções de 32bits.

Em novembro de 2010 a ARM lançou mais um perfil arquitetural para sua família de 
microcontroladores chamado ARMv8-M, que traz novos recursos para uso em IoT
fundamentados na segurança através da tecnologia TrustZone, entre outros
recursos. 

Já em 25 de outubro de 2016, nesta semana a arm lança os dois primeiros chips
que usam a arquitetura ARMv8-M especifica para microcontroladores, vejamos um 
pouco mais desta arquitetura para entendermos o que ela nos trás de tão importante.

## A arquitetura ARMv8-M

O perfil ARMv8 está presente nas três familias de processadores ARM, sendo
ARMv8-A, ARMv8-R e ARMv8-M com destaque nos recursos apresentados na figura
abaixo.

<figure>
<img src="/images/arm/ARMv8-profile-800x450.png" alt="Profile ARquitetural ARMv8" />
<figcaption>Perfil arquitetural ARMv8</figcaption>
</figure>

Como pode ser visto, todos possuem instruções 32bits, sendo o Cortex-M provido
apenas com o conjunto de instruções T32/Thumb&trade;

Abaixo está o video de Mike Muller, CTO da ARM, anunciando esta semana o 
lançamento de dois novos processadores Cortex-M baseados na arquitetura ARMv8-M.

<figure>
<iframe src="https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2FARMfans%2Fvideos%2F10154688274139588%2F&show_text=0&width=560" width="560" height="315" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allowFullScreen="true"></iframe>
<figcaption>Mike Muller CTO da ARM anuncia os novos microcontroladores ARM para
IoT na #ARMTechCon 2016.</figcaption>
</figure>



## A arquitetura ARMv8-M

ARMv8-M é uma arquitetura para esta nova geração da família de microcontroladores 
Cortex-M que tem como caracteristica serem deterministicos em tempo real e para 
uso embarcado, sendo a base para soluções embarcadas de alta produtividade e 
segurança.

A Arquitetura ARMv8-M é focada na produtividade e segurança facilitando o 
desenvolvimento de aplicações para o mercado IoT e Embarcados. Reduzindo a 
complexidade de desenvolvimento de soluções embarcadas seguras em SoCs complexos.

ARMv8-M além de adicionar baixo overhead com sua extenção de segurança baseada 
no ARM TrustZone®, também aperfeiçoa o mecanismo de Depuração e Rastreio de 
instruções com mais breakpoints e watchpoints flexíveis que melhoram a 
produtividade. Traz também uma unidade de proteção de mémoria MPU mais simples
de programar. E dois sub-perfis para atender projetos mid-range e high end.


ARMv8-M tem como baseline extendendo o ARMv6-M com:

 * Hardware para divisão para operações mais rápidas com Inteiros.
 * Instruções de comparação e ramificação para controle de código rápido.
 * Ramificação longa para optimizar linkagem, incluindo longas chamadas cruzadas.
 * Semaforos comuns para uso por multíplos processadores.
 * Bits ativos para repriorização dinamica de interrupções.
 * Sporte avançado para sistemas multiprocessador com adição de instruções
   para tipos de dados atômicos do C11 (instruções load-acquire e store-release)

Na linha principal de recurso o ARMv8-M tem total capacidade para aplicações 
embarcadas:

 * Altamente escalavel e configurável.
 * Adicionada extenso conjunto de instruções 32bit para uma performance 
   significantemente acima do ARMv6-M
 * Possui um DSP para inteiros  e extenção de ponto flutuante opcional para 
   processamento de sinais mais eficiente.
 * Coprocesador opcional para suporte a aceleração por hardware.

Para melhorar a produtividade de software ARMv8-M também adiciona:

Um modelo de programação simplificado para a unidade de proteção de mémoria. 
Permitindo definir a região apenas definindo o inicio e fim do endereçamento.
Encoragando os desenvolvedores a ativar a proteção de memoria resultando no 
almento da reliabilidade do software.

Aperfeiçoamento na depuração com melhoria no rastreamento e breackpoints taais
como suporte suspensão em faixas de endereços de 32bit.

Adiciona um rastreamento mais amplo e extensão de depuração self-hosted para 
tornar a depuração e rastreamento mais fácil em sistemas embarcados, reduzindo
dramaticamente o esforço de projeto e liberação de ciclos.

<figure>
<img src="/images/arm/ARMv8-M-TrustZone.png" alt="Tecnológia TrustZone para ARMv8-M"/>
<figcaption>Tecnológia TrustZone para ARMv8-M"</figcaption>
</figure>

O TrustZone para ARMv8-M é conceitualmene similar à tecnologia TrustZone usado 
em processadores Cortex-, mas é otimizado para aplicações embarcadas que 
demandam um consumo de energia ultra baixo.

O TrustZone para ARMv8-M é projetado para:

 * Segurança acessível para processadores pequenos e de baixo consumo de energia.
 * Habilitar multiplos domínios de segurança para software.
 * Simplificação da segurança de dispositivos embarcados através da separação do
   código seguro.
 * Restrição de acesso para garantir a memória e I/O apenas para para softwares 
   confiáveis.
 * Baixo overhead para chamadas cross-domain.
 * Preservação da baixa latencia de interrupções para ambos domínios, seguros e
   não seguros
 * compatiblidade de barramento com sistemas Cortex-A, habilitando estados de
   segurança TrustZone extenderem através de sistemas Cortex-A e Cortex-M.

Exemplos de uso:

 * Nós IoT seguros.
 * Simplific o deploy de softwares de multiplas origens.
 * Armazenamento e processamento seguro de informações confidênciais.
 * Proteção de propriedade intelectual do Firmware.
 * Restrição de acesso a software convidado, através de sandboxing.
 * Restrição de acesso a periféricos e I/O para softwares confiáveis 
 
 
Para complementar a arquitetura ARMv8-M, a especificação AMBA® 5 AHB5 foi 
desenvolvida para extender a segurança do TrustZone para todo o projeto do 
embarcado além do processador. Este padrão de interconexão adiciona controles de
segurança como também extende os tipos de mémoria requeridos para embarcados de 
alta performance e suporte.

A Família ARM então recebe agora os dois novos microcontroladorres empoderados
com a arquitetura ARMv8-M, sendo o Cortex-M23 para dispositívos de menor tamanho
e restrições de energia, e o Cortex-M33 para uso em dispositivos mais complexos.

Ambos os microcontroladores já tem fornecedores trabalhando para sua produção e 
em breve veremos no mercado os novos chips. 

<figure>
<img src="/images/arm/Cortex-M23-33-vendors-1024x300.png" 
	alt="Fabricantes que já estão trabalhando para disponibilizar suas versões de chips empoderados com o Cortex-M23 e Cortex-M33" ></img>
<figcaption>Fabricantes que já estão trabalhando para disponibilizar suas versões de chips empoderados com o Cortex-M23 e Cortex-M33</figcaption>
</figure>

Tais chips **não nascerão sem** um ecosistema capaz de desenvolver código específico
e otimizado para seus novos recursos, além de permitir rodar naturalmente os 
códigos escritos para seus irmãos da Família Cortex-M, sem os recursos de segurança. 
As grandes ferramentas de desenvolvimento do mercado já estão se preparando para
gerar códigos natívos para os novos microcontroladores, veja na figura:

<figure>
<img src="/images/arm/Cortex-M23-33-ecosystem-1024x600.png" alt="Ferramentas de desenvolvimeto que já estão se preparando para o Cortex-M23 e Cortex-M33"/>
<figcaption>Ferramentas de desenvolvimeto que já estão se preparando para o Cortex-M23 e Cortex-M33</figcaption>
</figure>
  
[Continua, clique aqui para segunda parte](/arm/cortex-m/iot/Lancados-novos-microcontroladores-para-IoT-parte-2-3/)
  
  