---
title: Configurando o Asterisk para os Primeiros Passos
excerpt: Como instalar o Asterisk e configura-lo para usar com Arduino
keywords: Asterisk, Arduino, PBX, PABX, PBX Virtual, PBX Digital
layout: article
share: true
toc: true
comments: true
feature:
 index: true
 category: true
tagcloud: true
ads: 
 show: true
coinbase:
  show: true
image:
  teaser: pbx_digital/asterisk-255x180.png
  feature: pbx_digital/asterisk-640x359.png
  credit: Asterisk
  creditlink: http://www.asterisk.org/
category: pbx_digital
---
**Atenção:** Acredito que você ja tenha tido sucesso em instalar o Asterisk conforme o tutorial [Instalação do Asterisk para Uso com Arduinos](/pbx_digital/Instalacao_do_Asterisk_para_uso_com_Arduino/) 
{: .notice-warning }

Vamos ao proximo passo a ser dado com o Asterisk após sua instalação, agora iremos configurar as extensões e canais de comunicação, usaremos apenas um tipo de canal,  controlado pelos protocolos SIP, o que será suficiente para tudo que desejamos apresentar e muito mais.

# Antes de Começar, Alguns Conceitos

Para se usar o Asterisk é preciso consolidar alguns conceitos, dentre eles:

  * [Canais de Audia]()
  * [Ramais]()
  * [URA]()
  * [Planos de Discagem]()
  * [Módulos/Extensões]()

Considerando que você já conhece tais conceitos vamos continuar.

# Arquivos de configuração Importantes

Durante a instalação usamos o comando `make sampless` para que tenhamos configurações padrões para uso do Asterisk, mas estas configurações não nos atende, portanto vamos fazer um backup delas, criando um diretório `backup` e movendo todos os arquivos que estão na pasta `/etc/asterisks` para a pasta de bakcup, porém mantenha uma copia dos seguintes arquivos:

  * asterisk.conf
  * indications.conf
  * logger.conf
  * cel.conf
  * features.conf
  * modules.conf

Deixe todos os arquivos intactos, porém sugiro que liste o conteúdo de cada um para se familiarizar mais com as configurações, o arquivo asterisk.conf e logger.conf podem ter configurações de depuração alteradas para melhorar a visualização de mensagens de erros.

# Quais Módulos iremos Usar

O primeiro arquivo que vamos intervir é o arquivo `modules.conf`, este arquivo informa ao Asterisk como carregar os módulos necessário ao nosso ambiente. O Asterisk é um software totalmente modular e além de vir com todos os módulos/extensões necessários para nosso trabalho, possui uma API bem madura para se desenvolver novos módulos.

Neste arquivo originalmente ele pede para que o Asterisk faça a carga automática dos módulos, porém queremos carregar apenas módulos que nos são interessantes, já que com a carga automática é carregado uma grande quantidade de módulos desnecessários. 

Portanto vamos criar um arquivo novo com apenas os módulos que iremos precisar em nosso Workshop.

Vamos começár criando o arquivo de novo `modules.conf` e na primeira linha coloque a diretiva que indica inicio de secão `[modules]`, em seguida na próxima linha coloque o parametro `autoload`, com a opção `no`, veja abaixo o exemplo de com ficará o arquivo, neste exemplo já listo todos os módulos necessários e como devem ser carregados:

Agora abaixo da diretiva autoload, coloque as diretivas conforme o exemplo a seguir, explicarei depois do exemplo os grupos de diretivas:

{% highlight ini linenos=table %}
[modules]
autoload=no
;
; Modulo de Configuração por Arquivo
preload=pbx_config.so
;
; Módulos de Aplicação com funções para planos de discagem
load=app_system.so
load=app_verbose.so
load=app_dial.so
load=app_record.so
load=app_userevent.so
load=app_playtones.so
load=app_playback.so
load=app_sayunixtime.so
;
; Recursos
load=res_rtp_asterisk.so
; Recurso que ira fazer a integracão com scripts que se comunicam com Arduino
load=res_agi.so
;
; Codecs de Audio
load=codec_alaw.so
load=codec_ulaw.so
load=codec_gsm.so
load=codec_ilbc.so
;
; Funções para Planos de Discagem
load=func_dialgroup.so
load=func_dialplan.so
load=func_callerid.so
load=func_channel.so
;
; Canais de Audio Local
noload=chan_alsa.so
noload=chan_oss.so
load=chan_console.so
; Canais de Audio VOIP, usaremos apenas SIP para os ramais
load=chan_sip.so
load=chan_aix.so
;
; Formatos de audio, observe diretiva “noload”, diz para não carregar
noload=format_g719.so
load=format_ilbc.so
load=format_g723.so
load=format_jpeg.so
load=format_sln.so
noload=format_sln16.so
noload=format_g726.so
noload=format_mp3.so
load=format_vox.so
load=format_g729.so
load=format_ogg_vorbis.so
load=format_wav_gsm.so
load=format_gsm.so
load=format_pcm.so
load=format_wav.so
noload=format_h263.so
noload=format_siren14.so
noload=format_h264.so
noload=format_siren7.so
{% endhighlight %}

Como pode ser visto nos comentários, carregamos primeiro um modulo que irá cuidar da configuração, 
este modulo nos oferece recurso como recargar de configuração, e principalmente a possibilidade 
de se usar arquivos de configuração em formato texto.

O módulo de configuração e carregado com a diretiva `preload` para que seja carregado com 
antecedência.

Em seguida, carregamos módulos de aplicação e úteis ao plano de discagem, porém o que mais nos 
interessa e que iremos lidar mais, além do plano de discagem propriamente dito, será o módulo 
`res_agi.so`, este módulo é responsável pela integração com aplicações externas, funcionando 
como um Gateway para o Asterisk e tais aplicações, será através deste recurso que iremos ver 
como desenvolver scripts para se comunicar com o Arduino.

Os módulos de prefixo `chan_`, criam os canais de audio e voip necessário ao funcionamento do 
Asterisk e todo o PBX e os módulos de prefixo `format_` carregam recursos para tratamentos dos 
arquivos de áudio nos formatos identificados, serão úteis para gravar e reproduzir arquivos de 
áudio.

Após esta mudança precisamos reiniciar o Asterisk já que fizemos mudaças em praticamente todos 
os arquivos de configuração, reiniciando é mais seguro se ter o resultado desejado.

Porém, ao se alterar apenas arquivos de configurações pode se usar o comando `rasterisk` que 
veremos a seguir.

# Próximos Passos
Veremos no próximo tutorial como criar nosso primeiro canal de comunicação e nossos ramais. 
Aguardem.

## Mais Informações:
Outras informações sobre o Workshop podem ser obtidos [clicando aqui, visitando nossa página no 
facebook](https://www.facebook.com/events/1500419536839268/)

<a href="/cursoarduino/" class="btn-success">Este trabalho é mantido com os cursos oferecidos no <br />
Curso Arduino Minas!</a>
