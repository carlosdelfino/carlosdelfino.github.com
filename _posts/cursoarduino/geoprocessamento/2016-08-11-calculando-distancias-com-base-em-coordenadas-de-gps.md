---
layout: article
title: "Calculando Distâncias com base em coordenadas de GPS"
date: "2016-08-11 09:19:03 -0300"
tags: [GPS, Milhas Náuticas, Milhas Terrestres, Longitude, Latitude, Coordenadas, Distância, Cálculo]
categories: [cursoarduino, geoprocessamento]
share: true
toc: true
comments: true
feature:
 category: true
 index: false
tagcloud: true
ads:
 show: true
image:
  teaser: cursoarduino/geoprocessamento/GPS_UP501_teaser.jpg
  feature: cursoarduino/geoprocessamento/GPS_UP501_feature.jpg
math:
   enable: true
   align: "left"
---

O primeiro conceito que é preciso conhecer e entender bem para se converter 
pares de coordenadas de um GPS é a Milha Náutica*.

<!--more-->

Revisado em: Dezembro de 2017.
{: .notice }

## A milha naútica

A milha náutica, que tem como simbolo comum `NM` do inglês **Nautical Miles*,
é o equivalente a 1' (um minuto) no grande circulo terrestre, ou seja
considerando que se está no equador e que se movimente a fração de angulo de 
1' (um minuto) sobre o mar em direção sul ou norte, terá andando uma milha 
náutica, portanto: 1' = 1NM`. 

Na Inglaterra e Estado Unidos, apesar de não ser 
um sistema aceito oficialmente pelos órgãos normativos internacionais, ainda é 
usado uma medida chamada Milhas Terrestres, este sistema foi baseado na medida 
Romana de distância, onde 1000 passos dados por um centurião (Comandante de uma 
Milicia Romana), ou seja Mile Passus, passos que eram duplos com relação aos 
nossos passos normais e mediam o equivalente a 63360 polegadas, o que em metros 
mede 1851,85 metros, arredondando temos então 1852Mt.

A Milha Náutica foi baseada em princípios científicos, baseada na curvatura da terra qualquer linha a contorná-la terá 360 graus. A linha do Equador mede aproximadamente 40000Km a medida feita por [Eratostenes]({% post_url perfil/2016-08-11-eratostenes %}) em 240 A.E.C., hoje a ciência comprovou que a medida não é muito distante, sendo 40072Km. Dividindo então esta linha por 360 graus, depois por 60 minutos e finalmente por 60 segundos (360° equivale a 60' - minutos), teremos então a distância aproximada de de 1851,85 mt para cada arco minuto (1').

Assim fica claro que a cada 1' (um minuto de arco) temos uma milha que são 1852Mt.

## O que é longitude e latitude

Agora precisamos entender bem o que são **Longitude** e **Latitude**, veja que nosso intuito é didático portanto não entraremos profundamente na questão. Estaremos lidando com o conceito de coordenadas Geográficas com relação a curvatura da Terra, e devido a sua imperfeição teremos valores arredondados e aproximados do real.

**Latitude** é o angulo entre o equador e uma determinada posição na terra quando nos movemos diretamente para um dos polos seja polo sul ou polo norte, sendo o limite de cada polo o angulo de 90°, ou seja a distância entre os dois polos é de 180°. A letra grega &phi;. A terra é riscada para indicar latitudes especificas e de grande importância que são chamados de ***paralelos*** dentre os mais importantes tempos:

