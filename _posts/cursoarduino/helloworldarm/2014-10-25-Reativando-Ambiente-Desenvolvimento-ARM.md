---
redirect_from: "/helloarm/Reativando-Ambiente-Desenvolvimento-ARM/"
title: Reativando meu Ambiente de desenvolvimento ARM
excerpt: A algum tempo tenho desejado trabalhar com microcontroladores mais complexos e avançados, além do AVR, não que o AVR não seja avançado, mas o ARM tem um atraivo muito grande por sua grande gama de fabricantes e opções existentes no mercado.
tags: [ARM, AVR, Plataforma de Desenvolvimento, Eclipse, IDE, CMSIS, AAME]
categories: [HelloWorldARM]
layout: article
share: true
toc: true
comments: true
image:
  teaser: helloworldarm/SAM4SxPlained-255x180.png
  feature: helloworldarm/SAM4SxPlained-400x280.jpg
  credit: Carlos Delfino 
  creditlink: /sobre_min/
imagebase: "/images/helloworldarm/"
google:
  plusone: true
ads:
 show: true
---
O meu primeiro encontro com a Arquitetura ARM, verdadeiramente, não como usuário mas como desenvolvedor
foi em um RoadShow da ATMel, fui a campinas especialmenete para poder conhecer de perto a empresa
que empoderava o Arduino, e tive a grata supresa de ganhar um SAM4S Xplained, uma plataforma de 
prototipagem que é tudo que eu precisava para dar meus primeiros passos com o ARM.

Isso faz alguns meses, mais de um ano, e quando cheguei de viajem claro que investir algum tempo
porém havia um problema com as plataformas de desenvolvimento da ATMel e também da ARM Ltda. Elas
são desenvolvidas para Windows e eu me ambiente para desenvolvimento era MAC e Linux.

Bem, como eu estava 100% dedicado ao Arduino, acabei focando no uso do Eclipse com AVR, usando o
plugin que me permitia desenvolver para AVR e inclusive para Arduino no meu bom e velho Eclipse,
que diga de passagem está ficando parrudo, já que rodo nele, Java, JBoss, Perl, Python, AVR, Agora
ARM e Ruby, inclusive buscando integrar com Jekyll para manter este site.

Mas nos últimos meses buscando me dedicar aos estudos para AAME, eu precisava urgentemente reativar
meu ambiente de desenvolvimento ARM, mas não poderia ser Windows, então pesquisei na internet e
achei um plugin perfeito para o ARM, chamado [GNU ARM Eclipse](http://gnuarmeclipse.livius.net/blog/).

Após reformular todo meu ambiente de desenvolvimento, já que eu estava estudando o ARM via GCC mais VI,
 e não estava sendo nada prático, precisei fazer poucos ajustes, o principal foi remover o GCC-none-eabi
 instalado via Port e instala-lo manualmente, ai tudo correu bem
 
 Abaixo vai um video simples que mostra o ambiente funcionando, espero apartir deste sábado (25/10/2014)
 postar mais coisas sobre ARM. O primeiro post será como preparar o ambiente para desenvolvimento
 O segundo será como piscar o LED da forma mais correta com um ARM.
 
 
 Por enquanto vamos nos contentar com o video abaixo que é apenas motivacional.
  <figure>
<!-- Place this tag where you want the widget to render. -->
<div class="g-post" data-href="https://plus.google.com/112098543595283009988/posts/GPLwYLTq3ni"></div>
<figcaption>Video apresentando o ambiente de desenvolvimento que irei usar para testar e escrever meus tutoriais sobre Programação e Arquitetura ARM</figcaption>
</figure>