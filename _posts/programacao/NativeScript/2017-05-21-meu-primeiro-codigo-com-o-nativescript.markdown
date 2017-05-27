---
title: "Meu Primeiro Código Com o NativeScript"
date: "2017-05-09 09:16:18 -0300"
tags: [NativeScript, JavaScript, TypeScript, Angular, CSS, Mobile, Android, iOS, Programação, Telerik]
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
 teaser: programacao/nativescript/NativeScript_logo.png
 feature: programacao/nativescript/NativeScript_logo_1800x600.png
---

Veremos aqui como criar nossa primeira aplicação usando o NativeScript. Lembre-se para ter sucesso nestes passos, você precisar ter o NodeJS instalado e acessível.

<!--more-->

**Atenção** Artigo em construção.
{: .notice }

Veja no [artigo anterior como instalar o NativeScript]({% post_url programacao/NativeScript/2017-05-06-o_que_e_nativescript_e_por_onde_comecar %}#primeiros-passos) e os [prerequisitos de conhecimento]({% post_url programacao/NativeScript/2017-05-06-o_que_e_nativescript_e_por_onde_comecar %}#a-instalação).

Vamos lá então. Primeiro entenda que sempre que falamos do cliente NativeScript, estamos falando do comando `tns`, este nome foi escolhido por representar *T* elerik *N* ative *S* cript.

Entáo vamos criar um projeto básico para acostumarmos a usar o comando. Digite então:

```
tns create HelloWorld
```

Será criado então uma pasta chamada HelloWorld com tudo que é necessário para seu primeiro projeto.

Mas veja, desta forma a pasta não contem um layout específico para uma determinar linguagem, sendo o JavaScript o padrão, para escolher se deseja programar especificamente em  TypeScript você pode usar a diretiva `--tsc` para que ele adicione os módulos necessários através do template respectivo., e caso queira usar o Angular você deve informar a diretiva `--ng`. Usando estas diretivas você precisa ter internet disponível para baixar os templates do GitHub na primeira vez que or usado, veremos mais detalhes sobre templates no post "[criar seu próprio template para uso em projetos futuros]({% post_url programacao/NativeScript/2017-05-24-criando_seu_proprio_template_nativescript %})".

Veja, apesar de atualmente todos terem sempre internet a disposição, pode haver casos onde não se tenha internet sempre ou de boa qualidade, então você pode vir a querer baixar um template e deixa-lo disponível em um diretório para usar sempre que desejar. Veremos no post citado acima como usarmos estes templates de modo offline.

Veja  o resultado do comando sem nenhuma diretiva extra:
```
$ tns create HelloWorld
|
> nativescript-dev-android-snapshot@0.0.9 postinstall /Users/extracbd/workspace/nativescript/EstudosDelfino/HelloWorld/node_modules/nativescript-dev-android-snapshot
> node postinstall.js

nativescript-theme-core@1.0.4 HelloWorld/node_modules/nativescript-theme-core

nativescript-dev-android-snapshot@0.0.9 HelloWorld/node_modules/nativescript-dev-android-snapshot
├── semver@5.3.0
├── adm-zip@0.4.7
├── shelljs@0.6.1
└── nativescript-hook@0.2.1 (mkdirp@0.5.1, glob@6.0.4)
Project HelloWorld was successfully created.

$
```
Vamos entrar no diretório e listar seu conteúdo para entendermos a estrutura de diretórios de uma aplicação desenvolvido com NativeScript, isso é muito importante para sucesso no desenvolvimento:

```
$ cd HelloWorld
$ ls -lha
total 8
drwxr-xr-x   7 extracbd  staff   238B 10 Mai  2017 .
drwxr-xr-x   6 extracbd  staff   204B 10 Mai  2017 ..
drwxr-xr-x  11 extracbd  staff   374B 10 Mai  2017 app
drwxr-xr-x   4 extracbd  staff   136B 10 Mai  2017 hooks
drwxr-xr-x   6 extracbd  staff   204B 10 Mai  2017 node_modules
-rw-r--r--   1 extracbd  staff   430B 10 Mai  2017 package.json
drwxr-xr-x   2 extracbd  staff    68B 10 Mai  2017 platforms
$
```
Todos os diretóriso criados sáo visiveis e não havendo diretorios ou arquivos  ocultos pelo {NS}.

#### APP

No diretório "app" fica armazenado seu código nativescript, recursos especificos de cada plataforma que são de responsabilidade do desenvolver manter, em especial o diretório `App_Ressources` que possui um diretório para cada plataforma e conteúdo bem pecular a cada uma delas.

Assim que terminar de ler este post, não deixe de se aprofundar na estrutura  deste diretório, lendo o post [Entendendo o Diretório "app" no {NS}]({% post_url programacao/NativeScript/2017-05-22-entendendo_o_diretorio_app_no_nativescript %}).

Neste diretório você irá encontrar o código oferecido pelo template escolhido, como usamos o comando `tns create` sem informar um template, foi utilizado o template padrão "HelloWorld", neste template há o extritamente necessário para executar um código escrito em JavaScript que exige o Logo do NativeScript.

Você deverá extender este códio para desenvolver então sua aplicação.

#### hooks

Outro diretório importante é o  "hooks", que  será descrito em detalhes no post [Entendendo o diretório "hooks"]({% post_url programacao/NativeScript/2017-05-22-entendendo_o_diretorio_hooks_no_nativescript %})

Inicialmente neste diretório são oferecidos dois scripts, um de preparação do projeto e outro que executa após a compilação e tais scripts são referentes ao Android, sendo instalado devido o pacote nativescript-dev-android-snapshot ou simplesmente android-=snapshot.

Para mais detalhes deste plugin, leia o post [O que faz o Android Snapshot]({% post_url programacao/NativeScript/2017-05-22-oque_faz_o_adroid_snapshot %})

#### node_modules

já o diretório "node_modules" é criado conforme a necessidade inicial de módulos de seu template, e irá conter todos os módulos demandos pelo template e tema mesma funcionalidade quando usado em projetos com NodeJS. Quando na criação do projeto, é carregados os modulos sugeridos pelo arquivo `package.json` do template.

Para detalhes sobre esta pasta, veja o artigo "[Como funcionao mecanismos de módulos do {NS}]({% post_url programacao/NativeScript/2017-05-24-como_funciona_o_mecanismo_de_modulos_no_nativescript %})"".

#### platforms
E finalmente durante o processo de criação, temos o diretório "platforms" que é criado vazio, onde é adicionado as bibliotecas, runtime e informações relevantes a cada plataforma de desenvolvimento.

Na primeira tentativa de construir o projeto (compilar) conforme a pltaforma informada, este diretorio será populado, ou atualizado o framework da plataforma escolhida no momento da construção, havendo assim um diretório para cada plataforma com seu respectivo nome.

#### package.json
E para finalizar esta faze de criação, o arquivo package.json que é criado com base no pacote de mesmo nome oferecido pelo template, usando as diretivas `dependencies` e `devDependencies` para popular o diretório `node_modules` citado acima.

Já os demais parametros personalizaveis conforme o projeto devem ser infromados pelo programador.
* description
* license
* readme
* repository

O parâmetro `nativescript.id` deve ser alterado assim que for definido um ID para sua aplicação, procure usar o mesmo ID de forma defintiva, pois ele irá ajudar a identificar sua aplicação durante todo o ciclo de vida, tanto no desenvolvimento como no mercado.

No que se reere a novos recursos, posteriormente veremos como adicionar novas dependências (modulos e plugins) para nosso projeto, sem ter que editar diretamente o projeto.

Como foi citado acima as dependências tanto de compilação como execução são inciialmente definidas pelo template, mas podemos fazer pequenas mudançãs para outras versõs caso o template tenha cido criado numa versão mais antiga que atualmente usada.

Depois da primeira tentativa de compilar o projeto, outros diretórios podem vir a ser criados como por exemplo `lib` que conterá bibliotecas relativas ao `iOS`

## Executando o primeiro aplicativo

Mesmo ainda não tendo nada codificado, podemos testar a execução de nosso projeto em um dispositivo emulado ou não.

Na primeira execução é preciso ter a internet disponível, ou já ter executado alguma outra tentaiva de executar algum exemplo conectado a internet, pois {NS} (NativeScript) irá fazer o donwload de módulos que não foram baixados juntos com o template em especial os módulos relativos a plataforma.

Como foi citado na [descrição do arquivo package.json](package.json) podemos informar uma versão de forma estática ou para ser usado sempre a última versão disponível, assim, esta poderá sempre atualizada quando o projeto for reconstruído ou atualizado.

### Executando com Android

```
$ tns run android --emulator
```

Ao executar pela primeira vez o comando, será carregado novos módulos em sua aplicação e configurados no arquivo `package.json`, abaixo temos a saída inicial da execução comando e carga dos arquivos e dependências, veja que apenas os pacotes princiapis são adicionados e as dependências são automaticamente aferidas como de costume:

```
Copying template files...
  ◜ Installing tns-androidbabel-traverse@6.24.1 node_modules/babel-traverse
├── babel-messages@6.23.0
├── globals@9.17.0
├── babylon@6.17.1
├── debug@2.6.6 (ms@0.7.3)
├── babel-types@6.24.1 (to-fast-properties@1.0.3, esutils@2.0.2)
├── lodash@4.17.4
├── invariant@2.2.2 (loose-envify@1.3.1)
├── babel-runtime@6.23.0 (regenerator-runtime@0.10.5, core-js@2.4.1)
└── babel-code-frame@6.22.0 (js-tokens@3.0.1, esutils@2.0.2, chalk@1.1.3)
  ◜ Installing tns-androidbabel-types@6.24.1 node_modules/babel-types
├── to-fast-properties@1.0.3
├── esutils@2.0.2
├── lodash@4.17.4
└── babel-runtime@6.23.0 (regenerator-runtime@0.10.5, core-js@2.4.1)
  ◟ Installing tns-androidbabylon@6.17.1 node_modules/babylon
  ◝ Installing tns-androidlazy@1.0.11 node_modules/lazy
Project successfully created.
```
Estas novas dependências que foram adicionadas são apenas necessárais durante o processo de desenvolvimento e construção da aplicação para Android, portanto elas são adicionadas como `devDependencies`:

```
"devDependencies": {
    "babel-traverse": "6.24.1",
    "babel-types": "6.24.1",
    "babylon": "6.17.1",
    "lazy": "1.0.11",
    "nativescript-dev-android-snapshot": "^0.*.*"
 }
```

### Executando com iOS

Vejamos agora o mesmo código sendo executado no iOS, lembre-se que para tal teste vc deve estar desenvolvendo em um MAC, já que as ferramentas de desenvolvimento para iOS como o xCode somente são compátiveis com MacOSx.

Para isso basta digitar o comando abaixo:

```
$ tns run ios
Copying template files...
Project successfully created.
```
a unica mudança realizada no projeto do HelloWorld é a adição da pasta `libs`.

## Conclusão

Agora podemos partir para um passo mais aprofundado, vamos [estudar a estrutura e conteudo da pasta `app`]({% post_url programacao/NativeScript/2017-05-22-entendendo_o_diretorio_app_no_nativescript %}) e depois fazer algumas mudanças nos códigos em direção aos nossos objetivos de aplicação.

## Fontes

* Documentação do NativeScript
