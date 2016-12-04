---
title: Encontrando e Removendo Arquivos e Diretórios Vazios
excerpt: "Quantas vezes não observando que temos milhares de arquivos e diretórios em nosso ambiente de trabalho e não sabemos se há algo útil, veja como achar arquivos vazios"
layout: article
tags: [Linux, CygWin, Windows, Mac]
categories: [LinuxWindowsMac]
ads:
 show: true
comment: true
share: true 
feature:
 index: true
 category: true
image:
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
---

**Atenção**: Este artigo foi obtido no site 
<a href="http://www.dicas-l.com.br/arquivo/find_remocao_de_arquivos_e_diretorios_vazios.php#.VGSyAZOS1xU" >Dicas-L</a>, <br />
e replicado aqui para efeito de arquivo.
{: .notice-warning }


Para remover diretórios e arquivos vazios (tamanho zero) de seu diretório pessoal (ou de qualquer outro lugar), utilize o comando find com as seguintes diretivas:

{% highlight Bash linenos=table %}
  find . -empty
{% endhighlight %}

O comando acima irá localizar tanto arquivos quanto diretórios. Para localizar apenas arquivos, utilize o comando:

{% highlight Bash linenos=table %}
  find . -type f -empty
{% endhighlight %}

Para localizar apenas diretórios:

{% highlight Bash linenos=table %}
  find . -type d -empty
{% endhighlight %}

Para remover os arquivos encontrados:

{% highlight Bash linenos=table %}
  find . -type d -empty | xargs rm
{% endhighlight %}

Para remover os arquivos ou diretórios vazios, apenas no diretório corrente:

{% highlight Bash linenos=table %}
  find . -maxdepth 1 -type d -empty | xargs rmdir
{% endhighlight %}

ou

{% highlight Bash linenos=table %}
  find . -maxdepth 1 -type f -empty | xargs rm
{% endhighlight %}

Lembrando, em sistemas GNU/Linux, um diretório também é um arquivo. Se não 
houver nenhum arquivo ou subdiretório, o arquivo identificador do diretório 
possui tamanho zero e atende aos requisitos de busca ilustrados neste texto.
