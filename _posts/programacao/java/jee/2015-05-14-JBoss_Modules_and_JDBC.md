---
title: "Módulos do JBoss e JDBC" 
tags: [jboss, datasource, jdbc, jee, j2ee, java, MySQL, JBoss EAP, JPA, JDO, Hibernate, Persistencia, módulos, biblioteca, jar, war, ear, deploy]
category: [programacao,java,jee,jboss]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
image:
  feature: programacao/java/jee/jboss-1800x1024.png
  teaser: programacao/java/jee/jboss-300x170.png
  credit: JBoss
  creditlink: http://jboss.org
tagcloud: true
coinbase:
 show: true
--- 

Em muitos projetos para JEE são utilizadas bibliotecas (arquivos JAR) que são 
comuns entre eles, e muitas vezes tais bibliotecas ocupam um espaço 
consideravel e causam uma maior demora para que seja feito o envio do 
arquivo para o servidor. Para evitar tal problema, temos o recurso de módulos.

<!--more-->

Veremos neste artigo como se beneficiar deste recurso inicialmente para a carga
dos drivers JDBC para o banco de dados, permitindo assim que estes drivers 
sejam usados por todos os projetos enviados ao servidor, não importanto se 
são do tipo EAR, WAR ou mesmo apenas JAR (EJB).

# O Container e o ambiente

Este artigo é uma serie de posts que irei apresentar as dificuldades e soluções
que encontrei para usar o JBoss como container de aplicações Java EE.

Estarei usando na maioria das vezes o JBoss 6.3.0 já que este me pareceu 
estável e seguro para meu propósito inicial.

[Mais detalhes sobre meu ambiente, pode ser obtido neste link]({% post_url programacao/java/2015-05-11-Meu_Ambiente_Programacao_Java %})

## Módulos

Bem, o JBoss EAP apresenta um conceito de módulos que facilita a carga das
classes e bibliotecas (Arquivos JAR) no qual o sistema depende para seu 
funcionamento, os módulos não são nada mais do que um agrupamento lógico de 
classes e o gerenciamento de dependências, a vantagem do uso dos módulos é que 
evitamos a carga duplicada da mesma biblioteca em diversos aplicativos, além da 
carga ser feita por demanda, evitando uma sobrecarga da mémoria com módulos que 
não estejam sendo usado por nenhuma aplicação ou serviço. Reduzindo também a 
sobrecarga sobre o classloader já que este fica seguimentado conforme a demanda
dos módulos necessários. 

Neste artigo iremos demonstrar como se beneficiar dos módulos para uso com os
drivers/connectores JDBC, em especial para o My/SQL que pode ser usado em 
diversos projetos, evitando assim que o driver seja carregado disponibilizado 
de forma duplicada.

Uma grande vantagem dos Módulos é que ele cria diversos Classpath e Classloads
em três níveis diferentes, sendo gerenciado de duas formas, estáticos e 
dinâmicos.

## Dinâmicos vs Estáticos

Conforme é feito o deploy (carga/depósito) dos módulos, este podem ser 
definidos como estáticos ou dinâmicos.

Os módulos Estáticos são depositados manualmente na pasta "modules" dentro da
estrutura de instalação do JBoss EAP 6, ´EAP_HOME/modules´ e tem seu nome 
composto conforme a estrutura de diretório que armazena os arquivos "JAR" 
e o arquivo modules.xml, sendo a última pasta a versão do módulo.

Na pasta 'modules', há dois grupos de módulos, os de sistema que incluem todos
os módulos do JBoss, seus serviços e aplicativos nativos, além de suas API, 
estes módulos de sistema ficam na sub-pasta 'system' que deve ser 
mantida sem alterações, a não ser que tenha conhecimentos avançados e esteja 
certo do que está fazendo.

Já o segundo grupo envolve os módulos personalizados ou os módulos de terceiros,
desta forma o administrador do JBoss pode fazer uma homologação previa de cada 
módulo antes de libera-lo e e o instale manualmente como sendo um módulo estático.

