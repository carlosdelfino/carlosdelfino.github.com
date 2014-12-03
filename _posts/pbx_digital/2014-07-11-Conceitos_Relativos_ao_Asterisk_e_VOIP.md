---
layout: article
title: Conceitos relacionados ao uso do Asterisk e VOIP
excerpt: Em todo contexto de trabalho com TIC (Tecnologia da Informação e Comunicação) temos conceitos que precisam ser assimilados, vejamos neste artigo alguns palavras e conceitos usados no ASTERISK, quais seus significados e relação.
category: pbx_digital
tags: [pbx, pbxdigital, voip, voz sobre ip, telefonia, comunicação, celular, pabx]
share: true
comments: true
feature:
 index: true
 category: true
ads: 
 show: true
coinbase:
  show: true
image:
   teaser: pbx_digital/asterisk-400x250.png
   feature: pbx_digital/asterisk-640x359.png
   credit: Asterisk
---
  * PBX (Private Branch Exchange)
é uma pequena central telefonica que pode ter apenas dois pontos de conexão telefônicos ou até mesmo centenas.

  * Virtual PBX
É o mesmo que PBX porém instalado remotamente em uma operadora ou mesmo criado através de softwares, podendo usar VOIP para comunicação entre os terminas.

  * IVR (Interactive Voice Response) ou URA (unidade de resposta audível)
O IVR ou URA é um recurso muito valioso em centrais telefonicas do tipo PBX, já que com este recurso podemos fazer atentimentos automáticos e distribuir a chamada conforme respostas do usuário, além disso podemos integrar a URA com o Arduino permitindo assim uma interação totalmente automática entre o usuário e o Arduino ou o Arduino e o Asterisk para fazer ligações para o usuário.

  * ACD (Automatic Call Distribution)
ACD permite que as ligações que chegam a central PBX sejam distribuídas conformem regras pre-estabelecidas, integrando a central com o Arduino podemos intervir nas regras de chamada conforme parâmetros coletados por ele.

  * FXO e FXS
Foreign Exchange Office e Foreign Exchange Sation, são tipos de canais (Channel), são canais telefônicos como em centrais PBXs, 
A FXO é como um aparelho telefônico, recebe sinais de controle como o sinal de chamada.
Já a FXS é como uma saída da central telefônica gerando sinalização e também oferece alimentação elétrica para funcionamento do aparelho telefônico.  Por exemplo para se conectar uma linha telefônica comum (PSTN) a um computador você precisa de um placa que tenha uma entrada FXO. Já para ligar seu telefone ao computador e este simular uma central telefonica você precisa de um canal FXS.

  * PSTN (PUBLIC SWITCHED TELEPHONE NETWORK)
É a sua operadora telefônica, em especial toda a infraestrutura que a constrõe.

  * POTS (Plain Old Telephone Service)
É o sistema telefônico clássico, amplamente utilizado no mundo, mesmo com o advento de linhas telefônicas como ISDN, ADSL, Fibra Ótica e Telefonica Celular.

  * ATA (Analog Telephone Adapter)
ATA é um adaptador de telefone comum para telefone IP, permitindo que se conecte um telefone padrão a sua rede IP e assim receber e fazer chamadas, um ATA normalmente é um dispositivo FXS.

  * Channel
São canais de comunicação, por onde há trafego de dados ou audio entre por exemplo o Asterisk e um ATA, no Asterisk não se distingue canais originador ou destino de chamada, nem mesmo canais FXO ou FXS.

  * SIP

  * Console

  <a href="/cursoarduino/" class="btn-success">Este trabalho é mantido com os cursos oferecidos no <br />
Curso Arduino Minas!</a>
  