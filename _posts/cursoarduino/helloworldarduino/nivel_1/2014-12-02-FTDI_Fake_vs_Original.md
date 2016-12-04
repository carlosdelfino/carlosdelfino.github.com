---
redirect_from: "helloworldarduino/FTDI_Fake_vs_Real/"
title: FTDI Fake vs Original
excerpt: Como diferenciar um Chip Fake (falso) de um Original? e como solucionar o problema que surgiu depois que a FTDI bloqueou o uso do driver original com chips Fakes (Falsos).
tags: [FTDI, FAKE, REAL, Fake vs Original, Original vs Original, Correção, Recuperação, Windows, Linux, Mac, Falso, Falsificado, FTDI, Serial. Driver, Porta, Conexão, Instalação, Correção, Firmware, Atualização, Bloqueio, Original, Chip]
categories: [HelloWorldArduino, Nivel_1]
layout: article
share: true
toc: true
comments: true
ads:
 show: true
feature:
 index: true
 category: true
coinbase:
  show: true
image:
  teaser: helloworldarduino/FTDI/ftdi-FT232RL-real-vs-fake-400x250.jpg
  feature: helloworldarduino/FTDI/ftdi-FT232RL-real-vs-fake-1200x592.jpg
  credit:  Zeptobars
  creditlink: http://zeptobars.ru/en/read/FTDI-FT232RL-real-vs-fake-supereal
tagcloud: true
---

Desde o final de agosto, em especial depois do dia 26, alguns projetos 
que usam FTDI (chip FT232RT) em seus projetos podem estar tendo problemas, 
exatamente a porta `COM` não aparece mais, isto está ocorrendo devido a 
empresa que produz o chip ter alterado seu driver para que inutilize o 
chip se este for falsificado, isso é feito de forma simples, intervindo 
no código de identificação, provocando a gravação de um novo código que 
impede que este chip seja corretamente identificado pelos drivers.

É importante salientar que isto somente ocorre em chips falsos.

Estou pesquisando como é a melhor forma e a mais simples para se identificar 
o chip falso, e até o momento a única forma encontrada é pela inscrição do 
código do chip, sendo original escrito a Laser, e o falsificado apenas impresso.

<figure>
<img src="{{site.url}}/images/helloworldarduino/FTDI/ftdi-FT232RL-real-vs-fake-1200x592.jpg" />
<figcaption>
Na foto ao lado que obtive no [Artigo](http://zeptobars.ru/en/read/FTDI-FT232RL-real-vs-fake-supereal), 
é possível ver a diferença de impressão.
</figcaption>
</figure>


Há formas de de verificar se o chip é original, porém exigem conhecimentos 
e habilidades que fogem de nosso contexto, já que irá ter que abrir o 
encapsulamento do chip, veja no link o processo.

Um fato interessante é que o chip fake usa tecnologia mais avançada, já que 
usa um microcontrolador.

No final saímos prejudicado de duas formas, o chip deixa funcionar e nosso 
projeto e se torna um fracasso se não conseguimos resolver a tempo a questão, 
e por outro porque o mercado está inundado de chips falsos, prejudicando grandes 
empresas e reduzindo o lucro das mesmas, bem, algumas com certeza não merecem 
tal redução e isso prejudica o departamento de pesquisa. 

E lembre-se um dia seu projeto pode ser vitima de falsificação, sendo você o 
prejudicado, procure usar sempre equipamentos originais, e quando for usar 
clones, use apenas os licenciados, ou então opte por componentes alternativos 
mais baratos desde que originais.

## Solucionando o problema, caso seu chip parou de funcionar

[Nesse link encontrei a solução abaixo](http://www.reddit.com/r/arduino/comments/2k0i7x/watch_that_windows_update_ftdi_drivers_are/clgviyl):

## Resetando o PID com o Windows 8.1

 * Certifique que o .Net 4.0 esteja instalado
 * Download FT_Prog no link http://www.ftdichip.com/Support/Utilities.htm#FT_Prog](http://www.ftdichip.com/Support/Utilities.htm#FT_Prog)
 * Download o Driver VCP no link [http://www.ftdichip.com/Drivers/VCP.htm](http://www.ftdichip.com/Drivers/VCP.htm)
 * Extraia e edite o arquivo `ftdibus.inf` e altere todos os valores `PID` de 6001 para 0000
 * Ative carregando o driver não assinado (no canto da tela -> alterar configuraçòes do PC -> Atualizaçòes -> Restaurar Windows -> Inicio Avançado -> Solucionar Problema -> Escolher opções avançadas ->  Desativar assinatura do drive reiniciar a carga do driver modificado no gerenciador de Hardware)
 * Iniciar FT_Prog
 * Scan
 * Alterar o descritor do driver para 6001
 * gravar (flash)

### Solucionando o problema no ubuntu

 [A solução abaixo pode ser vista neste link.](http://www.minipwner.com/index.php/unbrickftdi000)

 * Conecte seu dispotivo, execute o comando "lsusb" e verá algo como  "0403:0000".
 * Download [ft232r_prog (v1.24)](http://rtr.ca/ft232r/ft232r_prog-1.24.tar.gz) e extraia o programa.
 * Instale as dependenncias usando por exemplo o comando "sudo apt-get install make gcc libftdi-dev"
 * Altere para o diretório onde descompactou o ft232r_prog onde está o arquivo ft232r_prog.c.
 * Execute o comando "make"
 * Agora execute "sudo ./ft232r_prog --old-pid 0x0000 --new-pid 0x6001"
 * Tudo pronto. desconte seu equipamento e reconecte, rode novamente o comando "lsusb". Ele deve mostrar o ID 0403:6001

## fontes:

 * https://www.sparkfun.com/news/1629
 * http://www.ftdichipblog.com/?p=1053
 * http://zeptobars.ru/en/read/FTDI-FT232RL-real-vs-fake-supereal
 * http://www.reddit.com/r/arduino/comments/2k0i7x/watch_that_windows_update_ftdi_drivers_are/clgviyl
