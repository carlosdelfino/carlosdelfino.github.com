---
title: Novo Release Plugin GNU ARM Eclipse - 2.4.2-201411261616
excerpt: O Novo Release do Plugin Eclipse para GNU ARM foi liberado dia 26 do mês passado, e já pode ser baixado ou atulizado automáticamente 
tags: [ARM, SAM4, SAM4S, Xplained, ATmel, Programação, Assembly, Assembler, Eclipse, IDE, GCC, GNU, None-EABI, EABI, Protótipos, Curso, Hello World ARM, Hello World Arduino, Arduino Zero, Arduino DUE, Atualização]
layout: deprecated
deprecated:
  reason: Muitas novas versões deste plugin já foram liberadas, inclusive o mesmo já mudou de nome e em 2018 estarei trazendo as novidades, em breve público os links dos novos arigos.
categories: [helloworld,arm]
comments: true
share: true
feature: 
  index: true
  category: true
ads: 
 show: true
toc: true
coinbase:
  show: true
image:
  teaser: helloworldarm/SAM4SxPlained-255x180.png
  feature: helloworldarm/SAM4SxPlained-400x280.jpg
  credit: Carlos Delfino 
  creditlink: /sobre_min/
imagebase: "/images/helloworldarm/"
google:
  plusone: true
tagcloud: true
---

[Para baixar a mais nova atualização do Plugin  para usar o GNU ARM no Eclipse, basta clicar aqui.](https://sourceforge.net/projects/gnuarmeclipse/?source=CarlosDelfino)

A versão 2.4.2-201411261616 é um release de manutenção; a principal melhoria
inclue suporte para "Peripherals view" no plugin OpenOCD debug, e as configurações
explicitas para  "newlib-nano".

[Neste link pode ser obtido informações do que melhorou, ou leia abaixo](http://gnuarmeclipse.livius.net/blog/2014/11/26/version-2-4-2-201411261616-released/#more-1476?source=CarlosDelfino):

 * [feature-requests:#73] A "Peripherals view" agora também é visivel na aba 
   "OpenOCD" em  "C/C++ Build Settings", as configurações do link foram 
   extendidas com opções explicitas para configurar a "newlib-nano", 
   incluindo configurações para símbolos _printf_float e _scanf_float.   
 * [feature-requests:#70] O padrão do mecanismos de preferências padrões do 
   Eclipse é agora o mecanismo padrão para diversas configurações padrões 
   (mais informaçòes no Wiki) 
 * [feature-requests:#72]  A variável de configuração do Eclipse ${jlink_path}
   é automáticamente defindia para a pasta de instalação do J-Link, pela leitura
   do registro do Windows, ou pesquisando vários diretórios quando em SO como 
   OS X ou GNU/Linux.
 * O ${openocd_path} é automáticamente definida com o diretório de instalação do 
   OpenOCD da mesma forma.
 * A arquitetura Cortex-M7 foi adicionada a lista de arquiteturas suportadas do
   compilador

O seguintes bugs foram corrigidos:

 * [bugs:#128] Quando fechando o "Peripherals view", o monitor de memoria não é 
   descartado; _Corrigido_
 * [support-requests:#81] Em certas condições erradas, a seção de depuração trava; 
   o processamento de erro no "Peripherals View" foi melhorado e o problema corrigido.
 * Se um a descompactação de um pacote falhar, o diretório incompleto é preservado 
   erroneamente; corrigido, pacotes parcialmente instalados são mantidos em certas 
   condições, 
 * O valor para a opção de construção fpu_unit=, não era apropriado; Definido para o padrão 
   
Nos projetos gerados por templates, os seguintes problemas são identificados:

 * [bugs:#129] No código de inicialização, a área de dados tem um bug relacionado 
   com DATA_END_GUARD_VALUE; Corrigido; 
 * A origem da área de mémoria flash no mapa de mémoria para o projeto genério Hello 
   World ARM Cortex-M C/C++ era 0x0; corrigido
 * A biblioteca ST HAL assume que o handler SysTick está sempre presente e retorna;
   O Handler Systick padrão agora retorna;
 * Para grandes cores STM32 (F3, F4), o código de inicialização não era apto para
   inicializar multiplas regiões da RAM, como .data & .bss; Corrigido, um novo 
   mecanismo baseado em tabelas foi adicionado ao código do startup.c;
 * O arquivo _write.c, previamente alocado na pasta system, foi movido para
   a pasta application, já que ele possui uma dependencia com "application".
   
