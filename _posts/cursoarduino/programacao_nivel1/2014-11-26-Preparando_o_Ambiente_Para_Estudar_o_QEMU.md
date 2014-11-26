---
title: Preparando o Ambiente para Estudar o QEMU
excerpt: "O QEMU é um emulador de que nos permite executar códigos desenvolvidos para determinados processadores em outros, por exemplo tendo um código desenvolvido para ARM posso executa-lo em uma maquina i386, porém em muitos casos é preciso o respectivo sistema operacional. Neste estudo estarei propondo estudos com QEMU para uso da arquitetura Cortex-M na modalidade BareMetal e no máximo com RTOS como FreeRTOS"
category: [logicadeprogramacao]
tags: [QEMU, Bare Metal, Emulador, Make, Programação, Lógica, Compilação, Scripts, Shell, Ferramentas, Tools, Dicas, Algoritmo, Variáveis Automáticas, Variáveis, Variáveis Mágicas, Visibilidade de Variáveis, i386, ARM]
layout: article
comments: true
share: true
ads:
 show: true
toc: true
feature:
 index: true
 category: true
---

## Preparando o GIT para Commits e Patchs

Para que tenha bons resultados na proposta de seus Patchs para o QEMU é 
preciso que siga algumas orientações. Abaixo irei falar superficilamente
de algumas.

### Verificando os Patch 

Esta seção é baseada no link "[How to automatically run checkpatch.pl when developing QEMU](http://blog.vmsplice.net/2011/03/how-to-automatically-run-checkpatchpl.html)",
tradução livre do conteúdo.

Para cada patch gerado é importante fazer uma verificação usando o script
`checkpath.pl` que foi adicionado a pouco tempo ao repositorio do QEMU.

Este script pesquisa os patches criados por violações dos padrões de 
codificação definidos pela equipe do QEMU. Para executar o script 
automáticamente a cada commiting no repositório git (prática sugerida:
faça pequenos ajustes validos sempre e faça logo em seguida um commit),
e caso haja alguma violação abortar o processo para ajustes.

{% highlight bash %}
$ cd qemu
$ cat >.git/hooks/pre-commit
#!/bin/bash
exec git diff --cached | scripts/checkpatch.pl --no-signoff -q -
^D
$ chmod 755 .git/hooks/pre-commit
{% endhighlight %}

Algun commit que vilar o padrão de codificação como verificado por 
`checkpatch.pl` será abortado. 

Se vier a encontrar algum falso positivo, use `git commit --no-verify` 
para pular o pre-commit. Seja cuidadoso ao usar este recurso.

## Fontes:
 
 * [http://blog.vmsplice.net/2011/03/how-to-automatically-run-checkpatchpl.html](http://blog.vmsplice.net/2011/03/how-to-automatically-run-checkpatchpl.html)
 
 