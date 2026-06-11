# Pune Neuro Society — Brand Guidelines & Theme Revision

**Scope:** Visual + front-end standards for the Neurological Society of Pune (NSP) website and the ICTRIMS 2026 sub-section.
**Source of truth:** `assets/css/main.css` (design tokens), `upcoming_conferences.html` and `neuromeets.html` (modern page pattern).
**Status:** Living document. Last revised 2026-06-11.

---

## 1. Current Theme Audit

### What exists today
- **Framework:** Static HTML pages + Bootstrap grid + a large pre-built theme stylesheet (`main.css`) driven by CSS custom properties under the `--ztc-*` namespace. Plugins: AOS (scroll animation), Slick (sliders), Magnific Popup, Nice Select, FontAwesome 6.
- **Design tokens are defined but under-used.** `main.css` exposes a complete token system in `:root` (≈19 text colors, ≈21 background colors, a 10–80px font-size scale, 5 font weights, one font family). Most newer pages ignore these and hard-code values inline instead.
- **Two visual "eras" coexist:**
  - *Legacy theme tokens* — warm accent palette (orange `#FB8500`/`#F54200`, green `#28AA4A`) inherited from the purchased template.
  - *Current NSP brand* — a cooler, clinical **navy + blue** palette introduced on the newer pages (`neuromeets.html`, `upcoming_conferences.html`): dark navy `#02111A`, medical blue `#007bff`, teal `#17a2b8`.
- **Header / nav / footer are duplicated per page** rather than templated. They are consistent because they're copy-pasted; there is no include mechanism.
- **Spacing** is handled by fixed-height spacer divs (`.space6` … `.space48`, in 2px steps) plus Bootstrap utilities.

### Findings (issues)
| # | Observation | Impact |
|---|---|---|
| A | Page-specific colors (`#007bff`, `#17a2b8`, `#02111A`) are hard-coded inline, not tokenized | Drift risk; hard to re-theme |
| B | Legacy orange/green tokens still present but visually off-brand for a medical society | Inconsistent identity if reused |
| C | Header/footer copy-pasted across 8+ pages | Maintenance cost, divergence risk |
| D | Mixed accent definitions between legacy `--ztc-*` and new inline blue | Ambiguity for new contributors |
| E | No documented type scale in use — headings sized ad hoc per page | Inconsistent hierarchy |

### Strengths to preserve
- Consistent **Manrope** typeface everywhere.
- Strong, recognizable **dark-navy hero → blue accent** language on recent pages.
- Clean card system (rounded corners, soft shadow, hairline border) that reads "premium / clinical."
- Solid responsive scaffolding (Bootstrap + off-canvas mobile menu).

---

## 2. Recommended Theme Improvements

1. **Adopt the navy + blue palette as the single official brand** (Section 3). Retire legacy orange/green for NSP-branded pages; keep them only where the old template still requires them.
2. **Promote the page-level accents into tokens.** Add `--nsp-navy`, `--nsp-blue`, `--nsp-teal`, etc. to `:root` so future pages reference variables instead of hex literals.
3. **Standardize the type scale** to the hierarchy in Section 4 instead of per-page font sizes.
4. **Componentize repeated UI** (hero, section heading + underline, session/info card, day/hall tabs) under a shared `sp-`/`nm-` prefix convention so conference pages stay visually identical.
5. **Keep new page styling self-contained** in a page `<style>` block when it's section-specific (matches the existing `neuromeets`/`conferences` pattern) — but pull shared primitives into `main.css` over time.
6. **Always reuse the canonical header, off-canvas menu, and footer** verbatim; never redesign them per page.

---

## 3. Color Palette

