---
redirect_from: "/bluetooth/"
title: "BlueTooth, o que é e como Usar!"
excerpt: ""
tags: [BlueTooth,  BlueTooth LE, 802.15.1, 802.15.4, 802.11, WiFi, Piconet, ZigBee, xBee, Aprendizado, Rádio, RF, Arduino, Sensor, RS232, Serial, TTL, ZigBee,]
category: [HelloWorldArduino, Nivel 2]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
image:
  feature: helloworldarduino/bluetooth/Bluetooth_bb-1800x1113.png
  teaser: helloworldarduino/bluetooth/logo_bluetooth-320x320.jpg
  credit: Carlos Delfino
  creditlink: http://carlosdelfino.eti.br
tagcloud: true
coinbase:
 show: true
--- 

Vamos começar estudando alguns conceitos. Depois veremos como 
usar básicamente o Bluetooth no Arduino.

## Conceitos Básicos do BlueTooth

Para se atuar com projetos relativos ao BlueTooth é fundamental
que se conheça alguns conceitos Básicos, que serão listados e 
explicado logo abaixo.

### Protocolo BlueTooth

Acima de tudo o BlueeTooth é um protocolo, além do hardware
existe um procedimento que define como o hardware Bluetooth
se comunica e se comporta na presença de outros hardwares que
usam a mesma frequência.

Para uso com o Arduino, é apenas necessário que se compreenda
que o Bluetooth usa a frequencia de 2.4Ghz, e que apesar disso
não se comunica com outros equipamentos, como Wi-FI.

É importante saber que o Bluetooth é definido pelo padrão
802.15.1 do IEEE.

### Frequência de Trabalho do BlueTooth

O Bluetooth é definido pela norma IEEE 802.15.1 e utiliza 
a mesma frequência utilizada por diversos outros protocolos
de rede como WiFI definido pelo IEEE 802.11 e ZigBee mais 
conhecido na implementação xBee que é definido pela norma 
IEEE 802.15.4.

A Frequência usada por todos esta normas é a 2.4Ghz e não pode 
ser alterada porem a norma define claramente como deve ser gerido
os conflitos quando multiplos tipos de equipmantos se fazem
presente no mesmo ambiente, portanto não havendo uma sobrecarga
o Bluetooth irá funcionar adequadamente mesmo em ambientes densamente
povoados por WiFi, como ocorre em algumas regiões centrais, um exemplo
é o centros de capitais como São Paulo, Rio e Belo Horizonte.

| Nome | Bluetooth Classic | Bluetooth 4.0 Low Energy (BLE) | ZigBee | WiFi | 
|:-----|:-----:|:-----:|:-----:|:-----:|:-----:|
| Padrão IEEE | 802.15.1 | 802.15.1 | 802.15.4 | 802.11<br /> (a, b, g, n) | 
| Frequência (GHz) | 2.4 | 2.4 | 0.868<br /> 0.915<br /> 2.4 | 2.4 e 5 | 
| Máximo bit rate bruto (Mbps) | 1-3 | 1 | 0.250 | 11 (b)<br /> 54 (g)<br /> 600 (n) | 
| throughput médio (Mbps) | 0.7-2.1 | 0.27 | 0.2 | 7 (b)<br /> 25 (g)<br /> 150 (n) | 
| Distância Máxima (Outdoor) em Metros | 10 (class 2)<br /> 100 (class 1) | 50 | 10-100 | 100-250 | 
| Consumo relativo de potência | Médio | Muito Baixo | Muito Baixo | Alto | 
| Tempo de Vida da Bateria | Dias | Meses a Anos | Meses a Anos | Horas | 
| Tamanho da Rede | 7 | Indefinido | >64000 | 255 | 

Tal faixa de frequência é chamado de Spectrum é abrange a frequência
de 2.4 a 2.485Ghz que é a Faixa ISM, uma faixa que não precisa de 
licensiamento pois é usada para uso industrial, cientifico e médico
mas isso não a torna uma frequência aberta que pode ser usada 
indiscriminadamente. 

O Bluetooth divide tal faixa de frequeência em 79 canais de 1Mhz cada, 
que são alternados de forma a fugir das interferências, podendo fazer 
isso 1600 vezes por segundo o que é indicado como sendo 1600 hops/sec.

