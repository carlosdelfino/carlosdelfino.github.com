Todas as variáveis devem ser definidas considerando o diretório de trabalho, 
evite usar caminhos relativos, use sempe caminhos absolutos para apontar os
diretórios evitando assim problemas caso venha a precisar da variável em outro 
diretório.

Abaixo estão as variáveis agrupadas conforme sua necessidade e de forma a apontar
as novas bibliotecas e ferramentas compiladas.

E muito importante setar o `PATH`(caminho) para as ferramentas serem usadas,
procure organiar o `PATH` com os caminhos na ordem que deseja que elas sejam
encontras, evitando conflitos de versões.

{% highlight bash %}
~/ $ PATH=/c/Python27:/c/Python27/DLLs:$PATH
~/ $ PATH=/mingw64/bin/:$PATH
~/ $ PATH=/mingw64/x86_64-w64-mingw32/bin/:$PATH
~/ $ export PATH
{% endhighlight %}

Vamos agora definir o idioma de nosso ambiente, a ferramenta `locale` sem parametros 
nos fornece um conjunto de variáveis que podem definidas para interferir de forma
especifica ou geral na exibição de mensagens, os valores informados são os atuais.

Iremos usar em nosso ambiente o pt_BR como sendo o nosso idioma padrão, e a 
codificação `UTF-8` mas você pode escolher outros sem problemas. Apenas me informe 
caso precise de suporte. Pois poderá ter problemas se fizer uma escolha exotica
em relação aos ambientes comuns. Veja que a variável `LC_ALL` define o idioma e 
condificação para todos os tipos de mensagem.

Abaixo também defini a variável `LINGUAS` para definir os idiomas possíveis para 
o framework `gettext`.

{% highlight bash %}
~/ $ export LC_ALL="pt_BR.UTF-8"
~/ $ export LINGUAS="en pt pt-br"
{% endhighlight %}



{% highlight bash %}
~/ $ export CC=x86_64-w64-mingw32-gcc 
~/ $ export CXX=x86_64-w64-mingw32-g++
~/ $ export LD="x86_64-w64-mingw32-ld" 
~/ $ export NM="x86_64-w64-mingw32-nm" 
~/ $ export AR="x86_64-w64-mingw32-ar" 
~/ $ export RANLIB="x86_64-w64-mingw32-ranlib"
{% endhighlight %}

CROSS_PREFIX=x86_64-w64-mingw32-
 

~/qemu-delfino/ $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/ $ export GLIB_LIBS="-lglib-2.0"
~/qemu-delfino/ $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
~/qemu-delfino/ $ export GLIB_LIBS=""


```sh
~/qemu-delfino/ $  export CFLAGS="-m64 -pipe"

~/qemu-delfino/ $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/ $ export GNULIB_TOOL="~/qemu-delfino/gnulib/gnulib-tool"

~/qemu-delfino/ $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/ $ export GLIB_LIBS="-lglib-2.0"

~/qemu-delfino/ $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"


~/qemu-delfino/ $ export LIBFFI_CFLAGS=`pkg-config.exe libffi --cflags`
~/qemu-delfino/ $ export LIBFFI_LIBS=`pkg-config.exe libffi --libs`


```
```sh
~/qemu-delfino/ $ export CFLAGS="-O0 -g -pipe -Wall -mms-bitfields -mthreads -I/mingw64/include"
~/qemu-delfino/ $ export CPPFLAGS="-DG_ATOMIC_OP_USE_GCC_BUILTINS=1"
~/qemu-delfino/ $ export LDFLAGS="-L/mingw64/lib "

~/qemu-delfino/ $ export LIBFFI_CFLAGS='-I /mingw64/lib/libffi-3.99999/include'
~/qemu-delfino/ $ export LIBFFI_LIBS=-lffi
~/qemu-delfino/ $ export lt_cv_deplibs_check_method="pass_all"
~/qemu-delfino/ $ export LINGUAS="en pt pt-br"
~/qemu-delfino/ $ export GNULIB_SRCDIR="~/qemu-delfino/build/gnulib"  
~/qemu-delfino/ $ export GNULIB_TOOL="~/qemu-delfino/build/gnulib-tool"
```

```sh
~/qemu-delfino/ $ export GNULIB_SRCDIR="~/qemu-delfino/gnulib"  
~/qemu-delfino/ $ export GNULIB_TOOL="~/qemu-delfino/gnulib-tool"
~/qemu-delfino/ $ export GLIB_CFLAGS="-I /mingw64/include/glib-2.0 -I /mingw64/lib/glib-2.0/include"
~/qemu-delfino/ $ export GLIB_LIBS="-lglib-2.0"
~/qemu-delfino/ $ export ZLIB_CFLAGS="-I /mingw64/include/ -I /mingw64/include"
~/qemu-delfino/ $ export GLIB_LIBS=""

~/qemu-delfino/ $ export LIBFFI_CFLAGS=`pkg-config.exe libffi --cflags`
~/qemu-delfino/ $ export LIBFFI_LIBS=`pkg-config.exe libffi --libs`

```


```sh
~/qemu-delfino/ $ export CFLAGS=`sdl2-config --cflags --libs`
```

Ao final da compilação sete o path para enconrar o local onde estalou o QEMU.