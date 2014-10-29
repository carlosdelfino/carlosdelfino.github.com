---
title: Virtual Wire
excerpt: "Virtual Wire é uma biblioteca simples que usam o modulo 433/315Mhz (modulos subgiga), para criar um link de dados entre dois microcontroladores, e apesar de obsoleta ainda é uma das melhores escolha para projetos domésticos ou meso de pequeno porte."
categories: [HelloWorldArduino]
tags: [Arduino, Arduino Uno, Arduino Mega, Arduino Due, Arduino Leonardo, Virtual Wire, SubGiga, PLL, codificação, decodificação, manchester, OOK, ASK]
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

O módulo RF 433mHz é um modulo que atua na faixa de Rádio conhecida como SubGiga, 
é uma fáixa amplamente usada por rádio amadores e também por controle remoto, não 
percebemos interferencia entre os dois uso porque são poucos rádio amadores que 
utilizam tal faixa, como também a potência usada por controle remotos é muito 
baixa, por isso não é considera como uma boa opção para uso como modem via RF, mas 
sem dúvida, é uma das opções mais baratas que temos para montar equipamentos que 
precisam se comunicar sem fio. Ou mesmo ampliar a integração de nosso sistema 
desenvolvido com o Arduino e equipamentos de automação, como portões eletrônicos 
de garagem.

## A frequência é 433 ou 315Mhz?

Os módulos SubGiga, irei chama-los sempre assim, podem atuar tipicamente em três 
frequências:

 * 433MHz, 
 * 315Mhz, 
 
Isso não interfere em nada no protocolo e na forma de funcionamento, nem mesmo na 
velocidade de transmissão de dados.

As duas frequências 433Mhz e 315Mhz, são amplamente usadas em controle remotos 
para portões automáticos, e também para carros.

Na maioria dos módulos muda-se apenas a bobina do filtro no receptor, e o cristal 
resonador no transmissor.

## Potência

O mais interessante é a potência necessária para este módulo funcionar, conforme 
o FCC (orgão americano que regula as telecomunicações), é equivalnte a 0,001% da 
potência de uma lampada de 25W ou seja 0,25mW, e mais intereesante é que apenas 
0,00000002% da potência transmitida precisa chegar intacta na outra ponta para se
atingir uma velocidade de 2000bps (2000 bauds por segundos, sendo neste caso 2000 
bits por segundo).

Usando uma antena de boa qualidade a uma altura de 1,60m do chão, pode se atingir 
uma distância de até 1700m, em ambiente aberto.

O que podemos considerar uma excelente velocidade além de uma incrível distância 
com tal potência.

## Como os Dados são Codificados

Antes de prosseguir é importante compreender alguns conceitos como a diferença em 
Modulação e Codificação, para tanto leia o artigo [Conceitos Sobre Comunicação](/basicaodaeletronica/Conceitos_de_Comunicacao/)
Os modulos SubGiga, usam a codificação [ASK](/basicaodaeletronica/Modulacao_ASK/)/[OOk](/basicaodaeletronica/Codificacao_OOK/) 
ou seja, eles modulam a amplitude do sinal, em outras palavras a intensidade, 
conforme o nível em que se encontra a porta de dados.

Portanto se for nível 1 (5V) é emitido sinal na frequência de 433/315Mhz, sendo 
zero não é emitido nenhum sinal naquela frequência, e é por essa 
modulação/codificação que este tipo de rádio está tão sujeito a interferência, 
assim é preciso inserir uma segunda condificação sobre a codificação OOK para 
aumentar sua confiabilidade.  

## Porque VirtualWire

