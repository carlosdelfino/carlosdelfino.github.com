---
title: Fork no GIT Hub para propor novos recurso ou correções
excerpt: "Como fazer uma nova proposta de recurso ou correção no GITHub através de um FORK do projeto original"
category: [extra]
tags: [git, github, fork, push, pull, pull request, recursos, correções, procedimento, programação]
layout: article
comments: true
share: true
ads:
 show: true
toc: true
feature:
 index: true
 category: true
image:
 feature: logica_programacao/arm-nucleus-1200-677.jpg
 teaser: logica_programacao/chip-arm-A15-390x250.jpg
 credit: Juergen Jagst
 creditlink: http://community.arm.com/groups/processors/blog?start=15
tagcloud: true
---

Sempre que desejar propor novos recursos e correções para um projeto no GITHub
use a seguinte tática:

 1. Faça um fork do projeto em sua conta.
 1. Faça o clone do novo Fork em sua estação de trablaho, este clone será enviado ao servidor sempre que fizer "git push origin novo-recurso"
 1. Adicione como um novo repositorio remoto o repositório original, "git remote add https://github.com/coder/originalrepository oldrepository", neste comando "coder" é o nome do usuário, "originalrepository é nome do repositório original que deu origem ao fork, e "oldrepository" é o nome que será usado quanod desejar atualizar o código e branchs com o comando "pull" fazendo um merge dos novos releases relativos ao original.
 1. Agora crie um novo branch com o comando "git checkout -b mynewfeature", o nome do novo branch deve ser bem relevante conforme o novo recurso ou correção, tente manter um branch para cada recurso/correção, evite misturar muitas alterações em um único branch.
 1. Adicione as novas alterações e faça o commit "git commit -a", lembre-se descreva adequadamente o novo recurso/correção, use a primeira linha da descrição como título
 1. Envie o commit para o servidor informando o novo branch "git push origin mynewfeature", veja você deve enviar para seu fork a nova alteração
 1. Agora no site do GITHub faça um novo PullRequest informando o seu novo Branch como sendo a origem.

