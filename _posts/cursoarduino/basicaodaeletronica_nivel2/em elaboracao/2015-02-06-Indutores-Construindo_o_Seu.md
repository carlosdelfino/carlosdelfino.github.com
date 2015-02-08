---
redirect_from: "/basicaodaeletronica/nivel%202/O_que_e_indutor/"
title: "Indutores, Construindo o Seu!"
excerpt: Indutores são componentes amplamente usados em circuitos analógicos, em especial receptores ou transmissores de rádio, porém podem ser usados em circuitos para filtragem de sinais, como filtros de bassa faixa, altos e baixos para caixas de som. Neste artigo falarei um pouco sobre a construção de indutores, porem o uso será em um sensor capacitivo para o Arduino.
tags: [eletrônica, Eletrônica Básica, Aprendizado, Rádio, RF, Arduino, Sensor, Capacitivo, Indutor, Choque, Reator,  Oscilador, Passa Banda, Filtro, Passa Baixa, Tanque, Filtro Passa Alta, Conversor Analógico Digital, ADC, ACD]
category: [BasicaoDaEletronica, Nivel 2]
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
que ao ser interceptado pelo proprio fio condutor interfere assim 
no fluxo da corrente.

<img src="/images/basicaodaeletronica/indutores/indutor_basico_e_ideal-364x200.png" />

Como o Indutor é composto de diversos loops a própría corrente 
sobre sua estrutura causa interferência em seu fluxo pelo campo 
magnético que ela mesma forma.

_Com isso uma corrente continua que passa através do Indutor produz
um campo magnético constante, assim a corrente continua a fluir 
livremente através do condutor, porém ao sofrer variação na corrente
o campo magnético também sofre alteração, assim uma corrente alternada
em determinada frequência passará a sofrer resistência, quanto mais
elevada a frequência de oscilação da corrente, maior será a resitência.
Podendo tal resistência ser medida como reatância e tem uma defasagem
de 90 graus._

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

Iremos considerar aqui 
primáriamente os indutores de núcleo de Ar, já que é mais fácil de 
ser construido devido precisar apenas do fio. Em segunda parte iremos
sugerir estudos para construção utilizando um núcleo de ferrite. 

Para se construir um indutor você precisa ter algumas informações 
muito importantes em mãos, como por exemplo as medidas fisicas que 
pretente usar para construir seu indutor. 

Tais medidas são:

 * C = Comprimento da Bobina cm
 * D = Diametro da Bobina em cm
 * L = Indutância desejada em Henry 
 
Com estas informações você chegará ao número de voltas (espiras) (n) 
que deve dar no fio para obter o indutor adequado. Veja que você pode
adequar as fórmulas abaixo para obter outros valores, por exemplo
considerando que já sábe o número de voltas que deseja usar (pouco 
sentido), você poderá obter o diametro.

Normalmente se inicia a construção identificando o valor que se 
deseja, em seguida conforme o tipo de circuito se define o 
Comprimento e Diâmetro.

#### O Diâmetro/Sessão do Fio

O Diâmetro do fio não é muito importante para circuitos de alta 
corrente, mas claro evite usar fios muito grossos ou muito finos, 
sem um bom motivo para isso, procure usar um fio que apenas seja 
suficiente para dar sustentação mecânica a bobina, já que esta 
será de núcleo de ar. Veja bobinas com núcleos de plastico podem 
usar fios mais finos, a resitência em fios de cobre é bem baixa 
portanto não irá afetar seu projeto.

Além disso fios de maior seção que venham tornar a bobina mais
comprida, irão causar uma redução na indutância, já que o campo
magnético gerado por uma seção de espiras irá atingir um menor
número de espiras.

O uso de fios de seção retangular podem contribuir com o ajuste
do fio e melhorar seu suporte mecânico, porém as fórmulas aqui
apresentadas são para fios de seção retangular. Sem considerar
que o preço de tais fios é mais elevado, e são dificeis de serem
encontrados.

<figure>
<img src="/images/basicaodaeletronica/indutores/fio_secao_retangular_vs_circular-600x270.png" />
<figcaption>Imagem obtida no site: <a href="http://www.mecatronicaatual.com.br/educacao/1681-transformadores-de-baixa-tenso?utm_source=carlosdelfino&utm_medium=online&utm_content=text">http://www.mecatronicaatual.com.br/educacao/1681-transformadores-de-baixa-tenso</a></figcaption>
</figure>


### Formato da Bobina

