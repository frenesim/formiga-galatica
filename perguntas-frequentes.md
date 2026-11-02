---
layout: page
lang: pt
alt_url: /en/faq/
title: "Software à medida: perguntas frequentes"
permalink: /perguntas-frequentes/
description: "Respostas curtas sobre ferramentas de software feitas à medida para pequenas empresas: diagnóstico gratuito, preço, prazo, a quem se destina e onde trabalhamos."
faq:
  - q: "Como funciona o diagnóstico gratuito?"
    a: "É uma conversa de 30 minutos, sem compromisso, sobre o que teria maior impacto no dia a dia da empresa. Escolhemos consigo o problema com maior impacto que dê para resolver em poucas semanas. Não é uma auditoria nem um questionário."
  - q: "Quanto custa uma ferramenta feita à medida?"
    a: "Depende do problema e do que a ferramenta inclui. Por isso começamos por um primeiro passo pequeno, escolhido na conversa inicial, e combinamos o que inclui e quanto custa antes de começar."
  - q: "Quanto tempo demora?"
    a: "Um primeiro passo, pequeno, demora poucas semanas. O tempo concreto depende do problema, e falamos dele na conversa inicial. Depois do primeiro passo, decidimos juntos o que vem a seguir."
  - q: "A ferramenta fica minha?"
    a: "Sim. A ferramenta fica propriedade do cliente, sem mensalidades obrigatórias por utilizador. A manutenção é opcional."
  - q: "Para que tipo de empresas trabalham?"
    a: "Para pequenas empresas de escritórios e serviços (contabilistas, advogados, clínicas, imobiliárias), de oficinas e obras (construção, reparações, manutenção, pequenas fábricas) e de alojamento local."
  - q: "Onde trabalham?"
    a: "Atendemos presencialmente em Almada, Seixal, Barreiro, Setúbal, Sesimbra e Lisboa, e à distância em todo o país. Também recebemos no nosso escritório em Charneca da Caparica (Almada), por marcação."
  - q: "Têm trabalho que possa ver?"
    a: "Sim. O Agile Booking, uma ferramenta de gestão de alojamento local, está em uso desde 2015. A Tekclean, uma ferramenta de gestão comercial, está em uso desde 2020. Ambos estão descritos na secção Trabalho feito da página inicial."
  - q: "E se acharem que não podem ajudar?"
    a: "Dizemos-lhe com franqueza, na própria conversa, e não há qualquer custo."
---

<p class="lead">Respostas curtas às perguntas mais comuns. Se a sua não estiver aqui, <a href="{{ '/' | relative_url }}#contacto">escreva-nos</a>.</p>

{% for f in page.faq %}
## {{ f.q }}

{{ f.a }}
{% endfor %}

[Marcar conversa gratuita →]({{ site.company.calendly }}) · [Saber mais sobre o diagnóstico]({{ '/diagnostico-gratuito/' | relative_url }})
