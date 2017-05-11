---
title: "Meu Primeiro Código Com o NativeScript"
date: "2017-05-09 09:16:18 -0300"
tags: [NativeScript, JavaScript, TypeScirpt, Angular, CSS, Mobile, Android, iOS, Programação, Telerik]
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

Mas veja que desta forma a pasta não contem um layout específico para uma determinar linguagem, para escolher se deseja programar especificamente em  TypeScript você pode usar a diretiva `--tsc` para que ele adicione os módulos necessários, e caso queira usar o Angular você deve informar a diretiva `--ng`. Usando estas diretivas você precisa ter internet disponível para baixar os layouts do GitHub, veremos mais detalhes sobre Layouts no Artigo "[Criando Seus Próprios Layouts]()".

Veja, apesar de atualmente todos terem sempre internet a disposição, pode haver casos onde não se tenha internet sempre ou de boa qualidade, então você pode vir a querer baixar um template e deixa-lo disponível em um diretório para usar sempre que desejar, ou mesmo [criar seu próprio template para uso em projetos futuros]({% post_url programacao/NativeScript/2017-05-11-criando_seu_proprio_template_nativescript %}). Veremos a frente como usarmos estes templates de modo offline.

Veja abaixo o resultado do comando sem nenhuma diretiva extra:
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

estudio-1:EstudosDelfino extracbd$
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


## Executando o primeiro aplicativo

Mesmo ainda não tendo nada codificado, podemos testar a execução de nosso projeto em um dispositivo.

Na primeira execução é preciso ter a internet disponível, pois {NS} (NativeScript) irá fazer o donwload de módulos que não foram baixados juntos com o template em especial os módulos relativos a plataforma.

Como foi citado na [descrição do arquivo package.json](#descricao-do-arquivo-package.json) podemos informar uma versáo de forma estática ou para ser usado sempre a última versão disponível, assim, esta poderá sempre atualizada quando o projeto for reconstruído ou atualizado.

```
$ tns run ios
Copying template files...
Project successfully created.
```
## Fontes

* Documentação do NativeScript
