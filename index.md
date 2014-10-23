---
layout: home
permalink: /
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
