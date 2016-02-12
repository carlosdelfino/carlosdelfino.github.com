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
Seja Bem-Vindo!

Abaixo estão listadas as últimas 20 publicações de meu site, para 
 outras publicações visite o link [Categorias](/categorias/), ou 
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
