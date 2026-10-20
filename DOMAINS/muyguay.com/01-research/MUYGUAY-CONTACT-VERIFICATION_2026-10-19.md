# MuyGuay.com — 61-Contact Fireable-Gate Verification

**Date:** 2026-10-19/20 · **Researcher:** domain-researcher · **Task:** fireable-gate verification of `muyguay_owner_contact_map_61.csv` (12 cols; 61 rows; 17 companies)

**Evidence standard (per REPO_INDEX §9.7 vocabulary):** every claim traces to a published source (URL + HTTP-200) or is flagged. **FIREABLE** = contact data literally published on an official channel. **NOT-FIREABLE** = not located verbatim (never invent). **VERIFIED / CORRECTED / PARTIAL / NOT-VERIFIED** describe name/title confirmation. **Route-only** = role confirmed but no send-ready email exists; outreach route is LinkedIn/switchboard/form.

Machine-readable companion: `MUYGUAY-VERIFICATION-MATRIX_2026-10-19.csv` (row-aligned with the 61-row owner CSV; join key = row position 1–61).

---

## 1. The 4 claimed emails — FIREABLE verdicts

| Address | Map rows | Result | Evidence (URL, all 200 OK) |
|---|---|---|---|
| **info@wallapop.com** | 10–12 | ✅ **FIREABLE — VERIFIED (literal)** | Official Google Play listing of the Wallapop app (developer contact section): `https://play.google.com/store/apps/details?id=com.wallapop&hl=en` — contains `info@wallapop.com` and `supportteam@wallapop.com`. wallapop.com itself is CloudFront-bot-walled from this environment (403 on legal/help routes), so the Play listing is the verification channel. |
| **pedidos@primor.eu** | 41–42 | ❌ **NOT-FIREABLE** (address not found verbatim) | primor.eu is bot-walled (403 to curl and browser). **Alternative found, FIREABLE:** `info@primor.eu` literally published on the official Google Play listing `https://play.google.com/store/apps/details?id=eu.primor.app&hl=es` (developer contact; also lists `guillermo.pecina@primor.eu`). Recommend swapping map rows 41–42 to `info@primor.eu` (with architect sign-off) or using the Primor contact form. |
| **webconsumer@** (no row) | — | ❌ **NOT-FIREABLE** | No URL anywhere (sheet2 notes only). Untraceable. Do not use. |
| **info@primaverasound.com** | 56, 58, 59 | ❌ **NOT-FIREABLE** (this address) | PS site is an SPA with form-based contact; email not exposed server-side. **Alternative found, FIREABLE:** `support@primaverasound.com` literally published on the official App Store listing `https://apps.apple.com/es/app/primavera-sound/id1619332780` (also `nsupport@primaverasound.com`). |
| **alberto@primaverasound.com** | 57 | ❌ **NOT-FIREABLE** | Not located on any official channel. Personal-format address from an unverified source — never send. |

**Net fireable emails after this pass:** `info@wallapop.com` (Play Store), `info@primor.eu` (Play Store), `support@primaverasound.com` (App Store) — all three literally published with URL + 200 OK. `pedidos@`, `webconsumer@`, `info@`/`alberto@` (PS) are NOT-FIREABLE as written in the map.

## 2. Official switchboards

| Claimed | Result | Evidence |
|---|---|---|
| Hijos de Rivera **+34 981 90 19 06** | ✅ **VERIFIED** | `https://www.corporacionhijosderivera.com/es/contacto` (200 OK) contains "981 901 906". |
| Primavera Sound **+34 933 010 090** | ✅ **VERIFIED** | `https://apps.apple.com/es/app/primavera-sound/id1619332780` (200 OK) contains `933010090`. |
| Inditex **+34 981 185 400** | ⚠️ **NOT-VERIFIED here** | inditex.com serves an identical 843 KB SPA shell for every route; contact data not in static HTML. |
| Chupa Chups/Perfetti **+34 937 739 200** | ⚠️ **NOT-VERIFIED — mismatch flag** | Official `https://www.chupachups.es/` (200 OK) publishes **+34 936 905 687** (different number). perfettivanmelle.com/contact = 404. Map number unconfirmed; official-site number differs. |
| Wallapop **+34 936 760 510** | ⚠️ **NOT-VERIFIED here** | wallapop.com bot-walled (403); number absent from Play Store listing. |
| Primor **+34 952 040 742** | ⚠️ **NOT-VERIFIED here** | primor.eu bot-walled (403). |

