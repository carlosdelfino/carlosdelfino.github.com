---
title: "Um Primeiro código, Hello World, Usando C no Eclipse com CDT e Cygwin"
tags: [C, C++, Compilador, GCC Explorer, GCC, Navegador, Tempo Real, Aprendizado, ARM, Parallella, Epiphany, ARM64, AVR, x86, PowerPC, CygWin, Pelles C, Visual Studio, Borland, Borland C++, Visual C, Visual C++, IDE, Eclipse, Compilação, Hello World]
category: [programacao, Cplusplus]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
tagcloud: true
donate:
 show: true
 coinbase:
  show: true
 flattr:
  show: true 
---
Usar o Eclipse para programar em C e C++ não é difícil, porém não é uma tarefa para iniciantes, mas tentarei torna-la um pouco mais fácil com esta postagem.

<!--more-->

Para compilar softwares em **C** e **C++** no **Windows** é necessário instalar um compilador, o que no **Linux** se faz com poucos comandos, no **Windows** também é possível, mas não é uma tarefa nativa.

Para isso usaremos o **CygWin** um excelente pacote de ferramentas Linux migradas para o **Windows**, com o **CygWin** você pode ter quase tudo que há no **Linux** no **Windows**.

E em seguida considerando que você já instalou o **Eclipse**, sugiro o **Eclipse Neon** para **C++** que já vem com o **CDT**, *plugin* para programação em C e C++, veja que o **Eclipse** é uma **IDE** bastante customizada, totalmente personalizável, que nos permite instalar milhares de *plugins* para que ela se comporte o mais próximo de nossa necessidade. Visite o site http://eclipse.org e baixe o instalador do Eclipse e ao executá-lo selecione instalar o **Eclipse Neon Cpp**.

## Instalando o CygWin

Como já foi dito o **Cygwin** é uma ferramenta para se instalar outras ferramentas disponíveis nativamente apenas para linux, mas o Cygwin nos fez todo o trabalho para porta tais ferramentas para o **Windows**, permitindo assim termos em uma linha de comando tudo que poderíamos ter no Linux, de forma praticamente transparente.

Viste o site oficial do **Cygwin** http://www.cygwin.com e baixe o arquivo Setup para sua plataforma **Windows**, veja há dois arquivos para cada versão, uma para **Windows 32bits** e outro para **Windows 64bits**, procure usar o correto, apesar da versão para **Windows** 32 bits funcionar também no **Windows 64bits**.

Ao executar o arquivo `setup.exe` que você baixou, ele irá fazer algumas perguntas como:
* Se desejar instalar da internet ou se já tem os arquivos de instalação localmente, é bem provavel que não tenha estes arquivos localmente, então escolha da internet, vá em frente clicando em "Avançar".
* Agora você é questionado em qual diretório deseja instalar o **CygWin**, escolha `c:\cygwin` ou outro drive que tenha espaço suficiente, considere pelo menos 5GB, e evite usar espaços e caminhos longos, o ideal é o sugerido, informe também se a instalação é para todos os usuários do computador ou apenas para você. Continue em Frente clicando em "Avançar".
* Em qual diretório você deseja guardar os arquivos fontes baixados da internet, este arquivos são os pacotes que serão usados, e não precisaram estar sempre disponível, apenas quando desejar reinstalar ou instalar algo novo, pode ser em qualquer drive, eu normalmente escolho `c:\cygwin-downloads`, este diretório pode ser backup ou removido depois da instalação. Continue com "Avançar"
* Deixa a opção como está, neste tela foi perguntado se deseja usar um proxy, normalmente a conexão é direta, você saberá se precisa mudar esta configuração, siga clicando em ^Avançar".
* Agora você verá uma lista dos servidores *mirros* onde os pacotes podem ser baixados, sugiro que use um Brasileiro, mas a muito não vejo universidades brasileiras sendo *mirros* do **CygWin**, a academia está perdendo o foco no que se refere ao software livre? talvez, mas selecione então americano como "ftp://lug.mtu.edu" e para continuar, clique em "Avançar"

Você verá nesta tela o Setup baixando o arquivo de listagens dos pacotes disponíveis neste servidor, isso não demora muito. Pronto uma nova tela é exibida com a lista dos pacotes que você pode instalar, veja abaixo quais pacotes instalar.

Sugiro que escolha os seguintes pacotes, o próprio **CygWin** irá selecionar as dependências para nós, portanto não se preocupe com muitos detalhes, apenes selecione os principais, na caixa de pesquisa digite os nomes sugeridos abaixo, e marque para que fique com o status "keep" ou o número da versão sugerida, a maioria dos pacotes estarão na pasta **DEVEL**, quando contrário informo:

* **GCC**, selecione os pacotes "**cygwin32-gcc-core**", "**cygwin32-gcc-g++**", "**gcc-core**", "**gcc-g++**", "**mingwin64-i686-gcc-core**", "**mingwin64-i686-gcc-g++**", , "**mingwin64-x86-gcc-core**", "**mingwin64-x86-gcc-g++**", na pasta "**libs**" selecione o pacote "**libgcc1**";
* **GDB**, selecione o pacote "**gdb**"
* **AutoMake**, selecione todas as opções que comecem com **automake**

Pronto, mantenha os demais pacotes como sugerido, e clique em "*Avançar*". Na próxima tela será apresentado um resumo da instalação, basta manter tudo como sugerido, e clicar novamente em "*Avançar*".

