---
title: "Contando Bicicletas" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Visão Computacional, OpenCV, Linux, Câmera, Contador, Bicicleta]
categories: [Embarcados]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: /embarcados/nanopi-m3-03-1024x445.jpg
 teaser: /embarcados/nanopi-m3-03-300x174.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Como construir um contador de ciclistas, ou mesmo um contador de objetos, talvez pessoas em uma passarela, ou quem sabe um contador de carros? Tudo isso em uma caixinha de aproximadamente 10x10 cm, um computador de R$ 200,oo e uma câmera de R$ 40,00?

<!--more-->

A uns 2 anos talvez um pouco mais, eu estava fazendo um trabalho para a Strata Engenharia, e lá queria ter desenvolvido um equipamento para contabilizar carros na rodovia, mas não tinha ainda o conhecimento necessário e os equipamentos para tal aparelho, que envolvia software especializado e um hardware que na época achava que tinha a necessidade de ser um computador comum. O Raspberry já existia e apesar de todos falarem muito bem, não acreditava nele, e acertei mesmo na época sendo sendo um grande lançamento até hoje ele não é a solução adequada para um projeto como este.

Como todos nós sabemos hoje temos o que alguns erroneamente tem  chamado de Pocket PCs, mas na verdade o nome certo é Module PC, ou seja um Computador Pessoal em um módulo. Na verdade para ser um Pocket PC envolve termos uma unidade de processamento, memória para armazenamento quando desligado, HID (Human Interface Device) que envolve normalmente teclado, mouse e monitor, Softwares como agenda, contatos, pequeno editor de texto e planilha, e claro uma conexão com a internet preferencialmente WiFI, porque hoje ninguém vive mais ligados a cabo, não é mesmo. 

Mas o Module PC pode por um lado extrapolar este requisitos como por outro pode não atender a todos, por exemplo o novo Module PC NanoPI-M3 (veja imagem abaixo) da FriendlyARM produzido com um microprocessador ARM da família Cortex-A, fabricado pela Sansung e empoderado por um Cortex-A53, este processador possui 8 núcleos em um pequeno chip, realmente bem pequeno em dimensões para seu poder, e velocidade que chega a 1.4Ghz, e funciona com um fonte de 5V por 2 A, tem habilidades preemptivas que permite prever qual código deve ser executado, tem um bom cache de instruções adequado a este senário preemptivo, o que lhe dá um excelente desempenho e baixo consumo, este Module PC construído em uma pequena placa quadrada de aproximadamente 6,5cm. Muito poder, porém para se tornar um PocketPC deve ser acrecido de uma tela touch screen que deve ser adquirida a parte e ter instalado os softwares necessários para tal habilidade.

<figure>
<img src="/images/embarcados/nanopi-m3-detalhestecnicos-640x460.png" alt="Algumas características do NanoPI-M3"/>
<figcaption>Algumas características do NanoPI-M3 fornecido pela FrindlyARM</figcaption>
</figure>

Ao receber este presente da FriendlyARM para testes pensei inicialmente em fazer um computador de bordo para bicicletas, mas este projeto que tenho em mente envolve muitos sensores e iria demorar ficar pronto, então atendendo um chamado de um colega para colocar em funcionamento um contador de ciclistas que foi produzido pela LabProdam de São Paulo, vi que este projeto de contador seria perfeito para o NanoPI M3, pois demandaria apenas uma câmera e poderia ter seus primeiros testes em minha própria mesa. E seria um desafio transformá-lo em um contador de veículos, com os recursos que idealizei nos tempos que trabalhava na Strata Engenharia.

Então, partir logo para ver o que precisava fazer, em primeiro instante, pensei que teria que fazer grandes intervenções no código, mas minha maior surpresa foi que ao compilar o código original no NanoPI M3, este funcionou imediatamente, sem nenhuma intervenção sem contar que o consumo de processamento é mínimo e até o momento apenas a câmera tem deixado a desejar já que gastei R$ 20,00 não posso esperar muito dela.

Vejamos um pouco mais do projeto. abaixo já apresento um GIF que demonstra o consumo de processamento do código na versão que tenho em mãos e baixado diretamente do site do repositório da LabProdam com pequenas alterações que fiz, mas nada que justifique o desempenho atual este já era o mesmo antes das alterações:

<figure>
<img src="/images/embarcados/desempenho no Cortex-A53.gif" alt="GIF Animado apresentando o uso dos recursos computacionais do processador" />
<figcaption>GIF Animado apresentando o uso dos recursos computacionais do processador</figcaption>
</figure>

O projeto será documentado na página <a href="http://carlosdelfino.eti.br/ContadorDeCiclistas" >http://carlosdelfino.eti.br/ContadorDeCiclistas</a> e mesmo que eu venha a ter sucesso na migração para contagem de veículos, já que este é um grande desafio e necessita de amplos conhecimentos sobre processamento de imagens e detecção de padrões, eu ainda assim manterei o projeto com o mesmo nome original, até que seja interessante sua mudança.

Por falta de vídeos de trânsito em Ciclo Faixas e Ciclo Vias não tenho tido como fazer um teste mais real, mas os testes que fiz provocam processamento real no módulo exigindo do processador a mesma demanda que seria exigida com vídeos reais.

## Como ajudar e fazer uma parceria para o sucesso

Querendo ajudar no projeto a melhor forma no momento é compartilhar vídeos que trafego de bicicletas em ciclo vias e ciclo faixas, preferencialmente com visadas aéreas onde se possa ver uma faixa mínima de 20 metros da pista, um angulo de visão de 45 graus, de foma que dê para identificar visualmente o perfil da bicicleta e evitar filmar o rosto do ciclista.