Na verdade o nome [Virtual Wire é o nome da biblioteca que foi criada para uso 
com este módulo por Mike McCauley](http://www.airspayce.com/mikem/arduino/VirtualWire/),
esta biblioteca não é mais mantida, já que se tornou ultrapassada e foi substituida 
pela [RadioHead](http://www.airspayce.com/mikem/arduino/RadioHead/), uma biblioteca 
mais robusta e com mais recursos de códificação, endereçamento e outros recursos 
uteis para sistemas de comunicação de dados via rádio, porém não iremos tratar 
tal biblioteca neste artigo, apenas a VirtualWire que é ainda amplamente utilizada.

O nome VirtualWire é bem expressívo, já que se você tira os radios e liga o 
pino de transmissão com o pino de repeção você conseguirar obter o dado 
transmitido da mesma forma que usando os rádios, por isso o nome foi escolhido.


Arduino 1----------wires---------Arduino 2

(RX)D11-----------------------------D12(TX)

(TX)D12-----------------------------D11(RX)

    GND-----------------------------GND
    
    
## Modulação AM

Outra característica muito interessante deste módulos é o fato deles poderem ser 
usados como transmissores de áudio como usam a modulação por amplitude irão se 
comportar com um par, receptor transmissor AM, porém na faixa de 433/315Mhz.

Apenas o Receptor precisará de um acoplamento para converter sua saída de 5V para 
um nível adequado para uso com amplificadores.

Eu nunca testei tal característica, mas é amplamente comentada, apesar de pouco 
documentada.

## Instalando a Biblioteca VirtualWire

Instalar a biblioteca é muito simples, para tal é preciso baixar o arquivo de 
instalação da última versão que ainda está disponível, [clicando aqui, esta é 
a versão 1.27 do site oficial](http://www.airspayce.com/mikem/arduino/VirtualWire/VirtualWire-1.27.zip), 
algumas pessoas tem baixado a versão de Paul e Robin do site PJRC, que na verdade 
é a versão 1.15 da original.

Para instalar o procedimento é padrão, basta descompactar o arquivo e copiar o 
diretório VirtualWire para a pasta "Library" do Arduino em "Meus Documentos" 
(caso esteja usando windows), cuide para que a estrutura de diretórios esteja
preservada.

## Usando a Biblioteca

Vejamos abaixo um pequeno exemplo de como usar a biblioteca.  Já estarei publicando 
o artigo apartir daqui para que possam comentar e solicitar informações sobre o 
uso da biblioteca assim posso direcionar um pocuo conforme as dúvidas apresentadas.   

### Conectando os Fios

Vai um video so para verificar como ficou suas conexões.

<figure>
<iframe width="560" height="315" src="//www.youtube.com/embed/x-aBEU_jnmI" frameborder="0" allowfullscreen></iframe>
<figcaption>Video apresentando algumas informações práticas sobre o uso do módulo RF 433Mhz</figcaption>
</figure>

<figure>
<img src="{{ site.url }}/images/arduino/virtualwire/MX-FS-03V_MX-05V-400x190.jpg" />
<figcaption>Módulos MX-FS-03V (transmisor) e MX-05V (Receptor)</figcaption>
</figure>

Na figura acima podemos ver o a esquerda o módulo receptor, e a direita o módulo 
transmissor. É importante observar que ambos funcionam adequadamente a 5V, porém 
o módulo transmissor pode ser alimentado com até 12V para aumentar sua potência 
de transmissão.

**Atenção**: Nenhum dos módulos deve ter seu pino de dados conectado em pinos 
que tenha uma maior drenagem de corrente que o próprio pino do Arduino, ou 
seja na faixa dos uA (Micro Ampér), isso acontece porque o circuito dos 
módulos não são capazes de fornecerem corrente suficiente para alimentar por 
exemplo LEDs. 

A pinagem a ser usada segue a tabela abaixo:

#### Pinagem Módulo Transmissor:

Pinagem conforme a imagem acima da esquerda para a direita:

| Pino | Função | Obs. |
| ---- | ------ | ---- | 
|  1   | VCC    | No transmissor pode se fornecer uma alimentação de 3,5V a 12V conforme a potência de sinal desejada. |
|  2   | Dados  | O pino 2 e 3 são identicos fornecendo o sinal de dados |
|  3   | Dados  | Identico ao pino 2 |
|  4   | GND    | Deve ser conectado ao GND ou terra |

O Transmissor deve estar conectado ao pino 11, veremos mais detalhes sobre isso 
na analise do código.

#### Pinagem do Módulo Receptor 

**Atenção**: O módulo receptor funciona adequadamente com 5V. Não deve ser ligado 
a tensões superiores, isso não irá melhorar seu funcionamento.

| Pino | Função | Obs. |
| ---- | ------ | ---- | 
|  1   | Dados  | Ligar ao pino de entrada de dados que será usado no arduino. |
|  2   | VCC    | Este pino deve ser ligado a 5V, não há melhoria na recepção em ligar em tensões mais altas |
|  3   | GND    | GND ou Terra |

Já o Receptor deve estar conectado ao pino 12, veremos mais detalhes sobre 
isso na analise do código.

#### Porque usar o pino 11 e 12?

#### Alguns cuidados com a Biblioteca

Como esta biblioteca usa os pinos `11` e `12`, e também usa o `Timer 1`, ela 
pode sofrer ou causar interferências com
outras bibliotecas.

<figure><img src="{{ site.url }}/images/arduino/arduino_uno_schema_icsp-500x350.gif"/>
<figcaption>Esquema dos pinos ICSP e como são compartilhados com os demais pinos</figcaption>
</figure>
Observe que os pinos 11 e 12 no Arduino Uno São compartilhados com o conector 
ICSP, usado no protocolo ISP, isso pode conflitar com shields que tem SDCard 
entre outros.

Fique atento a tal fato, e não se esqueça de verificar se outras bibliotecas 
não estão usando o `Timer 1`.

Já o Arduino Mega não há conflitos nestes dois pinos, já que os equivalentes 
do ICSP estão nos pinos 52 e 50.

#### Antena

Ambos os módulos tem um ponto de solda para se conectar uma antena comum, um 
simples fio de aproximada 20cm no minimo 19cm (você pode enrola-lo em uma caneta
tipo BIC para ficar melhor condicionado).

Não entrarei em detalhes aqui sobre a confeção da antena, mas em breve irei fazer um 
novo post sobre o tema. 

### O Código

Agora que você está com tudo conectado conforme apresentado acima, vamos analisar 
como usar o código da biblioteca VirtualWire.

Iremos usar os dois exemplos que acompanha o código para analisar o funcionamento do
código e as melhores formas de usar a biblioteca.

A biblioteca utiliza diversas funções separadas para preparar o ambiente, uma vez
que é precisar usar  interrupções como a do Timer 1 para gerir alguns processos
não é muito adequado o uso de classes, apesar de não ser impossível, portanto os
desenvolvedores optarem em usar C puro ao invez de C++.

#### O Código do transmissor

Veja o código abaixo usado para o transmissor:

{% highlight c lineos %}

#include <VirtualWire.h>

void setup()
{
    Serial.begin(9600);	  // Debugging only
    Serial.println("setup");

    // Initialise the IO and ISR
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_setup(2000);	 // Bits per sec
}

void loop()
{
    const char *msg = "hello";

    digitalWrite(13, true); // Flash a light to show transmitting
    vw_send((uint8_t *)msg, strlen(msg));
    vw_wait_tx(); // Wait until the whole message is gone
    digitalWrite(13, false);
    delay(200);
}

{% endhighlight %}

Inicialmente você deve incluir o cabeçalho da biblioteca com a diretiva `#include <VirtualWire.h>`.

Em seguida na função `setup()` você deve definir como irá funcionar o controle de 
portadora, `ptt`, que significa _Press-to-Talk_ é um termo usado no rádio amador 
para ativar a portadora que será modulada, representando a chave do microfone, 
que é precionado na hora de falar. Como o rádio usa a mesma faixa de frequência 
e canal (subfaixa) para enviar e receber, quando se usa dois pares de transmissores 
e receptores, criando uma comunicação bi-direcional. Este módulo funciona exatamente 
como o rádio amador.

Bem, estes módulos não possuem o recurso de PTT, porém podemos simular sua presença, 
ativando ou desativando a alimentação do transmissor, mas lembre-se não conecte o 
transmissor diretamente a porta do arduino, use um transitor como driver. 

Neste exemplo a função `vw_set_ptt_inverted(true)`está indicando a lógica inversa
para ativar ou não o `PTT`, ou seja quando *alto* está desativado, quando *baixo* 
está ativo.

E finalmente, finalizando o processo de setup `setup()` é preciso definir a 
velocidade que se deseja transmitir o bits, no caso foi definida  como sendo
2kbs (dois mil bits por segundo), veja não se faz referência a *bauds* já que 
não há uma codificação complexa.

No `loop()` foi sugerido uma mensagem de teste __"hello"__, apenas para 
demonstrar o envio de uma string, iremos discutir mais a baixo o envio de 
comandos numéricos. Essa string é armazenada em um array de chars, apesar
do formato pouco típico no Arduino o produto é o mesmo, um `ponteiro` do típo
`char` ou um array de chars.

Neste exemplo LED do pino 13 é usado para sinalizar o tempo gasto para
envio da mensagem. Então ele é ativado.

E finalmente com a função `vw_send(uint8_t*,uint8_t)` é usada para enviar a 
sequência de dados.

Veja `uint8_t` é um tipo de dados primítivo do C que representa um byte sem
representação de sinal, neste caso pode ser um `char` (sem sinal), ou mesmo
o tipo `byte` (sem sinal).

Portanto, qualquer informação composta por bytes, pode ser enviada por esta
função, veremos mais baixo na seção [Enviando comandos números](#toc17), formas
diferentes de enviar dados.

E para garantir a transmissão a função `vw_wait_tx()` é chamada, essa função tem
o mesmo comportamento que a função `flush()` da porta serial, ela apenas esqera
que todos os dados sejam transmitidos, dando continuidade então ao código.

Como a biblioteca VirtualWire usa o Timer1 para gererir a sinalização e a amplitude
do sinal a ser enviado, outros processos podem ser executados normalmente, sem 
que seja preciso aguardar o total envio dos dados, porém é sempre bom chamar
a função `vw_wait_tx()` para que se faça um ponto de sincronismo e se certifique
que todo os dados foram enviados.

E fechando o loop o LED 13 é desativado e se aguarda com um delay de 200ms a próxima
interação.

#### O Código do receptor

O código do receptor e tão simples quando do transmissor, no processo de `setup()`
deve se observar apenas que para receber dados é preciso abilitar o receptor 
chamando a função `vw_rx_start()`, esta função ativa o receptor e o PLL por 
software para decodificação dos dados enviados. 

{% highlight c lineos %}
#include <VirtualWire.h>

void setup()
{
    Serial.begin(9600);	// Debugging only
    Serial.println("setup");

    vw_set_ptt_inverted(true); // Required for DR3100
    vw_setup(2000);	 // Bits per sec

    vw_rx_start();       // Start the receiver PLL running
}

void loop()
{
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;

    if (vw_get_message(buf, &buflen)) // Non-blocking
    {
	int i;

        digitalWrite(13, true); // Flash a light to show received good message
	// Message with a good checksum received, dump it.
	Serial.print("Got: ");
	
	for (i = 0; i < buflen; i++)
	{
	    Serial.print(buf[i], HEX);
	    Serial.print(" ");
	}
	Serial.println("");
        digitalWrite(13, false);
    }
}
{% endhighlight %}

### Mudando os pinos de dados Transmissor/Receptor

// Set the output pin number for transmitter data
void vw_set_tx_pin(uint8_t pin)

// Set the pin number for input receiver data
void vw_set_rx_pin(uint8_t pin)

// Set the output pin number for transmitter PTT enable
void vw_set_ptt_pin(uint8_t pin)


### Enviando comandos numéricos.  