---
title: "Usando o Algorítimo Localizador de Falhas" 
tags: [Mestrado, Aminadabe, WDM, SDH, Analise, Falhas, Correção, Detector, Localizador, Java, Estatística]
category: [pesquisa, infraestrutura]
layout: article
share: true
toc: true
comments: true
image:
 teaser: pensamentos/pensamento1-400x200.jpg
 feature: pensamentos/pensamento1-400x200.jpg
feature:
 category: true
 index: true
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Instruções para se usar o ALF em Java 8.

Certifique-se que o Java 8 esteja instalado e funcionando.

<!--more-->

[Baixe o ALF clicando aqui](https://github.com/carlosdelfino/ALF/releases/download/Instrucoes_de_uso_1/Instalacao.ALF.zip "Baixe o ALF clicando aqui.").

Em seguida descompacte o aquivo onde achar mais adequado, procure evitar caminhos longos, sugiro descompactar em uma pasta no raiz de seu computador.

Uma vez descompactado clique duas vezes no arquivo de nome _Alf_VII_F6c.jar_ espere abrir a janela principal do ALF, caso não abra em menos de um minuto, tente executar na linha de comando do windows com o seguinte comando:


    java -jar Alf_VII_F6c.jar

Você verá diversas mensagens sendo apresentadas na tela, não se preocupe é normal, somente verifique se alguma denota erro, se identificar alguma copie todas e me envie.

Abaixo está a tela que será apresentada:

![Biblioteca Tele Inicial](/images/instalando_alf/biblioteca_1.PNG)

## Carregando a Biblioteca

Como pode ver há um botão no meio da janela, que deve ser usado para carregar pela primeira vez a biblioteca, ao clicar no botão será aberto uma janela para escolher um arquivo de configuração da biblioteca de dispositivos, selecione o arquivo desejado, ele deve estar na pasta `cnf` e deverá ter a extensão `bib`

Veja a imagem abaixo:

![Carregando Biblioteca](/images/instalando_alf/biblioteca_2.PNG)

Clicando no arquivo será exibido a lista de componentes de sua rede como na imagem abaixo:

![Carregando Biblioteca](/images/instalando_alf/biblioteca_3.PNG)

## Carregando a Topologia

Pule para a próxima aba, você verá que as abas vão sendo liberadas conforme se carregam os recursos, agora você terá que carregar a topologia.

![Carregando Biblioteca](/images/instalando_alf/topologia_1.PNG)

Você verá diversos aquivos, use arquivo `topologia.top`, os arquivos de topologia tem a extensão `top`e também são encontrados na pasta `cnf`. 


![Carregando Biblioteca](/images/instalando_alf/topologia_2.PNG)

Pronto a topologia foi carregada e verá uma lista de relacionamento em formato arvore, com na tela baixo.


![Carregando Biblioteca](/images/instalando_alf/topologia_3.PNG)

Agora podemos ver duas novas abas dentro da aba topologia, uma como foi dito é a versão textual e a outra como pode ser visto abaixo, e a versão gráfica da topologia.

![Carregando Biblioteca](/images/instalando_alf/topologia_4.PNG)

## Carregando os Canais

Agora selecione a aba canais e veremos a tela abaixo, clique no botão e carregue o arquivo e carregue o arquivo `canais.can`, os arquivos de configuração de canais tem a extensão `can`.
 
![Carregando Biblioteca](/images/instalando_alf/canais_1.png)

A carga dos canais é bem mais lenta, porque é bastante complexa sua leitura, já que a topologia é desmembrada na composição descrita pela biblioteca, cada nó da topologia vira um conjunto de componentes/equipamentos.

DA mesma forma que em topologia, há duas novas abas uma para canais apresentado de forma hierárquica em uma arvore e a outra em forma de gráfico.

![Carregando Biblioteca](/images/instalando_alf/canais_3.png)

Já na aba gráfica os canais podem ser vistos em parte, é preciso rolar a tela para ver toda a imagem, é normal que os componentes fiquem vibrando, isto acontece porque o software tenta manter o gráfico organizado, para evitar que isso aconteça, aperte a tecla *F7*.

![Carregando Biblioteca](/images/instalando_alf/canais_4.png)

##Gerenciando a Rede.

Pronto o Alf está funcionando, na próxima atualização deste artigo descrevo como inserir falhas na rede, e como analisar tais erros descobrindo quem é o possível causador, e também como inserir um causador e descobrir os erros gerados e por sua vez descobrir quem poderiam ser os causadores.



