---
title: "Dizem que Linus Torvalds" 
tags: [Linux, Linus Torvalds, Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM]
categories: [Embarcados]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: perfil/linustorvalds-1600x800.jpg
 teaser: perfil/Linus-Torvalds-500x260.jpg
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Recebi esta sexta dia 14 de outubro de 2016 uma postagem alegando que Linus Torvalds prefere a arquitetura x86, claro eu como um amante da arquitetura ARM em especial pelo R de Risc não poderia deixar de ir a fundo nesta história e tentar entender bem porque ele, Linus, prefere o x86, e cheguei que seus motivos seriam os mesmo que o meus, quando um dia disse que Linux e melhor para servidor do que para desktop de clientes.

<!--more-->

Em entrevista para a Linaro Connect no "Fireside Chat com David Rusling" Linus justifica porque prefere a arquitetura x86, ele diz aproximadamente aos 21 minutos da entrevista que não deseja desapontar a comunidade ARM, mas prefere a arquitetura x86.

Porém, Linus deixa bem claro que sua escolha não se deve por um problema diretamente com o ARM e sua família de processadores, mas sim pelo fato dos processadores x86 terem uma infraestrutura de apoio mais padronizada, ou seja, de um computador para outro há maiores padrões arquiteturais que para um PC são importantes, principalmente para que o usa para desenvolvimento.

Ele cita na entrevista que o importante é ter um ambiente onde ele possa desenvolver, e o ARM traz um problema quando se gera novas versões já que em cada nova versão do kernel Linux é preciso gerar uma nova versão para cada seguimento de processador ARM, pois os mesmo não tem um padronização no que tange a infraestrutura de apoio. Diante disso é perceptível que o problema não é a arquitetura ARM, mas sim como seus implementadores a adotam. 

Do meu ponto de vista o grande problema do ARM é também sua grande qualidade, ter processadores optimizados para cada seguimento de mercado muito além de suas três famílias Cortex-A, Cortex-M e Cortex-R, já que dentro de cada família ainda temos processadores com arquiteturas diferenciadas (mesmo mantendo a mesma arquitetura de instruções) há processadores que buscam o maior desempenho em menor espaço, outros o maior desempenho e menor consumo com baixa tensão, sem falar nos que buscam mais processamento gráfico e por ai vai. 

E toda a infraestrutura que cobre as demandas de cada processador em especial dos processadores Cortex-A que rodam o Linux mais adequadamente são opcionais ou seja, há recursos de apoio que podem ser implementados pelo fabricante do chip em detrimento da especificação da ARM, sendo assim é possível no universo de centenas de fabricantes milhares de processadores diferentes todos ARM Cortex-A, mas tais sutis diferenças provocam a compilação de um novo Kernel para cada dispositivo com seu processador especifico.

O Ponto que eu digo que compreendo o Linus e intercede no que falei a alguns anos sobre usar o Linux apenas como servidor está exatamente no melhor uso do recursos, o Linux pode ser compilador para qualquer processador que dê suporte a sistemas Operacionais como é o caso ARM Cortex-A, porém é importante distinguir sua aplicação melhor, e claro que um ARM pode sim ser usado para um Servidor, mas será que é a melhor escolha? e quais tipos de servidores o ARM se encaixa? da mesma forma o Linux, em se tratando de PC, de Destkop, quais são as melhores escolhas, o usuário comum se perde no Linux por costume e falta de suporte real, o Windows mais fácil ser usado por leigos, e por técnicos em geral, do que o Linux, tornando o Linux uma ferramenta mais profissional por exigências técnicas em seu uso. Sendo assim se alguém pergunta se eu usaria Linux em meu computador pessoal, eu diria que até usuária mas prefiro usar o MAC, porque? porque 99% das vezes não me preocupo com nada mais além do que meu trabalho, já no Linux ou preciso as vezes me preocupar com alguns detalhes da manutenção do hardware que ainda é precário em relação ao MAC e o windows nem se compara, pois sempre teremos o problema com Malware, e claro há muitas ferramentas muito boas para Windows, no meu caso vivo entre os dois mundos Windows e Mac para poder aproveitar o melhor dos dois, mas quando penso em servidor seja para o que for, 95% das vezes o Linux é minha escolha, só perde quando obrigatoriamente tenho que usar algo ligado a infraestrutura de autenticação do Windows.

Abaixo se encontra a entrevista do Linus no Fireside Chat, tire suas próprias conclusões:
<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fuAebQvFnRI" frameborder="0" allowfullscreen></iframe>
<figcaption>Fireside Chat with David Rusling and
Linus Torvalds na integra com Linus Torvalds na Linaro Connect
</figcaption>
</figure>