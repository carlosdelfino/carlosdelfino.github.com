---
redirect_from: 
 - "/Carlos_Delfino_-_Consultoria_e_Projetos/"
 - "/Carlos_Delfino_-_Consultoria_e_Projetos/Inicio.html"
layout: home
permalink: /
excerpt: Seja Bem-Vindo ao nosso site, Dicas, Macetes, Artigos sobre microcontroladores AVR, ARM e Arduino, Programação em Java e PHP para Web Sistem distribuidos. Consultoria em Joomla e Moodle.
image:
   feature: carlosdelfino-palestra-400x161.png
title: "Início"
---

**Estamos trabalhando em um novo site, agora usando o Jekyll, com o layout Skinny Bones.**

Em cada artigo/post há a possibilidae de deixar sua sugestão e dúvidas sobre o tema tratádo.
Mesmo que um artigo ainda esteja sendo escrito, quando já for possível abrir uma debate sobre
o tema estarei publicando para que todos possam contribuir com comentários e dúvidas, permitindo
assim que o artigo seja direcionado conforme as necessidades de cada um.

<hr />
 
<div class="tiles">
{% for post in site.posts %}
   {% if post.feature.index %}
      {% include post-grid.html %}	
   {% endif %}
{% endfor %}
</div>
<!-- /.tiles -->
