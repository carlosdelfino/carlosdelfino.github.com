---
title: Redes WiFi - A Família 802.11
---

Redes WiFi sem dúvida é uma família, nomes diversos, padrões variados, equipamentos que juram estar normatizados e dentro de tais padrões, porém que não se comunicam adequadamente.

<!--more-->

A ser revisado!
{: .notice }

O Que mais me assusta nos tempos atuais não é a quantidade de padrões relacionados a Redes WiFi, mas a quantidade de profissionais no setor que sequer sabem que redes WiFi são padronizados pelo IEEE e que seu código de indentificação do padrão é 802.11, isso sim é assustador.

Antes vou contar um caso, uma empresa de Aquiraz depois de muita insistência se dispos a me atender com um acesso WiFI de 10Mbs (dez Mega bits por segundo), o mais intrigante é que um de seus profissionais, talvez meu conhecido de minha jornada aqui no Ceará, demonstrou grande habilidade em controlar de forma desfavorável meu acesso a internet, fazendo malabarismos e desperdiçando tempo e dinheiro em tentar me criar o pior acesso a internet que já tive na vida desde os tempos de modem 2400 Bps (Baunds por segundo), porém os mesmos não sabiam o que era um RFC ou mesmo o que é 802.11.

Mas deixando este profissionais de lado, vamos em frente com nossa história.

Eu sempre trato as siglas ligadas a velocidade da seguinte forma:

* bps - Bits por segundo;
* Bps - Baunds por segundo;
* B/s = Bytes por segundo;

*Atenção* o IEC (International Eletrotechnical Comission) estabeleceu novas siglas para medidas de armazenamento e velocidade de dados digitais, isso ocorreu em 1998, e só começou a ser adotado nos meados de 2002 e no Brasil apartir desta decada de 2010, sendo ainda timidamente usado, e quase ocultado pelo mercado tupininqui, e eu mesmo só vi informações em portugues claras sobre o assunto no Clube do Hardware quando tange ao uso das novas medidas para armazenamento de HDs comuns. Portanto para esclarecer este assunto um dia destes eu escrevo um artigo especifico e como está o senário na data da escrita.

#### Fontes sobre o assunto:

* https://en.wikipedia.org/wiki/Binary_prefix
* https://physics.nist.gov/cuu/Units/binary.html
* http://www.clubedohardware.com.br/blog/confuso-com-kb-x-kib-mb-x-mib-gb-x-gib-tb-x-tib-r3993/


Eu acredito que já escrevi algo sobre isso alguns meses atrás, mas vou rever tal post e se não existir o faço novamente para discutir o que são tais siglas como usa-las e como são usadas, e suas relações com banda, velocidade e atraso na rede.

As redes WiFI como já foi percebido é definida pelas normas IEEE 802.11, estas normas são definidas por sua vez, por um grupo de 600 membros aproximadamente no IEEE (Instituto de Engenharia Eletrica e eletrônica, orgão munidial que normatiza as redes de computadores, também).

A família 802, por sua vez, normatiza todos protocolos de redes, desde a camada física (cabos e equipamentos) até a camada de aplicação em alguns raros casos, mas estas camadas acima da camada de enlace são definidas dinamicamente por um mecanismo democrático da internet chamado RFC.

Para compreender o conceito de camadas, é preciso conhecer o que é o Modelo OSI definida pelo orgão internacional de nome ISO, confuso né, mas a gente acostuma, ISO siginifica _*I* nternacional *S* tandartization *O* rganization_ e OSI é seu modelo que foi criado como uma proposta para a MILNET (ai uma sigla, bem vai anotando ai e pesquisando se não conhece e siginfica _*O*pen *S*ystem *I*nterconection_.

Mas vamos focar mesmo neste artigo apenas no padrão 802.11 que é o que trata o WiFi e tudo que envolve ele, até o fornecimento de energia através do que é chamado PoE quando usamos roteadores, haaa, mas ai é 802.3 (802.3af mais especificamente) e neste caso é rede cabeada, ou ethernet em especial, e para quem não sabe 802.3 define tudo sobre redes cabeadas em especial Ethernet. Não entraremos em detalhes no 802.3, somente falaremos um pouquinho para contextualizar ao cenário atual de provedores locais.

O padrão 802.11 surgiu para padronizar o uso da faixa de frequência 2.4Ghz em transmisão de dados, isso ocorreu em 1997, além do Wi-Fi conhecido também como WLAN (Wireless Local Area Networ) existe também o HiperLan ([Hi Performance European Radio LAN](http://www.wirelesscommunication.nl/reference/chaptr01/wrlslans/hiperlan.htm)) e o HomeRF. É importante saber que Wi-Fi é um termo pertencente a [Wi-FI alliance](https://en.wikipedia.org/wiki/Wi-Fi_Alliance), um associação de empresas referencia de mercado que certifica os equipamentos WLAN para que estes sejam interoperaveis e que estejam em conformidade com o padrão 802.11, não podendo ser usado de forma indiscriminada.

O Termo Wi-Fi foi cunhado com base no termo Hi-Fi, que siginifica Wireless Internet - High Fidelity, ou seja Internet sem Fio (internet no sentido de inter redes) de alta fidelidade. Na época que termo foi cunhado já existiam redes sem fio como a [ALOHAnet](https://en.wikipedia.org/wiki/ALOHAnet) que conectava as ilhas Havaianas (não é o chinelo tá) com os Estados Unidos, esta rede não era padronizada e usava UHF para tal conexão, dá para imaginar a velocidade né.

O padrão foi então criado pelo IEEE e manteve-se na família 802, para que fosse definido o mais similiar ao que conhecemos hoje das redes cabeadas, o que é muito difícil de ser feito, mas pelo que vemos no cenário atual, foi que se teve sucesso. Hoje em muitas redes sequer percebemos quando usamos um sistema cabeado ou via rádio e claro com qualidade.

O padrão 802.11 quando lançado em 1997, previa uma velocidade máxima de 1 e 2Mbps (Mega bits por segundo), e foi padronizad o uso da frequência de 2.4Ghz que na época era usada apenas por fornos de microcondas e equipamentos hospitalares, esta frequência é conhecida como pertecente ao gurpo das frequências ISM (Industrial, Scientifical end Medical), são grupos de faixa de frequência para uso industrial médico e para pesquisa. Há um engano em dizer que tais frequências são de uso aberto e livre, porém quando usadas com o intuito Ciêntifico e até certa portência é permitido sem licensa.

Logo depois veio o padrão 802.11b, em 1999 também foi lançado o padrão 802.11a considerados na epoca padrões de alta velocidade pois adicionavam ao 802.11 a capacidade de transmissão de até 11Mbps, o primeiro mantendo a frequência de 2.4Ghz e o segundo 802.11a adicionando o uso da Frequência licensiada de 5Ghz. A frequência de 5Ghz ainda hoje é pouco usada o que traz grandes benefícios em desempenho.


### Fontes:

* http://grouper.ieee.org/groups/802/11/Reports/802.11_Timelines.htm
