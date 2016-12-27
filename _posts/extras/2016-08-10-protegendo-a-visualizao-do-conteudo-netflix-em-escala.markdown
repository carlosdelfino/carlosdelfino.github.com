---
layout: article
title: "Protegendo a Visualização do Conteúdo Netflix em Escala"
date: "2016-08-10 11:19:47 -0300"
tags: [extra, Netflix, segurança, servidores, freebsd, http, https, tls, aes]
categories: [extra, seguranca]
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
   teaser: pensamentos/pensamento2-400x200.jpg
   feature: pensamentos/pensamento2-400x200.jpg
---
O artigo citado abaixo, apresenta as propostas e implementações feitas pela equipe "Open Connect" da Netflix para melhorar o throughput de um único servidor de 8Gbps em 2012 para 90Gbps em 2016.

<!--more-->

A equipe tem investido tempo na melhoria do FreeBSD utilizado como sistema operacional que roda no hardware que compõem o Open Connect Appliance (OCA) responsável por amarzenar e servidor os conteúdos de video.

<figure>
<img alt="Netflix diagrama do modelo SendFile"
src="/images/extra/netflix/netflix-sendfile.png" />
<figcaption>Modelo Sendfile proposto e usado pelo Netflix</figcaption>
</figure>

O artigo está em inglês mas para quem não domina o idioma basta usar o google trator.

[Click aqui e boa leitura](http://techblog.netflix.com/2016/08/protecting-netflix-viewing-privacy-at.html).
