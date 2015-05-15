---
redirect_from: 
 - "/Carlos_Delfino_-_Consultoria_e_Projetos/"
 - "/Carlos_Delfino_-_Consultoria_e_Projetos/Inicio.html"
layout: home
permalink: /
image:
   feature: carlosdelfino-palestra-400x161.png
title: "Início"
---
Seja Bem-Vindo ao meu site, aqui você vai encontrar:

 * Dicas e Macetes em geral;
 * Artigos sobre microcontroladores AVR, ARM e Prototipação com Arduino, e outros;
 * Programação em Java e PHP para Web Sistem distribuidos. 
 * Consultoria em Linux, JBoss, Joomla e Moodle.

<!-- more -->

Abaixo estão listados as últimas 20 publicações que fiz até agora, para 
encontrar outras publicações visite o link [Categorias](/categorias/), ou 
procure por "[tags](/tags)".  

<hr />

# Artigos 
<div class="tiles">
{% for post in site.posts limit:20 %}
   {% if post.feature.index %}   
      {% include post-grid.html %}	
   {% endif %}
{% endfor %}
</div>
<!-- /.tiles -->
