---
redirect_from: /Carlos_Delfino_-_Consultoria_e_Projetos
layout: home
permalink: /
excerpt: Seja Bem vindo ao nosso site, Dicas, Macetes, Artigos sobre microcontroladores AVR, ARM e Arduino, Programação em Java e PHP para Web Sistem distribuidos. Consultoria em Joomla e Moodle.
image:
   feature: carlosdelfino-palestra-400x161.png
title: "Início"
---
Estamos trabalhando em um novo site, agora usando o Jekyll, com o layout Skinny Bones

<div class="tiles">
{% for post in site.posts %}
	{% include post-grid.html %}
{% endfor %}
</div>
<!-- /.tiles -->