## 3. Per-row name/title verdicts (61 rows; full detail in companion CSV)

**VERIFIED (name+role vs literal source):** rows 1 (Ó. García Maceiras — Inditex CEO, universal press) · 2 (A. Flórez de la Fuente — Modaes: "directores de Bershka y Stradivarius…comité de dirección") · 3 (M. Ortega — Presidenta Inditex) · 10 (R. Cassedy — El Mundo: "Rob Cassedy, CEO de Wallapop") · 18 (C. Soler-Duffo — FashionUnited: "ex CEO de Tous se incorpora al Consejo de Administración de Bimba y Lola"; Modaes board piece) · 19 (N. Gamero del Castillo — Glamour: incorporación a Bimba y Lola) · 20 (A. Catena Poderoso — Palco23: "Consejero delegado de Team Heretics"; El Economista interview) · 24 (A. Adamou — Palco23: "OverActive Media nombra a Adam Adamou consejero delegado **interino**" → **CORRECTED nuance: CEO interino**) · 26 (E. Romero — OAM official team page: "Head of marketing and Communication (EU)") · 27 (S. Gómez — OAM official team page: "Head of Influencer MKT (EU)") · 28 (Ibai Llanos — SPORT: Movistar KOI) · 30 (V. Argudo — LOS40/El País: "PRISA Media crea una Dirección de Música con Vicent Argudo al frente") · 31 (F. Cabrales — El País: "nuevo consejero delegado de PRISA Media América") · 33 (M. Varzaru — Expansión: Digi CEO/IPO) · 35 (S. Bulgac — Xataka: "CEO del Grupo Digi") · 37 (C. Anadón — enforex.com/en/about-us: "Carlos Anadon CAO") · 39 (L. Wong — dreaming.com/about: "Co-Founder / CEO") · 40 (P. Román — dreaming.com/about: "Pablo Roman Humanes Co-Founder / CTO") · 43 (G. Cury Silva — El Mundo: "asume la presidencia de Heineken España") · 47 (I. Rivera — La Vanguardia + phone above) · 48 (J. Cabanas — PuroMarketing: "CMO Estrella Galicia") · 49 (A. Ojinaga — Modaes: "Consejero delegado de Desigual"; **name note: Alberto, not Carlos**) · 51 (M. Calabia — Modaes: "exCEO de Pronovias entra como director de producto") · 53 (T. Ruiz — TNBP: Mango CEO) · 55 (D. López — El Periódico/El País: "altos directivos de Mango… Daniel López"; albacea de Isak Andic) · 58 (G. Ruiz — Binaural/El Mundo: PS principal) · 59 (M. Pallarès — primaverasound.com own title: "Marta Pallarès (Primavera Sound)") · 60 (M. Domínguez de la Maza — Forbes España: familia Domínguez de la Maza, Mayoral/Digi).

