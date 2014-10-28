---
title: Virtual Wire
excerpt: "Virtual Wire é uma biblioteca simples que usam o modulo 433/315Mhz (modulos subgiga), para criar um link de dados entre dois microcontroladores, e apesar de obsoleta ainda é uma das melhores escolha para projetos domésticos ou meso de pequeno porte."
categories: [HelloWorldArduino]
tags: [Arduino, Arduino Uno, Arduino Mega, Arduino Due, Arduino Leonardo, Virtual Wire, SubGiga]
layout: article
share: true
toc: true
comments: true
ads: true
image:
   teaser: arduino/virtualwire/td_libs_VirtualWire_3-680x286.jpg
   feature: arduino/virtualwire/td_libs_VirtualWire_3-680x286.jpg
imagebase: "/images/pensamentos/"
---

Este Artigo foi baseado no tutorial 
[VirtualWire Library  do site PJRC de Paul e Robin - Eletronic Projects Components Available Worldwide](https://www.pjrc.com/teensy/td_libs_VirtualWire.html)
e também no site original 
[VirtualWire Library no site AirSpayce.com disponibilizada por Mike McCauley](http://www.airspayce.com/mikem/arduino/VirtualWire/), além de outras fontes.
{: .notice-warning }

O Módulo RF adequado para este uso pode ser adquirido com nosso parceiro [Arduino Omega](http://www.arduinomega.com.br)
{: .notice-success }

O módulo RF 433mHz é um modulo que atua na faixa de Rádio conhecida como SubGiga, é uma fáixa amplamente
usada por rádio amadores e também por controle remoto, não percebemos interferencia entre os dois uso
porque são poucos rádio amadores que utilizam tal faixa, como também a potência usada por controle
remotos é muito baixa, por isso não é considera como uma boa opção para uso como modem via RF, mas sem 
dúvida, é uma das opções mais baratas que temos para montar equipamentos que precisam se comunicar sem fio. 
Ou mesmo ampliar a integração de nosso sistema desenvolvido com o Arduino e equipamentos de automação, 
como portões eletrônicos de garagem.

## A frequência é 433 ou 315Mhz?

Os módulos SubGiga, irei chama-los sempre assim, podem atuar tipicamente em três frequências:

 * 433MHz, 
 * 315Mhz, 
 
Isso não interfere em nada no protocolo e na forma de funcionamento, nem mesmo na velocidade de transmissão
de dados.

As duas frequências 433Mhz e 315Mhz, são amplamente usadas em controle remotos para portões automáticos, e
também para carros.

Na maioria dos módulos muda-se apenas a bobina do filtro no receptor, e o cristal resonador no transmissor.

## Potência

O mais interessante é a potência necessária para este módulo funcionar, conforme o FCC (orgão americano que 
regula as telecomunicações), é equivalnte a 0,001% da potência de uma lampada de 25W ou seja 0,25mW, e mais
intereesante é que apenas 0,00000002% da potência transmitida precisa chegar intacta na outra ponta para se
atingir uma velocidade de 2000bps (2000 bauds por segundos, sendo neste caso 2000 bits por segundo).

Usando uma antena de boa qualidade a uma altura de 1,60m do chão, pode se atingir uma distância de até 1700m,
em ambiente aberto.

O que podemos considerar uma excelente velocidade além de uma incrível distância com tal potência.

## Como os Dados são Codificados

Antes de prosseguir é importante compreender alguns conceitos como a diferença em Modulação e Codificação, 
para tanto leia o artigo [Conceitos Sobre Comunicação](/basicaodaeletronica/Conceitos_de_Comunicacao/)
Os modulos SubGiga, usam a codificação [ASK](/basicaodaeletronica/Modulacao_ASK/)/[OOk](/basicaodaeletronica/Codificacao_OOK/) 
ou seja, eles modulam a amplitude do sinal, em outras
palavras a intensidade, conforme o nível em que se encontra a porta de dados.

Portanto se for nível 1 (5V) é emitido sinal na frequência de 433/315Mhz, sendo zero não é emitido nenhum 
sinal naquela frequência, e é por essa módulação/codificação que este tipo de rádio está tão sujeito a 
interferência, assim é preciso inserir uma segunda condificação sobre a codificação OOK para aumentar sua 
confiabilidade.  

## Porque VirtualWire

Na verdade o nome [Virtual Wire é o nome da biblioteca que foi criada para uso com este módulo por Mike McCauley](http://www.airspayce.com/mikem/arduino/VirtualWire/),
esta biblioteca não é mais mantida, já que se tornou ultrapassada e foi substituida pela [RadioHead](http://www.airspayce.com/mikem/arduino/RadioHead/),
uma biblioteca mais robusta e com mais recursos de códificação, endereçamento e outros recursos uteis para sistemas
de comunicação de dados via rádio, porém não iremos tratar tal biblioteca neste artigo, apenas a VirtualWire que é 
ainda amplamente utilizada.

O nome VirtualWire é bem representativo, já que se você tira os radios e liga o pino de transmissão com o pino de repeção
você conseguirar obter o dado transmitido da mesma forma que usando os rádios, por isso o nome foi escolhido.


Arduino 1         wires         Arduino 1

    D11-----------------------------D12

    D12-----------------------------D11

    GND-----------------------------GND
    
    
## Modulação AM

Outra característica muito interessante deste módulos é o fato deles poderem ser usados como transmissores de áudio
como usam a modulação por amplitude irão se comportar com um par, receptor transmissor AM, porém na faixa de 433/315Mhz.

Apenas o Receptor precisará de um acoplamento para converter sua saída de 5V para um nível adequado para uso com amplificadores.

Eu nunca testei tal característica, mas é amplamente comentada, apesar de pouco documentada.

## Instalando a Biblioteca VirtualWire

Instalar a biblioteca é muito simples, para tal é preciso baixar o arquivo de instalação da última versão que ainda 
está disponível, [clicando aqui, esta é a versão 1.27 do site oficial](http://www.airspayce.com/mikem/arduino/VirtualWire/VirtualWire-1.27.zip), 
algumas pessoas tem baixado a versão de Paul e Robin do site PJRC, que na verdade é a versão 1.15 da original.

Para instalar o procedimento é padrão, basta descompactar o arquivo e copiar o diretório VirtualWire para a pasta
"Library" do Arduino em "Meus Documentos" (caso esteja usando windows), cuide para que a estrutura de diretórios esteja
preservada.

## Usando a Biblioteca

Vejamos abaixo um pequeno exemplo de como usar a biblioteca.  Já estarei publicando o artigo apartir daqui
para que possam comentar e solicitar informações sobre o uso da biblioteca assim posso direcionar um pocuo 
conforme as dúvidas apresentadas.   

### Conectando os Fios

Vai um video so para verificar como ficou suas conexões.

<figure>
<iframe width="560" height="315" src="//www.youtube.com/embed/x-aBEU_jnmI" frameborder="0" allowfullscreen></iframe>
<figcaption>Video apresentando algumas informações práticas sobre o uso do módulo RF 433Mhz</figcaption>
</figure>

<figure>
<img src="{{ site.url }}/arduino/virtualwire/MX-FS-03V_MX-05V-400x190.jpg" />
<figcaption>Módulos MX-FS-03V e MX-05V</figcaption>
</figure>

Na figura acima podemos ver o a esquerda o módulo receptor, e a direita o módulo transmissor.
é importante observar que ambos funcionam adequadamente a 5V, porém o módulo transmissor pode ser alimentado
com até 12V para aumentar sua potência de transmissão.

A pinagem a ser usada segue a tabela abaixo:

#### Pinagem Módulo Transmissor:

Pinagem conforme a imagem acima da esquerda para a direita:

| Pino | Função | Obs. |
| ---- | ------ | ---- | 
|  1   | VCC    | No transmissor pode se fornecer uma alimentação de 3,5V a 12V conforme a potência de sinal desejada. |
|  2   | Dados  | O pino 2 e 3 são identicos fornecendo o sinal de dados |
|  3   | Dados  | Identico ao pino 2 |
|  4   | GND    | Deve ser conectado ao GND ou terra |

#### Pinagem do Módulo Receptor 

**Atenção**: O módulo receptor funciona adequadamente com 5V. Não deve ser ligado a tensões
superiores, isso não irá melhorar seu funcionamento.

| Pino | Função | Obs. |
| ---- | ------ | ---- | 
|  1   | Dados  | Ligar ao pino de entrada de dados que será usado no arduino. |
|  2   | VCC    | Este pino deve ser ligado a 5V, não há melhoria na recepção em ligar em tensões mais altas |
|  3   | GND    | GND ou Terra |

#### Antena

Ambos os módulos tem um ponto de solda para se conectar uma antena comum, um simples
fio de aproximada 20cm no minimo 19cm (você pode enrola-lo em uma caneta tipo BIC para
ficar melhor condicionado).

Não entrarei em detalhes aqui sobre a confeção da antena, mas em breve irei fazer um 
novo post sobre o tema. 




Agora que você está com tudo conectado conforme apresentado acima