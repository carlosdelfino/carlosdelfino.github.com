---
title: Algoritmo para busca de Regras Implicitas
excerpt: Para usar o GNU Make aproveitando bem seus recursos, é importante comprender como funciona o algoritmo de busca de Regras Implicitas.
category: [logicadeprogramacao]
tags: [Make, Programação, Lógica, Compilação, Scripts, Shell, Ferramentas, Tools, Dicas, Algoritmo, Regras, Regras Implicitas, Targets, Rules, Implicit Rules]
layout: article
comments: true
share: true
ads:
 show: true
toc: true
feature:
 index: true
 category: true
tagcloud: true
---
Com base no 
[Manual do GNU Make](https://www.gnu.org/software/make/manual/html_node/Implicit-Rule-Search.html#Implicit-Rule-Search)
irei fazer abaixo uma descrição do algoritimo usado pelo make para 
busca de regras implicitas no arquivo makefile, é uma tradução livre 
e sujeita ainda a muitas correções, os termos especificos estão sendo 
analisados para uma melhor tradução e uso, sendo um material original 
e singular de minha autoria, estarei evitando me apoiar em material 
de terceiros e em portugues, buscando focar no material original dos 
autores e desenvolvedores originais.
{: .noticie-warning }

Há  conceitos que são importantes já serem compreendidos antes de
continuar a leitura desta publicação, o que é uma "_Regra_" (Rule) e o 
que é um "_Objetivo_" (Target), tais termos estarão presentes nesta
publicação e serão usados com a primeira letra maiscula para evitar 
dúvidas.

O procedimento de busca por "_Regras_ implicitas" (Implicit Rules), é 
executado, tanto pela _Regra_ (Rule) seguida de dois-pontos mas que não 
tenha um bloco de instruções, para cada _Objetivo_ (Target) de uma 
_Regra_ ordinária que não tenha um bloco de instruções, quanto também 
por cada prerequisito que não é _Objetivo_ de alguma _Regra_. 
O procedimento é também seguido recursivamente por prerequisitos 
proveniêntes de _Regras_ implicitas, na cadeia de busca por _Regras_.

_Regras_ de sufixo, não são mencionsados neste algoritmo porque _Regras_ 
de sufixo são convertidas por suas regras padrões equivalentes uma vez o
arquivo "makefile", tenha sido carregado.

Para um _Objetivo_ membro de um arquivo na forma 'arquivo(membro)', o 
seguinte algoritmo é executado duas vezes, primeiro usando o nome do 
'Objetivo' inteiro (t), e na segunda vez usando o '(membro)', como 
_Objetivo_ (t), se a primeira vez não encontrar a _Regra_.

 1. Quebrar (t) em uma parte do diretorio, chamado (d), e o restante 
    chamado (n). Por exemplo, se (t) é `src/foo.o`, então (d) é o valor
    `src/` e (n) é o valor `foo.o`.
 2. Faça uma lista de todo o padrão de _Regras_ do qual um dos _Objetivos_ 
    corresponde a "t" ou "n". Se o padrão de _Regras_ contém uma barra, 
    que é comparado com "t"; caso contrário, tente com o "n".
 3. Se alguma _Regra_ nesta lista não coincidir com nenhuma _Regra_,
    então remova todas as regras não-terminais da lista.
 4. Remova da lista todas a _Regras_ que não tem um bloco de instrução.
 5. Para cada padrão de _Regra_ na lista:
    1. Encontre a _Ramificação_ (s), que é uma parte não vazia de (t) ou (n)
       que coincide com '%' no padrão da _Regra_.
    2. Calcule os nomes de prerequisitos pela substituição de (s) por '%';
       se o padrão do _Objetivo_ não contiver uma barra, adicione (d) para 
       o inicio de cada nome de prerequisito.
    3. Teste quando todos os prerequisitos existem ou devam exitir. (Se um
       nome de arquivo é mencionado no makefile como um _Objetivo_ ou como 
       um prerequisito explicito, então nos dizemos que ele deve existir)
       
       Se todos os prerequisitos exisitrem ou não existirem, ou não há 
       prerequisitos, então esta _Regra_ é aplicada.
       
 6. Se nenhum padrão de _Regra_ foi encontrado até agora, tente de forma mais 
    vezes. Para cada padrão de _Regra_ na lista:
    1. Se a regra é terminal, ignore á, e vá para a próxima regra.
    2. Calcule os nomes de prerequisitos como antes.
    3. Teste ou todos os prerequisitos existenes ou que não existam.
    4. Para cada prerrequisito que não existir, siga este algoritmo recursivamente
       para ver se o prerrequisito pode ser atendido por uma _Regra_ implicita.
    5. Se todos os prerequisitos existem, podem existir, ou as _Regras_ implicitas
       podem ser executadas, então as _Regras_ se aplicam.
  7. Se a _Regra_ implicita não se aplica, a regra para .DEFAULT, se alguma, aplica.
     Neste caso, Dê a (t) o mesmo bloco de comandos que .DEFAULT tem. caso contrário,
     não há bloco de comandos para (t).    

Uma vez a _Regra_ regra que se aplica foi encontrada, para cada padrão de _Objetivo_
de uma regra otra que uma que coincida com (t) ou (n), o "%" no padrão é subistituido
com o (s) e o nome de arquivo resultante é gravado até o bloco de comandos reconstruir
o arquivo (t) que é _Objetivo_ é executado. Após o bloco de comandos é executado, cada 
um destes nomes de arquivos são armazenados no banco de dados e marcados como tendo 
sido atualizado e tendo a mesma situação de atualizado como no arquivo (t).

Quando o bloco de comandos de um padrão de _Regra_ é execudado para (t), as variáveis
automáticas  são setadas para corresponder com o _Objetivo_ e prerequisitos. Veja
sobre _Variáveis Automáticas_.


