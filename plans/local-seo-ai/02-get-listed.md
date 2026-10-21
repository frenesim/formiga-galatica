# Phase 2: Get listed

Owner: Humberto. Use exactly the NAP from `00-index.md` everywhere.

## Tasks

- [x] **Fix the business phone line (blocker)** — resolved 2026-10-21 by switching the site to +351 911 045 538 (still to test: call, SMS, WhatsApp and the `wa.me` button). Old line +351 910 193 681 (eSIM, WhatsApp Business) sends but doesn't receive calls, SMS or WhatsApp messages. Check before creating listings:
  - [ ] Is the number registered on the **WhatsApp Business Platform / Cloud API** (e.g. via a Meta developer app or webhook)? A Cloud API number can't be used in the WhatsApp app at the same time, and incoming messages go to the webhook, not the phone. If so, either remove it from the API (Meta Business Manager → WhatsApp Manager → delete number) and register it in the WhatsApp Business app, or keep the API and make sure the webhook stores/forwards messages.
  - [ ] With the operator: is the eSIM plan active for **incoming** voice/SMS (some digital/data or virtual numbers are outbound-only), and is call forwarding or "do not disturb"/call barring off? Test by calling and texting from another phone with WhatsApp closed.
  - [ ] Phone settings: the eSIM line is enabled for calls/SMS (dual-SIM default line), not just data.
  - [ ] Test end to end from another phone: call, SMS, WhatsApp, and the site's WhatsApp button (`wa.me` link).
  - [ ] Until fixed: decide whether to hide the phone/WhatsApp from the site and keep email + Calendly + form only.

- [ ] **Google Business Profile** — the most important item for "informática Almada"-type searches (map results).
  - Category: "Consultor de informática" (add "Serviço de desenvolvimento de software").
  - Service area: Almada, Seixal, Barreiro, Setúbal, Sesimbra. Hide the address if working from home.
  - Description, hours, phone, website, link to the Calendly booking.
  - Add photos (logo, founder photo) and the first post (link to the free diagnostic).
- [ ] **Google Search Console** — add domain property `galaticos.pt` (verify via Cloudflare DNS TXT), submit `https://formiga.galaticos.pt/sitemap.xml`.
- [ ] **Bing Webmaster Tools** — import from Search Console. Bing feeds ChatGPT search and Copilot.
- [ ] **Bing Places for Business** — same data as Google Business Profile.
- [ ] **Apple Business Connect** — Apple Maps / Siri.
- [ ] Give Claude the Search Console / Bing verification codes if a meta-tag verification is needed instead of DNS.
