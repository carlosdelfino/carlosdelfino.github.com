---
title: Parametrização do Eclipse para uso com o GNU ARM Eclipse
date: 2016-11-29 02:30:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, pranejamento]
layout: article-workshop-estacio-2016-1
share: true
toc: true
comments: true
feature:
 category: true
 index: true
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

### Parametros específicos para o C e C++.

Há outros parametros que somente estão disponíveis no Ecipse quando o plugin para programação em C e C++ estão instalados corretamente. Você pode ir até a arvore de parametros e escolher a opção _"C/C++"_ e então verá uma lista de conjunos de parametros.

Veja o que pode lhe atender melhor, o mais importante é você negociar com sua equipe aquilo que pode impactar no formato final do arquivo causando transtorno, especialmente na hora de fazer o processo de **Merge** de códigos entre programadores, pois se cada um usar quantidas de caracteres de espaço no lugar do TAB diferentes e usar uma formação de código diferente e sempre pedir a alto formatação irá ter problemas, pois a cada **commit** no repositório iremos ter pequenas mudanças irelevantes na escrita estrutural do código nada impacta em seu funcionamento mas será pecerbidas pelas ferramentas de versionamento.

### Ajustando a Formatação do código

Para ajustar a formatação de código para se ter entre todos os programadores o mesmo layout, você pode definir profiles de layout, o Eclipse já oferece alguns Laoyous prontos, e não iremos entrar em detalhes de como se criar um novo, pois não é o Objetivo deste Workshop, mas sim do Workshop Preparando seu Ambinte para **"[Projetos Open Source e Equipes distribuidas com Sistemas de Versionamento tipo GIT](Projetos Open Source e Equipes distribuidas com Sistemas de Versionamento tipo GIT)"**.

Siga então na janela de preferencias até o conjunto de parametros através do caminho _"C/C++"_, _"Code Style"_, _"Formatter"_., você verá então na parte direita as opções para escolher ou criar um novo formato, apenas escolha na lista o formato _"GNU [built-in]"_, este formato é o mais geral para projetos baseados em código criado pela comunidade **GNU**. Você pode altera-lo conforme negociado com sua equipe. Vale muito apena dedicar um reunião para este ajuste com a equipe.

## Indexando seu código em C/C++

Para usufruir adequadamente do auto completar do Eclipse quando se programa em **C/C++** os arquivos fonte de seu programa precisam ser automáticamente indexados, assim o Eclipse irá automáticamente lhe ajudar a identificar erros antes que eles aconteçam e lhe apresentar sugestões para autocompeltar quando estiver digitando.

Para isso abra novamente a tela de preferências e vá na avore de parametros até a coleção _"C/C++"_, _"Indexer"_. no conjunto "Indexing strategy", selecione ambas as opções _"Automatically update the index"_ e _"Update index immediately after every file-save"_, se já não estiverem selecionada, e selecionte também a opção _"Use active build configuration".

## Conclusão.

Como ver pela janela de configuração, há mais que uma centena de parametros que irão lhe ajudar a ter um abiente bem parametrizado e customizado conforme sua forma de trabalhar, para que se sinta mais a vontde e possa se comunicar com sua equipe perfeitamente, dependendo apenas de uma rápida reunião de definião de boas práticas para obter sucesso na qualidade do código gerado, e isso vale muito para o desenvolvimento de embarcados.

E o mais importante destes parametros para nós hoje são as opções citadas acima.

Boa Sorte.