### Primary brand (official — use these)
| Role | Hex | Notes |
|---|---|---|
| **Navy (primary dark)** | `#02111A` | Hero base, headings, footer, card headers. Token: `--ztc-bg-bg-16` / `--ztc-text-text-14` |
| **Navy 2 (gradient mid)** | `#0a3d62` | Hero/card-header gradient partner |
| **Navy 3 (gradient end)** | `#1a5276` | Hero gradient tail only |
| **Medical Blue (primary accent)** | `#007bff` | Buttons, links, active tabs, icons, underlines |
| **Blue hover/deep** | `#0056b3` | Button/active hover states |
| **Teal (secondary accent)** | `#17a2b8` | Icon highlights, gradient end on "special" cards |
| **Light Blue (tints)** | `#9ecbff`, `#eaf3fc` | Badges, on-navy labels, table day rows |

### Neutrals
| Role | Hex |
|---|---|
| Page background (default) | `#ffffff` |
| Section background (alt) | `#f5f8fb` |
| Body text | `#1f2d3a` / `#444` |
| Muted text | `#5a6a7a` |
| Hairline border | `#eef2f7` / `#e3e9f0` |

### Status / utility (use sparingly)
| Role | Hex |
|---|---|
| Notice / caution band | bg `#fff3cd`–`#ffeeba`, border `#ffc107`, text `#856404` |
| Affirmative ("For", success) | `#1e7e34` / `#27ae60` |
| Negative ("Against", emphasis) | `#c0392b` / `#e74c3c` |

**Rule:** No new random hues. New accents must be a tint/shade of navy, blue, or teal. **Avoid flashy multi-hue gradients** — gradients are restricted to navy→navy or navy→teal.

---

## 4. Typography Hierarchy

- **Typeface:** `Manrope` (`--ztc-family-font1`), loaded via Google Fonts (`wght@200..800`). FontAwesome for icons only.
- **Weights:** 400 regular · 500 medium · 600 semibold · 700 bold · 800 black (`--ztc-weight-*`).
- **Scale:** use the `--ztc-font-size-font-sNN` tokens (10–80px, 2px steps).

| Level | Size | Weight | Usage |
|---|---|---|---|
| Display / H1 (hero) | 3.0–3.5rem (≈48–56px) | 800–900 | Page hero title only |
| H2 (section heading) | 2.1–2.2rem (≈34px) | 800 | Section titles, with the gradient underline |
| H3 (card / session title) | 1.4rem (≈22px) | 800 | Card headers, session names |
| H4 / label | 0.9rem (≈14px) | 800, uppercase, letter-spacing | Eyebrow labels, info-item titles |
| Body | 1rem (16px) | 400–600 | Paragraphs, slot topics |
| Small / meta | 0.84–0.9rem | 600–700 | Times, captions, chairpersons |
| Micro / badge | 11–13px | 700–800, uppercase | Badges, tags, pills |

Headings use navy `#02111A`; eyebrow labels and active accents use blue `#007bff`.

---

## 5. Button Styles

### Canonical site button — `.vl-btn7`
Pill button defined in `main.css`: `border-radius: 70px`, padding `18px 28px`, font `Manrope` 20px **bold**, `text-transform: capitalize`, with an optional rotating circular arrow (54px). White base that inverts to navy text on hover. **Use this for primary site CTAs** ("Join Now", "View Full Scientific Program") so conference pages match the rest of the site.

```html
<a href="..." class="vl-btn7"><span class="text">View Full Scientific Program</span></a>
```

### Page-level button — `.sp-btn` (conference pattern)
For dense conference UIs, a lighter pill variant is acceptable and already in use:
- `.sp-btn--primary` — blue gradient `#007bff → #0056b3`, white text, soft blue shadow, lifts on hover.
- `.sp-btn--ghost` — transparent with `rgba(255,255,255,.45)` border on dark heroes; inverts to white-on-navy on hover.

Standard: radius ≥ 40px (pill), bold label, an icon allowed on the left, a visible hover state (translateY lift or color invert). Never use square, flat, hover-less buttons.

---

## 6. Card Styles

A single card recipe across the site:
- Background `#fff`, **radius 16–24px**, **1px border `#eef2f7`**, soft shadow `0 6–8px 30–40px rgba(2,17,26,.07–.08)`.
- **Header band** (optional): navy gradient `#02111A → #0a3d62`, white text; "special" variants may end in teal `#17a2b8`.
- **Eyebrow / number pill** on dark headers: translucent blue chip (`rgba(0,123,255,.22)` bg, `#9ecbff` text).
- Hover affordance on interactive cards: `translateY(-3px)` + deepened shadow.
- Inner rows separated by hairline `#f0f3f7`; icons in blue/teal.