### Range (distância) e Potência

O Bluetooth na sua versão atual chega a consumir 1/100 da potência dos
primeiros bluetooths produzidos que já eram bastante económicos e foram
desenvolvidos para funcionarem por longos periodos com baterias.

Os dispositivos Bluetooth são divididos em classes como listado a seguir:

 * Class 3 - Tem transmissão de 1 metro (em torno de 3 pés)
 * Class 2 - normalmente encontrados em telefones celulares e atingem até 10 metros (33 pés)
 * Class 1 - usado primáriamente na industria e atingem 100 metros (300 pés)

Os rádios Bluetooth de Classe 2 chegam a 2.5mW de potência de transmissão.


| Classe | Potência Max Saída (dBm) | Potência Máxima em (mW) | Distância Máxima |
|------|-----|-----|-----|
| 1 | 20 dBm | 100 mW | 100 m | 
| 2 | 4 dBm | 2.5 mW | 10 m | 
| 3 | 0 dBm | 1 mW | 10 cm | 


### A infraestrutura do Bluetooth

O Bluetooth tem dois tipos de dispositivos:

 * Escravo / Slave - São normalmente fones de ouvidos, mouses e teclados
   estes dispositivos atuam apenas como escravos de um um unico dispositivo
   mestre e somente se comunica com ele, não se comunicando com outros slaves
   e nenhum outro mestre, além do que foi inicialmente pareado. Porém o mestre
   pode ser mudado.
 * Mestre / Master - São normalmente os computadores e celulares, eles também 
   podem atuar como escravo, porém somente um master pode existir na rede
   Bluetooth, os demais devem ser escravos.
   
A rede Bluetooth é chamada de Piconet em alusão ao seu tamanho reduzido, já que
são limitadas a 7 dispositivos no Bluetooth comum, porém no Bluetooth LE é possível
chegar até a mais de 5000 (cinco mil) dispositívos.

É responsabilidade do master coordenar a PicoNet Bluetooth, e pode enviar e receber
dados dos slaves.  

### Como os dispositivos são endereçados

Na rede PicoNet do Bluetooth mesmo com poucos dispositivos,
em sua versão comum, utiliza um tipo de endereço similar 
ao utilizado em redes Ethernet, onde cada placa de rede tem
um endereço MAC (Media Access Control), cada dispositivo Bluetooth
tem também um endereço MAC para cada dispositivo fabricado.

Os Endereços MAC do bluetooth são compostos por 48 bits, sendo que
os primeiros 24 identificam o fabricante, e os 24 restante
representam o dispositivo. Tais endereços são atribuidos 
individualmente a cada equipamento e não é permitido que 
haja equipamentos compartilhando um endereço. 

<figure>
<img src="/images/helloworldarduino/bluetooth/device-rn-42-MAC-400x212.png" />
<figcaption>
Modem Bluetooth fornecido pela Sparkfun, modelo RN-42, e seu endereço MAC
já definido de fábrica. 
</figcaption>
</figure>

Como pode ser visto na figura acima, o endereço MAC já 
vem definido de fábrica, e é representado por 12 digitos 
hexadecimais.

Além do endereço MAC cada dispositivo Bluetooth pode ter um nome
atribuido, o RN-42 por exemplo vem com um nome como sugerido na 
imagem abaixo.
<figure>
<img src="/images/helloworldarduino/bluetooth/Dispositivos_Bluetooth_Listados-800x472.png" />
<figcaption>
Como o modem RN-42, vem nomeado de fabrica por padrão. 
</figcaption>
</figure>

Os dispositivos podem ter um nome com até 248 caracteres, 
e podem até compartilhar nomes, porém os dois últimos digitos
do MAC será adicionado ao nome para diferencia-los.

### O Processo de conexão

