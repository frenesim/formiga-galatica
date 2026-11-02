# Phase 2: Get listed

Owner: Humberto. Use exactly the NAP from `00-index.md` everywhere. Paste-ready text, order of work and Search Console steps: [02a-listing-copy.md](02a-listing-copy.md).

## Tasks

- [x] **Fix the business phone line (blocker)** — resolved 2026-10-21 by switching the site to +351 911 045 538 (still to test: call, SMS, WhatsApp and the `wa.me` button). Old line +351 910 193 681 (eSIM, WhatsApp Business) sends but doesn't receive calls, SMS or WhatsApp messages. Check before creating listings:
  - [ ] Is the number registered on the **WhatsApp Business Platform / Cloud API** (e.g. via a Meta developer app or webhook)? A Cloud API number can't be used in the WhatsApp app at the same time, and incoming messages go to the webhook, not the phone. If so, either remove it from the API (Meta Business Manager → WhatsApp Manager → delete number) and register it in the WhatsApp Business app, or keep the API and make sure the webhook stores/forwards messages.
  - [ ] With the operator: is the eSIM plan active for **incoming** voice/SMS (some digital/data or virtual numbers are outbound-only), and is call forwarding or "do not disturb"/call barring off? Test by calling and texting from another phone with WhatsApp closed.
  - [ ] Phone settings: the eSIM line is enabled for calls/SMS (dual-SIM default line), not just data.
  - [ ] Test end to end from another phone: call, SMS, WhatsApp, and the site's WhatsApp button (`wa.me` link).
  - [ ] Until fixed: decide whether to hide the phone/WhatsApp from the site and keep email + Calendly + form only.

- [ ] **Google Business Profile** — created 2026-10-31 under formigagalatica@gmail.com; most important item for "informática Almada"-type searches (map results). Address **shown** (decided 2026-11-01: clients can visit the office by appointment).
  - [x] Created: name, category "Computer consultant", address, service areas (Almada, Seixal, Barreiro, Setúbal, Sesimbra, Lisboa), phone, website, services, description, hours Mon–Wed (and probably Thu) 09:00–18:00.
  - [x] Video verification uploaded by Humberto on 2026-11-02. Google reviews it; the profile stays "Verification required" until approved. Do not edit name, address or category while it is pending.
  - [ ] **After approval:** replace description and the "Ferramentas feitas à medida" service text (still have the old "proposta com preço fechado e prazo" wording; new text in `02a-listing-copy.md`); confirm Friday and the weekend (closed) hours; add a secondary category; logo (`assets/brand/png/icon-orange-512.png`) and cover (`assets/og-image.png`); Humberto's own photo; first post (link to the free diagnostic).
- [x] **Google Search Console** — domain property `galaticos.pt` was already verified; sitemap `https://formiga.galaticos.pt/sitemap.xml` submitted 2026-10-31 (status Success, 9 pages discovered); indexing requested for `/`, `/en/`, `/diagnostico-gratuito/`, `/notas/`.
- [ ] **Bing Webmaster Tools** — import from Search Console (can be done now, no need to wait for Google verification). Bing feeds ChatGPT search and Copilot.
- [ ] **Bing Places for Business** — import from Google Business Profile once it is verified; same data, address shown.
- [ ] **Apple Business Connect** — Apple Maps / Siri. Needs Humberto's Apple Account; same data, address shown.
- [ ] Give Claude the Search Console / Bing verification codes if a meta-tag verification is needed instead of DNS.
