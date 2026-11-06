# Phase 2: Get listed

Owner: Humberto. Use exactly the NAP from `00-index.md` everywhere. Paste-ready text, order of work and Search Console steps: [02a-listing-copy.md](02a-listing-copy.md).

## Tasks

- [x] **Fix the business phone line (blocker)** — resolved 2026-10-21 by switching the site to +351 911 045 538 (tested end to end by Humberto 2026-11-02). Old line +351 910 193 681 (eSIM, WhatsApp Business) sends but doesn't receive calls, SMS or WhatsApp messages. Check before creating listings:
  - [ ] Is the number registered on the **WhatsApp Business Platform / Cloud API** (e.g. via a Meta developer app or webhook)? A Cloud API number can't be used in the WhatsApp app at the same time, and incoming messages go to the webhook, not the phone. If so, either remove it from the API (Meta Business Manager → WhatsApp Manager → delete number) and register it in the WhatsApp Business app, or keep the API and make sure the webhook stores/forwards messages.
  - [ ] With the operator: is the eSIM plan active for **incoming** voice/SMS (some digital/data or virtual numbers are outbound-only), and is call forwarding or "do not disturb"/call barring off? Test by calling and texting from another phone with WhatsApp closed.
  - [ ] Phone settings: the eSIM line is enabled for calls/SMS (dual-SIM default line), not just data.
  - [x] Test end to end from another phone: call, SMS, WhatsApp, and the site's WhatsApp button (`wa.me` link). Done by Humberto 2026-11-02.
  - [ ] Until fixed: decide whether to hide the phone/WhatsApp from the site and keep email + Calendly + form only.

- [ ] **Google Business Profile** — created 2026-10-31 under formigagalatica@gmail.com; most important item for "informática Almada"-type searches (map results). **Switched to service-area business, address hidden** on 2026-11-03 (first video failed: home office has no signage; the 2026-11-01 "address shown" decision is reversed).
  - [x] Created: name, category "Computer consultant", address, service areas (Almada, Seixal, Barreiro, Setúbal, Sesimbra, Lisboa), phone, website, services, description, hours Mon–Wed (and probably Thu) 09:00–18:00.
  - [x] First video uploaded 2026-11-02 — **not accepted** ("Verification not successful. To get verified, submit another recording").
  - [x] 2026-11-03: address hidden via Edit profile → Location → "Show business address to customers" off (Claude, in Chrome, confirmed saved: "No location; deliveries and home services only", 6 service areas kept). Hours now Mon–Fri 09:00–18:00, Sat–Sun closed.
  - [ ] **Record a new video live in the Business Profile app (Humberto, phone)** — service-area version: street sign + house number 14 at the address, workspace/equipment, business card or invoice with "FORMIGAGALÁCTICA", you opening the company email or the profile on screen (management proof). At least 30 s, unedited, no ID/bank/NIF in frame, no other people's faces. Tap **Review issues** first and note Google's exact rejection reason.
  - [ ] If it fails again: Google Business Profile help → Contact us.
  - [ ] **After approval:** replace description and the "Ferramentas feitas à medida" service text (still have the old "proposta com preço fechado e prazo" wording; new text in `02a-listing-copy.md`); Friday and weekend hours already set (Mon–Fri 09:00–18:00, closed Sat–Sun); add a secondary category; logo (`assets/brand/png/icon-orange-512.png`) and cover (`assets/og-image.png`); Humberto's own photo; first post (link to the free diagnostic).
- [x] **Google Search Console** — domain property `galaticos.pt` was already verified; sitemap `https://formiga.galaticos.pt/sitemap.xml` submitted 2026-10-31 (status Success, 9 pages discovered); indexing requested for `/`, `/en/`, `/diagnostico-gratuito/`, `/notas/`.
- [ ] **Bing Webmaster Tools** — import from Search Console (can be done now, no need to wait for Google verification). Bing feeds ChatGPT search and Copilot.
- [ ] **Bing Places for Business** — import from Google Business Profile once it is verified; same data, address hidden (service-area business).
- [ ] **Apple Business Connect** — Apple Maps / Siri. Needs Humberto's Apple Account; same data, address hidden (service-area business).
- [ ] Give Claude the Search Console / Bing verification codes if a meta-tag verification is needed instead of DNS.
