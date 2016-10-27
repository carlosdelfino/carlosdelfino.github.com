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

<p>
	<strong>
		<center>
	Para conhecer nosso Ambiente EAD, visite 
	<a href="http://arduino-minas.moodlecloud.com">http://arduino-minas.moodlecloud.com</a>.
		</center>
	</strong>
</p>

<hr />

Abaixo estão listadas as últimas 30 publicações de meu site, para 
 outras publicações visite o link [Categorias](/categorias/), ou 
procure por "[tags](/tags)".  

<hr />

# Artigos 
<div class="tiles">
{% if site.excerpt.index.limit %}
    {% assign limit = site.excerpt.index.size %}
{% else %}
    {% assign limit = 30 %}
{% endif %}
{% for post in site.posts limit:limit %}
   {% if post.feature.index %}   
      {% include post-grid.html %}	
   {% endif %}
{% endfor %}
</div>
<!-- /.tiles -->
