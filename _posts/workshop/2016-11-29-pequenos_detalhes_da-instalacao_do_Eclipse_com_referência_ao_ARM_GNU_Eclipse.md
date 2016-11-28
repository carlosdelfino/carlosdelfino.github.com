---
title: Pequenos detalhes da instalação do Eclipse com referência ao ARM GNU Eclipse
date: 2016-11-29 02:30:00 -0300
categories: [workshop, estacio_ceara, "2016_2"]
tags: ["Estácio do Ceará", FIC, arm, gnu, eclipse, plugin, gcc, none, eabi, Workshop, instalação]
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

Ao Instalar o QEMU é preciso observar alguns detalhes, nada complexo, porém são detalhes de suma importancia para o seu bom uso.

<!--more-->

## Configurando o Workspace

O Workspace não precisa de muitas configurações mas a mais importante e que evita muitos transtornos é quanto a interpretação dos caracteres exibiveis como letras acentuadas, caracteres especiais, em especial aqueles que estão fora da tabela ACII padrão, usaremos no nosso projeto e sugiro que sempre usem a página de código UTF-8.

Além da página de código é preciso cuidar também da finalização das linhas, já o windows e outros sistemas operacionais lidam diferentemente de como finalizar uma linha.

Veja que o ideal é usar o formato do Unix, sendo apenas um caracter de controle ao ao final da linha.

Veja na janela abaixo como alterar estas configurações, selecione a janela clicando na arvore de preferências em _"General"_, _"Workspace"_, caso as opções _"Text file encoding"_ e _"New text file line delimiter"_ não apareçam role a tela.

![](/images/workshop/estaciodoceara/siconect/2016-2/configuracoes-importantes-eclipse/workspace-3.png)

Apos finalizar a mudança clique no botão *Apply*, não precisa fechar a jenala ainda, vamos a próxima configuração.

## Formatação

Não que formatação impacta no desempenho do código ou em bugs, mas sem dúvida ajuda a evita-los, porque?

Porque a Equipe adota sempre o mesmo layout de código e assim a escrita fica mais rápida e o programador se sente mais seguro na nomeclatura usada, não consunde variáveis, identificar melhor os blocos de comando e estruturas de código.

Sem falar que reduzir o retrabalho na formatação quando enviado de um programador para outro através do sistema de versionamento.

Não há uma regra única, não á uma verdade única sobre o melhor forma de se formatar um código, isso deve ser negociado com sua equipe.

Para nosso trabalho, por hora ficamos determinados a usar a formatação GNU para código, assim se viermos a trocar código este será o formato que usaremos no final quando depositarmos nosso código no Repositório de versionamento.

Abaixo está a tela de pparametros/preferências do Eclipse para seleiconar a formatação a ser usada, para chegar a ela, siga a arvore de parametros até _"Formater"_ que está em _"C/C++"_

![](/images/workshop/estaciodoceara/siconect/2016-2/configuracoes-importantes-eclipse/formatacao-1.png)

Ao finalizar clique no botão *Apply*, não precisa fechar a jenela.

## Configurando alguns detalhes do editor

No editor a configuração mais importante é quantos caracteres udar na tabulação e e qual caracter usar, veja que algumas linguagens são senciveis ao uso do tab a padronização da quantidade de espaço para identação. Porém o C e o C++ não são, fazemos isso apenas por efeito de formatação e evitarmos retrabalho quando enviarmos para o sistema de versionamento.

Usaremos apenas 4 caracteres para a tabulação, e usaremos o espaço no lugar do caracter de controle *TAB*, Faça isso mudanod o valor na caixa de texto _"Dsiplayed tab width"_ e selecione a opção _"insert spaces for tabs"_

Para eveito de formatação procure também limitar as linhas a 80 colunas, caso negocie com a equipe um tamanho maior não há problema, em nosso workshop usaremos apenas 80 caracteres.

Veja na tela abaixo tais alterações, para chegar nesta janela selecione na arvore _"Text Editors"_ dentro de _"General"_.

![](/images/workshop/estaciodoceara/siconect/2016-2/configuracoes-importantes-eclipse/text-editor-2.png)

Não feche a janela, apenas clique em *Apply*.

## Indexação do código

O código fonte é indexado pelo eclipse para que se possa ter o recurso autocompletar e algumas indicações de erro de digitação atualizados, para que a indexação ocorra adequadamente, marque a opção _"Use active build configuration"_ na caixa _"Build configuration for the indexer"_ que é exibida na tela *"Indexer"*, quando selecionada na arvore de parametros _"C/C++"_, _"Indexer"_.

![](/images/workshop/estaciodoceara/siconect/2016-2/configuracoes-importantes-eclipse/index-2.png)


Clique no botão *Apply* para aplicar e em seguida clique em OK para fechar a janela.

 