O processo de conexão com dispotivos bluetoot é composto por alguns 
passos e definidos por três estados, listados abaixo:

 * Inquiry - se dois disposivos bluetooth são completamente
   desconhecidos entre sí, um dos dispositivos deve ser capaz
   de enviar uma mensagem do tipo "Inquiry", assim os demais
   dispositivos desconhecidos enviaram informações como seu
   MAC e nome;
   
 * Paging (Conectando) - Páging é o processo de formar uma conexão
   entre dois dispositivo Bluetooth, Antes desta conecão ser inicializada,
   cada dispositivo precisa conecer o endereço do outro (encontrado pelo 
   pelo processo "Inquiry");

 * Connection - Após o dispositivo completar o processo "Paging", ele
   entra no estado "Connection". Enquanto conectado "Connection", o 
   dispositovo pode ser um participante ativo na Piconet ou estar em
   modo de baixo consumo de energia, "Sleep Mode". Abaixo estão listados
   os modos que o dispositivo pode estar:
   * "Active Mode" - Este é o modo padrão quando conectado, quando o 
     dispositivo está ativo, transmitido ou recebendo dados;
   * "Sniff Mode" - Este é um modo de economia de energia, quando o dispositivo
     está com baixa atividade. Ele dormirá (sleep) e somente escutará por 
     transmissões em um determinado intervalo (por exempo a cada 100ms);
   * "Hold Mode" - é um modo temporario, entra em modo de economia de energia
     (Power-Saving) e retorna em um intervalo de tempo programado para o modo
     "Active". O Master pode comandar o Slave para entrar em "Hold Mode";
   * "Park Mode" - "Park" é como o "Sleep Mode", porém mais proundo, um dispositovo
     Master pode comandar um Slave a entrar em modo "Park", e este slave ficará 
     inativo até que o master o comande novamente para acordar;

Quando dois dispositivos estão pareados este podem estar em um estado chamado 
"Bonding", neste estado tais dispositivos são colocados em afinidade de tal
forma que sempre que se encontram novamente se conectam sem precisar nenhum 
processo de validação. Isso se dá com equipamentos como carros dotados de 
Bluetooth e Celulares, tal processo é definido durante o ato de "Parear" os
Dispositivos, onde cada um armazena informações de segurança relativas ao outro
em sua mémoria.

### Perfil do Bluetooth

A especificação do Bluetooth, define perfis que podem ser adotados 
por cada dispositivo, na tabela abaixo estão listados alguns perfis.
Lembrando que no nosso caso o Perfil mais indicado é o SPP (Serial 
Port Profile) já que estaremos apenas em primeiro instante buscando
criar uma forma de conexão virtual entre dois dispositivos, uma conexão
serial sem fio. Principal útilidade no qual inspirou os primeiros
dispositivos Bluetooth.

