---
title: Termos usados com Kubernets?
layout: article
tags: [kubernets, google, linux, windows, mac, redes, doker, containers, pods, serviços, ]
categories: [Redes,clouds]
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
   teaser: sdn/sdn2-768x283.jpg
   feature: sdn/sdn-500x259.jpg
---

Dentro do Kubernetes, há alguns termos para determinadas funções:

 * Minions: Nome dado para cada host do cluster;
 * Kubelet: Agente que roda nos hosts do cluster;
 * Pods: A menor unidade dentro de um cluster. Nada mais é do que containers rodando dentro de seu cluster de Kubernetes. Pode ser um container rodando nginx, php, apache etc…
 * Replication Controller: É o responsável por manter um número determinado de pods em execução. No RC é onde você diz quantos containers de nginx, php, apache você desejá que fiquem rodando; caso um caia, o RC cria outra instância automaticamente;
 * Services: É o responsável por atrelar uma faixa de IP para um determinado RC. Para que cada vez que o RC crie uma nova instância de pod, o mesmo inicie com um IP determinado pelo service.
 * Namespace: Com o namespace você pode dividir seu Cluster de Kubernetes em dois ambientes, Produção e Teste, podendo limitar os recursos computacionais para ambos.


## Fontes

* https://imasters.com.br/desenvolvimento/devops/usando-o-kubernetes-como-ferramenta-de-automatizacao-distribuicao-de-carga-monitoramento-e-orquestracao-entre-containers/