Uma vez o download os pacotes e a instalação tenha terminado, podemos continuar com o Eclipse, o download pode demorar um pouco, deixe ele prosseguir naturalmente, se precisar parar, basta repetir todos os passos, o mais importante é selecionar o mesmo servidor, assim evitará que sejam baixados os mesmos pacotes novamente. ao terminar o download e instalação basta clicar em "*Concluir*" na tela final, você pode nesta hora selecionar as caixas para que sejam criados atalhos para a área de trabalho e para o menu, fica a seu critério.

## Preparando o ambiente em especial a variável "Path" do windows

Como muito já sabem o ambiente do **Windows**, possui uma variável chamada "`Path`" que informa onde os programas devem ser executados para que via linha de comando consigamos achá-los sem ter que digitar o caminho completo, então edite as configurações de seu **Windows**, indo na tela de edição das "**Variáveis de Sistema**", ache o "`Path`" e edite adicionado a seguinte entrada:

> C:\cygwin\bin

Feche a tela clicando em "Ok", veja que usei o diretório que eu instalei o meu **Cygwin**, se escolheu outro diretório lembre-se de ajustar para sua instalação.

Se o Download e instalação do **Cygwin** já terminou você deve reiniciar seu computador.

## Criando meu primeiro projeto com o C ou C++ no Eclipse

Pronto agora que o cygwin já está instalado e tudo configurado já podemos usar os comandos do Linux no Windows, experimente usar o comando `ls -l` e verá o resultado como no Linux, até o comando para listar processo `ps -a`por exemplo, e por ai vai.

Mas o que queremos mesmo é criar nossos próprios códigos em C usando o Eclipse, e o GCC, vamos então a configuração do Eclipse.

Lembre-se estou considerando que você já baixo o instalador do Eclipse Neon, do site http://www.eclipse.org, e que já fez a seleção pelo **Eclipse Cpp**, que já vem com o plugin CDT instalado, faça assim que tudo dará certinho. Não irei neste *post* entrar em detalhes de como instalar o **CDT** no Eclipse, mas é bem simples.

Se quiser tentar instalar o plugin numa instalação extra, instale os plugins:

* Autotools support for CDT (Incubation)
* C/C++ Development Tools
* CDT Visual C++ Support


Sendo assim você já tem tudo atualizado e não precisa se preocupar com nenhum detalhe extra. Abra agora o Eclipse, 

Abra o Menu, *File (Arquivo)* > *New (Novo)* > *C++ Project (Projeto C++)*.

Veja que em parenteses estão os nomes em português do menu, os símbolos de ">" Maior Que, representam o menu mais interno.

Na nova janela que se abrir, digite o nome de seu projeto no campo "Project Name", pode ser algo como "Meu Projeto 1" ou mesmo "Demolidor 1", você escolhe o nome,não use símbolos no nome.

Abaixo você deve escolher o tipo de projeto, "*Project Type*", então escolha "*Hello World Ansi C Project*" (Projeto Hello World ANSI C), e na caixa a direita, "ToolChains", escolha "CygWin GCC".

Clique no botão "Next", na nova janela preencha os campos com seus dados, continue clicando em "Next", 

Pronto o projeto já está quase pronto, vamos agora selecionar as bibliotecas que usaremos para compilar este novo projeto, clique com o botão direito no nome de seu projeto e selecione a opção "*Properties*", siga a arvore de opções, *C/C++ General* > *Paths and Symbols* > *Includes* > *GNU C++*.

Click no botão "Add" (Adicionar), e digite os caminhos abaixo se eles não existirem ainda:


* C:/cygwin/lib/gcc/i686-pc-cygwin/5.4.0/include/c++
* C:/cygwin/lib/gcc/i686-pc-cygwin/5.4.0/include/c++/i686-pc-cygwin
* C:/cygwin/lib/gcc/i686-pc-cygwin/5.4.0/include/c++/backward
* C:/cygwin/lib/gcc/i686-pc-cygwin/5.4.0/include
* C:/cygwin/lib/gcc/i686-pc-cygwin/5.4.0/include-fixed
* C:/cygwin/usr/include

**OBS**, verifique a versão que instalou e corrija o caminho para que fique correto, no meu caso estou com a versão 5.4.0, talvez você pegue versões superiores, então corrija o número da versão, não se esqueça também que eu instalei em c:/cygwin, se você instalou em outro diretório faça o ajuste, então agora basta clicar em "*Apply*" > "*OK*".

Pronto agora você já pode clicar sobre o nome do projeto, clicar com o botão direito e selecionar "Build Project", o projeto será construido, compilado e linkado para a plataforma selecionada, que no caso foi PC, ou seja para o Windows, será criado uma pasta "Debug", ou "Release", entre nesta pasta e verá seu executável lá dentro, clique com o botão direito sobre ele, e selecione "Run AS" > "Local C/C++ Application"


## Conclusão

Por hora atingimos nosso objetivo, conseguimos executar um programa em C no Eclipse, agora você já pode praticar códigos mais avançados e substituir a ideia que usa da Faculdade (como o **Pelles C**) e já dar um passo mais profissional, e se já usava outra IDE profissional como o **Visual Studio** ou **Borland C+**+, já está livre da pi ratária e mais próximo do universo de código aberto.