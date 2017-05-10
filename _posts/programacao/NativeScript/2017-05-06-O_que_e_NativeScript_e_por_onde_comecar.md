---
title: O que é NativeScript e por onde começar?
tags: [NativeScript, TypeScirpt, Angular, CSS, Mobile, Android, iOS, Programação, Telerik]
category: [programacao, mobile, NativeScript]
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
show: true
image:
 teaser: nativescript/NativeScript_logo.png
 feature: nativescript/NativeScript_logo.png
---

NativeScript, um Framework que permite desenvolver aplicações multiplataforma, como dispositivos moveis, e outros baseados em Android, iOS e futuramente WindowsCE.

<!--more-->

NativeScript é um framework multiplataforma mantido pela Telerik e pela comunidade na Web já que é um framwork OpenSource e gratuito.

Este Framework permite o desenvolvimento de aplicações para dispositivos moveis baseados no Android e iOS, além da promeça futura de vir a ser compativel com o WindowsCE. Outros dispositivos como SmartTV que usem Android podem se beneficiar dos recursos de desenvolvimento do NativeScript.

O NativeScript além de usar XHTML e CSS para enriquecer a interface e a UX, permite, mas não obriga, o desenvolvimento utilizando Angular com total integração ao novo Angular 2, é internamente desenvolvido usando o TypeScript, permitindo o uso desta nova linguagem e também permite o desenvolvimento com JavaScript nativo nas versões modernas.

Umas das grandes vantagens do uso do NativeScript é não ser necessário o uso de WebViews para ter portabilidade em sua aplicação, já que este framework transcompila para JavaScript todo código escrito e por sua vez o compila de forma nativa conforme a plataforma escolhida, dando a aplicação desenvolvida um desempenho máximo.

NativeScript tem também acesso 100% natívo a API da plataforma utilizada, permitindo assim total compatibilidade com frameworks desenvolvidos pelos fabricantes de dispositivos moveis, facilitando ainda o desenvolvimento de novas bibliotecas para os recursos disponíveis nativamente tornando cada vez mais transparente seu uso dentro de sua aplicação.

Quando usando JavaScript é possível aproveitar pacotes disponibilizados via npm, CocoaPods and Gradle de forma transparente, como já se utiliza com Node.js.

Utilizando Angular, o que não é obrigatório, se tem acesso a avançados recursos disponíveis para desenvolvimento Web através do Angular 2.

## A Arquitetura do NativeScript

A Arquitetura do NativeScript é bem simples e pode ser vista na imagem abaixo que é autoesplicativa.

![Arquitetura do NativeScript](/images/nativescript/architecture.png)

## Primeiros Passos

Para dar os primeiros passos com o NativeScript sugerimos usar um dos tutoriais abaixo, um com base em JavaScript puro e outro com Angular. Mas antes siga a instruções apresentadas a seguir para instalar o Frmework em seu ambiente de trabalho.

<div id="start-button-container">
  <a href="http://docs.nativescript.org/angular/tutorial/ng-chapter-0" class="Btn" id="ng-start-button">Get Started with TypeScript & Angular</a>
  <a href="http://docs.nativescript.org/tutorial/chapter-0" class="Btn" id="js-start-button">Get Started with JavaScript</a>
</div>

<script>
  // Quick script to randomize the tutorial button order
  var container = document.getElementById("start-button-container");
  var ngButton = document.getElementById("ng-start-button");
  var jsButton = document.getElementById("js-start-button");

  if (Math.floor(Math.random() * 2) == 0) {
    container.insertBefore(jsButton, ngButton);
    ngButton.style.marginTop = "1em";
    ngButton.style.marginBottom = "1em";
  } else {
    jsButton.style.marginTop = "1em";
    jsButton.style.marginBottom = "1em";
  }
</script>

