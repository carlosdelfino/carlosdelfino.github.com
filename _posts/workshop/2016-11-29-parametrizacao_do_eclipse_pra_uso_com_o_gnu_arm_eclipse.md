---
title: Parametrização do Eclipse para uso com o GNU ARM Eclipse
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, pranejamento]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

Para se desenvolver no eclipse é preciso fazer uma pequena parametrização de base.

<!--more-->

Essa parametrização de base é mais importante ainda quando se vai desenvolver um projeto que seja multiplataforma, ou seja vai ser programador em sistemas operações diferentes como o Windows e Linux. Além de outros detalhes que veremos a seguir.

## Salvando os arquivos corretamente.

Quando programamos em C/C++ é fundamental que adotemos uma página de código para codifiação de arquivos que seja utilizavel em qualquer dos ambientes que o aplicativos será utilizado, evitando assim a interpretação erronea de caracteres especiais. Como letras acentuadas e outros caracteres especiais.

A Página de código mais importante é a página de código UTF-8 para este propósito ela é similar a tabela ASCII, que será muito usado na programação para embarcados quando se comunicando serialmente entre dispositivos.

Além disso entre os sistemas Unix e o Windows á uma discrepancia em como se finalizar uma linha, sendo o windows dois caracteres de controle o Carrige Return (CR) e New Line (NL) e no Unix apenas um New Line (NL).

Portanto para se acertar tais parametros, no windows clique no menú _Windows_ na barra de menus do Eclipse, em seguida selecione _preferrencies_ e na arvore de parametros de preferência que é apresentada a esquerda da nova janela, escolha o caminho _General_,_Workspace_.

Então irá na parte direta da janela, será apresenado uma coleção de parametros que podem ser ajustados conforme sua prefererência de trabalho, mas o mais importante o que se refere a _"Text file encoding"_ e _"New text file line delimiter"_.

Em "Text file encoding", normalmente no windows vem selecionado o padrão que é Cp1252, porém você deve mudar para a opção que lhe permite selecionar na caixa de seleção o padrão **UTF-8**, não escolha outro padrão, apenas este.

Já em "New text file line delimiter", você deve selecinar também a caixa que permite seleção e escolher o sistema operacional "Unix" como sendo o seu padrão de delimitação de linhas.

Finalmente basta você clicar no botão **Apply**, e para fechar a janela clique no botão **Ok**.

## Número de linhas e número máximo de caracteres por linha.

E bom ao se programar no Eclipse definir que sejam apresentaqdas os números de linhas para que facilite encontrar o ponto exato onde está ocorrendo um erro quando sua aplicação falha ao ser executada, o Eclipse nos permite definir que o editor nos mostre estas linhas.

Além disso, é bom também delimitar uma margem para o número máximo de caracteres em uma linha, o Eclipse não irá lhe impedir que continue escrevendo nesta linhas, mas será apresentada uma linha que ajuda a identificar tal limite.

Para isso, abra novamente a janela de preferências como explicado acima. E siga na arvore de paramtros até _"General"_, _"Editors"_, _"Text Editors"_. No conjunto de parametros relativos a _"Text Editors"_, você poderá definir além destas informações todo o comportamento do editor de texto do Eclipse para qualquer linguagem e tipo de edição.

Escolha então que deseja inserir espaços no lugar do caracter de controle **"Tab"**, _"Insert spaces for tabs"_.

Escolha também a opção _"Show print margin"_ e indique a quantidade de caracteres, _"Print margin column:"_, como sendo no máximo 80, você pode negociar com sua equipe um valor diferente adequado a todos, mas lembren-se que nem todos tem monitores gigantes de alta definição.

Outros paramtros podem ser setados conforme sua demanda de trabalho e interesse de personalizar o editor, fique a vontad,e mas lembre-se de anotar quais parametros mudou, até que domine toda a interface.

