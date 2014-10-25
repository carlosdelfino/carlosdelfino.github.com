---
permalink: /colecaodelinks/
title: Uma coleção de links
excerpt: Aqui coleciono links, sites que acho interessante, estão categorizados pelas tags que representam.
layout: archive
share: true 
---
<div class="bullets">
{% for post in site.categories.colecaodelinks %}
   {% include link-list-bullets.html %}
{% endfor %}
</div><!-- /.bullets -->
