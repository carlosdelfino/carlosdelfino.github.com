---
title: "Integrando Asterisk com Google Speech para uso com Arduino"
tags: [pbx, digital, voip, google, text-to-speech, google-speech,voz, telefonia, audio, pbx-digital]
category: pbx_digital
layout: article
comments: true
toc: true
share: true
feature:
 index: true
 category: true
ads: 
 show: true
coinbase:
 show: true
image:
 teaser: pbx_digital/asterisk-255x180.png
 feature: pbx_digital/asterisk-640x359.png
 credit: Asterisk
 creditlink: http://www.asterisk.org/
---
O Google possui um serviço de reconhecimento da fala, e um complementar que é o de leitura de texto, o primeiro Chamado de Google Speech-to-Text e o segundo chamado de Google Text-to-Speech. Usando os dois serviços podemos obter novas funcionalidades no Asterisk, como a leitura de noticias, dados que possam estar disponível em serviços internos da empresa relativos a relatórios montados automaticamente ou mesmo pelo funcionário.

<!--more-->

Mas o mais interessante no nosso contexto, em especial considerando a Internet das Coisas (IoT - Internet of Things) onde podemos dar voz as coisas quando estas se comunicando pelo Asterisk. A ideia é quando o usuário fizer uma ligação para um determinado ramal que pertença a algo que está integrado este lhe informe detalhes de seu estado, ou mesmo quando algo atingir um determinado limite como uma planta com pouca agua, seja feita uma ligação interconectando quem cuida da planta com esta, e assim a planta enviando uma mensagem informando o que deseja, podendo ser que seja regada ou mesmo que seja mudado sua posição devido a temperatura do ambiente.

## Configurando o Google Speech
Bem, o que desejamos então e dar voz a esta planta para que ela possa usar o sistema de ramais da sua casa ou empresa, para isso usaremos como dito a cima o Google Speech.

Bem para usarmos o Google Text-to-Speech, abreviando Google TTS, não precisamos anda além do texto um script e o acesso a internet para obter do Google o audio referente ao texto.

Mas, para obter o texto com base no audio, precisamos ter também uma conta no Google APP, então vamos conversar para ai.

## Criando uma Chave de Acesso
Visite a URL: https://console.developers.google.com/project
Crie um projeto, ative a API do Google Speech no menu “APIs” e crie uma chave de acesso (key) no menu credencial, não entraremos aqui em detalhes sobre isso, mas é bem simples, tal chave deve ser criada visitando o menu “Credential” e clicando no botão “Create New Key”, então clique na nova janela no botão “Browser Key”, deixe o campo texto que surgiu em branco e clique finalmente no botão “create”.

Eu irei fornecer aqui uma chave de testes, que estará disponível enquanto ela não for usada com abuso, ou seja um total de 50 requisições por dia, portanto faça seus testes com ela se não quiser criar agora uma conta para você.

Instalando os pré-requisitos para trabalhar com Audio e o Google Speech
Para convertermos os arquivos de forma a obter o reconhecimento do audio e sua conversão para o Google Speech-To-Text (Google STT), precisamos de alguns bibliotecas e ferramentas.

O Google STT, reconhece dois formatos de audio, o FLAC e o SPX conhecido como SPEEX, este último é um formato padrão para reconhecimento da fala em ferramentas gratuitas, porém usaremos aqui apenas o FLAC.

Para trabalhar com o FLAC precisamos do conversor universal de audio o “SOX”,  entre outras bibliotecas que usaremos, então instale os seguintes requisitos e suas respectivas dependências em seu ambiente de trabalho, caso seja o linux e tenha o apt-get use “apt-get install” seguido dos nomes abaixo.

 * curl
 * wget
 * flac
 * bison
 * git
 * libwww-perl
 * libjson-any-perl
 * speex
 * libspeex-dev

## O Script de interação com o Asterisk
Para que possamos obter os arquivos textos que serão enviados ao seu dispositivo controlado com o Arduino (ou outro controlador) precisamos de um script que será acionado pelo AGI (Asterisk Gateway Interface).

O Script ira obter o audio enviado pelo ramal, e em seguida enviado ao Google Speech-to-Text que devolverá o texto interpretado, tal texto será então lido pelo Google Texto-To-Speech para confirmar a solicitação e final enviado ao Arduino.

<a href="/cursoarduino/" class="btn-success">Este trabalho é mantido com os cursos oferecidos no <br />
Curso Arduino Minas!</a>
