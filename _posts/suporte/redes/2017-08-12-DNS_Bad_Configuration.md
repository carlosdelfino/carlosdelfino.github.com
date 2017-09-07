---
layout: article
title: "DNS Probe Finished Bad Config"
date: "2016-08-10 17:58:07 -0300"
tags: [dig, dns, bind, dominio, ip, windows, consulta, administração, manutenção, nslookup, config, gateway, firewall, roter, roteador]
categories: [Suporte, Redes]
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
   teaser: unifi/unifi-controller-with-security-gateway.png
   feature: unifi/unifi-controller-with-security-gateway.png
---


Falhas de conexões, lentidão e o pior de tudo "DNS Bad Configuration (DNS Probe Finished Bad Config)".

<!--more-->

## Meu Retorno ao Campo de Suporte e Implantação de Redes.

Bem, como podem ver não deixer de atuar no cmapo de redes, em especial Wi-Fi, onde pretendo focar meus esforços de estudo e suporte quanto ao nixo de atuação.

Para os que me conhecem a pouco tempo entendam, dos meus 30 anos de mercado, comecei a atuar com redes de computadores aos 21 anos ou seja 24 anos atrás quando conheci o Xenix, minha primeira rede foi uma cabeada via portas seriais RS232, usando os comandos **CU** (Connect to Unix), **DD**, **CAT** e **UUCP** (Unix to Unix Copy) dentre outros, migrando posteriormente para redes com protocolo NetBeui (SMB - Samba) com windows 3.1 e logo em seguida Linux com o próprio Samba.

Agora diante do que podiamos fazer naquela época que era ilimitado literalmente, apesar dos poucos recuros, hoje temos um universo tão amplo que se limitou a termos que usarmos muitas vezes uma interface gráfica para lidar com tantas  opçoes de parametrização, isso algumas vezes nos limita ao que a interface permite ou nossa capacidade de absorção de todo o conhecimento existente até então no setor.

O que me levou a escrever este post e outros relacionados que virão conforme demanda de documentar minha vivencia no setor, é como acabei de dizer, a necessidade de documentar minha vivência no setor. Além da programação, tanto com Microcontroladores (C/C++), Java e JavaScript (NativeScript) também atuo no campo de suporte, onde vou focar apartir de agora apenas em redes Wi-Fi em especial para condominios fechados, residênciais e comerciais, além de eventos.

## O Problema com o DNS

Na migração de uma rede existente implantada a alguns anos, em torno de 2 anos, usando um excelente Roteador Wi-FI da TP-LInk que permite inclusive o uso de antena externa através de um conector de expanção. Percebemos depois da migração que a rede apresenta em alguns momentos lentidão, e ouve momentos que recebiamos a mensagem "***DNS Probe Finished Bad Config***", diante desta mensagem o cliente se queixou nunca ter visto antes e ficamos intrigados com o problema, pois poderia ser um problema local, ou mesmo o Gateway que estaria falhando na comunicação com o DNS da Embratel, já que conforme conversamos com a Embratel não havia nenhum insidente que pudesse justificar o problema no DNS da Embratel.

Pesquisando na internet, percebi que tal problema é exclusivo do "Chrome", porém percebi além da lentidão, algumas falhas em outros softwares como o FreeDownloader, infelizmente devido ao fato do cliente não querer contratar os nossos serviços de analise e suporte não posso me dedicar muito além de deixar a rede implantada 100% no que tange ao nosso equipamento, mas aos demais não posso assumir interven;óes, ou seja apenas com um contrato de suporte é que poderia estar a disposição de fazr uma analise profunda para verificar se o problema é na maquina ou outro além de nosso equipamento instalado.

## O problema do Suporte.

No nosso mercado, pelo menos o que eu estou com o pé nele, vejo uma dificuldade muito grande em separar implantação de solução com suporte, o cliente me solita por exemplo a implantação deuma rede WIFI de autodesempenho como a que tenho desenvolvido com produtos Unifi da Ubiquit, porém isso não implica em dar suporte em suas maquinas sejam qual for o sistema operacional usado e também no acesso do provedor a internet, mas é de minhas responsabilidade sem dúvida implantar a infraestrutura bem configurada, com os firmwares mais adequados (nem sempre o ultimo é o melhor) para que esta rede funcione 100%.

Mas no decorrer da implantação pode ocorrer novos problemas, como um registro corrompido, uma atualização dos softwares


## O que fazer para resolver o problemas

Instale um software como o CCleanner e faça uma limpeza geral da maquina e dos cookies do navegador.

Em seguida digite os seguintes comandos:

```Shell
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
ipconfig /renew
```



## Fontes

* http://www.tweaking.com/articles/pages/increase_network_performance,1.html
