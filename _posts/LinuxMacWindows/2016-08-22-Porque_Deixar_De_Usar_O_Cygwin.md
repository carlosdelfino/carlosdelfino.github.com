Por muito tempo o Cygwin foi o conjunto de ferramentas que me ofereceu no Windows algo perto do que eu tinha no Linux. Mas devido a algumas dificuldades tenho analisado outras alternativas.

<!--more-->

Diante de diversas dificuldades no uso do Cygwin com o Ruby, Node.JS e o GCC, resolvi buscar novas opções, em conversas com colegas, todos foram unanimes em dizer que o MinGW é a melhor alternativa no que se refere ao GCC padrão para ser usado no Windows.


E no que se refere ao [Ruby](http://rubyinstaller.org/downloads/) e [Node.JS](https://nodejs.org/en/download/), não há muitos problemas, basta usar as versões adequadas para o windows e fazer a instalação padrão, e claro não deixar de instalar o DevKit do Ruby conforme sugere o site.

Use os links acima para então instalar o Ruby e Node.JS e vamos aproveitar e instalar também o [Python](https://www.python.org/downloads/release/python-2712/) neste link. vamos usar a versão 2.7 pois é a mais compatível existente e sem dúvida é uma excelente escolha.

Não deixe de instalar o [VisualStudio  C++](https://www.visualstudio.com/pt-br/features/cplusplus.aspx), e a versão do [Compilador Visual C++ para Python](https://www.microsoft.com/en-us/download/details.aspx?id=44266).

Então em seguida instale o Ruby DevKit:

```
cd c:\ruby\devkit\
ruby dk.rb init
```

Verificar no arquivo de configuração `config.yml` gerado se sua instalação do Ruby está corretamente identificada e em seguida executar:

```
ruby dk.rb install
```

Você também pode instalar o [RubyOnRails](http://railsinstaller.org/en) se deseja desenvolver aplicações para WEB.




Se por qualquer motivo quiser remover todas as gemas do Ruby e instalar de novo você pode usar o seguinte comando:

```
 ruby -e "`gem list`.split(/$/).each { |line| puts `gem uninstall -Iax #{line.split(' ')[0]}` unless line.strip.empty? }"
```

lembrando que algumas gemas como `JSON`, `BIGDecimal` e `RDoc` não podem ser removidas.

Depois é só começar a instalar tudo instalando primeiro o `Bundler`

```
gem install bundler
```

Em seguida entre em seu projeto onde já há um arquivo `Gemfile` parametrizado e use o comando `bundler install` e faça isso para cada projeto que já tem o `Gemfile` assim terá todas as gemas instaladas e configuradas adequadamente.

Lembre-se de fazer isso do prompt do DOS normalmente. Não use outro tipo de prompt.


Para o Python temos também uma ferramenta para gerenciar pacotes, no caso ela se chama PIP, ela já vem instalada quando usamos as versões superiores a 2.7.9, se por algum motivo não estiver usando esta versão, baixe o arquivo [Get-pip.py](https://bootstrap.pypa.io/get-pip.py) e o execute com o seguinte comando:

```
python get-pip.py
```

E para ter seu ambiente atualizado rode o pip como sugerido abaixo, caso ele não esteja no path, procure ele dentro do diretório `Script` de sua instalação do Python.

```
pip install -U pip setuptools
```

Pode ser que você tenha um erro nesta primeira tentativa, apresentando um stack trace do Python, tente executar o comando mais uma vez, e pode ser que tudo instale corretamente.

Para o Python isso é o suficiente por hora.

Há Não se esqueça de instalar o [GIT](https://git-scm.com/download/win) também. E claro o Eclipse será uma ótima escolha para seu ambiente de desenvolvimento ficar 100% completo. Tem um artigo no meu site que apresenta como instalar o Eclipse e o GCC para uso com ARM Cortex-M.



Vamos instalar também duas ferramenta para que você possa testar seus aplicativos em outras ambientes sem muito stress, então instale o [Virtual Box](https://www.virtualbox.org/wiki/Downloads) e o [Vagrant](https://www.vagrantup.com/downloads.html) esta ferramenta vai lhe ajudar a obter de outros desenvolvedores o ambiente já pronto para seu projeto, ou mesmo você criar o seu para que possa reconstrui-lo sempre que preciso ou compartilhar com colegas.
