---
permalink: /links/
title: Uma coleção de links
excerpt: Aqui coleciono links, sites que acho interessante, estão categorizados pelas tags que representam.
layout: archive
share: true 
---
<div class="tiles">
{{ site.categories }}
{% for post in site.categories.colecaolinks %}
   {% include link-list-bullets.html %}
{% endfor %}
</div><!-- /.tiles -->