Já os módulos dinânicos são carregados de dentro de seus aplicativos quando são
feito a carga para o servidor diretamente. Os módulos dinâmicos são parte das
bibliotecas de seus projetos sejam eles em formato EAR, WAR ou JAR.

# Como construir um módulo Stático

Os módulos estáticos tem um formato que deve ser observado para sua construção.
O mais importante é que não é necessário alterar os arquivos JAR que contem
suas classes para usa-los como módulos státicos.

O primeiro passo é criar a estrutura de diretório que irá conter seu módulo.

_*Veja*_: iremos usar um diretório temporário para construir a estrutura de 
nosso módulo. Então esta estrutura deverá ser copiada integralmente para a 
pasta `EAP_HOME/modules`.

Então em uma pasta temporária qualquer crie uma estrutura de diretório que
represente a estrutura a abaixo:

{% highlight sh %}
   > com/mysql
        /main
{% endhighlight %}

Como pode observar é utilizado uma estrutura similar a de pacote do java.

A estrutura quase sempre é terminada com uma pasta `main´, esta pasta deve
conter os arquivos da versão principal utilizada. Portanto caso seu pacote
tenha mais de uma versão das bibliotecas você deverá criar uma pasta para 
cada versão, vejamos abaixo uma estrutura que irá conter duas versões do
driver mysql:


{% highlight sh %}

    > com/mysql
        /main
        /5.0.8

{% endhighlight %}

{% assign mysqljconnector = site.data.links['mysqljconnector'] %}
Agora vamos copiar o arquivo do MySQL JConnector para a pasta main, [baixe
o pacote do conector do site oficial clicando aqui,
( {{ mysqljconnector.name }}]({{ mysqljconnector.link }}) ).
Usaremos a versão 5.1.35 que é a atual para a data que escrevemos este arquivo.
Caso baixe uma versão mais atual ou inferior, ajuste os nomes dos arquivos para
esta nova versão.

Descompacte o pacote, e copie o arquivo que terá o nome 
`mysql-connector-java-5.1.35-bin.jar` para a sub pasta `main` de seu novo módulo.


{% highlight sh %}

   > com/mysql
        /main
           mysql-connector-java-5.1.35-bin.jar
        /5.0.8

{% endhighlight %}

### Arquivo Module.xml

Vamos agora criar o arquivo descritor do módulo, este arquivo é formatado com 
XML portanto deve serguir as regras de criação de tais arquivos, veja 
o nosso módelo abaixo, para obter mais informações neste formato, vá na 
pasta `docs` de sua instalação do JBoss e entre na subpasta `schemas`, onde
poderá encontrar os arquivos XSD que definem este XML.

{% assign schema_module_xsd = site.data.links['schema_module_xsd'] %}
No link a seguir você pode ter acesso ao XSD na integra para a versão JBoss 
EAP 6.3 [{{ schema_module_xsd.name }}]({{ schema_module_xsd.link }}).

Abaixo está o exemplo que atende as nossas necessidades para o MySQL J/Connector
 gist d4c084202f820b1a4d11 %}

Na linha 2 temos o parametro `name`, este parametro define o nome do pacote, e
deve ser um reflexo da estrutura de diretórios criada para conter os arquivos
sem incluir a última pasta que será referencia a versão (incluindo a padrão, 
`main`). veja que usamos `.` para separar as subpastas, ficando o nome
`com.mysql`.

Da linha 3 até 5, definimos os recursos que devem ser carregados, e o mais
importante é que carregemos o arquivo `JAR` que contem as classes de nosso
driver JDBC.

Já nas linhas 6 até 9, definimos as dependências deste módulo, portanto outros 
módulos conforme os nomes listados aqui devem já estar disponíveis no servidor.

Não se preocupe os requisitos sugeridos, `javax.api` e `javax.transaction.api`
são nativos do jboss, portanto são módulos do sistema.

Bem nosso módulo já está pronto agora você pode escolher a melhor forma de 
enviar esta estrutura ao administrador do JBoss para que ele faça a homologação.
Abaixo está a estrutura que criamos, neste caso temos apenas a versão principal
disponível

{% highlight sh %}
 > com/mysql
        /main
           mysql-connector-java-5.1.35-bin.jar
           module.xml
{% endhighlight %}

### Configurando duas versões de um mesmo módulo

Para se disponíbilizar duas versões, ou `slot` como é chamado pelo _JBoss_, de um 
mesmo módulo, basta criarmos uma nova sub pasta dentro da pasta principal do 
módulo como já citamos, veja abaixo como fica a estrutura.

{% highlight sh %}
 > com/mysql
        /main
           mysql-connector-java-5.1.35-bin.jar
           module.xml
        /5.0.8
           mysql-connector-java-5.0.8-bin.jar
           module.xml
{% endhighlight %}

O arquivo module.xml deve ser ajustado na linha 2 adicionado o parametro `slot`, 
e na linha 4, para a nova versão do arquivo `JAR`. Deixando todos os demais 
dados intactatos. Veja abaixo como deve ficar.

module.xml-exemplo-2-slots
{% gist d4c084202f820b1a4d11  %}


## Registrando o novo Módulo

Agora que o módulo já foi enviado para o administrador homologar e instalar, 
ele deverá recriar esta estrrutura na pasta `EAP_HOME/modules`. E reiniciar o 
servidor.

Neste tutorial iremos considerar apenas o uso do JBoss no modo _standalone_. 
Em breve estaremos publicando um tutorial de como construir um pequeno cluster
de servidores, e faremos alguns artigos complementando o que for necessário
para uso em dóminios.

Como o módulo ainda não é referenciado por nenhum serviço ou aplicação instalada
no JBoss ele não é carregado, portanto nenhuma referência surge nos LOGs.

### Registrando a versão padrão (_main_) do módulo JDBC 

Agora o administrador irá abrir a ferramenta de administração do jboss via 
linha de comando para fazer o registro do novo Módulo como um Driver JDBC, para
isso use o comando abaixo que se encontra na pasta `EAP_HOME/bin`:

{% highlight sh %}
$ jboss-cli.sh
{% endhighlight %}

Assim que o prompt do `jboss-cli` abrir, 

{% highlight sh %}
$ bin/jboss-cli.sh 
You are disconnected at the moment. Type 'connect' to connect to the server or 'help' for the list of supported commands.
[disconnected /]
{% endhighlight %}

digite o comando `connect`, você deverá receber um novo prompt como segue abaixo na linha 3:

{% highlight sh linenos %}
You are disconnected at the moment. Type 'connect' to connect to the server or 'help' for the list of supported commands.
[disconnected /] connect
[standalone@localhost:9999 /] 
{% endhighlight %}

Antes de darmos o próximo passo que seria digitar o comando abaixo no promp da 
ferramenta `jboss-cli`, vamos compreender como é estruturado este comando. 

 driver-jdbc-jboss-cli-standalone-command
{% gist d4c084202f820b1a4d11 %}

Na linha 1 identificamos o `subsystema` que será usado no caso `datasources`, 
separado por uma barra segue a seção que receberá o comando `jdbc-driver`, e 
finalmente separado por dois pontos vem o comando. As barras invertidas são para
dar continuidade na linha com a próxima, já que todo o comando deve ser digitado
em uma única linha. Observe que informamos o nome do driver, usaremos `mysql`.

Na linha 2 continuarmos o comando apenas abrindo o parentes para que possamos 
informar os parâmetros a serem usados na adição do novo jdbc-dirver e na linha 
7 este parentes obrigatoriamente é fechado.

na linha 3 informamos novamente o nome do jdbc-driver através do parametro 
`driver-name`, obrigatóriamente deve ser o mesmo nome informado na linha 1.

Agora na linha 4, informamos o nome do módulo que será usado para obter as
classes e toda a informação necessária, este módulo como definimos acima foi 
chamado de `com.mysql`, e assim que devemos referência-lo no parâmetro 
`driver-module-name`.

Já na linha 5 e 6 informamos as classes usadas pelos drivers, os nomes e seus 
conteúdos são bem sugestivos e fácil de se identificar a aplicação de cada um 
dos parâmetros `driver-xa-datasource-class-name` e `driver-class-name`.


Bem, agora digite no prompt do `jboss-cli` exatamente como acima, ou todo o comando
em uma unica linha sem as barras invertidas.

Você deverá receber de retorno a seguinte resposta da ferramenta:

driver-jdbc-jboss-cli-standalone-command-result
{% gist d4c084202f820b1a4d11  %}

Finalmente depois disso, você já poderá usar o Driver-JDBC ao configurar um 
novo DataSource. Não iremos discutir aqui como fazer a configuração do 
DataSource, em breve publicaremos um artigo descrevendo passo a passo.

### Registrando outro slot do módulo JDBC

Bem como vimos registrar um módulo que seja um Driver-JDB é muito simples,
vejamos agora se for o caso onde demandamos diversas versões do mesmo driver
para cada datasource, assim o comando de registro é muito simples, basta
adicionar um paramtro extra que informa qual slot usar, veja o comando 
ajustado abaixo 

 driver-jdbc-slot-jboss-cli-standalone-command
{% gist d4c084202f820b1a4d11 %}

Na linha 5 está o novo parametro `module-slot` que recebe o valor definido para 
o slot do módulo, conforme registrado acima, `5.0.8`.

Ao executar o comando o resultado será o mesmo:

driver-jdbc-jboss-cli-standalone-command-result
{% gist d4c084202f820b1a4d11  %}

E nos LOGs para ambos os casos também se vé o informe de sucesso da carga do
novo driver:

 driver-jdbc-jboss-cli-standalone-command-result-log
{% gist d4c084202f820b1a4d11 %}

## Próximos passos

Agora que já temos nosso módulo para um novo JDBC-Driver, basta configurar um 
novo DataSource. Não pretendo escrever um artigo sobre este tema, já que é um
processo muito simples de ser feito pela interface web de administração do JBoss.

Mas conforme demanda iremos publicando novos artigos que possam contribuir com 
processo mais delicados e complexo de administração e *deploiment* de aplicações
seja elas, do tipo WAR, EJB/JAR ou EAR.

Na nossa lista está uma versão em portugues do melhor método para se fazer o 
deploy de uma aplicação que dependa do Spring e outros Frameworks como o 
PrimeFaces, utilizando também o conceito de módulos.



## Fontes

 * [Layered Distributions and Module Path Organization](https://developer.jboss.org/wiki/LayeredDistributionsAndModulePathOrganization)
 * [Data Source Configuration in AS 7](https://developer.jboss.org/wiki/DataSourceConfigurationInAS7)
 * [JBoss Modules](https://docs.jboss.org/author/display/MODULES/Introduction)
 * [How To Put An External File In The Classpath](https://developer.jboss.org/wiki/HowToPutAnExternalFileInTheClasspath)
 * [About Modules and the New Modular Class Loading System used in JBoss EAP 6](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/6.3/html/Development_Guide/sect-About_Modules_and_the_New_Modular_Class_Loading_System_used_in_JBoss_EAP_6.html)
 * [Disable Subdeployment Module Isolation for All Deployments](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/6.3/html/Administration_and_Configuration_Guide/Disable_Sub-Deployment_Module_Isolation_for_All_Deployments1.html)
 * [ Install a JDBC Driver as a Core Module](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/6.3/html/Administration_and_Configuration_Guide/Install_a_JDBC_Driver_as_a_Core_Module1.html)
 * [Introduction to the Service Provider InterfacesIntroduction to the Service Provider Interfaces](http://docs.oracle.com/javase/tutorial/sound/SPI-intro.html)
 * [CLI Recipes - Remove Default Datasource and Driver, and so on](https://docs.jboss.org/author/display/AS71/CLI+Recipes#CLIRecipes-RemoveDefaultDatasourceandDriver)