Caso queria participar na codificação, o momento é o melhor, pois quero passar a fazer identificação de formas geométricas na imagem, ou seja, identificar as rodas (círculos) o quadro (triângulos e trapézios) e quem sabe identificar o rosto dos ciclistas quando houver filmagem frontal. Só de identificar as rodas, e as linhas que formam o corpo do ciclista já será um grande passo neste projeto.

## O que tenho feito no código atual

A versão atual do projeto está sendo reescrito usando conceitos OO mais consolidados, e buscando a redução ao máximo de passagens de parâmetros em chamadas de funções dentro de loops. Criei uma nova classe para gerir toda a configuração é uma classe grande com muitos métodos e aparentemente pesada, mas sua função é apenas concentrar os parâmetros da aplicação, salvando os parâmetros em um aquivo do tipo *JSON* quando for importante restaurá-los entre seções. Também removi da função `main`, o ponto de entrada do aplicativo as operações especificas do programa, ficando ali apenas a instanciação das classes iniciais e pontos de entrada do processamento. que fica agora a carga da Classe `CycloTracker`, esta classe tem 5 estágios importantes:

 1) Criação da classe e recebimento da classe de configuração, 
 2) Inicialização onde os objeto de apoio são criados conforme a configuração passada, 
 3) Definição dos callbacks se houver algum, 
 4) Obtenção dos parâmetros da câmera
 5) e finalmente processamento do loop.

As demais classes não sofreram ainda intervenção a não ser quando é necessário o uso da classe `CycloConfig`.

Ouve uma pequena alteração na classe responsável por gravar os objetos identificados e gravar um cópia da imagem em seu procedimento de montagem da *string* de contagem e nome do arquivo. 

A classe `InteractionHandler` teve mudanças leves no procedimento de reconfiguração das áreas e removi o uso de classes estáticas ao máximo encapsulando melhor o procedimento e sua interação com a classe `CycloConfig`. 

As demais classes como Câmera e `CoordTransform` sofreram mudanças para seguir o mesmo modelo e foi criada a classe `CameraConfig` para ajudar na gravação dos parâmetros da câmera porém nenhuma delas é usada no projeto atual a não ser para testes.

Além disso adicionei mais mensagens do processo interno demonstrando em que estágio o programa se encontra e ajudando assim na depuração.

Agora no próximo estágio do projeto estarei estudando como funciona o sistema de rastreio de objetos e como melhorá-lo, torná-lo reaproveitável para uso em diversos tipos de projeto de rastreamento por visão computacional, tornando as classes mais genéricas e parametrizáveis possível. Esta interferência irá ocorrer em especial nas classes `ObjectTracker` e `ObjectCounter`.

## Raspberry PI vs NanoPI M3

Algumas pessoas tem me questionado a possibilidade de usar um RaspberryPI neste tipo de projeto, infelizmente os modelos atuais do RaspberryPI não são muito adequados, talvez o modelo 3B possa rodar relativamente bem, mas mesmo assim ainda é inferior ao NanoPI M3.

Os modelos A+, Zero e o Modelo 2 B e 3 B, do RaspberryPI o mais avançado usa um Cortex-A7 de 4 núcleos a 1.2Ghz, o que perde um pouco para o NanoPI M3, tanto pela metade dos núcleos como a velocidade sendo um pouco inferior.

Bem meu intuito não é apontar quem seja melhor, mas sim que seja mais adequado ao projeto, vejo no NanoPI M3 uma grande escolha, e vejo mercado através de alguns poucos comentários que há pessoas adotando uma tecnologia apenas porque outro a está usando, um colega me disse que optou pelo Raspberry PI porque todos usavam, mas quem são todos, são os que ele escolheu como sendo os que deve acreditar, pois estou usando outro e comprovadamente tendo sucesso com o NanoPI M3, e mesmo assim ele ainda acha que o melhor argumento é o fato de outros em maior quantidade terem comprado o RaspberryPI mesmo que não demonstrem um real sucesso com seus projetos ou pelo menos os resultados mais adequados.

A grande questão é essa, saber fazer a escolha por parâmetros puramente técnicos, já que hoje em dia documentação e meios de comunicação sem limites não nos falta. Portando escolher porque tem mais gente por perto não a forma certa, é sem dúvida um erro, a melhor forma é se arriscar e aprender a usar a melhor tecnologia que lhe atende. Neste caso está sendo sem dúvida o NanoPI M3.

## Conclusão

Em resumo, como podem ver o projeto tem demonstrado ser perfeitamente executável neste Module PCs como o NanoPI, mesmo que, ainda limitado a qualidade da câmera, e terei uma melhor referência quando obtiver uma câmera com maior resolução e que possa gerar mais frames por segundo.

Sozinho sem dúvida chegar a algum lugar com este projeto, mas devido a sua natureza tanto de estudos, pesquisa como desenvolvimento de conhecimento compartilhado é importante a colaboração da comunidade colegas e amigos sejam do setor de TICs ou sejam de outros setores, em especial com filmagens de câmeras.

Em breve posto mais notícias sobre o projeto, por hora deixo o convite para acompanhá-lo pelo GitHub, veja detalhes na pagina: <a href="http://carlosdelfino.eti.br/ContadorDeCiclistas" >http://carlosdelfino.eti.br/ContadorDeCiclistas</a>