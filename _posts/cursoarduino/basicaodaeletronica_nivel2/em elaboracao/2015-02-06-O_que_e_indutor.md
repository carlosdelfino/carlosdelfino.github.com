---
title: "Indutores, Consruindo o Seu!"
excerpt: Indutores são componentes amplamente usados em circuitos analógicos, em especial receptores ou transmissores de rádio, porém podem ser usados em circuitos para filtragem de sinais, como filtros de bassa faixa, altos e baixos para caixas de som. Neste artigo falarei um pouco sobre a construção de indutores, porem o uso será em um sensor capacitivo para o Arduino.
tags: [eletrônica, Eletrônica Básica, Aprendizado, Rádio, RF, Arduino, Sensor, Capacitivo, Indutor, Choque, reator,  Passa Banda, Filtro, Passa Baixa, Tanque, Filtro Passa Alta, Conversor Analógico Digital, ADC, ACD]
category: [BasicaoDaEletronica,Nivel 2]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
image:
  feature: basicaodaeletronica/indutores/indutores-1400x400.png
  teaser: basicaodaeletronica/indutores/indutor_toroidal_ferrite-400x321.jpg
  credit: Diversas Origens
  creditlink: 
tagcloud: true
coinbase:
 show: true
--- 

## O que são Indutores e seu funcionamento

Os indutores são componentes eletrônicos de fácil fabricação, são 
construidos com diversos loops de fio, voltas, que formam assim um
campo magnético que inteferem no fluxo da corrente.

Quando a corrente passa pelo fio esta induz um campo magnético 
que ao ser interceptado por outro campo interfere assim no fluxo 
da corrente.

<img src="/images/basicaodaeletronica/indutores/indutor_basico_e_ideal-364x200.png" />

Como o Indutor é composto de diversos loops a própría corrente 
sobre sua estrutura interferência em seu fluxo pelo campo magnético 
que ela mesma forma.

Com isso uma corrente continua que passa através do Indutor produz
um campo magnético constante, assim a corrente continua flui 
livremente através do condutor, porém ao sofrer variação na corrente
o campo magnético também sofre alteração, assim uma corrente alternada
em determinada frequência passará a sofrer resistência, quanto mais
elevada a frequência de oscilação da corrente, maior será a resitência.
Podendo tal resistência ser medida como reatância e tem uma defasagem
de 90 graus.

## Indutor ou Bobina?

Os indutores possuem outros nomes que são também adotados na 
literatura, e pode variar conforme o circuito aplicado.

O termo Bobina, Choque, e até mesmo Reator reference ao mesmo 
componente. 

<img src="/images/basicaodaeletronica/indutores/magnetic_ballasts_237x200.jpg" />
Os _Reatores_ são um tipo de bobina utilizados especialmente 
em lampadas florescentes, são grandes e pessados e hoje em 
muitos casos são substituidos por circuitos especiais, sua 
função é regular o fluxo de corrente.

<img src="/images/basicaodaeletronica/indutores/common-mode-choke-800x308.png" />
O Termo _Choke_ ou _Choque_ vem do inglês _choking_ ou seja
bloquear, quando usado em filtros que eliminam altas frequências.
Os Choques são normalmente construidos em pares de forma que
a carga imposta a eles tenha os dois polos ligados a cada
bobina que estão em série com o circuito, ao contrário dos 
transformadores que tem a bobina em paralelo com a carga e a
fonte.

Já o termo bobina se refere apenas ao fato de um indutor ser
um fio enrolado como uma bobina.

# Formatos de Indutores

Todos os indutores tem um formato similar, podendo variar
na forma do rolamento, seu núcleo e se são do tipo duplo.

<img src="/images/basicaodaeletronica/indutores/indutor_nucleo_ar-219x200.png" /> 
Os indutores podem ser enrolados sobre o ar ou si mesmos,
são chamados simplesmente de "Indutores de Núcleo de Ar".
Tais indutores não possuem núcleo, ou quando possuem são
feitos de materiais que não possuem propriedades magnéticas
como o plastico, madeira ou resina, tais nucleos quando 
usados tem apenas função de dar suporte mecânico.


Há também os indutores que são construidos sobre suporte
metálicos como ferro doce, como os usados em transformadores.
São pesados e usados para altas tensões.

Já os indutores construídos sobre ferrite são usados para altas
frequências, muito comuns em receptores ou transmissores de rádio 
ou circuitos de alta frequência.

Há indutores que são construidos de forma a terem seu núcleo 
ajustados, tendo assim suas caracteristicas alteradas conforme
o núcleo é inserido na bobina.

<img src="/images/basicaodaeletronica/indutores/indutor_nucleo_ferrite-248x200.png" />
Há indutores de ferrite que são construidos também em formato
toroidal, são compactos e de excelente estabilidade. Uma das
grandes qualidades dos Indutores Toroidal, é o fato de sofrerem
menor interferência de outros indutores próximos e também não 
causarem interferências em outros componentes e linhas de corrente. 
Sendo chamados de Indutores auto blindados.

## Identificando os Valores dos Indutores

Como citado acima os indutores podem ter diversos formatos, mas o 
que é mais relevante é seu comportamento elétrico, e isso é dado
conforme o valor medido em Henries, chamado de indutância, e alguns 
incluem também um valor paralelo em Ohms já que podem ser construidos 
sobre resitores, ou oferecer tal caracteristica Ohmica devido ao 
diametro do fio construido. Porém Indutores possuem também a Reatância 
Indutiva como os capacitoresPossuem a Reatância Capacitive, e esta 
Reatância está defasada em 90 graus com relação a fase da corrente 
alternada aplicada sobre ele. Não iremos entrar em detalhes neste 
artigo sobre o assunto. Portando iremos cosiderar aqui apenas seu 
valor medido em Henris e será cosiderado os demais valores como 
sendo um componente ideal.

<img src="/images/basicaodaeletronica/indutores/escala_indutancia_multimetro_minipa_et-2082c-800x480.jpg" />
Os indutores dificilmente terão valores maiores que 100mH (Cem 
Milionesimos de Henry) ou menores que 1uH (Um Micro Henry),
Porém você irá encontrar multimetros que  tem escalas com leituras 
entre 20H e 2mH e outros até menores. 

## Obtendo novos valores com associação

Os indutores quanto montados em série ou paralelo possuem seus 
valores somados ou divididos da mesma forma que resistores.

## Construindo seus Próprios Indutores

Em analise das melhores opções para construção.
{: .notice-warning }

## Fontes
 
 * http://www.circuitstoday.com/how-to-make-an-air-core-inductor 
 * http://pt.wikipedia.org/wiki/Balastro_(eletricidade)
 * http://en.wikipedia.org/wiki/Choke_(electronics)
 * 