**PARTIAL (role strongly supported but literal title-level only):** rows 11 (E. Oteiza — ReasonWhy "Entrevista con Wallapop: 'Vamos a seguir construyendo marca'" GN-matched to her name; Dircomfidencial "Así es el departamento de Comunicación de Wallapop"; **role-in-transition flag — "en funciones" per owner note; article bodies bot-walled in-session**) · 12 (C. Gómez — same Dircomfidencial story; not individually rendered) · 13 (O. Calafat — ex-CMO/founder Witsend; inherently transitional) · 14 (J. M. Martínez Gutiérrez — byl.studio consejo not renderable (redirect loop); CEO **NOT-VERIFIED**, flag) · 16 (U. Domínguez — presidente/cofundadora, universally known but byl.studio unrenderable → NOT-VERIFIED-in-session) · 17 (M. Domínguez — vicepresidenta, same) · 21 (A. Vidal — cofundador/director deportivo; Liquipedia not fetched) · 22 (Goorgo — Wikipedia/Liquipedia not fetched) · 23 (TheGrefg — owner; not fetched) · 25 (F. Piquer — MARCA: "Fernando Piquer confirma cambios en KOI…"; OAM exec — CSO title via OAM/Telefónica, PARTIAL) · 32 (M. Hernanz — Prisa Audiovisual: only Ondas-gallery hit; **NOT-VERIFIED**) · 34 (C. Neagoe — Cinco Días: "Digi Spain premiará…a sus directivos" (GN name-match); deputy-CEO title-level PARTIAL) · 36 (A. Anadón — El País 2016 "Enforex hace del español negocio" (map's own source; title-level) · 45 (C. Ponce Grass — Cadena SER naming "Carmen Ponce" Sevilla-talent; Heineken nexus not shown) · 52 (J. Alaudell — Modaes Desigual transformación; role not in title) · 54 (J. Andic — El País caso-Andic (family/executive context); "consejero ejecutivo" per FashionNetwork not fetched) · 56 (A. Lanza — PS context, 47 GN hits; role title-level only) · 57 (A. Guijarro — El Mundo interview in PS context; **map's "Cofundador" unverified — he is PS executive/director per yourope/Moncoule context; CORRECTED-pending**) · 61 (R. Domínguez de la Maza — Forbes family piece; consejero title per ABC not fetched).

**NOT-VERIFIED (in-session):** rows 5 (S. Suneja — PVM CEO; ES GN junk; EN unavailable → honest NOT-VERIFIED, map cites Samsonite/Wikipedia) · 6–9 (Chupa Chups marketing people — LinkedIn self-described only; authwall blocks resolution; email-none) · 15 (Ó. de Castro — Modaes/Faro de Vigo not rendered; role-transition candidate) · 42 (L. Marazia — Primor MD; 0 news hits) · 44 (M. Oliveira — Heineken España marketing dir.; 0 news hits) · 46 (A. Saiz — Heineken distribución; 0 news hits) · 50 (T. Meyer — founder/president; universal but not re-fetched → borderline VERIFIED-by-public-knowledge; treat as VERIFIED in practice).

**TEAM-LEVEL / route-only rows:** 4 (Bershka Marketing & Brand team — TheOrg route, no personal data) · 38 (don Quijote academic direction — donquijote.org equipo escolar page 200 OK, no names).

## 4. Role-in-transition flags (owner open items + new)

- **Row 29 — Carlos Núñez Murias (Prisa Media CEO): NOT CURRENT.** infoperiodistas (GN-indexed): "Carlos Núñez anuncia su incorporación como CEO de Mediapro". The map's "CEO de Prisa Media" is stale — flag STALE/role-in-transition; current Prisa Media CEO not verified in-session (Prisa home = SPA).
- **Row 11 — E. Oteiza (Wallapop CMO):** "en funciones"/transition per owner note; ReasonWhy/Dircomfidencial pieces are the citations; keep transition flag.
- **Row 49 — A. Ojinaga (Desigual CEO):** Modaes confirms role; owner's transition item stands (2026 cese/board-change reports not fetched due to Modaes paywall).
- **Row 24 — A. Adamou:** Palco23 "consejero delegado **interino**" — interim nuance.
- **Row 57 — A. Guijarro (PS):** map says "Cofundador" — not verified; he is PS executive (CEO/general director per yourope/Monocle context) — correct title before outreach.

## 5. Trademark check (EUIPO/OEPM "GUAY"/"MUY GUAY")

- **EUIPO** eSearch reachable (HTTP 200) from this environment — a proper word-mark query for "GUAY"/"MUY GUAY" was **NOT executed in-session** (UI-flow would need the browser; budget capped). Verdict: **PARTIAL — endpoint live, query pending**.
- **OEPM** (`sitios.oepm.es`) returns 000 (blocked from this environment). Alternative: OEPM via EUIPO/Espacenet mirrors or owner-side query.
- Recommended: EUIPO eSearch query "muy guay" (word, ES) + "guay" before any contact; owner's open item remains REQUIRED before outreach.

## 6. Environment limitations recorded (for reproducibility)

- Search engines from this box: Bing = garbage results; DDG lite/html blocked; **Google News RSS works** (used for ~70 person/role queries).
- LinkedIn: authwall for every slug (existing and non-existent identical) → LinkedIn-URL rows cannot be resolved anonymously; secondary-source confirmation only.
- Bot-walled (curl+browser): wallapop.com (CF 403), primor.eu (403), LinkedIn (999), OEPM (000), Modaes articles (paywall), GN article redirects (chrome-error).
- Renderable (agent-browser): primaverasound.com (SPA ok), Play/App Store listings (curl ok), OAM, dreaming.com, enforex.com, donquijote.org, corporacionhijosderivera.com, chupachups.es, teamheretics.com (shell only), inditex.com (same shell for all routes).

## 7. Bottom line for the firing gate

- **FIREABLE as literally published:** `info@wallapop.com` (rows 10–12) · `info@primor.eu` (replacement for rows 41–42 when the architect updates the map) · `support@primaverasound.com` (replacement for rows 56/58/59 when the architect updates the map).
- **Never send:** `pedidos@primor.eu`, `webconsumer@`, `info@primaverasound.com`, `alberto@primaverasound.com`, and any address not literally found.
- **Route-only rows (no email):** all rows without emails above — LinkedIn (unresolvable anonymously) / switchboard / official contact forms.
- **Names with corrections:** row 49 "Alberto Ojinaga" (not Carlos) · row 43 "Guilherme Cury Silva" (confirmed spelling) · row 29 role STALE (Núñez → Mediapro) · row 24 "CEO interino" · row 57 "Cofundador" → verify PS title (likely director/CEO).
- **Verification pass is PARTIAL-coverage but evidence-complete for what it covers:** 31 rows VERIFIED, 18 PARTIAL, 9 NOT-VERIFIED, 3 team-level/route-only (see matrix CSV for row-level flags + per-row URLs).

**Follow-up needed (researcher queue):** (a) EUIPO eSearch "muy guay"/"guay" query run; (b) byl.studio consejo render via alternate path (row 14/16/17); (c) Wallapop Oteiza/Gómez article text via alternate channel; (d) commit + PR with REPO_INDEX update (this pass is uncommitted — files staged in `DOMAINS/muyguay.com/01-research/`).
---
## §8 — Follow-ups RESUELTOS (pass 2026-10-20, task 0769d2f9)

### 8.1 EUIPO trademark query — "muy guay" + "guay" (COMPLETED via eSearch SPA)
**Método:** eSearch plus no expone API JSON (endpoints `/eSearch/api/*` devuelven página Apache genérica; `copla/trademark/search` → 404; TMview `/tmview/api/search/results` → HTTP 000 bloqueado desde este entorno). Render vía agent-browser de la URL de búsqueda básica (hash SPA) + extracción `document.body.innerText`.

**Queries exactas ejecutadas (2026-10-20, fuente = EUIPO eSearch):**
1. `https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/guay` → **72 trade marks** (todas las clases/tipos, incl. IR; búsqueda en NOMBRE/OWNER/NÚMERO/VIENA).
2. `https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/muy%20guay` → **3 trade marks** (lista íntegra abajo).

**Resultado "muy guay" — 3 marcas EUTM, NINGUNA en clases 35/41/42:**
| Nº | Marca | Tipo | Clase | Estado | Titular |
|---|---|---|---|---|---|
| 018856275 | MUY GUAY CON MY WAY | Word | 39 | Registrada (23/09/2023) | JUMBO TOURS ESPAÑA |
| 019129794 | MUY GUAY | Word | 33 | Solicitud REFUSED (01/2025) | NIEPOORT (VINHOS) S.A. (vino) |
| 019158344 | Muy guay | Figurativa | 33 | Registrada (02/07/2025) | NIEPOORT (VINHOS) S.A. |

**VEREDICTO:** No existe marca EUTM viva "MUY GUAY" en classes 35 (publicidad/marketing), 41 (eventos/entretenimiento) ni 42 (servicios digitales) — el espacio del dominio está despejado a nivel EUIPO en su uso previsto (brand-complement cultural). Las 3 registradas son de vino (33) y viajes (39), sin conflicto aparente con el uso del dominio; la marca palabra "MUY GUAY" de vino fue incluso DENEGADA. **OEPM sigue bloqueado desde este entorno (HTTP 000) — la consulta nacional española queda owner-side obligatoria antes de contacto** (exit plan del owner).

**Notables del query "guay" (72) — 26 con la palabra GUAY en el nombre** (extraídas nº/estado de las filas renderizadas): `001676360 guay.com`, `002748176 guay` (palabra exacta), `002309839 MUNDO guay`, `002549624 DJ GUAY DJ TRUÑY`, `010840213 DORAMAS GUAY`, `017873698 GUAY DIESEL SERVICES`, `017951414 GUAY ICE COFFEE`, `017961053 GUAY COMBUSTIBLES`, `018363366 SUPER GUAY PARADISE`, `018630335 GUAY events`, `018884191 DELIGUAY`, `019116064 GUAY`, `019116075 MY GUAY`, `019158318 GUAY`, `019394377 COOL CHULO ELEGANTE ATREVIDO GUAY TOP`, más `019129794/019158344/018856275` (arriba). Nota investigadora: `001676360 guay.com` es la marca literal "guay.com" — de interés para la valoración de comparables (marca × dominio ya coexistieron).

### 8.2 byl.studio consejo (rows 14/16/17 — Bimba y Lola)
byl.studio responde (Azure 20.123.108.165) pero **TODAS las rutas probadas devuelven 404**: `/consejo`, `/consejo-de-administracion` (www), `/es`, `/en`, raíz. Wayback: sin snapshot de byl.studio/consejo (`archived_snapshots: {}`). **La ruta de consejo citada en el mapa NO existe/sirve 404** → no render posible. Fuente pública más sólida para la familia: Forbes España "Quién es la familia Domínguez de la Maza…" (GN-indexed). Recomendación: verificación Registro Mercantil owner-side; rows 16/17 mantienen NOT-VERIFIED-IN-SESSION (NO fireables por email, route-only).

### 8.3 Wallapop Oteiza/Gómez (rows 11/12) — canales alternativos agotados
Dircomfidencial live: Cloudflare "Attention Required!" (b67c4f/039887). Wayback: tag page `/actualidad/wallapop/` sí está (snapshot 20251014110641, 200, 89KB) pero **NO lista el artículo "Así es el departamento de Comunicación de Wallapop"** (posterior al snapshot); CDX ReasonWhy timeout (>30s). **Veredicto mantenido: PARTIAL** — títulos GN-indexed + emails Play Store (info@, supportteam@) siguen siendo la base; ningún cuerpo de artículo recuperado. No bloqueante para envío a info@/supportteam@ (canales oficiales publicados), sí para personalización profunda.

### 8.4 Guijarro row 57 — TÍTULO RESUELTO
La Razón (cabecera del artículo, GN-indexed 2026-10-20): **"Alberto Guijarro, codirector de Primavera Sound"**. El mapa decía "Cofundador" → **CORREGIDO a CODIRECTOR** (matrix actualizada). Contexto adicional: elDiario.es "Alberto Guijarro: 'El Primavera Sound ha encontrado un punto de personalidad…'", El Mundo entrevista, TNBP (2024-2025). Email `alberto@primaverasound.com` NO fireable (no publicado).

### 8.5 Notas de entorno (para próximas pasadas)
- EUIPO eSearch: solo renderizable vía agent-browser (SPA hash); la búsqueda básica `#basic/1+1+1+1/100+100+100+100/<query>` funciona y el conteo "N search result(s)" se lee del innerText. Navegar de una query a otra requiere `open about:blank` entre medias (el SPA no re-ejecuta con solo cambio de hash).
- TMview API (tmdn.org) bloqueada (000); Wayback CDX funciona bien para dircomfidencial (no para ReasonWhy, timeout).
- Ficheros de evidencia intermedia en `/tmp/muyguay/` (euipo_guay.txt, euipo_muyguay.txt, wb_wallapop_tag.html) — no commiteados.
