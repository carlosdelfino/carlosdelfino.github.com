---
layout: index
title: Certificados
permalink: /certificados/
share: true
toc: false
comments: false
ads:
  show: true
image:
  feature: carlosdelfino-palestra-400x161.png
---

Aqui estão listados meus certificados de cursos, treinamentos e eventos que participei.

<!--more-->

<style>
.certificados-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
  margin: 2rem 0;
}
.certificado-card {
  width: 280px;
  border: 1px solid #ddd;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
  background: #fff;
  text-align: center;
}
.certificado-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}
.certificado-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
}
.certificado-card .titulo {
  padding: 0.75rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: #333;
}
/* Modal/Lightbox para exibir o certificado */
.cert-modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.8);
  z-index: 99999;
  justify-content: center;
  align-items: center;
}
.cert-modal-overlay.active {
  display: flex;
}
body.cert-modal-open {
  overflow: hidden;
}
.cert-modal-content {
  position: relative;
  width: 90%;
  max-width: 900px;
  height: 85vh;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}
.cert-modal-content object,
.cert-modal-content embed,
.cert-modal-content iframe,
.cert-modal-content img {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
}
.cert-modal-content img {
  object-fit: contain;
}
.cert-modal-fallback {
  text-align: center;
  padding: 2rem;
}
.cert-modal-fallback a {
  color: #448dd6;
  font-size: 1.1rem;
  font-weight: 600;
}
.cert-modal-close {
  position: absolute;
  top: 10px; right: 16px;
  font-size: 2rem;
  color: #fff;
  background: rgba(0,0,0,0.5);
  border: none;
  border-radius: 50%;
  width: 40px; height: 40px;
  cursor: pointer;
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
}
</style>

<!-- Modal para exibir certificado -->
<div class="cert-modal-overlay" id="certModal">
  <button class="cert-modal-close" onclick="fecharModal()">&times;</button>
  <div class="cert-modal-content" id="certModalContent">
  </div>
</div>

