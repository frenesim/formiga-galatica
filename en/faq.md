---
layout: page
lang: en
locale: en_GB
alt_url: /perguntas-frequentes/
title: "Made-to-measure software: FAQ"
permalink: /en/faq/
description: "Short answers about made-to-measure software tools for small businesses: the free diagnostic, price, timing, who it is for and where we work."
faq:
  - q: "How does the free diagnostic work?"
    a: "It is a 30-minute conversation, with no commitment, about what would make the biggest difference to your business day to day. We pick with you the problem with the biggest impact that can be solved in a few weeks. It is not an audit or a questionnaire."
  - q: "How much does a made-to-measure tool cost?"
    a: "It depends on the problem and on what the tool includes. That is why we start with a small first step, chosen in the first conversation, and we agree what it includes and what it costs before we begin."
  - q: "How long does it take?"
    a: "A small first step takes a few weeks. The exact time depends on the problem, and we talk about it in the first conversation. After the first step, we decide together what comes next."
  - q: "Do I own the tool?"
    a: "Yes. The tool belongs to the client, with no mandatory per-user monthly fees. Maintenance is optional."
  - q: "What kind of businesses do you work with?"
    a: "Small businesses in offices and services (accountants, lawyers, clinics, estate agents), workshops and construction (building, repairs, maintenance, small factories) and short-term rentals."
  - q: "Where do you work?"
    a: "In person in Almada, Seixal, Barreiro, Setúbal, Sesimbra and Lisbon, and remotely anywhere in Portugal. We also receive clients at our office in Charneca da Caparica (Almada), by appointment."
  - q: "Do you have work I can see?"
    a: "Yes. Agile Booking, a short-term rental management tool, has been in use since 2015. Tekclean, a sales management tool, has been in use since 2020. Both are described in the Work section of the home page."
  - q: "What if you don't think you can help?"
    a: "We tell you honestly, in the conversation itself, at no cost."
---

<p class="lead">Short answers to the most common questions. If yours isn't here, <a href="{{ '/en/' | relative_url }}#contacto">write to us</a>.</p>

{% for f in page.faq %}
## {{ f.q }}

{{ f.a }}
{% endfor %}

[Book a free call →]({{ site.company.calendly }}) · [More about the diagnostic]({{ '/en/free-diagnostic/' | relative_url }})
