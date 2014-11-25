---
title: Preparando Seu Ambiente Para Programar Com ARM
excerpt: Neste artigo vou apresentar os passos que segui para ter sucesso na montagem de meu ambiente de desenvolvimento com o ARM, em especial, usando a placa de aprendizado, SAM4S Xplained.
tags: [ARM, SAM4, SAM4S, Xplained, ATmel, Programação, Assembly, Assembler, Eclipse, IDE, GCC, GNU, None-EABI, EABI, Protótipos, Curso, Hello World ARM, Hello World Arduino, Arduino Zero, Arduino DUE]
layout: article
categories: [helloworldarm]
comments: true
share: true
feature: 
  index: true
  category: true
ads: 
 show: true
toc: true
image:
  teaser: helloworldarm/SAM4SxPlained-255x180.png
  feature: helloworldarm/SAM4SxPlained-400x280.jpg
  credit: Carlos Delfino 
  creditlink: /sobre_min/
imagebase: "/images/helloworldarm/"
google:
  plusone: true
---

O primeiro passo para deixar seu ambiente preparado para programar com microcontroladores 
ARM em especial a familia de Microcontroladores Cortex-M, considerando que você 
já compreende os principais conceitos envolvidos nesta arquiteutra, é instalar 
3 ferramentas principais:

 * [GCC ARM None EABI]();
 * [Eclipse  com CDT]();
 * [GNU ARM Eclipse Plugin]();

Em cada um dos passos listados acima você verá que existem outros passos relativos,
e iremos rever alguns conceitos e informações que são importantes no momento para   
se ter sucesso, como a instalação do pacote XDF-ASF da ATMel que irá compor nossos 
projetos ARM.

Claro para se ter sucesso no uso total dos recursos instalados você irá precisar 
algo mais que um Arduino DUE ou Arduino Zero, já que para efetuar depuração dos 
códigos você precisará de uma placa de apoio a depuração como  JTag entre outros. 

## A Placa de Prototipação 

O Arduino DUE poderia ser a opção para nosso estudo, ou um Arduino Zero, mas
ambos não possuem recurso para depuração, sendo necessário portanto um hardware de 
apoio a depuração para que possamos avançar adequadamente. Mesmo o Arduino DUE
sendo hoje uma das melhores opções para quem deseja iniciar no mundo ARM/Cotext-M.

