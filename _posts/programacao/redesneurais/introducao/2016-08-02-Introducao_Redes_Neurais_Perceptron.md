---
title: Introdução as Redes Neurais, Perceptron 
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
Os perceptrons são o tipo de rede neural artificial mais antigo e mais simples, foi idealizado pelo pesquisador Rosenblatt em 1958, ele desejava criar um mecanismo de reconhecimento de padrões geometricos inspirado no funcionamento da retina.

<!--more-->

O perceptron é um tipo de rede bem simples composta tipicamente por uma camada, havendo um conjunto de entrada, normalmente função linear, para acoplamento, com a camada interna, já esta camada é do tipo degrau, e finalmente a saída da rede neural é do tipo linear para novo acomplamento.

O perceptron padrão pode ser descrito pela seguinte equação:

$$
\begin{cases}
   i = \sum_{i=1}^n w_i \; * \; x_i -  \theta \\ 
   y = g(i)
\end{cases}
$$

Uma boa aplicação do perceptron, seria um algortimo de controle de um sistema de irrigação, feito com o arduino, o perceptron pode facilmente ser implementado para rodar em um arduino recebendo sinais do mundo externo via uma ou mais portas analógicas e assim acionando uma porta digital ou mesmo alterando o valor em uma porta pwm.

Veremos num artigo a frente a implementação deste perceptron.

## Uma rede perceptron de dois neurônios

A melhor representação do uso do perceptron é a rede neural do tipo XOR como apresentado abaixo.

<figure>
<figcaption>A imagem apresenta um perceptron para resposta do tipo XOR.</figcaption>
<img src="/images/redesneurais/introducao/perceptron-xor.png" />
</figure>

Segue a baixo a tabela da verdade para o perceptron que símula o XOR.

| x | y | xor |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |


## Onde obter mais informações?


Caso esteja buscando aprender mais e compartilhar conhecimento, participe de nosso grupo no facebook: [Artificial Intelligence and Neural Network](https://www.facebook.com/groups/ArtificialNeuralNetwork/)