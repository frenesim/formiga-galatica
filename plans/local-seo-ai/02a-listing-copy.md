# Phase 2 kit: copy and order of work

Paste-ready text for Google Business Profile, Bing Places and Apple Business Connect. Use the same text on all three (NAP consistency). Facts come from the site and `llms.txt`; change them here first if they change.

## Order of work

1. **Test the phone end to end** (call, SMS, WhatsApp, the site's `wa.me` button) from another phone. Google may verify by phone or SMS.
2. **Search Console** (fast, and the sitemap starts being read).
3. **Google Business Profile** (verification can take days, so start early).
4. **Bing Webmaster Tools**: import from Search Console.
5. **Bing Places**: import from Google Business Profile once it is verified.
6. **Apple Business Connect**.

## Decision before creating the Business Profile

- **DECIDED 2026-11-01: show the address.** Clients can visit the office (first door of the house) by appointment. Keep Google as created (address shown); use the same on Bing and Apple, and state "by appointment" in hours/notes. The question below is kept for the record.
- **Show the address, or service-area business with the address hidden?** Rua Rogério Paulo, 14, Charneca da Caparica is the registered address. Show it only if clients can visit you there; otherwise choose "I deliver goods and services to my customers" and hide it. Decide, then use the same choice on Bing and Apple. (The site footer and JSON-LD show the registered address either way; that is a legal requirement and doesn't conflict.)

## Google account

The profile is owned by the Google account that creates it: **formigagalatica@gmail.com** (humberto@galaticos.pt forwards there). Turn on two-step verification, and add a second owner later under Settings → People and access.

## Name, contact, categories

| Field | Value |
|---|---|
| Business name | Formiga Galática (no keywords added; Google rejects them) |
| Website | https://formiga.galaticos.pt/ |
| Phone | +351 911 045 538 |
| Email | humberto@galaticos.pt |
| Hours | Mon–Fri 09:00–18:00 |
| Primary category | **Not verified.** Type "consultoria", "TI" and "informática" in the category box and pick the most specific IT-consulting option offered (Google's own advice: one primary category, as specific as possible) |
| Secondary categories | Type "software" and pick the closest software-development option, if one is offered |
| Service area | Almada, Seixal, Barreiro, Setúbal, Sesimbra, Lisboa |
| Languages | Português, English |
| Appointment link | https://calendly.com/humberto-pinto1 |

## Description (PT, 629 characters; limit 750)

> A Formiga Galática é uma pequena consultora de informática em Almada. Criamos ferramentas úteis, feitas à medida, para várias areas de negócio: orçamentos, recolha de documentos dos clientes, marcações, registo de horas e materiais, gestão de reservas. Começamos por uma conversa gratuita e sem compromisso sobre o que mais pesa no dia a dia da empresa. Escolhemos o problema com maior impacto que dê para resolver em poucas semanas, resolvemo-lo e, se fizer sentido, crescemos a partir daí. A ferramenta fica propriedade do cliente, sem mensalidades obrigatórias por utilizador. Atendemos Almada, Seixal, Barreiro, Setúbal, Sesimbra e Lisboa, presencialmente, e todo o país à distância.

## Description (EN, 594 characters), for Bing and Apple if they offer English

> Formiga Galática is a small IT consultancy in Almada, Portugal. We build useful, tailor-made tools for multiple business areas: quotes, collecting documents from clients, appointments, hours and materials tracking, booking management. We start with a free, no-commitment conversation about what weighs most on the business day to day. We pick the problem with the biggest impact that can be solved in a few weeks, solve it and, if it makes sense, grow from there. The client owns the tool, with no mandatory per-user subscription. We serve Almada, Seixal, Barreiro, Setúbal, Sesimbra and Lisbon in person, and the whole country remotely.

## Services (Google "Services" section; no prices, they depend on the pricing model)

| Service | Description |
|---|---|
| Diagnóstico informático gratuito | Conversa de 30 minutos, sem compromisso, sobre o que mais pesa no dia a dia da empresa. Escolhemos juntos por onde começar. |
| Ferramentas feitas à medida | Programas simples para o trabalho da empresa. Começamos pelo problema com maior impacto que dê para resolver em poucas semanas. A ferramenta fica propriedade do cliente. |
| Substituição de folhas de Excel | Passar informação espalhada por várias folhas para uma ferramenta única, com uma só versão. |
| Orçamentos e acompanhamento de obras | Orçamentos, registo de horas e materiais, do orçamento à fatura sem repetir dados. |
| Recolha de documentos dos clientes | Pedidos, lembretes e receção de ficheiros num só sítio, com a lista de quem entregou e quem falta. |
| Redução de mensalidades de programas | Rever os programas que a empresa paga todos os meses e o que usa de facto. |

## First post (Google "Updates")

> **Diagnóstico informático gratuito para pequenas empresas**
> Uma conversa de 30 minutos sobre o que, na sua opinião, teria maior impacto no dia a dia da empresa. Escolhemos juntos o problema por onde começar, um que dê para resolver em poucas semanas. Sem compromisso.
> Button: **Marcar** → https://calendly.com/humberto-pinto1

(Or "Learn more" → https://formiga.galaticos.pt/diagnostico-gratuito/)

## Photos

- Logo (square): `assets/brand/png/icon-orange-512.png`
- Cover/share image (1200×630): `assets/og-image.png`
- A photo of Humberto (needed: not in the repo)
- Do not use stock photos.

## Search Console steps

(Done 2026-10-31: the domain property already existed; sitemap and indexing requests are in. Steps below kept for reference.)

1. https://search.google.com/search-console → Add property → **Domain** → `galaticos.pt`.
2. Copy the TXT record it shows. Cloudflare → `galaticos.pt` → DNS → Add record → type TXT, name `@`, paste value, DNS only. Back in Search Console, **Verify**.
3. If a URL-prefix property for `https://formiga.galaticos.pt/` already exists (the `googlea439…html` file), keep it; the domain property is in addition.
4. Sitemaps → enter `sitemap.xml` → Submit.
5. URL inspection → paste `https://formiga.galaticos.pt/` → Request indexing; repeat for `/en/`, `/diagnostico-gratuito/` and `/notas/`.
