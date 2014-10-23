---
permalink: /categorias/
title: Lista das Categorias Existentes
excerpt: Listagem de todas as categorias existentes no site
layout: archive
share: true 
---
<div class="tiles">
{% for category in site.categories%}
   {% include category-grid.html %}
{% endfor %}
</div><!-- /.tiles -->


