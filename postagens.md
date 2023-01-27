---
layout: index
permalink: /postagens/
title: "Últimas Postagens"
share: true
ads:
  style: horizontal
---
Últimos artigos escritos para este site.

<!--more-->

Os artigos aqui postados quando tendo o nome de autor como *Carlos Delfino*, é de inteira responsabilidade deste, porém alguns arigos podem ser copias, com a devida autorização, de outros sites ou escrito por amigos especialmente para este site, neste caso, compartilha-se com o autor original da ideia expostas mas não se toma como  responsável pelo que foi escrito e por sua originalidade.

Estes artigos não tem cunho acadêmico ou jornalístico, mas podem vir a ser base ou baseados de alguma publicação acadêmica que participamos.

Para ver esta listagem por [categorias](/categorias) ou [tags](/tags) clique no respectivo link.

<div class="tiles">
{% for post in site.posts %}
	{% unless post.noshow.posts %}
		{% include grids/post-grid.html %}
	{% endunless %}
{% endfor %}
</div><!-- /.tiles -->
