---
redirect_from: "/cursoarduinominas"
permalink: /cursoarduino/
title: Curso Arduino Minas
layout: archive
share: true
comments: true
excerpt: "Abaixo estão listados os cursos que ministramos, ou estamos elaborando, use o campo comentário para obter mais informações."
---
<div class="tiles">
{% for post in site.categories.cursoarduino%}
   {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->