<div class="certificados-gallery">
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--semana-dos-reparos-em-inversores-solares.png" alt="Semana Dos Reparos Em Inversores Solares" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--semana-dos-reparos-em-inversores-solares.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Semana Dos Reparos Em Inversores Solares</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--instructiva-analise-de-datasheets.png" alt="Instructiva Analise De Datasheets" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--instructiva-analise-de-datasheets.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Instructiva Analise De Datasheets</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--tmtd-tecnicas-de-manutencao-por-teste-de-dispositivos.png" alt="Tmtd Tecnicas De Manutencao Por Teste De Dispositivos" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--tmtd-tecnicas-de-manutencao-por-teste-de-dispositivos.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Tmtd Tecnicas De Manutencao Por Teste De Dispositivos</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--instructiva-manuseio-de-osciloscopio.png" alt="Instructiva Manuseio De Osciloscopio" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--instructiva-manuseio-de-osciloscopio.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Instructiva Manuseio De Osciloscopio</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--instructiva-dicas-de-reparo-em-fontes-chaveadas.png" alt="Instructiva Dicas De Reparo Em Fontes Chaveadas" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--instructiva-dicas-de-reparo-em-fontes-chaveadas.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Instructiva Dicas De Reparo Em Fontes Chaveadas</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--instructiva-reparos-na-pratica-em-fontes-chaveadas.png" alt="Instructiva Reparos Na Pratica Em Fontes Chaveadas" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--instructiva-reparos-na-pratica-em-fontes-chaveadas.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Instructiva Reparos Na Pratica Em Fontes Chaveadas</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--instructiva-especialista-em-substituicao-de-componentes-e-engenharia-reversa-de-pcb.png" alt="Instructiva Especialista Em Substituicao De Componentes E Engenharia Reversa De Pcb" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--instructiva-especialista-em-substituicao-de-componentes-e-engenharia-reversa-de-pcb.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Instructiva Especialista Em Substituicao De Componentes E Engenharia Reversa De Pcb</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--eletronica-para-iniciantes-instructiva.png" alt="Eletronica Para Iniciantes Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--eletronica-para-iniciantes-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Eletronica Para Iniciantes Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/instructiva--especialista-em-manutencao-de-fontes-chaveadas-20-instructiva.png" alt="Especialista Em Manutencao De Fontes Chaveadas 20 Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/instructiva--especialista-em-manutencao-de-fontes-chaveadas-20-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Especialista Em Manutencao De Fontes Chaveadas 20 Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/ingles_1-comprovante_de_inscricao_1926248-curso-de-ingles-aprenda-mais.png" alt="Ingles 1 Comprovante De Inscricao 1926248 Curso De Ingles Aprenda Mais" onclick="abrirModal('{{ site.baseurl }}/certificados/ingles_1-comprovante_de_inscricao_1926248-curso-de-ingles-aprenda-mais.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Ingles 1 Comprovante De Inscricao 1926248 Curso De Ingles Aprenda Mais</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/embarcatech-2025-1-etapa.png" alt="Embarcatech 2025 1 Etapa" onclick="abrirModal('{{ site.baseurl }}/certificados/embarcatech-2025-1-etapa.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Embarcatech 2025 1 Etapa</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/masterclass-esp32-introducao-completa-certificado.png" alt="Masterclass Esp32 Introducao Completa Certificado" onclick="abrirModal('{{ site.baseurl }}/certificados/masterclass-esp32-introducao-completa-certificado.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Masterclass Esp32 Introducao Completa Certificado</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/freertos-essencial-com-stm32-uc-e5db1a00-4fbf-4768-99ee-533ed2d6d82e.png" alt="Freertos Essencial Com Stm32 Uc E5Db1A00 4Fbf 4768 99Ee 533Ed2D6D82E" onclick="abrirModal('{{ site.baseurl }}/certificados/freertos-essencial-com-stm32-uc-e5db1a00-4fbf-4768-99ee-533ed2d6d82e.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Freertos Essencial Com Stm32 Uc E5Db1A00 4Fbf 4768 99Ee 533Ed2D6D82E</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/hackathon-hack-to-work.png" alt="Hackathon Hack To Work" onclick="abrirModal('{{ site.baseurl }}/certificados/hackathon-hack-to-work.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Hackathon Hack To Work</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/principais-desafios-para-desenvolvimento-de-carreira.png" alt="Principais Desafios Para Desenvolvimento De Carreira" onclick="abrirModal('{{ site.baseurl }}/certificados/principais-desafios-para-desenvolvimento-de-carreira.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Principais Desafios Para Desenvolvimento De Carreira</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/hack-to-work-formacao-conecta-futuro-tech.png" alt="Hack To Work Formacao Conecta Futuro Tech" onclick="abrirModal('{{ site.baseurl }}/certificados/hack-to-work-formacao-conecta-futuro-tech.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Hack To Work Formacao Conecta Futuro Tech</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/diploca-fic-faculdade-integrada-do-ceara-projeto-e-implementacao-de-redes-de-computadores.png" alt="Diploca Fic Faculdade Integrada Do Ceara Projeto E Implementacao De Redes De Computadores" onclick="abrirModal('{{ site.baseurl }}/certificados/diploca-fic-faculdade-integrada-do-ceara-projeto-e-implementacao-de-redes-de-computadores.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Diploca Fic Faculdade Integrada Do Ceara Projeto E Implementacao De Redes De Computadores</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/freertos-from-ground-up-on-arm-processors.png" alt="Freertos From Ground Up On Arm Processors" onclick="abrirModal('{{ site.baseurl }}/certificados/freertos-from-ground-up-on-arm-processors.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Freertos From Ground Up On Arm Processors</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/mastering-stm32cubemx-5-and-cubeide-embedded-systems.png" alt="Mastering Stm32Cubemx 5 And Cubeide Embedded Systems" onclick="abrirModal('{{ site.baseurl }}/certificados/mastering-stm32cubemx-5-and-cubeide-embedded-systems.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Mastering Stm32Cubemx 5 And Cubeide Embedded Systems</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/tudo-sobre-manuseio-de-osciloscopio-instructiva.png" alt="Tudo Sobre Manuseio De Osciloscopio Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/tudo-sobre-manuseio-de-osciloscopio-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Tudo Sobre Manuseio De Osciloscopio Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/especialista-em-substituicao-de-componentes-e-engenharia-reversa-de-pcb-instructiva.png" alt="Especialista Em Substituicao De Componentes E Engenharia Reversa De Pcb Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/especialista-em-substituicao-de-componentes-e-engenharia-reversa-de-pcb-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Especialista Em Substituicao De Componentes E Engenharia Reversa De Pcb Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/dicas-de-reparos-em-fontes-chaveadas-instructiva.png" alt="Dicas De Reparos Em Fontes Chaveadas Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/dicas-de-reparos-em-fontes-chaveadas-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Dicas De Reparos Em Fontes Chaveadas Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/analise-de-datasheet-instructiva.png" alt="Analise De Datasheet Instructiva" onclick="abrirModal('{{ site.baseurl }}/certificados/analise-de-datasheet-instructiva.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Analise De Datasheet Instructiva</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/gerenciamento-de-projetos-utilizando-a-metodologia-do-pmi-bolsa-de-valores-regional-do-ceara.png" alt="Gerenciamento De Projetos Utilizando A Metodologia Do Pmi Bolsa De Valores Regional Do Ceara" onclick="abrirModal('{{ site.baseurl }}/certificados/gerenciamento-de-projetos-utilizando-a-metodologia-do-pmi-bolsa-de-valores-regional-do-ceara.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Gerenciamento De Projetos Utilizando A Metodologia Do Pmi Bolsa De Valores Regional Do Ceara</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/desvendando-um-projeto-social-gpl-lgpl.png" alt="Desvendando Um Projeto Social Gpl Lgpl" onclick="abrirModal('{{ site.baseurl }}/certificados/desvendando-um-projeto-social-gpl-lgpl.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Desvendando Um Projeto Social Gpl Lgpl</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/etica-profissional-dominio-informatica.png" alt="Etica Profissional Dominio Informatica" onclick="abrirModal('{{ site.baseurl }}/certificados/etica-profissional-dominio-informatica.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Etica Profissional Dominio Informatica</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/proprio-programacao-de-orientacao-ao-candidato-a-empresario.png" alt="Proprio Programacao De Orientacao Ao Candidato A Empresario" onclick="abrirModal('{{ site.baseurl }}/certificados/proprio-programacao-de-orientacao-ao-candidato-a-empresario.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Proprio Programacao De Orientacao Ao Candidato A Empresario</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/planet-internet-telephony-gateway-voip-recitronic.png" alt="Planet Internet Telephony Gateway Voip Recitronic" onclick="abrirModal('{{ site.baseurl }}/certificados/planet-internet-telephony-gateway-voip-recitronic.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Planet Internet Telephony Gateway Voip Recitronic</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/conexao-digital-novas-tecnologias-para-maior-produtividade-e-sustentabilidade-das-ongs.png" alt="Conexao Digital Novas Tecnologias Para Maior Produtividade E Sustentabilidade Das Ongs" onclick="abrirModal('{{ site.baseurl }}/certificados/conexao-digital-novas-tecnologias-para-maior-produtividade-e-sustentabilidade-das-ongs.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Conexao Digital Novas Tecnologias Para Maior Produtividade E Sustentabilidade Das Ongs</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/seminario-big-data-analise-de-dados-e-inteligencia-corportaiva-implementacao-de-solucoes-analiticas-avancadas-envolvendo-mineracao-integracao-e-visualizacao.png" alt="Seminario Big Data Analise De Dados E Inteligencia Corportaiva Implementacao De Solucoes Analiticas Avancadas Envolvendo Mineracao Integracao E Visualizacao" onclick="abrirModal('{{ site.baseurl }}/certificados/seminario-big-data-analise-de-dados-e-inteligencia-corportaiva-implementacao-de-solucoes-analiticas-avancadas-envolvendo-mineracao-integracao-e-visualizacao.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Seminario Big Data Analise De Dados E Inteligencia Corportaiva Implementacao De Solucoes Analiticas Avancadas Envolvendo Mineracao Integracao E Visualizacao</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/palestra-ministrada-arduino-e-suas-aplicacoes-fic-faculdade-integrada-do-ceara.png" alt="Palestra Ministrada Arduino E Suas Aplicacoes Fic Faculdade Integrada Do Ceara" onclick="abrirModal('{{ site.baseurl }}/certificados/palestra-ministrada-arduino-e-suas-aplicacoes-fic-faculdade-integrada-do-ceara.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Palestra Ministrada Arduino E Suas Aplicacoes Fic Faculdade Integrada Do Ceara</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-seguranca-de-redes-insoft.png" alt="Curso Seguranca De Redes Insoft" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-seguranca-de-redes-insoft.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Seguranca De Redes Insoft</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/introducao-ao-rup-rational-unified-process-insoft.png" alt="Introducao Ao Rup Rational Unified Process Insoft" onclick="abrirModal('{{ site.baseurl }}/certificados/introducao-ao-rup-rational-unified-process-insoft.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Introducao Ao Rup Rational Unified Process Insoft</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-gestao-de-pessoas-e-lideranca-una.png" alt="Curso Gestao De Pessoas E Lideranca Una" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-gestao-de-pessoas-e-lideranca-una.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Gestao De Pessoas E Lideranca Una</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/paqlestra-o-que-voce-ve-ver-diferente-para-ser-diferente-senac-mg.png" alt="Paqlestra O Que Voce Ve Ver Diferente Para Ser Diferente Senac Mg" onclick="abrirModal('{{ site.baseurl }}/certificados/paqlestra-o-que-voce-ve-ver-diferente-para-ser-diferente-senac-mg.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Paqlestra O Que Voce Ve Ver Diferente Para Ser Diferente Senac Mg</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/mini-curso-de-eletrotecnica-eeep-professora-alda-facanha.png" alt="Mini Curso De Eletrotecnica Eeep Professora Alda Facanha" onclick="abrirModal('{{ site.baseurl }}/certificados/mini-curso-de-eletrotecnica-eeep-professora-alda-facanha.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Mini Curso De Eletrotecnica Eeep Professora Alda Facanha</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/administracao-de-confloitos-una.png" alt="Administracao De Confloitos Una" onclick="abrirModal('{{ site.baseurl }}/certificados/administracao-de-confloitos-una.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Administracao De Confloitos Una</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/palestra-gestao-da-qualidade-de-vida-no-trabalho-senacmg.png" alt="Palestra Gestao Da Qualidade De Vida No Trabalho Senacmg" onclick="abrirModal('{{ site.baseurl }}/certificados/palestra-gestao-da-qualidade-de-vida-no-trabalho-senacmg.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Palestra Gestao Da Qualidade De Vida No Trabalho Senacmg</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-ei-empreendedor-individual-sebrae-ce.png" alt="Curso Ei Empreendedor Individual Sebrae Ce" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-ei-empreendedor-individual-sebrae-ce.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Ei Empreendedor Individual Sebrae Ce</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-apf-analise-e-planejamento-financeiro.png" alt="Curso Apf Analise E Planejamento Financeiro" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-apf-analise-e-planejamento-financeiro.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Apf Analise E Planejamento Financeiro</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/palestra-off-balance-como-estrategia-de-captacao-de-recursos-senac-mg.png" alt="Palestra Off Balance Como Estrategia De Captacao De Recursos Senac Mg" onclick="abrirModal('{{ site.baseurl }}/certificados/palestra-off-balance-como-estrategia-de-captacao-de-recursos-senac-mg.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Palestra Off Balance Como Estrategia De Captacao De Recursos Senac Mg</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/desenvolvimento-de-aplicacoes-em-java-basico-e-avancado.png" alt="Desenvolvimento De Aplicacoes Em Java Basico E Avancado" onclick="abrirModal('{{ site.baseurl }}/certificados/desenvolvimento-de-aplicacoes-em-java-basico-e-avancado.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Desenvolvimento De Aplicacoes Em Java Basico E Avancado</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/masterclass-esp32_-introducao-completa-embarcados.png" alt="Masterclass Esp32  Introducao Completa Embarcados" onclick="abrirModal('{{ site.baseurl }}/certificados/masterclass-esp32_-introducao-completa-embarcados.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Masterclass Esp32  Introducao Completa Embarcados</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-xml-desenvolvimento-de-aplicacoes-insoft-sebrae.png" alt="Curso Xml Desenvolvimento De Aplicacoes Insoft Sebrae" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-xml-desenvolvimento-de-aplicacoes-insoft-sebrae.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Xml Desenvolvimento De Aplicacoes Insoft Sebrae</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-analise-e-projeto-de-sistemas-orientados-a-objeto-usando-uml-insoft-sebrae.png" alt="Curso Analise E Projeto De Sistemas Orientados A Objeto Usando Uml Insoft Sebrae" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-analise-e-projeto-de-sistemas-orientados-a-objeto-usando-uml-insoft-sebrae.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Curso Analise E Projeto De Sistemas Orientados A Objeto Usando Uml Insoft Sebrae</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/workshop-da-pos-em-ti-faculdade-pitagoras.png" alt="Workshop Da Pos Em Ti Faculdade Pitagoras" onclick="abrirModal('{{ site.baseurl }}/certificados/workshop-da-pos-em-ti-faculdade-pitagoras.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Workshop Da Pos Em Ti Faculdade Pitagoras</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/formacao-de-mobilizadores-comunitarios-pela-promocao-dos-direitos-humanos-e-defesa-da-democracia-fundo-brasil-mobilize.png" alt="Formacao De Mobilizadores Comunitarios Pela Promocao Dos Direitos Humanos E Defesa Da Democracia Fundo Brasil Mobilize" onclick="abrirModal('{{ site.baseurl }}/certificados/formacao-de-mobilizadores-comunitarios-pela-promocao-dos-direitos-humanos-e-defesa-da-democracia-fundo-brasil-mobilize.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Formacao De Mobilizadores Comunitarios Pela Promocao Dos Direitos Humanos E Defesa Da Democracia Fundo Brasil Mobilize</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/2026-04-03-championchip-introducao-aos-semicondutores.png" alt="2026 04 03 Championchip Introducao Aos Semicondutores" onclick="abrirModal('{{ site.baseurl }}/certificados/2026-04-03-championchip-introducao-aos-semicondutores.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">2026 04 03 Championchip Introducao Aos Semicondutores</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/embedded-expert-io--certificate-of-completion-for-mastering-stm32cubemx-5-and-cubeide-embedded-systems.png" alt="Certificate Of Completion For Mastering Stm32Cubemx 5 And Cubeide Embedded Systems" onclick="abrirModal('{{ site.baseurl }}/certificados/embedded-expert-io--certificate-of-completion-for-mastering-stm32cubemx-5-and-cubeide-embedded-systems.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificate Of Completion For Mastering Stm32Cubemx 5 And Cubeide Embedded Systems</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/embedded-expert-io--certificate-of-completion-for-freertos-from-ground-up-on-arm-processors.png" alt="Certificate Of Completion For Freertos From Ground Up On Arm Processors" onclick="abrirModal('{{ site.baseurl }}/certificados/embedded-expert-io--certificate-of-completion-for-freertos-from-ground-up-on-arm-processors.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificate Of Completion For Freertos From Ground Up On Arm Processors</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/embedded-expert-io--modern-bare-metal-embedded-c-programming-from-ground-uptm.png" alt="Modern Bare Metal Embedded C Programming From Ground Uptm" onclick="abrirModal('{{ site.baseurl }}/certificados/embedded-expert-io--modern-bare-metal-embedded-c-programming-from-ground-uptm.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Modern Bare Metal Embedded C Programming From Ground Uptm</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/gran-faculdade--certificado-curso-livre-lideranca-gran-faculdade.png" alt="Certificado Curso Livre Lideranca Gran Faculdade" onclick="abrirModal('{{ site.baseurl }}/certificados/gran-faculdade--certificado-curso-livre-lideranca-gran-faculdade.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado Curso Livre Lideranca Gran Faculdade</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/gran-faculdade--trilha-reinvencao-gran.png" alt="Trilha Reinvencao Gran" onclick="abrirModal('{{ site.baseurl }}/certificados/gran-faculdade--trilha-reinvencao-gran.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Trilha Reinvencao Gran</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/gran-faculdade--praticas-ageis-na-gran.png" alt="Praticas Ageis Na Gran" onclick="abrirModal('{{ site.baseurl }}/certificados/gran-faculdade--praticas-ageis-na-gran.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Praticas Ageis Na Gran</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/gran-faculdade--lideranca-360-influencia-proposito-e-alto-impacto.png" alt="Lideranca 360 Influencia Proposito E Alto Impacto" onclick="abrirModal('{{ site.baseurl }}/certificados/gran-faculdade--lideranca-360-influencia-proposito-e-alto-impacto.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Lideranca 360 Influencia Proposito E Alto Impacto</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica.png" alt="Certificado Curso De Eletronica" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado Curso De Eletronica</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-historico.png" alt="Certificado Curso De Eletronica Historico" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-historico.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado Curso De Eletronica Historico</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-verso.png" alt="Certificado Curso De Eletronica Verso" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-verso.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado Curso De Eletronica Verso</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-frente.png" alt="Certificado Curso De Eletronica Frente" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado-curso-de-eletronica-frente.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado Curso De Eletronica Frente</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_assinado.png" alt="Certificado   Curso De Eletronica Assinado" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_assinado.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado   Curso De Eletronica Assinado</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_-_verso_assinado.png" alt="Certificado   Curso De Eletronica   Verso Assinado" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_-_verso_assinado.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado   Curso De Eletronica   Verso Assinado</div>
</div>
<div class="certificado-card">
  <img src="{{ site.baseurl }}/certificados/thumbs/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_-_frente_assinado.png" alt="Certificado   Curso De Eletronica   Frente Assinado" onclick="abrirModal('{{ site.baseurl }}/certificados/curso-tecnico-de-eletronica-global-tec--certificado_-_curso_de_eletronica_-_frente_assinado.pdf', 'pdf')" title="Clique para visualizar">
  <div class="titulo">Certificado   Curso De Eletronica   Frente Assinado</div>
</div>
</div><!-- /.certificados-gallery -->

<script>
function abrirModal(url, tipo) {
  var overlay = document.getElementById('certModal');
  var content = document.getElementById('certModalContent');
  if (tipo === 'pdf') {
    content.innerHTML = '<object data="' + url + '" type="application/pdf" width="100%" height="100%"><p class="cert-modal-fallback">Seu navegador não suporta visualização de PDF embutido. <a href="' + url + '" target="_blank">Clique aqui para abrir o certificado</a></p></object>';
  } else {
    content.innerHTML = '<img src="' + url + '" alt="Certificado">';
  }
  overlay.classList.add('active');
  document.body.classList.add('cert-modal-open');
}
function fecharModal() {
  var overlay = document.getElementById('certModal');
  var content = document.getElementById('certModalContent');
  overlay.classList.remove('active');
  document.body.classList.remove('cert-modal-open');
  content.innerHTML = '';
}
document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById('certModal');
  if (modal && modal.parentNode !== document.body) {
    document.body.appendChild(modal);
  }
  modal.addEventListener('click', function(e) {
    if (e.target === this) fecharModal();
  });
});
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') fecharModal();
});
</script>
