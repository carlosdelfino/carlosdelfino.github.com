---
title: Introdução as Redes Neurais, Principais Funções 
tags: [Redes Neurais, Inteligência Artificial, Inteligência, Artificial, RNN, NN, LTSM, Formulas, Rampa Simetrica, Simetrica, Ativação Lógistica, Hiperbólica, Tangente, Tangente Hiperbólica, Função Logistica]
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
Abaixo uma coleção de funções que podem ser usadas para construção de redes neurais, aqui apresento as principais funções, e discutirei posteriormente o melhor uso de cada uma.

<!--more-->

## Função Logística

$$
f(x) = \frac{1}{1+e^(-\beta*x)}
$$

| x | f(x;.01) | f(x;0.02) | f(x;0.03) | f(x;0.04) | f(x;0.05) |
| --- | --- | --- | --- | --- | --- |
| -1.000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| -900 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| -800 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| -700 | 0,001 | 0,000 | 0,000 | 0,000 | 0,000 |
| -600 | 0,002 | 0,000 | 0,000 | 0,000 | 0,000 |
| -500 | 0,007 | 0,000 | 0,000 | 0,000 | 0,000 |
| -400 | 0,018 | 0,000 | 0,000 | 0,000 | 0,000 |
| -300 | 0,047 | 0,002 | 0,000 | 0,000 | 0,000 |
| -200 | 0,119 | 0,018 | 0,002 | 0,000 | 0,000 |
| -100 | 0,269 | 0,119 | 0,047 | 0,018 | 0,007 |
| 0 | 0,500 | 0,500 | 0,500 | 0,500 | 0,500 |
| 100 | 0,731 | 0,881 | 0,953 | 0,982 | 0,993 |
| 200 | 0,881 | 0,982 | 0,998 | 1,000 | 1,000 |
| 300 | 0,953 | 0,998 | 1,000 | 1,000 | 1,000 |
| 400 | 0,982 | 1,000 | 1,000 | 1,000 | 1,000 |
| 500 | 0,993 | 1,000 | 1,000 | 1,000 | 1,000 |
| 600 | 0,998 | 1,000 | 1,000 | 1,000 | 1,000 |
| 700 | 0,999 | 1,000 | 1,000 | 1,000 | 1,000 |
| 800 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |
| 900 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |
| 1.000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |

|[Influência do Parametro B na função de Ativação Tangente Hiperbólica](\images\redesneurais\introducao\logistica-1.png)

no gráfico abaixo apresento a mesma função em um formato tridimencional, onde o eixo z é a variação das alternativas para $\beta$.

|[Influência do Parametro B na função de Ativação Tangente Hiperbólica Visão Tridimensional ocnforme variação de Beta](\images\redesneurais\introducao\logistica-1-3d.gif)


## Função Tangente Hiperbólica 

$$
f(x) = \frac{1-e^(\beta*x)}{1+e^(\beta*x)}
$$

na formula acima `e` é o número de euler portanto
$ e= 2.718281828459045235360287$, e $\beta$ é uma constante que ajusta a inclinação da curva, veja o gráfico baixo, onde o segundo parametro o que vai após o ponto e virgula é o valor de $\beta$.

| x | f(x;.01) | f(x;0.02) | f(x;0.03) | f(x;0.04) | f(x;0.05) |
| --- | --- | --- | --- | --- | --- |
| -1.000 | -1,000 | -1,000 | -1,000 | -1,000 | -1,000 |
| -900 | -1,000 | -1,000 | -1,000 | -1,000 | -1,000 |
| -800 | -0,999 | -1,000 | -1,000 | -1,000 | -1,000 |
| -700 | -0,998 | -1,000 | -1,000 | -1,000 | -1,000 |
| -600 | -0,995 | -1,000 | -1,000 | -1,000 | -1,000 |
| -500 | -0,987 | -1,000 | -1,000 | -1,000 | -1,000 |
| -400 | -0,964 | -0,999 | -1,000 | -1,000 | -1,000 |
| -300 | -0,905 | -0,995 | -1,000 | -1,000 | -1,000 |
| -200 | -0,762 | -0,964 | -0,995 | -0,999 | -1,000 |
| -100 | -0,462 | -0,762 | -0,905 | -0,964 | -0,987 |
| 0 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| 100 | 0,462 | 0,762 | 0,905 | 0,964 | 0,987 |
| 200 | 0,762 | 0,964 | 0,995 | 0,999 | 1,000 |
| 300 | 0,905 | 0,995 | 1,000 | 1,000 | 1,000 |
| 400 | 0,964 | 0,999 | 1,000 | 1,000 | 1,000 |
| 500 | 0,987 | 1,000 | 1,000 | 1,000 | 1,000 |
| 600 | 0,995 | 1,000 | 1,000 | 1,000 | 1,000 |
| 700 | 0,998 | 1,000 | 1,000 | 1,000 | 1,000 |
| 800 | 0,999 | 1,000 | 1,000 | 1,000 | 1,000 |
| 900 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |
| 1.000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |

|[Influência do Parametro B na função de Ativação Tangente Hiperbólica](\images\redesneurais\introducao\tangente-hiperbolica-1.png)

no gráfico abaixo apresento a mesma função em um formato tridimencional, onde o eixo z é a variação das alternativas para $\beta$.

|[Influência do Parametro B na função de Ativação Tangente Hiperbólica Visão Tridimensional ocnforme variação de Beta](\images\redesneurais\introducao\tangente-hiperbolica-1-3d.gif)
