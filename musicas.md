---
permalink: /musicas/
title: Músicas que eu Curto Escutar
layout: archive
share: true
comments: true
image:
  feature: musicas_filmes/mesadesom-2000x962.jpg
  teaser: musicas_filmes/mesadesom-300x144.jpg
---
<div class="tiles">
{% for post in site.categories.musicas %}
   {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->
