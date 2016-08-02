---
title: Introdução as Redes Neurais, Perseptron 
tags: [Redes Neurais, Inteligência Artificial, Inteligência, Artificial, RNN, NN, LTSM, Formulas, Rampa Simetrica, Simetrica, Ativação Lógistica, Hiperbólica, Tangente, Tangente Hiperbólica, Função Logistica, perseptron]
categories: [redesneurais, introducao]
layout: article
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
   teaser: pensamentos/pensamento2-400x200.jpg
   feature: pensamentos/pensamento2-400x200.jpg
math: true
---
Os perceptrons são o tipo de rede neural artificial mais antigo, foi idealizado pelo pesquisador Rosenblatt em 1958, desejava criar um mecnismo de reconhecimento de padrões geometricos inspirado no funcionamento da retina.

<!--more-->

O perceptron é um tipo de rede bem simples composta tipicamente por uma camada, havendo um conjunto de entrada, normalmente função linear, para acoplamento, com a camada interna, já esta camada é do tipo degrau, e finalmente a saida da rede neural é do tipo linear para novo acomplamento.

<figure>
<figcaption>A imagem apresenta um perceptron para resposta do tipo XOR.
<img src="/images/redesneurais/introducao/perceptron-xor.png" />
</figure>

Segue a baixo a tabela da verdade para o perceptron.

| x | y | xor |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

