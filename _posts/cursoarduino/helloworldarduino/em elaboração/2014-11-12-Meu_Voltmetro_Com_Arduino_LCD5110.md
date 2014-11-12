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
---

**Aguarde:** Capítulo 1
{: .notice-warning }

Primeiro codigo básico, usando o display LCD5110 do Nokia 5110;

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