Sem problema algum você pode optar por desenvolver apenas com TypeScirpt sem o uso do Angular, para isso inicie seu aprendizado com o uso do JavaScript e vá adotando aos poucos o TypeScirpt seguindo a [documentação TypeScript](https://www.nativescript.org/using-typescript-with-nativescript-when-developing-mobile-apps), A escolha do TypeScript é indicada como sendo a melhor, uma vez que o NativeScript internamente é desenvolvido nesta linguagem, outra grande vantagem da escolha do TypeScript se dá a recursos inerentes a própria linguagens como ser fortemente tipada e Orientada a Objetos.


Para desenvolver no NativeScript você já deve ter um conhecimento básico em JavaScript, CSS, A linha de comando através de algum terminal e Shell como o Bash ou Prompt de Comandos do Windows, e algum editor de texto ou preferencialmente uma IDE como o Eclipse ou Atom.

### A instalação

A instalação do NativeScript é muito simples, uma vez que você já tenha o Node.JS instalado e possa facilmente usar a erramenta "NPM", assim basta digitar o comando:

```
$d npm -g install NativeScript
```

Para verificar se está tudo pronto, para começar teste se o comando `tns`, basta digita-lo e dar enter e terá um resultado como o apresentado abaixo, na primeira vez que executar o comando você será questionado se se deseja colaborar com a Telerik autorizando o envio de relatorios de erros de seu ambiente de forma anonima:

```
$ tns
Do you want to help us improve NativeScript by automatically sending anonymous usage statistics? We will not use this information to identify or contact you. You can read our official Privacy Policy at
? http://www.telerik.com/company/privacy-policy Yes
Error reporting will be enabled. You can disable it by running '$ tns error-reporting disable'.
# NativeScript
┌─────────┬────────────────────────────────────────────────────────────────┐
│ Usage   │ Synopsis                                                       │
│ General │ $ tns <Command> [Command Parameters] [--command <Options>]     │
│ Alias   │ $ nativescript <Command> [Command Parameters] [--command       │
│         │ <Options>]                                                     │
└─────────┴────────────────────────────────────────────────────────────────┘

## General Commands
┌───────────────┬───────────────────────────────────────────────────────────┐
│ Command       │ Description                                               │
│ help <Command │ Shows additional information about the commands in this   │
│ >             │ list in the browser.                                      │
│ autocomplete  │ Configures your current command-line completion settings. │
│ usage         │ Configures anonymous usage reporting for the NativeScript │
│ -reporting    │ CLI.                                                      │
│ error         │ Configures anonymous error reporting for the NativeScript │
│ -reporting    │ CLI.                                                      │
│ doctor        │ Checks your system for configuration problems which might │
│               │ prevent the NativeScript CLI from working properly.       │
│ info          │ Displays version information about the NativeScript CLI,  │
│               │ core modules, and runtimes.                               │
└───────────────┴───────────────────────────────────────────────────────────┘

## Project Development Commands
┌───────────────┬───────────────────────────────────────────────────────────┐
│ Command       │ Description                                               │
│ create        │ Creates a new project for native development with         │
│               │ NativeScript.                                             │
│ init          │ Initializes an existing project for native development    │
│               │ with NativeScript.                                        │
│ platform add  │ Configures the current project to target the selected     │
│ <Platform>    │ platform.                                                 │
│ platform list │ Lists all platforms that the project currently targets.   │
│ platform      │ Removes the selected platform from the platforms that the │
│ remove        │ project currently targets. This operation deletes all     │
│ <Platform>    │ platform-specific files and subdirectories from your      │
│               │ project.                                                  │
│ platform      │ Updates the NativeScript runtime for the specified        │
│ update        │ platform.                                                 │
│ <Platform>    │                                                           │
│ prepare       │ Copies relevant content from the app directory to the     │
│ <Platform>    │ subdirectory for the selected target platform to let you  │
│               │ build the project.                                        │
│ build         │ Builds the project for the selected target platform and   │
│ <Platform>    │ produces an application package or an emulator package.   │
│ deploy        │ Deploys the project to a connected physical or virtual    │
│ <Platform>    │ device.                                                   │
│ emulate       │ Deploys the project in the native emulator for the        │
│ <Platform>    │ selected target platform.                                 │
│ run <Platform │ Runs your project on a connected device or in the native  │
│ >             │ emulator, if configured.                                  │
│ debug         │ Debugs your project on a connected physical or virtual    │
│ <Platform>    │ device.                                                   │
│ test init     │ Configures your project for unit testing with a selected  │
│               │ framework.                                                │
│ test          │ Runs the unit tests in your project on a connected        │
│ <Platform>    │ physical or virtual device.                               │
│ install       │ Installs all platforms and dependencies described in the  │
│               │ package.json file in the current directory.               │
│ plugin        │ Lets you manage the plugins for your project.             │
│ livesync      │ Synchronizes the latest changes in your project to        │
│               │ devices.                                                  │
└───────────────┴───────────────────────────────────────────────────────────┘

## Publishing Commands
┌─────────────────┬──────────────────────────────────────────────────┐
│ Command         │ Description                                      │
│ appstore        │ Lists applications registered in iTunes Connect. │
│ appstore upload │ Uploads project to iTunes Connect.               │
└─────────────────┴──────────────────────────────────────────────────┘

## Device Commands
┌─────────────────────┬───────────────────────────────────────────────────┐
│ Command             │ Description                                       │
│ device              │ Lists all recognized connected physical or        │
│                     │ virtual devices.                                  │
│ device log          │ Opens the log stream for the selected device.     │
│ device run          │ Runs the selected application on a connected      │
│                     │ device.                                           │
│ device list         │ Lists the installed applications on all connected │
│ -applications       │ devices.                                          │
└─────────────────────┴───────────────────────────────────────────────────┘

## Global Options
┌───────────────┬───────────────────────────────────────────────────────────┐
│ Option        │ Description                                               │
│ --help, -h, / │ Prints help about the selected command in the console.    │
│ ?             │                                                           │
│ --path        │ Specifies the directory that contains the project. If not │
│ <Directory>   │ set, the project is searched for in the current directory │
│               │ and all directories above it.                             │
│ --version     │ Prints the client version.                                │
│ --log trace   │ Prints a detailed diagnostic log for the execution of the │
│               │ current command.                                          │
└───────────────┴───────────────────────────────────────────────────────────┘
```

**ATENÇÃO:** caso venha a ter algum erro relativo as permissões com o uso do NPM leia este tutorial, escrito em inglês ""[Fixando as permições do NPM](https://docs.npmjs.com/getting-started/fixing-npm-permissions)

Pronto, já está tudo preparado para dar os primeiros passos.

Agora você deve escolher qual plataforma deseja desenvolver, lembrando que iOS é restringido pela Apple para desenvolvimento apenas no MacOSX, sendo assim caso escolha esta plataforma deverá ter um Mac atualizado e preparado para desenvolvimento com xCode atualizado, além das instruções acima.

Caso venha escolher o Android para sua plataforma de desenvolvimento, basta ter a plataforma Android de desenvolvimento instalada com um dispositivo Android Emulado já configurado, Não é obrigatório a instalação do Android Studio, porém ele pode ser útil, e nas instalações novas é a forma mais eficiente para instalar o Android SDK.

### Meu primeiro aplicativo

Para esperimentar o NativeScript na prática sugerimos a leitura dos [tutoriais acima sugeridos](#primeirospassos), mas para ajudar escrevemos um pequeno tutorial que está disponível no [próximo artigo desta série]({% post_url programacao/NativeScript/2017-05-09-meu-primeiro-codigo-com-o-nativescript %}).

## Fontes

* Manuais da Telerik para o NativeScript
