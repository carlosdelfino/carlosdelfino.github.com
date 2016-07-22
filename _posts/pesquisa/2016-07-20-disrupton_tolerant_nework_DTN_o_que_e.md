---
title: "Disruption Tolerant Networking, o que é?" 
tags: [Pesquisa, low-Earth orbit, near-Earth orbit, deep space, DTN, SSI, Solar System Internet, Space Internet, ISS, International Spacial Station, Baixa orbita, orbita próxima, espaço profundo, Internet do Sistema Solar, Estação Espacial Internacional, Ground Station, Estações Terrestres, Daly/Disruption Tolerant  Network, Rede tolerante a disrupção e atrasos, Disrupção, Atrasos, Reliable Solar System Internet Connection, Reliable Solar System Internet, NASA Advanced Exploration Systems, AES, Consultative Committee for Space Data Systems, CCSDS, Internet Engineering Task Force, IETF, Interplanetary Overlay Network, ION]
categories: [pesquisa, dtn]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 teaser: dtn/dtn-identifier.png
 feature: pensamentos/pensamento1-400x200.jpg
ads: 
 show: true
tagcloud: true
coinbase:
 show: false
---
Reliable Solar System Internet Connection também conhecido como Disruption Tolerant Network (DTN).

A comunicação da terra com qualquer espaçonave é uma missão complexa, amplamente envolve extremas distâncias. Quando o dado transmitido e recebido attravés de milhares a milhões de milhas, o atraso e o potencial para quebra (disrupção) da conexão ou perda de dados é bastante significante. Delay/Disruption Tolerant Networking (DTN) é a solução da NASA para conexão entre redes para missões no espaço de forma confiável.

<!--more-->