Variants in use: `nm-card` (NeuroMeets), `sp-session` (program session), `faculty-item` (faculty grid), info/notice/secretary blocks. All share the same radius + border + shadow DNA.

---

## 7. Conference Page Styling Standards

Conference (ICTRIMS) pages follow a fixed section order and pattern:

1. **Logo strip** — white band above the hero, partner logos centered, ~62px tall, separated by 1px dividers, equal optical height.
2. **Hero** — navy gradient (`#02111A → #0a3d62 → #1a5276`), faint background image at `opacity ~0.08`, eyebrow badge, big title, subtitle, an inline **meta row** (date / venue / halls with teal icons), then a CTA pair (primary + ghost).
3. **Section rhythm** — alternate white and `#f5f8fb` (`--alt`) sections; each opens with a centered `h2 + sub + gradient underline` heading block.
4. **"At a glance" table** — navy header row, light-blue day-divider rows, horizontal scroll on mobile, em-dash (`—`) for empty halls.
5. **Detailed program** — **Day tabs** (1/2/3) → **Hall sub-tabs** (A/B) → **session cards** with a header (session no., title, time, chairpersons) and **slot rows** (`time | topic | speaker`).
6. **Semantic slot decorations** — badges for Quiz / Panel / Debate / CPC / Ceremony; For/Against rows for debates; full-width dashed bands for breaks, tinted bands for meals.
7. **AOS** `fade-up` / `zoom-in` on entrance; `AOS.init({ once: true })`.
8. **Download CTA** to the brochure PDF in both hero and footer of the section.

Data must be **real HTML** transcribed from the official program — never embedded PDF images or screenshots.

---

## 8. Logo Usage Guidelines

- **Use official logos only.** Never generate, recreate, or approximate a partner logo. Crop from the official source artwork (e.g., brochure cover) when a file is missing.
- **Canonical ICTRIMS partner set** lives in `assets/img/ictrims/`:
  - `logo-nsp.jpg` — Neurological Society of Pune
  - `logo-ian.jpg` — Indian Academy of Neurology
  - `logo-ictrims.jpg` — ICTRIMS
  - `logo-ecf.jpg` — European Charcot Foundation
- **NSP master logo:** `assets/img/logo/21-Logo.png` (header/footer), `21-Logo-sm.png` (mobile off-canvas), `preloader.png` (loader).
- **Aspect ratio:** never stretch. Constrain by height only (`height:62px; width:auto; object-fit:contain`); let width float. Maintain clear space around each mark.
- **Placement:** partner logos belong in a dedicated white logo strip, optically balanced and equal height, in the order NSP → IAN → ICTRIMS → ECF.
- **Background:** place logos on white or very light backgrounds for legibility; do not drop full-color logos directly on the navy hero.

---

## 9. Spacing System

- **Vertical spacers:** fixed-height utility divs `.space6 … .space48` in **2px increments** (`<div class="space24"></div>`). Use these for predictable gaps between stacked blocks.
- **Section padding:** `80px` top/bottom on desktop (`.sp-section`), reduced to `~50px` on mobile.
- **Card padding:** header `24px 30px`, body `~10–40px`; tighten to `~20px` on mobile.
- **Component gaps:** grid/flex `gap` in a 4px-based rhythm (12 / 14 / 16 / 18 / 20 / 24 px).
- **Radius scale:** chips/badges 6–30px · buttons 40–70px (pill) · cards 16–24px.
- **Grid:** Bootstrap 12-col (`container` / `row` / `col-lg-*`) for page layout; CSS grid for internal slot rows.

Keep to this ladder — avoid arbitrary one-off pixel values.

---

## 10. Mobile Responsiveness Standards