Não vou listar por hora os perfis existentes para o Blootooth, já 
que para este artigo apenas o SPP nos atenderá, mas caso deseje
conhecer quais perfis podem exister, existe uma excelente 
[Lista de perfis no Wikipedia](http://pt.wikipedia.org/wiki/Perfis_Bluetooth).

## Conectando o Arduino ao Bluetooth

O esquema abaixo é nossa referência para os projetos. estaremos usando
neste tutorial o móduo Bluetooth RN-42 da Sparkfun, este módulo é bastante
versátil, atuando como Slave e Master, e com outros profiles para HID além
do SSP. 

<figure>
<img src="/images/helloworldarduino/bluetooth/Bluetooth_Esquematico-1000x830.png" />
<figcaption>
O esquema de um pequeno circuito básico para teste e uso em nosso tutorial.
</figcaption>
</figure>

A seguir está este mesmo esquema montado em uma protoboard. 
<figure>
<img src="/images/helloworldarduino/bluetooth/Bluetooth_bb-1800x1113.png" />
<figcaption>
A montagem do esquema apresentado na imagem anterior, agora na protoboard.
</figcaption>
</figure>


### Significado da sinalização dos LEDs

Há dois LEDS normalmente nos modens Bluetooth e no RN-42 eles se
comportam da seguinte forma:

 * O LED vermelho com a indicação "Stat":
   * piscando 10 vezes por segundo está em modo de configuração
   * piscando 2 vezes por segundo, o móduo não está em configuração, mas o tempo para entrar no modo está contando.
   * piscando 1 vez por segundo está nos modos "Discoverable"/"Inquiring"/"Idle", fora do modo de configuração, e o tempo de configuração venceu.
   
### Configurando e controlando o Módulo Bluetooth
   
O Módulo Bluetooth indepedente de sua funcionalidade principal
pode estar em dois modos principais, um é no modo de configuração
o outro é quando está em comunicação com o outro Bluetooth, assim
seu canal de comunicação, normalmente a serial, se torna a via de
comunicação física do tunel formado pelo protocolo Bluetooth entre
os equipamentos.


### Um primeiro código

Abaixo está um primeiro código que usaremos para comunicar 
diretamente com o Bluetooth é sugerido pela Sparkfun e 
neste estágio nos atende perfeitamente, já que nosso 
objetivo é apenas testar a comunicação com o Modem Bluetooth
em modo de Comando.

{% highlight C linenos=table %} 
language:c
/*
  Example Bluetooth Serial Passthrough Sketch
 by: Jim Lindblom
 SparkFun Electronics
 date: February 26, 2013
 license: Public domain

 Este sketch de exemplo converte um modulo bluetooth RN-42
 para comunicar em 9600 bps (dos 115200 padrões), e passa
 algum dado serial entre o "Serial Monitor" e o moduo.
 */

// O projeto precisa da SotwareSerial para usar os pinos
// 2 e 3 como porta serial.
#include <SoftwareSerial.h>  

#define bluetoothTx  2  // TX-O pin of bluetooth mate, Arduino D2
#define bluetoothRx  3  // RX-I pin of bluetooth mate, Arduino D3

// veja não precisamos de um objeto especial para lidar com o módulo
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
  Serial.begin(9600);  // Inicializa o serial monitor em 9600bps

  bluetooth.begin(115200);  // O Bluetooth inicia a conexão em 115200bps
  
  bluetooth.print("$");  // Deve ser impressos três "$" individualmente!
  bluetooth.print("$");
  bluetooth.print("$");  // Para entrar em modo de comando
  
  delay(100);  // Aguarda 100 mS para entrar em modo CMD
  
  bluetooth.println("U,9600,N");  // Altera o baudrate para 9600, sem paridade.
  // 115200 pode ser muito rápido para uso com SoftwareSerial
  bluetooth.begin(9600);  // Iniciar bluetooth serial em 9600
}

void loop()
{
  if(bluetooth.available())  // Se o Módulo Bluetooth enviar algum caracter
  {
    // envia o caracter recebido do módulo para o Serial Monitor
    Serial.print((char)bluetooth.read());  
  }
  if(Serial.available())  // Se algo foi digitado e enviado no Serial Monitor
  {
    // Envia o caracter para o Módulo Bluetooth
    bluetooth.print((char)Serial.read());
  }
  // Fica em loop infinitamente!!!
}
{% endhighlight  %} 

## Fontes
 
 * [http://en.wikipedia.org/wiki/Frequency-hopping_spread_spectrum](http://en.wikipedia.org/wiki/Frequency-hopping_spread_spectrum?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [http://www.wirelessdevnet.com/channels/bluetooth/features/bluetooth.html](http://www.wirelessdevnet.com/channels/bluetooth/features/bluetooth.html?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [http://www.bluetooth.com/Pages/Basics.aspx](http://www.bluetooth.com/Pages/Basics.aspx?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [https://learn.sparkfun.com/tutorials/bluetooth-basics](https://learn.sparkfun.com/tutorials/bluetooth-basics?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [https://learn.sparkfun.com/tutorials/using-the-bluesmirf/hardware-hookup](https://learn.sparkfun.com/tutorials/using-the-bluesmirf/hardware-hookup?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [https://www.bluetooth.org/en-us/specification/adopted-specifications](https://www.bluetooth.org/en-us/specification/adopted-specifications?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3478807/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3478807/?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [http://en.wikipedia.org/wiki/MAC_address](http://en.wikipedia.org/wiki/MAC_address?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
 * [https://developer.bluetooth.org/TechnologyOverview/Pages/Profiles.aspx](https://developer.bluetooth.org/TechnologyOverview/Pages/Profiles.aspx?utm_source=carlosdelfino&utm_medium=online&utm_content=text)