Tradução livre de: [https://www.nasa.gov/content/dtn](https://www.nasa.gov/content/dtn)

A Lua está em torno de 250 mil milhas de distancia e Marte está a 140 milhões de distância na média. Para comunicar através destas vastas distâncias, NASA gerencia três redes de comunicações compostas de estações terrestres distribuídas e satélites repetidores no espaço para transmissão e recepção que suporta tanto a NASA como missões de outras empresas. Esta são a Deep Space Network - DNS (Rede do Espaço Profundo), a Near Eart Network - NEN (Rede próxima a Terra), e a Space Network - SN (Rede do Espaço)

<figure>
<img alt="Identificador para Disruption Tolerant Network" src="/images/dtn/dtn-identifier.png"/>
<figcaption>
As missões da NASA tem usado relés de comunicação simpes ou direto, mas em missões futuras, irá requerer comunicação similar a Internet (Internet-like).
</figcaption>
</figure>

Paras missões anteriores da orbita low-Earth para o espaço profundo, a NASA tem usado "point-to-point" (conexão direta), ou links simples por relé para comunicar com as espaçonaves; estas operações são bem similares a comunicação por sistemas telefônicos que se conectam diretamente dois nós de comunicação. Enquanto este abordagem tem sido um sucesso para as missões já realizadas, nas explorações conceitualmente para o futuro será introduzido muito mais necessidades complexas de comunicação, com a transferência de dados entre muitos nós. Estas transmissões será necessária operar como o a internet na Terra - Envolvendo muitos saltos (hops) via espaconáveis de relé e outros nós intermediários, criando a fundação para a "Solar System Internet" - SSI (Internet do Sistema Solar).

![Imagem conceitual da rede de comunicação de dados baseada em Relé por Salto Simples (Single-Hope-Relê)](/images/dtn/dtn-single-hop.png)

Como a internet terrestre, a SSI irá oferecer usos bem definidos, plataformas padronizadas onde será construído uma vasta variedade de aplicações pela seleção de serviços end-to-end (fim a fim). A SSI irá utilizar o pacote de protocolos DTN (Delay/Disruption Tolerant Network), que pode ser usado em alguns senários,incluindo aqueles com tempos maiores que a transmissão da luz (delay) ou frequente perda de link (disruption), onde o protocolo da internet (IP) falha.


## Como a DTN funciona
 
<figure>
<img alt="Concept image depicting the Disruption Tolerant Network" src="/images/dtn/dtn-ssi.png" />
<figcapion>
O Protocolo DTN (Disruption Tolerant Network Protocol) irá ativar a Solar System Internet, pertindo que dados sejam armazenados em nós até ser transmitidos com sucesso.
</figcapion>
</figure>

DTN é um modelo de rede computacional e um sistema de regras para transmissão de informações, oferece referência para uma suíte de protocolos, que estende a  capacidade da internet terrestre para se comunicar em ambientes desafiantes no espaço onde a internet convencional não funciona adequadamente. Estes ambientes são tipicamente sujeitos a frequente desrupção (corte), links que são limitados em uma direção, possibilidades de longos atrasos e altas taxas de erros.

A Suíte de Protocolos DTN pode operar em conjunto com a Suíte de IP Terrestre ou pode operar de forma independente. DTN provê garantia de entrega de dados usando um mecanismo automático do tipo gravar e enviar (Store-and-forward). Cada pacote que é recebido é formado imediatamente se possível. Mas armazenado para transmissões futuras se não for possível adequadamente mas que seja esperado que seja possível no futuro. Como resultado, somente o próximo salto será avaliado quando usando DTN.

O Suíte DTN também contem gerenciamento de rede, segurança, roteamento e qualidade de serviço (QoS - Quality-of-Service), que são similares as capacidades providas pelo Suíte da internet terrestre.

Porém DTN foi desenvolvido com aplicações espaciais em mente, os benefícios possíveis quando aplicações terrestres são sujeitas a frequentes disrupções e altas taxas de erros são comuns. Alguns exemplos incluem respostas a desastres e redes de sensores sem fio.

* **Melhorias na operação e contexto**: O mecanismo armazenar e enviar do DTN juntamente com a retransmissão automática provê mais detalhes sobre eventos durante as interrupções de comunicação que ocorrem como resultado da troca ou transferências entre estações terrestres e em condições atmosféricas pobres, e reduz de forma significante a necessidade de agendamento das estações terrestres para enviar ou receber dados, que pode muitas vezes exigir até 5 dias de planejamento antes da transmissão se efetivar.
* **Interoperabilidade e Reuso**: A Suíte de protocolo padronizado habilita a interoperabilidade de estações terrestres e espaçonaves operadas por alguma agencia especial ou entidade privada com ativos espaciais. Ela também permite a NASA usar o mesmo protocolo de comunicação para futuras missões (de baixa orbita terrestres, orbita aproximada ou espaço profundo - low-Earth orbit, near-Earth orbit or deep space)
* **Eficiência, Utilização e Robustez do Link Espacial**: DTN permite transmissões de dados mais eficientes e confiáveis resultando em uma banda mais útil. DTN também melhora a confiabilidade por ter múltiplos caminhos de redes e ativos para um potencial salto (pontos) de comunicação.
* **Segurança**:  O Pacote de segurança do protocolo DTN (DTN Bundle Protocolo Security) permite checagem de integridade, autenticação e criptografia, 
* **Qualidade de Serviço (QoS)**: O Suíte do Protocolo DTN permite muitos níveis de prioridade aser definido para diferentes tipos de dados, assegurando que o dado mais importante seja recebido na frente do dado sem importância.

## O Futuro do DTN
O Suíte de protocolos DTN está em desenvolvimento pelo projeto DTN da NASA Advanced Exploration Systems (AES) (NASA Advanced Exploration Systems (AES) DTN). A equipe AES DTN é também suporte para a padronização do DTN tanto pelo Comite Consultivo para Sistemas de Dados Espaciais (Conultative Committee Space Data Systems - CCSDS) e a Engineering Task Force (IETF) e todos os protocolos DTN que serão padrões internacionais abertos, suportado por softwares Open-Source. Várias implementações DTN existem e estão publicamente disponíveis, incluindo a implementação da nada do Interplanetary Overlay Network (ION).

Em Maio de 2016, a Estação Espacial Internacional (ISS), implementou um serviço de DTN institucional para suporte a cargas úteis. A implementação do DTN Institucional da ISS aperfeiçoa imensamente a confiabilidade da transmissão de dados de carga útil cientifica e reduz a sobrecarga operacional e planejamento, e prove uma arquitetura para suporte para missões de suporte, enquanto avança a tecnologia DTN para suportar o futuro do SSI.

Várias outras missões da NASA tem usado DTN, tais como o experimento Deep Impact Networking (DINET), A Missão 1 de observação da Terra (EO-1) e a demonstração de comunicação lunar através de Laser (LLCD), e muito mais está sendo visto para o DTN no futuro. Como resultado, a equipe AES DTN está trabalhando  com o programa  Comunicação Espacial e Navegação (Space Communication and Navigation - SCaN) para integrar o DTN com redes de comunicação da NASA, incluindo o DSN, NEN e SN, para dar suporte a futuras missões. A equipe AES DTN está também trabalhando com o grupo especial de interesse em Redes InterPlanetárias (InterPlanetary Networking Special Interest Group - IPNSIG) para ajudar a fazer o SSI real.


### Mais sobre Redes Tolerantes a Disrupção (Disruption Tolerant Networking)

* [Página da DTN TechPort](https://techport.nasa.gov/view/11772)
* [Junho de 2016 - New Solar System Internet Technology Debuts on the International Space Station](https://www.nasa.gov/feature/new-solar-system-internet-technology-debuts-on-the-international-space-station)
* [Dezembro de 2013 - Disruption Tolerant Networking Experiments with Optical Communications](https://www.nasa.gov/directorates/heo/scan/news_DTN_Experiments_with_Optical_Communications.html)

### Additional Information:

* [DTN Tutorial](http://ipnsig.org/wp-content/uploads/2015/09/DTN_Tutorial_v3.2.pdf)
* [CCSDS Bundle Protocol Specification](http://public.ccsds.org/publications/archive/734x2b1.pdf)
* [Licklider Transmission Protocol for CCSDS](http://public.ccsds.org/publications/archive/734x1b1.pdf)
* [CCSDS Solar System Internetwork (SSI) Architecture](http://public.ccsds.org/publications/archive/730x1g1.pdf)
* [Rationale, Scenarios, and Requirements for DTN in Space](http://public.ccsds.org/publications/archive/734x0g1e1.pdf)
* [Bundle Protocol Specification RFC5050](https://tools.ietf.org/html/rfc5050)

<figure>
<iframe width="420" height="315" src="https://www.youtube.com/embed/0gCMIiJdYPQ" frameborder="0" allowfullscreen></iframe>
<figcap>This animation shows how our traditional Internet Protocols (IP) can be disrupted and cause delays or data losses, then shows how the Delay/Disruption Tolerant Network (DTN) allows data to be transmitted even when there is poor connectivity.
<br/>Credits: NASA
</figcap>
<figure>