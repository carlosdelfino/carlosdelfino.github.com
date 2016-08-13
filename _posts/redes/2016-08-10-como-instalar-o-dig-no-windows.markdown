---
layout: post
title: "Como Instalar o DIG no Windows"
date: "2016-08-10 17:58:07 -0300"
tags: [dig, dns, bind, dominio, ip, windows, consulta, administração, manutenção, nslookup]
categories: [Redes,Administração de Dominios]
share: true
toc: true
comments: true
feature:
 category: true
 index: true
tagcloud: true
ads:
 show: true
image:
   teaser: pensamentos/pensamento2-400x200.jpg
   feature: pensamentos/pensamento2-400x200.jpg
---
"DIG" vem do inglês *Domain Information Groper* é uma ferramenta de redes de computadores, utilizada para consultas sobre registros de DNS de um determinado domínio, host ou IP.

<!--more-->

Para usar o DIG é muito simples basta digitar `dig seudominio.ou.ip`, ele irá conectar em seu DNS padrão e consultar as informações disponíveis. Caso tenha problema com o DNS padrão, ou quiser testar um DNS especifico, você pode informar o ip do servidor usando **@** por exemplo: `dig carlosdelfino.eti.br @8.8.8.8`, com este comando obtenho informações do meu dominio **carlosdelfino.eti.br** no servidor de DNS do google (8.8.8.8).

Caso não tenha o DIG em seu computador é provavel que seja um coputador com o sistema operacional Windows, ou que não tenha o Bind instalado, é possível instalar o DIG no windows sem instalar o Bind, para isso faça o dowload do bind conforme a versão do seu windows, use um dos links abaixo:

* [Download para Windows 32Bits](https://www.isc.org/downloads/file/bind-9-10-4-p2/?version=win-32-bit)
* [Download para Windows 64Bits](https://www.isc.org/downloads/file/bind-9-10-4-p2/?version=win-64-bit)
* [Download para Windows Xp](https://www.isc.org/downloads/file/bind-9-10-4-p2/?version=win-xp)

Veja, é importante usar a versão correta do seu windows, principalmente se ele não for o XP, não use a versão 32 bits em um windows 64bits, isso se dá pelo fato de ao instalar uma versão 32 bits no widnows de uma ferramenta que irá rodar no prompt de comando ele tentará rodar como sendo 64Bits, as versões windows de 64 bits que tentam rodar aplicações 32bits, usam uma abstração especial, deixando a apalicação mais lenta, e no caso de ferramentas como o DIG ele irá buscar os executaveis de tais versões 32 bits na pasta SysWOW64 dentro do diretório de instalação do windows, o significado do nome **SysWOW64** é arquivos de *Sistemas* (System) do Windows (32bits) no Windows 64, do inglês ***System Windows (32bits) on Windows 64bits***.

Agora que você fez o download do pacote correto do BIND, descopacte este pacote uma pasta temporária, não exeucte nenhum programa ainda, apenas descompacte.

Em seguida copie os seguintes arquivos para a pasta **system32** de seu windows, lembre-se você precisa de ter previlégios de administrador para fazer isso.

* dig.exe
* host.exe
* libbind9.dll
* libdns.dll
* libeay32.dll
* libisc.dll
* libisccfg.dll
* liblwres.dll
* libxml2.dll

Em seguida execute o programa de instalação `vcredist_x64.exe` para a versão 64 bits, ou outro similar para sua versão de forma a instalar o pacote **Microsoft Visual C++ Redistributable**, caso já não esteja instalado a versão 2012. você também pode baixar o [Microsoft Visual C++ Redistributable](http://www.microsoft.com/en-us/download/details.aspx?id=30679#) Clicando neste link.

Pronto seu DIG para windows já está funcional com todos os recursos que encontrária no DIG para o linux, e agora pode diagnosticar e obter informações privilegiadas sobre dominios e ips na internet, veja que este comando não substitui o **Whois**, falaremos dele em outra ocasião.

## Fontes

* http://pt.wikipedia.org/wiki/DiG
* http://www.microsoft.com/en-us/download/details.aspx?id=30679#
* https://blog.paranoidpenguin.net/2014/09/how-to-install-dig-on-a-windows-8-1-64-bit-system/
