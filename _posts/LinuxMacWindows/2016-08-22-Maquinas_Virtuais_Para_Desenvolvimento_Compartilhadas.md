Instalar o Vagrant não é um trabalho dificil, mas não é somente o que está publicado no site original.


No windows, instale primeiro o [GIT](https://git-scm.com/downloads) através deste link, ele é preciso para uso do SSH, você pode também usar o [WinSCP](https://winscp.net/eng/download.php), mas com certeza se já pretendo usar o GIT este será a melhor escolha.

Agora instale o [Vagrant](https://www.vagrantup.com/downloads.html) usando o link sugerido.

Agora instale o [Virtual Box](https://www.virtualbox.org/wiki/Downloads), o Vagrant vai precisar dele pra executar as maquinas virtuais.

Para finalizar instale o [Paker](https://www.packer.io/downloads.html) uma ferramenta que irá lhe ajudar a gerar suas Box para compartilhas com outros desenvolvedores de seu projeto e amigos.

Não entrarei em detalhes no processo de instalação porque todos são muito simples, basta fazer a famosa instalação "Next, Next, Next", se souber o que está fazendo pode mudar alguns parâmetros para personalizar sua instalação, mas para a primeira tentativa sugiro que mantenha o padrão.

No caso do VirtualBox se estiver usando o Windows, certifique-se que o Hiper-V não esteja instalado e ativo, ele irá impedir que o VirtualBox use o VT-X, se receber alguma mensagem relativa a falta deste recurso basta verificar se o Hiper-V está instalado através da ferramenta "Recursos do Windows", e se estiver, remova, se precisar dela, terá que ter outra instalação do Windows para que possa usar as maquinas virtuais, isso não é um problema do Vagrant ou do VirtualBox, mas do Hiper-V.

Bem, agora que tudo está pronto vamos fazer nosso primeiro teste com o Vagrant, eu preparei uma maquina Virtual, baseada no Ubuntu para meus testes, ela é baseada na máquina Virtual `hashicorp\precise64`, e você pode usa-la sem problemas, diferença do meu box é que ela está atualizada para o Ubuntu 14.04.15 LTS.

Caso queira usar a versão do box `hashicorp\precise64` tera que seguir as instruções da seção abaixo [Instalando Hashicorp\precise64](#instalando_hashicorp_precise64).





## Instalando Hasicorp\precise64

Para instalar a versão do box `hashicorp\precise64` é preciso algumas atualizações, depois de instalado como descrito assima as ferramentas e inicializado sua pasta de projeto, substitua as referencias ao meu box `carlosdelfino\first-box` pela referencia `ahshicorp\precise64`.

quando estiver já logado no sistema via ssha com o comando `vagrant ssh` rode o seguinte comando para atualizar o VirtualBox:

```
sudo apt-get install virtualbox-guest-additions-iso
```

Este comando vai instalar a versão mais atual do VBox Quest.


