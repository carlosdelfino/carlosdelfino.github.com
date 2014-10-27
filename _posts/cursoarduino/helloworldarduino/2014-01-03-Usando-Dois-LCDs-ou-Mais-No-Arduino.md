---
title: Usando dois ou mais LCDs com Arduino
excerpt:  Como usar dois ou mais LCDs compartilhando pinos, de forma inteligente e permitindo economiar portas.
categories: [HelloWorldArduino]
layout: article
comments: true
toc: true
share: true
image:
  teaser: liquidcrystal/16X2_Character_LCD_Module_STN_Yellow_Green_L-400x187.png
  feature: liquidcrystal/16X2_Character_LCD_Module_STN_Yellow_Green_L-600x280.jpg
  credit: Starting Eletronics
  creditlink: http://startingelectronics.com/beginners/components/LCD/
tags: [Arduino, LCD, Liquid Crystal, Arduino, Display, visor]
---
Veja no video abaixo como deve ser conectado a fiação para usar dois ou mais LCDs com o Arduino.
<figure>
<iframe width="420" height="315" src="//www.youtube.com/embed/GM67gKqR7d4" frameborder="0" allowfullscreen></iframe>
<figcaption>Veja o video de monstração, e depois leia o texto abaixo, caso tenha dúvida use o campo abaixo de comentários.</figcaption>
</figure>

## Pinagem padrão para LCDs
Na imagem abaixo pode ser visto um LCD de 2 por 16 colunas, todos os LCDs que usam este tipo de barramento paralelo podem ser conectados desta forma, usando apenas o `E` `Enable` para selecionar o LCD que será controlado.
<figure>
<img src="{{ site.url }}/images/liquidcrystal/LCD-2x16-pins.jpg" />
<figcaption>LCD de 2 linhas por 16 Colunas</figcaption>
</figure>

| Pin |  Name   |   Function           |
|:---:|:-------:|:---------------------|
| 1   | Anode	| Backlight Anode (+)  |
| 2   | Cathode	| Backlight Cathode (-)|
| 3   | VSS	| 0V (GND)             |
| 4   | VDD	| +5V                  |
| 5   | V0	| Contrast             |
| 6   | RS	| Register select      |
| 7   | R/W	| Read / Write         |
| 8   | E	| Enable               |
| 9   | DB0	| Data bit 0           |
| 10  | DB1	| Data bit 1           |
| 11  | DB2	| Data bit 2           |
| 12  | DB3	| Data bit 3           |
| 13  | DB4	| Data bit 4           |
| 14  | DB5	| Data bit 5           |
| 15  | DB6	| Data bit 6           |
| 16  | DB7	| Data bit 7           |

