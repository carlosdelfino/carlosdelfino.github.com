---
layout: archive
permalink: /
title: "Lateost Posts"
---
Estamos trabalhando em um novo site, agora usando o Jekyll, com o layout Skinny Bones

<div class="tiles">
{% for post in site.posts %}
	{% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->
