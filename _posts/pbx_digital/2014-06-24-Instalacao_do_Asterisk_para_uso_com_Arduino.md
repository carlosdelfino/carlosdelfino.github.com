---
title: Instalação do Asterisk para uso com Arduino
excerpt: Como instalar o Asterisk e configura-lo para usar com Arduino
keywords: Asterisk, Arduino, PBX, PABX, PBX Virtual, PBX Digital
layout: article
share: true
toc: true
comments: true
feature:
 index: true
 category: true
ads: 
 show: true
coinbase:
  show: true
image:
  teaser: pbx_digital/asterisk-255x180.png
  feature: pbx_digital/asterisk-640x359.png
  credit: Asterisk
  creditlink: http://www.asterisk.org/
category: PBX_Digital
---
Antes de começarmos é importante lembrar que Asterisk foi desenvolvido para o SO Linux, porém há ports para outros SOs como FreeBSD, MACOSX e até para Windows, mas o mais interessante e o fato de haver ports para que possa ser usado com RaspberryPI e até para Beagle Bone.

Para instalar o Asterisk é preciso seguir alguns passos, dentre eles você deve primeiro fazer o Download dos seguintes pacotes, para isso crie uma pasta por exemplo chamada “/usr/src/asterisk”, ou outro local que achar mais indicado em sua instalação Linux. (sim iremos nos basear no Linux, já que o Asterisk roda bem melhor nesta SO), observe neste tutorial estarei usando o Ubuntu em sua última versão.

Use os seguintes comandos para baixar os pacotes:

{% highlight bash linenos=table %}
wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-11-current.tar.gz
wget http://downloads/asterisk.org/pub/telephony/libpri/libpri-1.4.current.tar.gz
wget http://downloads/asterisk.org/pub/telephony/libss7/libss7-1.0.2.tar.gz
wget http://downloads/asterisk.org/pub/telephony/dahdi-linux/dahdi-tools/dahdi-tools-current.tar.gz
wget http://downloads/asterisk.org/pub/telephony/dahdi-linux/dahdi-linux/dahdi-linux-current.tar.gz
wget http://openr2.googlecode.com/files/openr2-1.3.3.tar.gz
{% endhighlight %}
Agora que baixou os pacotes descompacte cada um e certifique-se que as pastas foram criadas conforme o nome de cada arquivo.

## Compilando os pacotes e instalando

Vamos começar a instalação pelo pacote dahdi-linux-current.tar.gz, portanto entre no diretorio que foi criado ao descompactar este pacote e digite os seguintes comandos em cada linha:

{% highlight bash linenos=table %}
make clean
make
make install
{% endhighlight %}

O próximo pacote deve ser o dahdi-tools-current.tar.gz, siga o mesmo procedimento mudando para o diretório criado com a descompactação e em seguida digite os comandos no diretório

{% highlight bash linenos=table %}
make clean
./configure
make
make install
{% endhighlight %}

Continuarmos o mesmo procedimento agora no pacote libpri-1.4.current.tar.gz, digitando os seguintes comandos em cada linha:

{% highlight bash linenos=table %}
make
make install
{% endhighlight %}

Agora compilamos o pacote openr2-1.3.1-tar.gz, Este pacote não necessário ao nosso Workshop, porém mantive sua instalação para divulgação, já que se o usuário vier a desejar integrar seu Asterisk aos sistema telefônico Brasileiro irá precisar desta biblioteca de sinalização.

Descompacte como os anteriores entre no diretório criado e digite os comandos em cada linha, este pacote não será necessário em nosso workshop, já que seu uso é para quem pretende ter linha E1 em seu ambiente:

{% highlight bash linenos=table %}
./configure --prefix=/usr
make
make install
{% endhighlight %}

O pacote libss7-1.0.2.tar.gz para terminar os prequistos manuais, seguindo também os mesmo procedimentos:

{% highlight bash linenos=table %}
make clean
make
make install
{% endhighlight %}

E finalmente o próprio Asterisk que não tem segredos na instalação sendo necessário os seguintes comandos, obseve que ao digitar o comando “make menuselect” você pode sair dele sem mudar nenhuma seleção, porém se quiser arriscar (experimentando) ou sabe exatamente o que faz, pode mudar as seleções para atender suas necessidades:

{% highlight bash linenos=table %}
contrib/scripts/get_ilbc_source.sh
contrib/scripts/get_mp3_source.sh
contrib/scripts/install_prereq
make menuselect
make
make install
make samples
make config
{% endhighlight %} 

Pronto, em tese o Asterisk está pronto e instalado para iniciar nosso workshop.

## Melhorando a Segurança da Instalação
Após a instalação acima, tudo estará configurado para ser executado como Root, porém isso não é uma boa prática, e o ideal é criar um usuário especifico para rodar este processo. 

Para isso inicie criando um usuário e um grupo com os dois comandos abaixo:

{% highlight bash linenos=table %}
adduser --system --home /var/lib/asterisk --no-create-home asterisk
addgroup asterisk
{% endhighlight %}

Não se esqueça de adicionar o usuário “asterisk” ao grupo de mesmo nome que acabou de criar.

Agora mude o proprietários e grupo das pastas relativas ao Asterisk usando o comando abaixo:

{% highlight bash linenos=table %}
chown -R asterisk:asterisk /var/lib/asterisk \
                           /var/log/asterisk \
                           /var/run/asterisk \
                           /var/spool/asterisk
{% endhighlight %}

A pasta de configuração no diretório “etc” deve ter o proprietário como sendo o “root” porém o grupo deve ser “asterisk”, permitindo assim que membros deste grupo possam acessa-la:

{% highlight bash linenos=table %}
chown -R root:asterisk /etc/asterisk/
{% endhighlight %}

Agora ajuste os direitos de acesso assim todos os proprietários poderão acessar livremente as respectivas pastas, o grupo poderá lê-las sem problemas, e os demais usuários ficaram sem acesso:

{% highlight bash linenos=table %}
chmod -R u=rwX,g=rX,o= /var/lib/asterisk \
                       /var/log/asterisk \
                       /var/run/asterisk \
                       /var/spool/asterisk \
                       /etc/asterisk
{% endhighlight %}

Agora para finalizar estas configurações, entre no diretório “/etc/default/” e edite o arquivo asterisk, neste arquivos estão os parâmetros padrões para inicialização automática do Asterisk no linux. Procure as duas linhas que se refere respectivamente ao usuário e grupo e mude o nome destes para os nomes criados nos comandos acima.

Finalmente reinicialize ou inicialize o Asterisk usando o comando:

{% highlight bash linenos=table %}
service asterisk restart
{% endhighlight %}


<a href="/cursoarduino/" class="btn-success">Este trabalho é mantido com os cursos oferecidos no <br />
Curso Arduino Minas!</a>