Eu estarei usando a [SAM4S Explained](http://www.atmel.com/tools/sam4s-xpld.aspx), 
uma pequena e muito poderosa placa para estudos e aprendizado sobre Arquitetura
Cortex-M e a Fámilia SAM4 da ATmel, já que vem equipada com um Cortex-M4, produzido 
pela ATMel, um SAM4S16C, veja [neste link o datasheet](http://www.atmel.com/images/atmel-11100-32-bit-cortex-m4-microcontroller_datasheet.pdf)
deste microcontrolador. Não se assuste com o tamanho do arquivo, realmente é muita 
informação para quem está iniciando, mas com o tempo será façilmente assimilada.

Além do SAM4S, há também o apoio de um outro microcontrolador o SAM3U4C que roda 
o Software JLink para executar a tarefa do depurador. 

<figure>
<img src="{{ site.url }}/images/helloworldarm/SAM4SxPlained-400x280.jpg" />
<figcaption>SAM4S XPlained, uma placa de introdução e aprendizado sobre
o mundo Cortex-M da ATMel</figcaption>
</figure>

Bem vamos a instalação.

## GCC ARM None EABI

o `GCC ARM None EABI` é um toolchain baseado no GCC, ou seja um conjunto de 
ferramentas que permite compilar códigos em C para microcontroladores ARM 
observando as normas `EABI` para construção e organização do código gerado 
em assembly. Além disso este compilador é do tipo `Bare-Metal`, ou seja gera 
código para ser excutado diretamente no microcontrolador sem ajuda de um 
sistema operacional, por isso a presença do termo `none`, já que o código 
gerado não é nem para Linux, Windows, MAC e etc.


### Fazendo o Download do GCC ARM

Antes de iniciar a instalação, claro, você deve ter que fazer o download da 
ferramenta GCC para ARM, e esta deve ser obtida clicando em um dos links 
abaixo, se um dos links apresentar problemas por favor nos avise:

 * [GCC ARM None EABI para Windows](https://launchpad.net/gcc-arm-embedded/4.8/4.8-2014-q3-update/+download/gcc-arm-none-eabi-4_8-2014q3-20140805-win32.exe)
 * [GCC ARM None EABI para Linux](https://launchpad.net/gcc-arm-embedded/4.8/4.8-2014-q3-update/+download/gcc-arm-none-eabi-4_8-2014q3-20140805-linux.tar.bz2)
 * [GCC ARM None EABI para MAC](https://launchpad.net/gcc-arm-embedded/4.8/4.8-2014-q3-update/+download/gcc-arm-none-eabi-4_8-2014q3-20140805-mac.tar.bz2)

### Instalando o GCC ARM
 
Depois de feito o download, basta descompactar o arquivo e copia-lo em uma 
pasta que será sua pasta de trabalho, eu irei usar paths referentes à minha 
instalação que é em um MAC OS X, porém se estiver usando o Windows, basta
muar o path para a pasta q	ue você escolheu.

**Atenção**: Evite usar espaços nos nomes de diretório e também de arquivos.
{: .notice-warning }

No meu caso o path onde foi instalado o GCC ARM foi: 
`/usr/local/gcc-arm-none-eabi-4_8-2014q3/`,
se preferir você pode criar um link para a pasta usando um nome curto para o diretório
ou renomear o diretório como preferir.

**Atenção**: Evite colocar este diretório em seu path do SO, evitando assim conflito
de versões do GCC caso precise usar mais de uma versão.

## Eclipse com CDT

Da mesma forma que você precisou fazer o downloado do GCC, terá que fazer do 
Eclipse, como para o GCC também há vários releases do Eclipse conforme o sistema
operacional usado e também conforme recursos que desejamos, no nosso caso e 
estaremos usando o Eclipse Luna, este deverá vir já com o plugin CDT, e abaixo 
estão os links prontos para que você escolha conforme seu sistema operacional.

Veja no Caso do Eclipse você deve escolher se deseja usar a versão 32Bits ou 
64Bits conforme o sistema operacional adotado.

 * [Eclipse Luna + CDT para Windows 32 Bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-win32.zip)
 * [Eclipse Luna + CDT para Windows 64 bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-win32-x86_64.zip)
 * [Eclipse Luna + CDT para MAC OS X 32 Bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-macosx-cocoa.tar.gz)
 * [Eclipse Luna + CDT para MAC OS X 64 Bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-macosx-cocoa-x86_64.tar.gz)
 * [Eclipse Luna + CDT para Linux 32 Bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-linux-gtk.tar.gz)
 * [Eclipse Luna + CDT para Linux 64 Bits](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/SR1-RC3/eclipse-cpp-luna-SR1-RC3-linux-gtk-x86_64.tar.gz)
 
**Atenção**: se perceber pequenas diferenças nas imagens deste tutorial com sua tela
    não se assuste, estou usando o [Eclipse Luna Automotive](https://www.eclipse.org/downloads/packages/eclipse-ide-automotive-software-developers-includes-incubating-components/lunasr1). uma versão do Eclipse Luna
    para uso em desenvolvimento de soluções ligadas ao campo de Automação veicular.
{: .notice-success }

### Instalando o Eclipse 

A Instalaçãodo Eclipse é bem simples, seja qual for o release, basta descompactar 
o diretório, no meu caso optei em gravar na seguinte pasta: `/Application/IDE/Eclipse/Luna/Automotive`

Os próximos passos são executados com o eclipse, basta executar o arquivo `eclipse`
que está dentro da pasta descompactada. 

### Certificando que o Plugin para C/C++ está instalado

Agora que o Eclipse já está funcionando, o procedimento de teste é bem simples,
tecle a sequência [CTRL]+[N], e você deve ver uma tela similar a apresentada na
imagem abaixo:

<figure>
<img alt="Testando se o ambiente está pronto para iniciar instalações, criando um projeto C/C++" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 1.png">
<figcaption>Testando se o ambiente está pronto para iniciar instalações, criando um projeto C/C++</figcaption>
</figure>

Selecione na arvore de opções do wizard, um projeto do tipo C++, a opção certa 
é `C++ Project`.

Então será apresentada uma tela como segue:

<figure>
<img alt="Escolha agora o template que deseja usar, para este este teste, sugiro ir direto ao template 'Hello World C++ Project'" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 2.png"> 
<figcaption>Escolha agora o template que deseja usar, para este este teste, sugiro ir direto ao template 'Hello World C++ Project'</figcaption>
</figure>

Nas telas a seguir apenas precione `next` até a janela que te pergunta pelo 
caminho do GCC, ainda não iremos compilar um código, então apenas escreva
GCC e clique em nexto, já que e não faremos nada além de criar este 
'Hello World', sem compila-lo, explicarei porque no final desta seção.

<figure>
<img alt="Aqui você pode escrever informações relativas a licença de seu projeto, nome do autor, e qual texto será usado para teste do 'Hello World'" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 3.png"> 
<figcaption>Aqui você pode escrever informações relativas a licença de seu projeto, nome do autor, e qual texto será usado para teste do 'Hello World'</figcaption>
</figure>

<figure>
<img alt="Nesta janela você pode escolher as formas de compilação disponibilizada com referência pelo Eclipse CDT, Debug e Release, em um artigo futuro iremos discutir sobre isso." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 4.png"> 
<figcaption>Nesta janela você pode escolher as formas de compilação disponibilizada com referência pelo Eclipse CDT, Debug e Release, em um artigo futuro iremos discutir sobre isso.</figcaption>
</figure>

<figure>
<img alt="Nesta janela você pode escolher as formas de compilação disponibilizada com referência pelo Eclipse CDT, Debug e Release, em um artigo futuro iremos discutir sobre isso." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 4.png"> 
<figcaption>Nesta janela você pode escolher as formas de compilação disponibilizada com referência pelo Eclipse CDT, Debug e Release, em um artigo futuro iremos discutir sobre isso.</figcaption>
</figure>

<figure>
<img alt="Aqui você deve espessificar o prefixo do seu compilador, por enquando deixe em branco, e o caminho também." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 5.png"> 
<figcaption>Aqui você deve espessificar o prefixo do seu compilador, por enquando deixe em branco, e o caminho também.</figcaption>
</figure>


E para finalizar a criação, o Eclpse poderá lhe será perguntado se quer mudar de 
pespectiva, já que o Eclipse pode ser usado para várias linguagens e tarefas, 
como gerenciar seu projeto de código, ele terá diversas pespectiva que lhe 
apresentam janelas e recursos, e neste momento iremos usar a pespectiva para 
C/C++, respondendo sim ele mudará isso para você automáticamente.

Pronto nosso primeiro teste está pronto, nosso objetivo aqui é compilar códigos 
para uso com o microcontroladores ARM, e não iremos testar este código agora, já
que para compila-lo teriamos que instalar e configurar um ToolChain para seu 
ambiente especificamente, aumentando este tutorial, mais ainda. 

Veja na janela abaixo o resultado final esperado:

<figure>
<img alt="Nosso primeiro projeto de teste criado com o Eclipse, como não informamos um prefixo nem um path para o GCC ele irá usar o padrão de seu sistema operacional, se ouver." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 7.png"> 
<figcaption>Nosso primeiro projeto de teste criado com o Eclipse, como não informamos um prefixo nem um path para o GCC ele irá usar o padrão de seu sistema operacional, se ouver.</figcaption>
</figure>

No meu caso tenho no path do sistema operacional um GCC padrão, então ele 
automáticamente encontrou o GCC e seu Toolchain, e identificou a biblioteca
padrão que será usada para compilar nosso código, mas não se preocupe agora,
em ter sucesso em compilar um código, apenas certifique-se que o projeto foi 
criado corretamente, talvez ele se queixe de erros no seu código se não achou 
o GCC padrão, o que neste caso é perfeitamente aceitável.

Veja nesta janela que ao lado esquerdo temos a arvore do diretório, nesta janela
pode vir a ter uma pasta chamada `Include`, ela somente aparece se o compilador
foi identificado corretamente e se há includes para seu projeto, portanto logo
que criar seu projeto ela deve aparecer com as bibliotecas padrões de seu compilador.

Já no meio, temos um arquivo aberto que é o código fonte do exemplo criado, e do 
lado direito temos a janela `Outline`, que contém a estrutura do código fonte
em evidência na janela de arquivos abertos.

Esta é a perspectiva padrão para códigos em C/C++, e você poderá muda-la ou criar
novas perpectivas como desejar.

Vamos agora ao próximo passo dentro do que interessa neste tutorial.

## GNU ARM Eclipse Plugin

Agora que temos o Eclipse CDT funcionando corretamente no que é necessário para 
este passo, vamos instalar o GNU ARM Eclipse Plugin, o plugin que irá nos dar 
recursos básicos e facilitadores para lidar com o desenvolvimento para 
MicroControladores ARM, depuração com JLink ou OCD.

Lembrando que este plugin é somente para a arquitetura ARM, e pode atender no
desenvolvimento com o Arduino DUE e Arduino Zero, porém outros Arduinos baseados
na arquiteutra AVR, deverão usar outro plugin, e poderão compartilhar este ambiente.
Em proximo post eu irei relatar como fazer a instalação do Plugin AVR para Eclipse.

### Instalando o GNU ARM Eclipse Plugin

A instalação do GNU ARM Eclipse Plugin é muito simples, copie o link: 
`http://gnuarmeclipse.sourceforge.net/updates` e cole na janela de atualização
que deve ser acessada visitano o menu `help -> install new software`, veja
nas imagens abaixo:

<figure>
<img alt="Selecionando o menu de instalação de novos Softwares" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 8.png">
<figcaption>Selecionando o menu de instalação de novos Softwares.</figcaption>
</figure>

Cole o link `http://gnuarmeclipse.sourceforge.net/updates` na caixa de texto,
`work with:` e tecle enter então será feito o download das versões disponíveis,
e apresentado uma lista para selção, selecione o conjunto `GNU ARM C/C++ Cross Development Tools`
e precione o botão `next`.
<figure>
<img alt="Tela de instalação de atualizações e novos plugins" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 9.png">
<figcaption>Tela de instalação de atualizações e novos plugins.</figcaption>
</figure>

A seguir lhe será dado detalhes sobre o que será instalado em seu ambiente,
click `next` novamente. 
<figure>
<img alt="Tela apresentando detalhes do que será instalado" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 10.png">
<figcaption>Tela apresentando detalhes do que será instalado.</figcaption>
</figure>

Em seguida confirme a aceitando os termos de licença, basta selecionar o primeiro
item da lista, que agrupa todos os demais e selecionar o botão de seleção 
`I accept the terms of the license agreement`, que está no canto inferior direito
da janela, acima dos botões de controle, clique no botão `Finish` para finalizar 
a instalação.
<figure>
<img alt="Tela que solicita o aceite dos termos de licença" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 11.png">
<figcaption>Tela que solicita o aceite dos termos de licença.</figcaption>
</figure>

Ao terminar esta instalação, o Eclipse irá lhe solicitar que reinicialize a 
interface. Observe que este processo pode demorar alguns minutos conforme
a velocidade de sua internet.

<figure>
<img alt="Arquivos sendo baixados" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 12.png">
<figcaption>Arquivos sendo baixados.</figcaption>
</figure>

Caso seja questionado pelo fato dos softwares não serem autenticados/assinados, 
confirme clicando em OK, veja a tela abaixo.

<figure>
<img alt="Confirmando autenticidade do pacote" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 13.png">
<figcaption>Confirmando autenticidade do pacote.</figcaption>
</figure>

Pronto, tudo deve correr como citado acima, sem nada a mais ou a menos, 
portanto seu ambiente já está pronto para que possa criar seu primeiro projeto.

Mas antes, como iremos trabalhar focados no CMSIS e no XDK-ASF (Atmel) precisamos
instala-los, veja como proceder nas próximas seções comentadas a baixo.
 
### Instalando pacotes CMSIS

Vamos instalar o Pacote CMSIS conforme oferecido pelo Plugin ARM GNU Eclipse,
veja que este pacote é na verdade oferecido pela  KEIL que é a ferramenta
divulgada oficialmente pela ARM Ltd. como sendo sua indicação para queme deseja
trabalhar com Processadores e Microcontroladores ARM.

Para aprender mais sobre a interface de desenvolvimento e outros produtos da KEIL
visite o link [http://www.keil.com/product/](http://www.keil.com/product/).

Inclusive há um plugin da KEIL para usar o  MDK-ARM e uVision com Eclipse, se 
deseja usar tais ferramentas veja mais detlahes no link: 
[http://www.keil.com/support/man/docs/ecluv/ecluv_install.htm](http://www.keil.com/support/man/docs/ecluv/ecluv_install.htm), 
já que não pretendemos focar nesta ferramenta 

A isntalação do pacote CMSIS com o ARM Gu Eclipse é feita clicando no icone destacado
na imagema baixo:

<figure>
<img alt="Abrindo a pespectiva de instalação de pacotes do CMSIS" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 14.png">
<figcaption>Abrindo a pespectiva de instalação de pacotes do CMSIS.</figcaption>
</figure>

Ao abrir pela primeira vez a pespectiva irá parecer estar vazia, já que ainda
não existe nenhum pacote disponível para instalação, para baixar as definições
de pacote é preciso atualiza-los clicando no botão atualizar, conforme é destacado
na imagem abaixo.
<figure>
<img alt="Atualizando as definições disponíveis." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 15.png">
<figcaption>Atualizando as definições disponíveis.</figcaption>
</figure>

Uma vez solicitado a atualização das definições e pacotes CMSIS, você verá 
na barra do rodapé do Eclipse quantos porcento faltam para finalizar, e na
janela um pouco acima, verá quantos pacotes já foram baixados, veja a imagem
abaixo. 
<figure>
<img alt="Baixando os pacotes, andamento do processo." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 16.png">
<figcaption>Baixando os pacotes, andamento do processo.</figcaption>
</figure>

O download dos pacotes pode levar de 1 a vários minutos dependendo de sua internet
veja a imagem abaixo como ficará a lista de pacotes depois de terminado o download.
<figure>
<img alt="Como ficará a lista de pacotes depois de terminado o Download." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 18.png">
<figcaption>Como ficará a lista de pacotes depois de terminado o Download.</figcaption>
</figure>

Agora selecione na arvore de pacotes a coleção da ATmel, e na janela ao lado 
selecione o pacote `SAM4 DFP`, clique no icone acima de um pacote com a setinha
para baixo, conforme sinalizado na imagem.
<figure>
<img alt="Baixando o pacote SAM4 DFP para ATmel." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 19.png">
<figcaption>Baixando o pacote SAM4 DFP para ATmel.</figcaption>
</figure>

Você pode ver que há uma aba, para as placas de prototipagem, infelizmente a 
SAM4S Xplained somente tem a versão profissional, mas vale a pena baixar
e estudar seu uso.
<figure>
<img alt="A aba Boards." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 20.png">
<figcaption>A aba Boards.</figcaption>
</figure>

Pronto, agora iremos instalar o pacote XDK-ASF para estudos e teste. 
Este é o último passo neste tutorial, uma vez terminado, iremos 
trabalhar outro tutorial demonstrando como criar um projeto com base
nesta instalação.

### Instalando o pacote XDK-ASF da ATMel

O pacote XDK-ASF é um pacote genérico da ATmel que contem tudo que você precisa 
para começar a desenvolver com os microcontroladores sejam eles ARM ou AVR. 
Portanto ele lhe será útil tanto com a linha SAM3 usada no Arduino DUE, como na 
linha ATMega e ATtiny usada no Arduino UNO e outras variações.

Maiores informações sobre o pacote XDK-ASF pode ser obtido no link
[http://www.atmel.com/tools/AVRSOFTWAREFRAMEWORK.aspx](http://www.atmel.com/tools/AVRSOFTWAREFRAMEWORK.aspx).

No link a seguir você pode fazer o download direto do pacote XDK-ASF, porém 
pode lhe ser solicitado que preencha um pequeno formulário, com seu nome,
email e outros dados, preencha os dados e receberá um novo link para download.
{: .notice-success }


[Para download do pacote clique aqui.](http://www.atmel.com/images/asf-standalone-archive-3.19.0.95.zip) 
{: .notice-success }

Depois de feito o download do pacote, basta descompacta-lo no próprio workspace, 
se desejar crie um projeto geral para no Eclipse para este pacote, mas não é uma
boa ideia, já que é um pacote muito grande e pode a indexão se tornar pouco eficiente.

Agora que tudo está pronto, no proximo artigo demonstro como criar um projeto 
baseado no exemplo do QTouch para o SAM4S Xplained e como depura-lo.
**Aguarde**, postarei o link aqui assim que estiver pronto.
{: .notice-success } 

## Criando um projeto ARM para testar sua instalação.

Após tudo instalado, você irá perguntar, onde eu configuro o GCC e digo qual
usar se não o coloquei no Path do meu Sistema Operacional?

Bem, você irá informar a cada vez que criar um novo projeto qual GCC pretente
usar, não se preocupe. 

Digite a sequência [CTRL]+[N] para que possa abrir a janela de novo projeto.

A primeira vista nada mudou, você terá a listagem de projetos, escolha
criar um `C++ Project` como antes.

<figure>
<img alt="Criando meu primeiro projeto ARM C/C++" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 1.png">
<figcaption>Criando meu primeiro projeto ARM C/C++.</figcaption>
</figure>

Em seguida digite o nome que deseja dar ao projeto, e escolha na lista
o projeto do tipo `Hello World ARM C++ Project`, você verá que somente
um toolchain está disponível, o `Cross ARM GCC`.

<figure>
<img alt="Dando nome e selecionando o tipo e toolchain para o projeto ARM C/C++" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 21.png">
<figcaption>Dando nome e selecionando o tipo e toolchain para o projeto ARM C/C++.</figcaption>
</figure>

Abaixo segue imagens na sequência para criar o projeto e o resultado obtido,
veja que neste exemplo a última imagem mostra o código em assembly, não entrarei
em detalhes aqui como é o procedimento para obtenção deste código, isso será feito
no próximo artigo.

<figure>
<img alt="Informações delicensiamento e configuraçòes iniciais da compilação, não mexa no último campo." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 22.png">
<figcaption>Informações delicensiamento e configuraçòes iniciais da compilação, não mexa no último campo.</figcaption>
</figure>

<figure>
<img alt="Nomes de configurações de referência." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 23.png">
<figcaption>Nomes de configurações de referência.</figcaption>
</figure>

<figure>
<img alt="Nomes de configurações de referência." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 23.png">
<figcaption>Nomes de configurações de referência.</figcaption>
</figure>

Agora você deve selecionar o nome do toolchain usado, isso irá impactar na 
construção do path para acesso das ferramentas de compilação.

Selecione `GNU Tools for ARM Embbedded Processors (arm-none-eabi-gcc)`.
<figure>
<img alt="Seleção do prefixo do Toolchain." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 24.png">
<figcaption>Seleção do prefixo do Toolchain.</figcaption>
</figure>

Digite o caminho onde foi instalado/descompacto o toolchain, como explicado acima.

<figure>
<img alt="caminho do Toolchain." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 25.png">
<figcaption>Camiho do Toolchain.</figcaption>
</figure>

<figure>
<img alt="Resultado final esperado" src="{{ site.url }}/images/instalacaoambiente/Captura de tela 26.png">
<figcaption>Projeto criado, resultado final esperado.</figcaption>
</figure>

Após a primeira compilação já temos alguns arquivos interessantes, veja que
tenho acesso ao código assembly do projeto, porém ainda não fizemos a configuração
necessária para gerar tal arquivo, isso somente será explicado no próximo artigo,
é um processo simples, mas não queremos deixar este artigo maior ainda.

<figure>
<img alt="Resultado final já com arquivo do código assembly gerado." src="{{ site.url }}/images/instalacaoambiente/Captura de tela 27.png">
<figcaption>Resultado final já com arquivo do código assembly gerado.</figcaption>
</figure>


## Um video de todo este processo

**Aguarde**, postarei o link aqui assim que estiver pronto.
{: .notice-warning } 

## O que aprender agora?

 * [Programando e Aprendendo Sem Ter Um ARM](/helloworldarm/Programando_e_Aprendo_Sem_Ter_Um_ARM/)
 