A Bobina deve ser construida em um formato circular, evitando formas
ovais e quadradas mesmo que com os cantos arredondados. Fios de senção
rentangular podem ser usados para um melhor ajuste mecânico, mantendo
assim as voltas bem justas. Porem os calculos aqui apresentados serão
para fios de seção circular. Faça seus testes e ajuste a fórmula.

Não usaremos aqui bobinas toroidais apenas bobinas com núcleo de ar
em formatos lineares.

#### O Diâmetro da Bobina

O Diametro da bobina é muito importante, para simplificar procuramos
sempre usar um diametro de 0,7cm (um lápis) a 1,2cm (diametro de uma 
pilha AA). Sendo o ideal 1cm (equivalente a uma pilha AAA).

Veja o exemplo comparativo com Lapis e Pilha não significa que estes
serão mantidos como núcleos até mesmo porque sua composição metálica
irá interferir drasticamente no campo magnético mudando assim o valor
obtido na prática.

_É importante observar que aumentando o diâmetro da bobina você 
terá que dar menos voltas no fio, assim você consegue obter maiores 
valores para sua indutância, em um menor comprimento._

Com base no Diâmetro ou mesmo o Raio da bobina você irá obter o
tamanho da área da circunferência que uma volta de fio terá.

 
#### O Comprimento da Bobina  

O comprimento da bobina é algo que impacta bastante em seu 
funcionamento inclusive porque pode sofrer danos no manuseio, 
e assim alterando seu valor. A Sustentação mecânica neste momento 
evita que ela sofra deformação em seu diametro e forma circular. 
Já no comprimento evita que as voltas se afastem uma das outras, 
e que não seja linear podendo se curvar sobre seu próprio peso,
já que é importante para que o campo magnético atinja igualmente
todos os fios.

Depois de uma bobina pronta, você pode fazer um ajuste fino, 
aumentando ou diminuindo o espaçamento entre os fios, porém mantendo
todas as espiras no mesmo espaçamento.

### O Cálculo

Como já disse acima que o cálculo será feito para bobinas de núcleo
de AR, porém com um pequeno ajuste tal calculo poderá ser usado para 
bobinas de ferrite, mas não irei tratar deste formato inicialmente.

Iremos considerar neste calculo apenas fios de seção circular, já 
que os fios de seção retangular podem ter densidades diferentes
conforme são enrolados, tendo assim uma bobina de maior ou menor
comprimento, quando for preciso enrolar os fios bem juntos.

#### A área da Espira

A bobina é composta por espira e todas devem ter o mesmo diâmetro.
Para iniciarmos o calculo é preciso que saibamos qual área cada
espira irá ocupar, e a formúla é simples e padrão, basta usar a
fórmula de calculo da circunferência.

Assim "S" que representa na formula tal área pode ser calculada
com a seguinte fórmula:
<figure>
<img src="/images/basicaodaeletronica/indutores/calculo_area_circunferencia-500x300.png" />
<figcaption>
O calculo ao lado é o calculo padrão para obter a área da 
circunferência.

Sendo ¶ o valor padrão da constante PI ou seja 3,14 (para 
simplificar).

O calculo pode ser fácilmente ajustado caso se tenha o Diametro
ou o Ráio. </figcaption>
</figure>

#### Calculando o Número de Espiras

Para uma bobina que tenha apenas um nível de espira, ou seja
os fios não serão enrolados sobre camadas, deve usar a formula 
abaixo.

<figure>
<img src="/images/basicaodaeletronica/indutores/calculo-indutancia-800x330.png" />
<figcaption>
Finalmente o cálculo, na figura temos uma bobina de comprimento "C", 
área da espira representado por "S". E o resultado é dado em voltas em "n".
<br />
<br />
Caso queira saber qual a indutância de uma bobina com base nas medidas físicas
a segunda formula deve ser usada. 
</figcaption>
</figure>



## Fontes
 
 * http://www.circuitstoday.com/how-to-make-an-air-core-inductor?utm_source=carlosdelfino&utm_medium=online&utm_content=text 
 * http://pt.wikipedia.org/wiki/Balastro_(eletricidade)?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://en.wikipedia.org/wiki/Choke_(electronics)?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://pt.wikipedia.org/wiki/Indutor?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://www.newtoncbraga.com.br/index.php/como-funciona/4097-art560?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://www.circuitstoday.com/how-to-make-an-air-core-inductor?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://www.newtoncbraga.com.br/index.php/artigos/49-curiosidades/4151-art572.html?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 * http://www.radioamadores.net/indutancias.htm?utm_source=carlosdelfino&utm_medium=online&utm_content=text
 