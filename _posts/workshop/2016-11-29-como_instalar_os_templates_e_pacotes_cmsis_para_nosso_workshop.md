---
redirect_from: 
 - "/workshop/estacio_ceara/2016_2/Como_Instalar_os_Templates_para_Nosso_Workshop/"
title: "Como Instalar os Templates e Pacotes CMSIS para Nosso Workshop"
date: 2016-11-29 03:10:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, templates, keyl, stm32f3,stm32f4,stmicroeletronics]
layout: article-workshop-estacio-2016-1
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
coinbase:
 show: true
---

Para usar o Plugin GNU ARM Eclipse o ideal é tenhamos os templates para cada arquiteutra instalada e que seja baixado os pacotes CMSIS de cada microcontrolador.

<!--more-->

## Templates

Os Templates são layouts e exemplos de códigos, você pode criar seus próprios templates, porém por hora iremos usar os que já estão prontos.

Ao instalar o plugin GNU ARM Eclipse selecione também o plugin "GNU ARM C/C++ Generic Cortex-M Project Template" na verdade um extenão do plugin GNU ARM Eclipse. Veja a imagem abaixo:

![](/images/workshop/estaciodoceara/siconect/2016-2/helloword_arm_cortex-m/ampliando_plugins-instalados-do-gnuarm-eclipse-templates.png)

Se selecionou este pacote durante a instalação pode faze-lo agora sem problemas. Siga o processo de instalação padrão do Eclipse.

## Pacotes CMSIS

Os Pacotes CMSIS - Cortex® Microcontroller Software Interface Standard são um conjunto de bibliotecas, um framework, disponibilizado pela ARM® para complementar a definião arquitetural dos processadores Cortex-M, para que os programdores tenha funções unificadas entre os diferentes modelos de microcontroladores contribuindo assim para uma melhor colaboração e adoção de novas tecnologias.

Iniciando com o CMSIS-CORE, uma camada de abstração do hardware independente do fornecedor, o projeto do CMSIS expande em outras áreas tais como a referência de projeto dos componentes de software e seu gerenciamento e referências para interface de depuração. Veja o gráfico abaixo.

![Diagrama de Blocos do CMSIS](/images/arm/cmsis/CMSISv4_small.jpg)

Como o maior custo de um projeto de embarcado é o softare, o uso de um framework como o CMSIS reduz drasticamente tal custo, principalmente quando é necessário trocar o microcontrolador já que a interface de código com o hardware do CMSIS abstrai as diferenças quando surgem.

O CMSIS constribui também para uma padronização do acesso a interfaces seriais, periféricos e sistemas operacionais real-time como o FreeRTOS e uOS.

Os pacotes CMSIS disponiblizados pela KEIL e pelo GNU ARM Eclipse é constituido também de manuais e biblioteca de funções especificas de cada fabricante contribuindo para compilação de códigos de forma otimizada para o microcontrolador escolhidos, além de permitir que nos concentramos no nosso algortimo sem nos procuparmos com detalhes do hardware.

A Instalação dos pacotes CMSIS além de contribuir com parametros para osprocessadores tmbém contribuem com detalhes de placas de prototipação fornecidas pelos fabricantes de chip.

A instalação dos pacotes devem normalmente ser feita diretamente pelo Eclipse, através da interface gerenciamento de pacotes que é acessível clicando no icone _"Make the C++ Packs Perspective Visible"_ fazendo a atualização dos cabeçalhos e poseteriormente o download de cada template.

Já na tela de gerenciamento (Perspectiva) dos pacotes CMSIS, basta clicar no icone atualizar, mas como já teremos um pacote preprocessador para ajudar no download faremos apenas a título de prática, já que tal pacote tem mais de 500Mbs de dados úteis.

[Interface/perspectiva do Eclipse para instalação de pacotes do CMSIS](/images/workshop/estaciodoceara/siconect/2016-2/instalando_pacotes_cmsis.png)

