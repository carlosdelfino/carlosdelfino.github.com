---
layout: post
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

O primeiro conseito que é preciso conhecer e entender bem para se converter pares de coordenadas de um GPS para distâncias em quilometros é a Milha Nautica que tem como simbolo comum `NM` quem vem do inglês **Nautical Miles**.

<!--more-->

A milha náutica é o equivalente a 1' (um minuto) no grande circulo terrestre, ou seja considerando que se está no equador e que se movimente a fração de angulo de 1' (um minuto) sobre o mar em direção sul ou norte, terá andando uma milha náutica, portanto: `1' = 1NM`. Na Inglaterra e Estado Unidos, apesar de não ser um sistema aceito oficialmente pelos orgãos normativos internacionais, ainda é usado uma medida chamada Milhas Terrestres, este sistema foi baseado na medida Romana de distância, onde 1000 passos dados por um centuirão (Comandante de uma Milicia Romana), ou seja Mile Passus, passos que eram duplos com relação aos nossos passos normais e mediam o equivalente a 63360 polegadas, o que em metros mede 1851,85 metros, arredondando temos então 1852Mt.

A Milha Náutica foi baseada em principios ciêntificos, baseada na curvatura da terra qualquer linha a contorná-la terá 360 graus. A linha do Equador mede aproximadamente 40000Km a medida feita por [Eratostenes]({% post_url 2016-08-11-eratostenes %}) em 240 A.E.C., hoje a ciência comprovou que a medida não é muito distante, sendo 40072Km. Dividindo então esta linha por 360 graus, depois por 60 minutos e finalmente por 60 segundos (360° equivale a 60' - minutos), teremos então a distância aproximada de de 1851,85 mt para cada arco minuto (1').

Assim fica claro que a cada 1' (um minuto de arco) temos uma milha que são 1852Mt.

Agora precisamos entender bem o que são **Longitude** e **Latitude**, veja que nosso intuito é didatico portanto não entraremos profundamente na questão. Esstaremos lidando com o conceito de coordenadas Geográficas com relação a curvatura da Terra, e devido a sua imperfeição teremos valores arredondados e aproximados do real.

**Latitude** é o angulo entre o equador e uma determinada posição na terra quando nos movemos diretamente para um dos polos seja polo sul ou polo norte, sendo o limite de cada polo o angulo de 90°, ou seja a distancia entre os dois polos é de 180°. A letra grega &phi;. A terra é riscada para indicar latitudes especificas e de grande importancia que são chamados de ***paralelos*** dentre os mais importantes tempos:

* O Equador, divide a terra ao meio, tendo um lado o hemisfério sul, e do outro, o hemisfério norte.
* O trópico de Câncer é o trópico ao norte do equador terrestre, correspondendo ao paralelo 23.4378° (23º26’16") de latitude norte. Junto com o equador, delimita a zona tropical norte.
* O trópico de Capricórnio é o paralelo situado 23.4378° ao sul do equador terrestre (23º26’16" de latitude sul). Delimita junto com o equador a zona tropical sul.
* O Círculo Polar Ártico terrestre corresponde ao paralelo da latitude 66º 33’ 44" (ou 66.5622°) Norte.
* Círculo Polar Antártico terrestres corresponde ao paralelo cuja latitude é 66º6/10 Sul e que corresponde ao complemento de 23º4/10 abatido nos trópicos.

## Calculando a Distâncias

Iremos discutir aqui três cenários, o primeiro distâncias pequenas, inferiores a 7° que se baseiam apenas na mudança de latitude ou longitude unicamente, depois distâncias pequenas, inferiores a 7° que tem variação de ambos, Latitude e Longitude. E o terceiro caso, grandes distãncias ou seja superior a 7°.

Há profissionais que consideram distâncias de até 14°, mas optaremos or 7° pois teremos uma maior precisão para distãncias entre um estado e outro no Brasil.

A escolha deste ângulo se dá pelo fato de percebermos facilmente a curvatura da terra quando já temos uma distância de 777,84Km.

### Calculando Pequenas Distâncias com apenas a Latitude ou Longitude

Vamos começar fazendo o calculo de distância entre dois pontos de forma simples, sem considerar a curvatura da terra. Vamos considerar dois Pontos A e B que variem apenas em sua Latitude:

* Ponto A
  * Longitude:  38°31'21.72"O
  * Latitude:    3°48'30.80"S
* Ponto B
  * Longitude:  38°31'21.72"O
  * Latitude:    3°48'21.28"S

Neste caso não precisamos nos preocupar o par da coordenada, então iremos trabalhar apenas com o valor que varia, no caso da Latítude, chamamos esta variação de DLA (Distancia Latitudinal).

Então aplicamos a fórmula para descobrir o **DLA**, onde **LA_F** é a *Latitude Final*, e **LA_I** é a *Latitude Inicial*:

Para medidas em graus decimais:
$$
DLA = | LA_F - LA_I |
$$

Pra medidas em graus padrão:
$$
DLA = | (LAG_F * 60) + LAM_F + (LAS_F / 60) - (LAG_I * 60) + LAM_I + (LAS_I / 60) |
$$

Como podemos ver o DLA é a distância em graus (seja na notação padrão ou decimal), LAG, LAM e LAS são respetivamente, Graus da Latitude, Minutos da Latitude, Segundos da Latitude, e devemos trabalhar com o módulo da distância, apenas usamos o sinal se desejarmos saber qual a direção que seguimos, o quenão é o caso aqui, então considerando as duas latitudes informadas,  3°48'30.80"S e 3°48'21.28"S basta subtrai-las, individualmente para cada unidade, veja que quando a latitude é ao sul (S) usamos valores negativos, e quando a Longitude é a Oeste (O) usamos também valores negativos. Ficando assim nosso cálculo:

$$
DLA_G = ( -3) - ( -3)       * 60 = 0   \\
DLA_M = (-48) - (-48)       *  1 = 0   \\
DLA_S = (-21.28) - (-30.80) / 60 = 0.1586666\ldots   \\
\, \\
DLA = DLA_G + DLA_M + DLA_S \\
DLA =   0   +   0   + 0.1587 \\
DLA = 0.1587
$$

Agora temos nossa distãncia longitudinal que é `0.1587` e assim podemos calcular quantos quilometros temos de distancia entre os dois pontos apenas multiplicando pelo relação existente de 1' (Um minuto) para a Milha Maritima é 1NM e que 1 NM são 1852Mt, então basta fazer a multiplicação final:

$$
DT = DLA * 1852
DT = 0.1587 * 1852
DT = 293.91
$$

Como desejamos o cálculo em Mt multiplicamos por 1852, se quissemos em Km deveriamos ter usado 1.852.

Assim a distância entre o Pnto A e Ponto B no castelão é de 293.91Mt, vamos arredonar para 294Mt, Ainda não podemos conferir a distância está correta porque optamos em usar apenas uma das coordenada considerando que a outra está fixa, mas se formos ver na realidade o Castelão não está alinhado com meridiano, então a Longitude também altera.

Agore tente obter duas Longitudes e faça o mesmo calculo, o principio é o mesmo.

### Calculando Pequenas distâncias variando Longitude e Latitude

Ainda considerando que qualquer distância que varie menos de 7 graus não é necessário ledouble em consideração a curvatura da Terra, usaremos então apenas o calculo da Hipotenusa para descobrirmos a distância entre os dois pontos quando se varia tanto a Longitude quando a Latitude, o calculo é bem simples também Vejamos.

Basta fazermos o calculo de cada distancia separadamente pra começar, sendo assim calculamos o DLA (Distância Latitudinal) e DLO (Distância Longitudinal) seja em metros ou KM, em seguida calculamos a hipotenusa destas distâncias:

$$
DT = \sqrt{(DLA * 1.852)^2 + (DLO * 1.852)^2}
$$

Com isso obtemos a distância na medida escolhida. Vamos fazer um teste com dados reais. Como podemos ver a Longitude varia pouco no nosso exemplo, mas é o suficiente para termos um calculo prático.

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

A diferença em relação ao outro calculo é pequena devido a pequena inclinação Longitudinal.

Vejam se está certo medindo a distância entre os dois pontos no google Maps. Poderá haver pequenas diferenças de 50 metros uma vez que os pontos não estão 100% sincronizados.

Abaixo está a imagem do Google Earth que usamos.

<figure>
<img alt="Coordenadas do Castelão, Fortaleza, CE" src="/images/cursoarduino/geoprocessamento/coordenadas-castelao.jpg" />
<figcaption>
Coordenadas do Estádio Castelão em Fortaleza, CE, a imagem ao lado permite visualizar as marcações suadas para calculo do comprimento do estádio sua maior extenção.
</figcaption>
</figure>

### Calculo para Grandes Distâncias

Iremos ver agora como proceder o calculo para grandes distãncias, consideraremos então distâncias maiores que 7°, seja na Longitude ou Latitude ou ambos.

## Codigos de exemplo

O Codigo abaixo é o código simplificado considerando a curvatura da terra, este código pode ser usado diretamente no Arduino UNO, Mega, DUE ou qualquer outro, lembrando que o Arduino UNO e Mega não tem funções nativas para trigonometria, portanto pode ser um pouco lento sua execução, mas veremos logo a frente um código que é alternativa para este problema quando usamos distâncias menores que 7°.

{% highlight C %}
double calcDistancia(double lat_inicial, double long_inicial, double lat_final, double long_final) {

    double d2r = 0.017453292519943295769236; // PI / 180

    double dlong = (long_final - long_inicial) * d2r;
    double dlat = (lat_final - lat_inicial) * d2r;

    double temp_sin = sin(dlat/2.0);
    double temp_cos = cos(lat_inicial * d2r);
    double temp_sin2 = sin(dlong/2.0);

    double a = (temp_sin * temp_sin) + (temp_cos * temp_cos) * (temp_sin2 * temp_sin2);
    double c = 2.0 * atan2(sqrt(a), sqrt(1.0 - a));

    return 6368.1 * c; // convert radius to KM, (minimal radius 6,357 maximal radius 6,378)
}
{% endhighlight %}

### Outros Cálculos interessantes

#### Obtendo Distância e Angulo

{% highlight C %}
// Retorna um array com distância e angulo
double* calcDistanciaEAngulo(double lat_inicial, double long_inicial, double lat_final, double long_final) {
    // convert angles to radians
    double lat_inicial = lat_inicial * PI / 180;
    double long_inicial = long_inicial * PI / 180;
    double lat_final = lat_final * PI / 180;
    double long_final = long_final * PI / 180;
    // find cartesian coordinates
    double x1 = cos(lat_inicial) * cos(long_inicial);
    double y1 = cos(lat_inicial) * sin(long_inicial);
    double z1 = sin(lat_inicial);
    double x2 = cos(lat_final) * cos(long_final);
    double y2 = cos(lat_final) * sin(long_final);
    double z2 = sin(lat_final);
    // vector from initial to terminal point
    double xv = x2 - x1;
    double yv = y2 - y1;
    double zv = z2 - z1;

    // distance
    double distanceChordal = sqrt(xv * xv + yv * yv + zv * zv);
    double distance = 2 * asin(distanceChordal / 2);

    // magic formula for azimuth from  http://en.wikipedia.org/wiki/Azimuth
    double Azimuth = atan(sin(long_final - long_inicial) / (cos(lat_inicial) * tan(lat_final) - sin(lat_inicial) * cos(long_final - long_inicial)));
    if (lat_final < lat_inicial) {
        Azimuth = Azimuth + PI;
    }

    // output
    double azimuth = Azimuth * 180 / PI;
    double resp[] = {distance, azimuth};
    return resp;
}
{% endhighlight %}

#### Calculando cordenada do destino

{% highlight C %}
double g(latitude, longitude, azimuth, distance) {

    // convert angles to radians
    double latitude = latitude * PI / 180;
    double longitude = longitude * PI / 180;
    double Azimuth = azimuth * PI / 180;

    // find cartesian coordinates
    double x1 = cos(latitude) * cos(longitude);
    double y1 = cos(latitude) * sin(longitude);
    double z1 = sin(latitude);

    // unit vectors pointing East and North
    double xEast = -y1 / sqrt(x1 * x1 + y1 * y1);
    double yEast = x1 / sqrt(x1 * x1 + y1 * y1);
    double zEast = 0;
    double xNorth = -x1 * z1 / sqrt(x1 * x1 + y1 * y1);
    double yNorth = -y1 * z1 / sqrt(x1 * x1 + y1 * y1);
    double zNorth = sqrt(x1 * x1 + y1 * y1);

    // unit vector with the given azimuth angle
    double xv = xNorth * cos(Azimuth) + xEast * sin(Azimuth);
    double yv = yNorth * cos(Azimuth) + yEast * sin(Azimuth);
    double zv = zNorth * cos(Azimuth) + zEast * sin(Azimuth);

    // terminal point in Cartesian coordinates
    double x2 = x1 * cos(distance) + xv * sin(distance);
    double y2 = y1 * cos(distance) + yv * sin(distance);
    double z2 = z1 * cos(distance) + zv * sin(distance);

    // terminal point in spherical coordinates
    double lat2 = asin(z2) * 180 / PI;
    double lng2 = atan2(y2, x2) * 180 / PI;

    // output
    return {lat2,lng2};
}
{% endhighlight %}

## Fontes:

Abaixo listo algumas fontes interessante de conhecimento e testes dos conceitos aqui discutidos.

* http://www.pilotopolicial.com.br/calculando-distancias-e-direcoes-utilizando-coordenadas-geograficas/
* http://mundoestranho.abril.com.br/materia/por-que-a-milha-nautica-ediferente-da-milha-terrestre
* https://pt.wikipedia.org/wiki/Milha_n%C3%A1utica
* https://pt.wikipedia.org/wiki/Tr%C3%B3pico
* https://pt.wikipedia.org/wiki/C%C3%ADrculo_Polar_%C3%81rtico
* https://pt.wikipedia.org/wiki/C%C3%ADrculo_Polar_Ant%C3%A1rtico
* http://stackexchange.com/questions/286835/distance-measurement-between-latitude-longiture-pairs?rq=1
* https://en.wikipedia.org/wiki/Earth_radius
* http://geographiclib.sourceforge.net/
* http://www.movable-type.co.uk/scripts/latlong.html
* http://www.sunearthtools.com/pt/tools/distance.php