- **Breakpoints (Bootstrap-aligned):** `≤991px` (tablet), `≤576px` (phone), plus a `≤450px` off-canvas width tweak.
- **Navigation:** desktop inline menu (`d-none d-lg-block`) ↔ hamburger + off-canvas drawer (`d-block d-lg-none`); the drawer is populated from `.vl-mobile-menu-active` by `main.js`.
- **Layout reflow:** multi-column grids collapse to 2-up then 1-up; the program "slot" grid (`time | topic | speaker`) collapses from 3 columns → 2 → 1 stacked.
- **Tables:** wrap in an `overflow-x:auto` container so wide schedules scroll horizontally instead of breaking layout.
- **Hero:** reduce padding and title size (`3.4rem → 2.1rem`); stack CTA buttons full-width.
- **Tap targets:** tabs/buttons remain ≥ ~40px tall; day tabs go `flex:1` to fill the row.
- **Images:** `max-width:100%`, `object-fit:contain`; logo strip shrinks to ~46px and hides dividers.
- **Test matrix:** verify at 1440 / 991 / 576 / 360 px widths.

---

# How `ictrims-2026-scientific-program.html` Follows These Guidelines

| Guideline | How the page complies |
|---|---|
| **1 – Audit / consistency** | Built by cloning the proven `neuromeets.html` pattern: identical header, off-canvas menu, footer, preloader, scroll-progress widget, and the full plugin/script stack — so it reads as native to the site, not a new design. |
| **2 – Theme direction** | Uses only the navy + blue + teal brand language; page-specific styles are scoped in a single `<style>` block under the `sp-` prefix (matching the existing convention), no legacy orange/green. |
| **3 – Color palette** | Navy `#02111A → #0a3d62 → #1a5276` hero, blue `#007bff` accents/active states, teal `#17a2b8` icons, alt sections `#f5f8fb`, hairline `#eef2f7`. The amber band is reused only for the official "Anigre Hall" notice. No off-palette hues; gradients restricted to navy/teal. |
| **4 – Typography** | Inherits Manrope from `main.css`; hero H1 ≈3.4rem/900, section H2 ≈2.1rem/800 with the gradient underline, session H3 1.4rem/800, uppercase micro-badges at 11px — matching the documented scale. |
| **5 – Buttons** | The cross-link from `upcoming_conferences.html` uses the canonical `.vl-btn7`; in-page CTAs use `.sp-btn--primary` (blue gradient) and `.sp-btn--ghost` (outline on navy), both pill-shaped with hover lift/invert. |
| **6 – Cards** | Every session is an `.sp-session` card: white, radius 20px, 1px `#eef2f7` border, soft shadow, navy gradient header with a translucent blue number pill; "special" cards (symposia, free papers) end the header gradient in teal. |
| **7 – Conference standards** | Implements the full prescribed order: logo strip → navy hero with meta row + dual CTA → "Program at a Glance" table → Day tabs → Hall A/B sub-tabs → session cards with `time/topic/speaker` slots, plus semantic badges (Quiz/Panel/Debate/CPC), For/Against rows, and break/meal bands. All content is real HTML transcribed from the PDF — no embedded images. |
| **8 – Logos** | Displays the four official marks from `assets/img/ictrims/` (`logo-nsp`, `logo-ian`, `logo-ictrims`, `logo-ecf`) in the correct order, on a white strip, `height:62px; width:auto; object-fit:contain` to preserve aspect ratios. No generated logos. |
| **9 – Spacing** | 80px section padding (50px mobile), card padding `24px 30px`, gap rhythm in 4px steps, badge/button/card radii on the documented ladder; Bootstrap grid for page structure. |
| **10 – Responsiveness** | Reuses the site's off-canvas mobile nav; `@media` at 991/576/450px; the 3-column slot grid collapses to 2→1, the glance table scrolls horizontally, the hero shrinks and stacks its buttons, and the logo strip drops to 46px and hides dividers. |

**Net result:** the page is production-ready and visually indistinguishable in language from the rest of the NSP site, while fully encoding the ICTRIMS 2026 scientific program as accessible, responsive HTML.
