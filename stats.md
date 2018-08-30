---
layout: post
title: Estatísticas
hours: 0
solved: 0
---

{% for post in site.posts %}
    {% assign minutes = minutes | plus: post.minutes %}
    {% assign solved = solved | plus: post.solved %}
{% endfor %}

Seguem algumas estatísticas úteis sobre o meu progresso na matéria. A ideia de inserir estes contadores foi inspirada por (basicamente copiada de) [Nathan Benedetto Proença](http://github.com/nathanPro) com a permissão do mesmo.

- Horas de Treinos Registradas: **{{ minutes | divided_by: 60 | floor }}:{{ minutes | modulo: 60 }}**
- Problemas Resolvidos em Contest Registrados: **{{ solved }}**
