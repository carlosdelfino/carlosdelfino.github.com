---
title: Encoder Seu Funcionamento e Bibliotecas para Arduino
excerpt: Encoders são medidores de pulsos por onda quadrada que informam a direção do giro para um determinado eixo onde está acoplado, sendo amplamente usados em motores, knobs e potenciometros digitais.
tags: [Eletrônica, Arduino, Curso, Tutoriais, Curso Arduino, Hello World Arduino, Encoder, Nível Iniciante, Protocolos, Motores]
categories: [HelloWorldArduino]
layout: article
share: true
toc: true
comments: true
ads: 
 show: true
image:
  teaser: encoder/take_2__0107.jpg
  feature: encoder/take_2__0107.jpg
  credit: USDigital
  creditlink: http://www.usdigital.com/products/a2k
imagebase: "/images/encoder/"
tagcloud: true
---

Neste artigo iremos tratar especialmente dos encoders giratórios, porém o funcionamento dos 
demais enconders lineares, como as fitas usadas em impressoras jato de tinta, tem o mesmo 
funcionamento.

# O Funcionamento do Encoder

<img src="{{ site.url }}{{ page.imagebase }}td_libs_Encoder_pos4.png" width="350px" align="left"/>Na 
figura ao lado podemos ver as ondas geradas por um encoder veja cada enconder é composto um disco 
perfurado, e dois LEDs acoplados a dois sensores, assim quando o disco gira cada LED tem sua luz 
cortada em relação ao sensor, gerando assim pulsos sincronizados.

Os Pulsos são gerados defasados em 90º um do outro, e como pode ser visto na figura acima, a ordem
que são gerados determina o sentido de rotação do encoder. (sendo o encoder de fita, em que direção),
Já a velocidade dos pulsos irá indicar a velocidade do giro, podendo conforme a quantidade de pulsos
em um giro determinar quantos RPMs são executados pelo eixo.

Nas abaixo no final deste post, você poderá conhecer diversos encoders, e verá que há encoders de maior
precisão, sendo determinado pela quantidade de pulsos por giro. Na primeira fotografia abaixo "figura 1", 
é possível visualizar um Encoder de grande precisão o mesmo é contruido de forma a se obter diversas
resoluções de pulsos conforme sua aplicação, podendo chegar a mais de 3000 pulsos por giro. Tais encoders
são usados em ambientes que exijam grande precissão como braços roboticos.

# A Bibliteca para uso Com Arduino
Aguarde, em breve coloco mais informações e exemplo de parametrização para o melhor uso da Biblioteca, 
[Click aqui para visitar o site da melhor biblioteca para uso com Encoder e Arduino](http://www.pjrc.com/teensy/td_libs_Encoder.html)
{: .notice }

# Alguns Modelos de Encoder
Abaixo apresento alguns modelos de encoder, veja que não estão listados abaixo os modelos lenares
baseados em fita ou regua, tais encoders são muito utilizados em impressoras e CNCs, ou equipamentos
que controle curso de carros e esteiras.

Siga os links para  obeter valores e detalhes téncnicos, deixe nos comentários suas dúvidas sobre os
 modelos e complementarei este artigo em cada imagem, ampliando a descrição ou postando novos modelos.
 
<figure>
<img src="{{ site.url }}/images/encoder/incremental-rotary-encoders-14277-2359763.jpg" width="250px"/>
<figcaption> Figura 1<br />
<a href="http://www.directindustry.com/prod/ges-group/incremental-rotary-encoders-14277-28194.html">Encoder Rótativo Profissional para uso industrial ou veícular.</a>
</figcaption>
</figure>
<figure>
<img src="{{ site.url }}/images/encoder/parallax-incremental-rotary-encoder-large.jpg" width="250px"/>
<figcaption> Figura 2<br />
<a href="http://www.robotshop.com/en/parallax-incremental-rotary-encoder.html">Potenciometro incremental encoder da Parallax, no site Robocore.</a>
</figcaption>
</figure>
<figure>
<img src="{{ site.url }}/images/encoder/A31-Free-Shipping-1PC-New-font-b-Rotary-b-font-font-b-Encoder-b-font-Module.jpg" width="250px" />
<figcaption> Figura 3<br />
Potenciometro encoder, rotatório infinito, montado como módulo<br />
<a href="http://www.aliexpress.com/cheap/cheap-rotary-encoder.html">Diversos Modelos no Aliexpress</a>
</figcaption>
</figure>
<figure>
<img src="{{ site.url }}/images/encoder/take_2__0107.jpg" width="250px"/>
<figcaption><a href="http://www.usdigital.com/products/a2k">A2K Absolute Optical Encoder: Kit Version</a>
</figcaption>
</figure>

<figure>
<img src="{{ site.url }}/images/encoder/optical_kit_encoder_disc encoder_module.jpg" width="250px"/>
<figcaption>
<a href="http://sensor-china.en.alibaba.com/product/714912193-214329834/optical_kit_encoder_disc_encoder_module.html">Kit Optico para montagem de Encoder, Site Alibaba</a>
</figcaption>
</figure>
<a href="https://www.google.com/search?q=encoder&espv=2&biw=1280&bih=661&source=lnms&tbm=isch&sa=X&ei=oG9KVPWFPJeNNrCOgbAO&ved=0CAYQ_AUoAQ" class="btn-success">Clique aqui e veja milhares de modelos de Encoders</a>

<a href="/cursoarduino/" class="btn-success">Este trabalho é mantido com os cursos oferecidos no <br />Curso Arduino Minas!</a>
