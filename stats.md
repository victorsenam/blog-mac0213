---
layout: post
title: Estatísticas
hours: 0
solved: 0
---

{% for post in site.posts %}
    {% assign minutes = minutes | plus: post.minutes %}
{% endfor %}

- Horas Registradas: **{{ minutes | divided_by: 60 | floor }}:{{ minutes | modulo: 60 }}**
