---
layout: post
title: Entendendo o Diretório "app"
date: "2017-05-24 21:56:59 -0300"
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
Precisamos compreender bem dois diretórios que compõem nosso projeto, além da estrutura como um todo. Veremos neste post o diretório *app* que contem nosso código e parametros importantes para cada plataforma.

<!--more-->
Como vimos no [post anterior]({% post_url programacao/NativeScript/2017-05-21-meu-primeiro-codigo-com-o-nativescript %}) todo o projeto em NativeScript possui uma estrutura muito bem definida, que pode ser visto na listagem abaixo:

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
Veremos agora especificamente o diretorio `app` onde fica armazenado seu código e outros parâmetros de sua aplicação, seja qual for sua plataforma principal para desenvolvimento.

Além disso iremos entender um pouco mais do arquivo `package.json` e de conceitos de template, este será aprofundado no post "[criando seu próprio template para uso em projetos futuros]({% post_url programacao/NativeScript/2017-05-24-criando_seu_proprio_template_nativescript %})".

Vejamos o que temos dentro do diretório `app`:

```
$ ls -lha
total 64
drwxr-xr-x  11 extracbd  staff   374B 21 Mai 15:10 .
drwxr-xr-x   7 extracbd  staff   238B 21 Mai 17:57 ..
drwxr-xr-x   4 extracbd  staff   136B 21 Mai 15:10 App_Resources
-rw-r--r--   1 extracbd  staff   662B 21 Mai 15:10 app.css
-rw-r--r--   1 extracbd  staff   445B 21 Mai 15:10 app.js
-rw-r--r--   1 extracbd  staff   242B 21 Mai 15:10 bundle-config.js
-rw-r--r--   1 extracbd  staff   1,5K 21 Mai 15:10 main-page.js
-rw-r--r--   1 extracbd  staff   1,6K 21 Mai 15:10 main-page.xml
-rw-r--r--   1 extracbd  staff   592B 21 Mai 15:10 main-view-model.js
-rw-r--r--   1 extracbd  staff   798B 21 Mai 15:10 package.json
-rw-r--r--   1 extracbd  staff   164B 21 Mai 15:10 references.d.ts
```

#### App_Resources
O primeiro subdiretório que vemos é o diretório `App_Resources`, diretório responsável por manter arquivos específicos de cada palataforma, este diretório é dividido em outros subdiretórios conforme a plataforma, nas versões atuais do NativeScript suportam `Android` e `iOS`.

Cada uma destas subpastas conterá arquivos específicos da palataforma, como imagens específicas para densidade do display, diretórios e arquivos de parametrização conforme modelos e versão dos dispositivos.

Veremos mais detalhes de cada subpasta, quando formos tratar especificamente de cada plataforma. Por hora, é importante salientar que é preciso mante-las atualizadas de forma sincronizada com imagens/figuras e parâmetros equivalentes a cada uma delas. Tire um tempo e passeei pelos subdiretórios de cada plataforma.

#### package.json

Você já deve ter percebido que há dois arquivos `package.json`, um na raiz de seu projeto e outro neste diretório (`app`).

O primeiro foi criado com base no `package.json` oferecido pelo template, porém aproveitando apenas as diretivas `dependencies`e `devDependencies`, todas as demais diretivas devem ser populadas pelo desenvolvedor.

já o segundo, que está presente no diretório `app` deve ser mantido como está, e não pode ser alterado, ele é um espelho do original oferecido pelo template e vem acrescido de dois novos parametros:
* `_id`, que é o *id* original do template.
* `_from`, que é o *id* de origem da atual aplicação.

Não iremos intervir nestes arquivos, veja mais detalhes no post que ensina a criar um projeto do zero ou que trata com detalhes tal arquivo.

#### app.js

As aplicações no NativeScript, como em outras, precisa ter um ponto de inicio, e é essa a função do arquivo `app.js`, veja que a estenção é para indicar que estamos usando a linguagem *JavaScript*, veremos mais detalhes em outros posts para a Linguagem *TypeScript* e para uso do *Angular*.

Neste arquivo você pode parametrizar sua aplicação, carregar módulos em segundo plano e outras costumizações, mas o mais importante a ser feito é que sua ultima ação seja passar o controle ao módulo principa de sua aplicação.

Veja que cada módulo identificado pelo nome de seu arquivo principal. Vejamos a seguir como são nomeados os módulos.

##### A Composição dos nomes de módulos.

Vamos ver agora rapidamente como identificar os módulos de uma aplicação, e como fazer referência a eles dentro de seu código. Para detalhes e estudo mais aprofundado desta metodologia de nomear arquivos leia o post [Nomeando Módulos e a Especificação CommonJS]({% post_url programacao/JavaScript/2017-05-29-nomeando_modulos_e_a_especidicacao_commonjs %})

##### Importando um módulo.

Como o NativeScript é construido sobre o NodeJS, usamosos mesmos recursos para importar um módulo como é usado no JavaScript, seguindo a especificação [CommonJS specification](http://wiki.commonjs.org/wiki/CommonJS), para mais detalhes veja o post [Nomeando Módulos e a Especificação CommonJS]({% post_url programacao/JavaScript/2017-05-29-nomeando_modulos_e_a_especidicacao_commonjs %}).



**Atenção** Artigo sendo escrito.
{: .notice }