* O Equador, divide a terra ao meio, tendo um lado o hemisfério sul, e do outro, o hemisfério norte.
* O trópico de Câncer é o trópico ao norte do equador terrestre, correspondendo ao paralelo 23.4378° (23º26’16") de latitude norte. Junto com o equador, delimita a zona tropical norte.
* O trópico de Capricórnio é o paralelo situado 23.4378° ao sul do equador terrestre (23º26’16" de latitude sul). Delimita junto com o equador a zona tropical sul.
* O Círculo Polar Ártico terrestre corresponde ao paralelo da latitude 66º 33’ 44" (ou 66.5622°) Norte.
* Círculo Polar Antártico terrestres corresponde ao paralelo cuja latitude é 66º6/10 Sul e que corresponde ao complemento de 23º4/10 abatido nos trópicos.

## Calculando a Distâncias

Iremos discutir aqui três cenários, o primeiro distâncias pequenas, inferiores a 7° que se baseiam apenas na mudança de latitude ou longitude unicamente, depois distâncias pequenas, inferiores a 7° que tem variação de ambos, Latitude e Longitude. E o terceiro caso, grandes distâncias ou seja superior a 7°.

Há profissionais que consideram distâncias de até 14°, mas optaremos or 7° pois teremos uma maior precisão para distâncias acima deste valor.

A escolha deste angulo se dá pelo fato de percebermos facilmente a curvatura da terra quando já temos uma distância de 777,84Km.

### Calculando Pequenas Distâncias com apenas a Latitude ou Longitude

Vamos começar fazendo o cálculo de distância entre dois pontos de forma simples, sem considerar a curvatura da terra. Vamos considerar dois Pontos A e B que variem apenas em sua Latitude:

* Ponto A
  * Longitude:  38°31'21.72"O
  * Latitude:    3°48'30.80"S
* Ponto B
  * Longitude:  38°31'21.72"O
  * Latitude:    3°48'21.28"S

Neste caso não precisamos nos preocupar o par da coordenada, então iremos trabalhar apenas com o valor que varia, no caso da Latitude, chamamos esta variação de DLA (distância Latitudinal).

Então aplicamos a fórmula para descobrir o **DLA**, onde **LA_F** é a 
*Latitude Final*, e **LA_I** é a *Latitude Inicial*:

Para medidas em graus decimais:

$$
DLA = | LA_F - LA_I |
$$

Pra medidas em graus padrão:

$$
DLA = | (LAG_F * 60) + LAM_F + (LAS_F / 60) - (LAG_I * 60) + LAM_I + (LAS_I / 60) |
$$

Como podemos ver o DLA é a distância em graus (seja na notação padrão ou decimal), LAG, LAM e LAS são respetivamente, Graus da Latitude, Minutos da Latitude, Segundos da Latitude, e devemos trabalhar com o módulo da distância, apenas usamos o sinal se desejarmos saber qual a direção que seguimos, o que não é o caso aqui, então considerando as duas latitudes informadas,  3°48'30.80"S e 3°48'21.28"S basta subtrai-las, individualmente para cada unidade, veja que quando a latitude é ao sul (S) usamos valores negativos, e quando a Longitude é a Oeste (O) usamos também valores negativos. Ficando assim nosso cálculo:

$$
DLA_G = ( -3) - ( -3)       * 60 = 0   \\
DLA_M = (-48) - (-48)       *  1 = 0   \\
DLA_S = (-21.28) - (-30.80) / 60 = 0.1586666\ldots   \\
\, \\
DLA = DLA_G + DLA_M + DLA_S \\
DLA =   0   +   0   + 0.1587 \\
DLA = 0.1587
$$

Agora temos nossa distância longitudinal que é `0.1587` e assim podemos calcular quantos quilômetros temos de distância entre os dois pontos apenas multiplicando pelo relação existente de 1' (Um minuto) para a Milha Marítima é 1NM e que 1 NM são 1852Mt, então basta fazer a multiplicação final:

$$
DT = DLA * 1852
DT = 0.1587 * 1852
DT = 293.91
$$

Como desejamos o cálculo em metros (mt) multiplicamos por 1852(mt), se quissemos em kilometros (Km) devemos usar 1.852(km).

Assim a distância entre o Ponto A e Ponto B no castelão é de 293.91Mt, vamos arredondar para 294mt, Ainda não podemos conferir se a distância está correta porque optamos em usar apenas uma das coordenada considerando que a outra está fixa, mas se formos ver na realidade o Castelão não está alinhado com meridiano, então a Longitude também altera.

Agore tente obter duas Longitudes e faça o mesmo cálculo, o principio é o mesmo.

### Calculando Pequenas distâncias variando Longitude e Latitude

Ainda considerando que qualquer distância que varie menos de 7 graus não é necessário levar em consideração a curvatura da Terra, usaremos então apenas o cálculo da Hipotenusa para descobrirmos a distância entre os dois pontos quando se varia tanto a Longitude quando a Latitude, o cálculo é bem simples também Vejamos.

Basta fazermos o cálculo de cada distância separadamente pra começar, sendo assim calculamos o DLA (Distância Latitudinal) e DLO (Distância Longitudinal) seja em metros ou KM, em seguida calculamos a hipotenusa destas distâncias:

$$
DT = \sqrt{(DLA * 1.852)^2 + (DLO * 1.852)^2}
$$

Com isso obtemos a distância na medida escolhida. Vamos fazer um teste com dados reais. Como podemos ver a Longitude varia pouco no nosso exemplo, mas é o suficiente para termos um cálculo prático.

* Ponto A
  * Longitude:  38°31'21.72"O
  * Latitude:    3°48'30.80"S
* Ponto B
  * Longitude:  38°31'20.89"O
  * Latitude:    3°48'21.28"S

$$
DLA_G = ( -3) - ( -3)       * 60 = 0   \\
DLA_M = (-48) - (-48)       *  1 = 0   \\
DLA_S = (-21.28) - (-30.80) / 60 = 0.1586667\ldots   \\
\, \\
DLA = DLA_G + DLA_M + DLA_S \\
DLA =   0   +   0   + 0.1587 \\
\, \\
DLA = 0.1587 * 1.852 \\
DLA = 293.9124Mt \\
DLO_G = (-38) - (-38)       * 60 = 0   \\
DLO_M = (-31) - (-31)       *  1 = 0   \\
DLO_S = |(-20.89) - (-21.71)| / 60 = 0.82\ldots   \\
\, \\
DLO = DLO_G + DLO_M + DLO_S \\
DLO =   0   +   0   + 0.0136667 \\
DLO = 0.0137 * 1.852 \\
DLO = 25.3724Mt \\
$$

Agora que temos o DLO e o DLA calculamos a hipotenusa.

$$
DT = \sqrt{DLA^2 + DLO^2} \\
DT = \sqrt{293.9124^2 * 25.372^2}\\
DT = 295.0054Mt
$$

A diferença em relação ao outro cálculo é pequena devido a pequena inclinação Longitudinal.

Vejam se está certo medindo a distância entre os dois pontos no Google Maps. Poderá haver pequenas diferenças de 50 metros uma vez que os pontos não estão 100% sincronizados.

Abaixo está a imagem do Google Earth que usamos.

<figure>
<img alt="Coordenadas do Castelão, Fortaleza, CE" src="/images/cursoarduino/geoprocessamento/coordenadas-castelao.jpg" />
<figcaption>
Coordenadas do Estádio Castelão em Fortaleza, CE, a imagem ao lado permite visualizar as marcações usadas para cálculo do comprimento do estádio sua maior extenção.
</figcaption>
</figure>

### Cálculo para Grandes Distâncias

Iremos ver agora como proceder o cálculo para grandes distâncias, consideraremos então distâncias maiores que 7°, seja na Longitude ou Latitude ou ambos.

## Códigos de exemplo

### Código em PHP

Abaixo é apresentado um código em PHP que foi obtido no site Stackoverflow e que é muito simples, este código pode ser usado para se calcular a distância entre dois pontos com base em sua latitude e longitude.

{% highlight php %}
function calcDistancia($lat_inicial, $long_inicial, $lat_final, $long_final)
{
    $d2r = 0.017453292519943295769236;

    $dlong = ($long_final - $long_inicial) * $d2r;
    $dlat = ($lat_final - $lat_inicial) * $d2r;

    $temp_sin = sin($dlat/2.0);
    $temp_cos = cos($lat_inicial * $d2r);
    $temp_sin2 = sin($dlong/2.0);

    $a = ($temp_sin * $temp_sin) + ($temp_cos * $temp_cos) * ($temp_sin2 * $temp_sin2);
    $c = 2.0 * atan2(sqrt($a), sqrt(1.0 - $a));

    return 6368.1 * $c;
}
{% endhighlight %}


### Código em C e C++

O Código abaixo é o código simplificado considerando a curvatura da terra, veja que ele não difere muito do código usado na linguagem PHP, e este código pode ser usado diretamente no Arduino UNO, Mega, DUE ou qualquer outro, lembrando que o Arduino UNO e Mega não tem funções nativas para trigonometria, portanto pode ser um pouco lento sua execução, mas veremos logo a frente um código que é alternativa para este problema quando usamos distâncias menores que 7°.

{% highlight C %}
double calcDistancia(double lat_inicial, double long_inicial, double lat_final, double long_final) {

    double d2r = 0.017453292519943295769236;

    double dlong = (long_final - long_inicial) * d2r;
    double dlat = (lat_final - lat_inicial) * d2r;

    double temp_sin = sin(dlat/2.0);
    double temp_cos = cos(lat_inicial * d2r);
    double temp_sin2 = sin(dlong/2.0);

    double a = (temp_sin * temp_sin) + (temp_cos * temp_cos) * (temp_sin2 * temp_sin2);
    double c = 2.0 * atan2(sqrt(a), sqrt(1.0 - a));

    return 6368.1 * c;
}
{% endhighlight %}


## Fontes:

* http://www.pilotopolicial.com.br/calculando-distancias-e-direcoes-utilizando-coordenadas-geograficas/
* http://mundoestranho.abril.com.br/materia/por-que-a-milha-nautica-ediferente-da-milha-terrestre
* https://pt.wikipedia.org/wiki/Milha_n%C3%A1utica
* https://pt.wikipedia.org/wiki/Tr%C3%B3pico
* https://pt.wikipedia.org/wiki/C%C3%ADrculo_Polar_%C3%81rtico
* https://pt.wikipedia.org/wiki/C%C3%ADrculo_Polar_Ant%C3%A1rtico
