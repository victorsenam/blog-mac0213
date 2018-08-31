---
layout: post
title: Estatísticas
hours: 0
solved: 0
---

{% for post in site.posts %}
    {% assign minutes = minutes | plus: post.minutes %}
{% endfor %}

{{ minutes | divided_by: 60 | floor }}:{{ minutes | modulo: 60 | divided_by: 10 | floor }}{{ minutes | modulo: 60 | modulo: 10 }} horas registradas.
