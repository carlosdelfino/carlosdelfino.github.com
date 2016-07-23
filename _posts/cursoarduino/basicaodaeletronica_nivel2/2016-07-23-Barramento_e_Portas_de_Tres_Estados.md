---
title: "Barramento e Portas de Tres Estados" 
---

Muitos protocolos em especial o I2C, utilizam uma única linha do barramento para envio e recebimento de dados, o que leva a necessidade de monitorar o barramento para identificar se este está em uso por outro dispositivo que  participe na comunicação ou mesmo que apenas compartilhem o mesmo barramento. <br /><!--more-->

Para isso há o barramento de três estados. Quando um dispositivo ou porta que não precisa monitorar nem transmitir dados, este entra em um estado que chamamos de estado Z (ou podemos chamar neutro), além dele não interferir no nível de sinal do barramento ele também não drena nenhuma corrente.

Os barramentos de dados ou de clock sempre estão em nível 1 ou 0 (quando TTL 5V ou 0V e 3.3V ou 0V), porém quando entram no estado Z, estes além de não interferir no barramento, também não drenam nem monitoram o barramento deixando-o livre para a comunicação dos demais dispositivos.

Muitos dispositivos ficam em modo de escuta para simular o estado Z.
 
