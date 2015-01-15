---
title: Meu Voltimetro com Arduino
excerpt: Construindo um voltimetro e osciloscopio simples com o Arduino.
layout: article
tags: [Arduino Uno, Arduino Mega, Arduino leonardo, voltimetro, osciloscopio, Nokia5110, Nokia, 5110, LCD, SPI, Conversão Anlógica Digital, Anlógica]
categories: [helloworldarduino]
ads:
 show: true
comment: true
share: true 
feature:
 index: false
 category: false
tagcloud: true
---

**Aguarde:** Capítulo 1
{: .notice-warning }

Este tutorial mostra como criar um pequeno e simples multimetro microcontrolado.

## Material Necessário

 * Um Arduino UNO (preferivel com chip  ATMega328 DIP, se cometer um erro e queima-lo será fácil substítu-lo)
 * Em torno de 9 jumpers
 * Uma protoboard média
 * um Modulo com LCD do tipo LCD5110 (aquele usado no celular Nókia 5110)
 * Uma chave push button

## Primeiro código básico

O código abaixo é um primeiro passo para construir seu multímetro.
No próximo capítulo explico como montar o circuito, vamos primeiro analisar
 o código.

{% highlight C linenos=table %}
/*
 * Desenvolvendo um pequeno multimero e osciloscopio com o Arduino.
 * Autor: @CarlosDelfino <consultoria@carlosdelfino.eti.br>
 * 
 * 
 * Conexões
 *      SCK  - Pin 13
 *      MOSI - Pin 11
 *      DC   - Pin 9
 *      RST  - Pin 8
 *      CS   - Pin 10
 */
#include <SPI.h>
#include <LCD5110_Graph_SPI.h>

// dc, rst, cs
LCD5110 myGLCD(9, 8, 10);

#define READ (4)

extern unsigned char SmallFont[];
extern unsigned char TinyFont[];

float y;
uint8_t* bm;
int pacy;


int ymin = 0;
int ymax = 47;
int xmin = 0;
int xmax = 83;

void setup()
{
  myGLCD.InitLCD();
  myGLCD.setFont(TinyFont);
  pinMode(READ, INPUT_PULLUP);
}

void loop()
{
  myGLCD.clrScr();
  myGLCD.drawRect(0, 0, 83, 47);
  myGLCD.drawLine(0, 23, 84, 23);
  myGLCD.drawLine(41, 0, 41, 47);


  myGLCD.setFont(TinyFont);
  myGLCD.print("T=", 0 , ymax - 4);
  myGLCD.print("V=", 0 , 0);

  myGLCD.update();

  int lastx, lasty;
  lastx = lasty = 0;
  for (int x = 0; x < xmax; x++)
  {
    while (digitalRead(READ));

    int tmp;
    //tmp = map(y,ymin, ymax, xmin, xmax);
    tmp = analogRead(A5);

    float v = tmp * .004882812;

    tmp = map(tmp, 0, 1023, ymin, ymax);

    myGLCD.printNumI(millis(), 9, ymax - 4);
    myGLCD.printNumF(v, 2, 9, 0);


    myGLCD.invPixel(x, tmp);
    lastx = x;
    lasty = tmp;

    myGLCD.update();
    delay(500);
  } 

}
{% endhighlight %}

## Analisando o código

O código é muito simples incluimos a biblioteca SPI

## Primeiro contato com o Módulo LCD5110

Tenho 2 dois modelos do módulo LCD5110, um comprado diretamente na DX, e outro
com nosso parceiro [Arduino Omega](http://arduinomega.com.br/index.php?route=product/product&product_id=60&search=5110)

Ambos são baseados no mesmo LCD e no controlador `PCD8544` da PHILIPS, porém 
cada um tem um backlight diferente e a pinagem do módulo em local diferente,
mas ambos são conectados usando o barramento SPI, que é uma caracteristica do PCD8544.

Mas este controlador usa 3,3V como alimentação, e não é seguro liga-lo a 5V,
isso irá queima-lo, veremos no próximo cápitulo como conecta-lo corretamente.

## Montando o Circuito

iremos ver a montagem do circuito no próximo cápitulo, para evitarmos que o artigo fique 
grande, e para que possamos discutir livremente cada etapa do projeto., além claro
de pudermos fazer pequenos ajustes conforme a necessidade do projeto.

Se já entendeu todo o código, agora você pode ir para [O Cápitulo 2](2014-11-17-Meu_Voltmetro_Com_Arduino_LCD5110_CAP_2.md). 

 