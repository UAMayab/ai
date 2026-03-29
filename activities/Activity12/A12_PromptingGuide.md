# A12 — Prompting Guide for Claude.ai
## How to Build the Patitas Chic Website Step by Step

This guide teaches you how to work with Claude.ai as a development partner — not just a code generator. Follow the phases in order. Each phase builds on the previous one, and each exchange with Claude counts toward your chat transcript requirement.

---

## Before You Start — How Claude.ai Works

Claude.ai is a **conversational AI assistant** that generates code from natural language descriptions. To get good results, you need to:

1. **Give context first** — tell Claude what kind of project you are building before asking for code
2. **Be specific** — "add a product card with a pink badge" is better than "make it look nice"
3. **Iterate** — if something is wrong, paste the problem back and ask Claude to fix it
4. **Ask why** — ask Claude to explain what a piece of code does so you understand it

> **Important:** Claude generates code based on your description. The more detail you provide from the `A12_CompanyBrief.md` file, the better the result. **Do not skip steps** — each phase builds on the previous one.

---

## Phase 1 — Project Setup and Structure (Prompt 1)

Start a **new conversation** in Claude.ai. Your first prompt sets the context for the entire project. Copy, customize, and paste this prompt:

```
I need to build a single-page website for a fictional Mexican dog fashion company
called Patitas Chic. The website should be built in a single HTML file with
embedded CSS and JavaScript (no external frameworks like Bootstrap or React).

Here is the company context:
- Company: Patitas Chic — Moda Canina
- Tagline: "Porque tu perro también merece brillar"
- Location: Mérida, Yucatán, México
- Style: elegant, colorful, inspired by Yucatán culture

Brand colors:
- Primary (Maya Jade): #1A6B5A
- Secondary (Cenote Blue): #1E7BA6
- Accent (Flamingo Pink): #F4848A
- Gold: #D4A017
- Background: #FAFAF7
- Text: #2C2C2C

The website must include these six sections (in this order):
1. Navigation bar — sticky, with the company name/logo and links to all sections
2. Hero — full-width banner with the tagline and a "Shop Now" CTA button
3. About Us — company story and three brand values (pet safety, sustainability, local artisans)
4. Products — a grid of product cards (I will provide the product data in the next message)
5. Testimonials — a section with 4 customer reviews with star ratings
6. Contact — address, phone, email, store hours, and a contact form

Please generate:
1. The complete HTML skeleton with all six sections as empty placeholder <section> tags
2. A <style> block with CSS variables for the brand colors, base typography using
   Google Fonts (Playfair Display for headings, Lato for body), and a reset
3. A sticky navigation bar with working smooth-scroll links to each section
4. The full hero section with the tagline and CTA button

Do not generate the other sections yet — I will ask for them one by one.
```

---

## Phase 2 — About Us Section (Prompt 2)

Once Claude gives you the skeleton, hero, and navbar, ask for the About section:

```
Now please add the About Us section. Here is the content to use:

STORY (2-3 sentences): Patitas Chic was founded in 2019 by two childhood friends
from Mérida — Valentina Cruz Montejo (fashion designer) and Rodrigo Acuña Herrera
(veterinarian). They combined fashion design with animal welfare expertise to create
handcrafted dog fashion inspired by Yucatán's rich textile heritage. All materials
are 100% pet-safe, hypoallergenic, and eco-friendly.

THREE VALUES (show as icon cards):
1. 🐾 Pet Safety First — all fabrics and dyes are vetted by our in-house vet
2. 🌿 Sustainability — we use eco-friendly henequén blends and organic cotton
3. 🤝 Local Artisans — we work with Mayan embroidery artisans from Ticul and Maní

SHELTER NOTE: 5% of every sale goes to Huellas de Amor, a local dog rescue in Mérida.

Style the value cards with a light background, a rounded border, and an icon on top.
Use the Maya Jade color (#1A6B5A) for the icon emoji background circles.
```

---

## Phase 3 — Products Section (Prompt 3)

```
Now please add the Products section. Display the products in a responsive grid
(3 columns on desktop, 2 on tablet, 1 on mobile). Each product card should have:
- A colored placeholder image area (use a gradient based on the product color)
- Product name
- Category badge (e.g., "Dress", "Shirt", "Accessory")
- Short description (1 sentence)
- Price in MXN
- A tag badge (e.g., "⭐ Bestseller", "🏺 Artisan Crafted") where applicable
- An "Add to Cart" button (button does not need to work — just styled)

Here are the 8 products with their data:

1. Vestido Henequén Princess — $890 MXN — Dress
   Flowing dress with hand-embroidered flowers inspired by the Yucatán terno gown.
   Colors: Ivory, Sky Blue, Soft Coral | Tag: ⭐ Bestseller
   Gradient: linear-gradient(135deg, #f0e6d3, #e8b49a)

2. Guayabera Canina — $650 MXN — Shirt
   Miniature guayabera shirt with classic pleating, perfect for weddings and events.
   Colors: White, Sky Blue, Blush Pink | Tag: 🎉 Perfect for Events
   Gradient: linear-gradient(135deg, #dce8f5, #a8c8e8)

3. Huipil Bordado — $1,200 MXN — Made to Order
   Hand-embroidered huipil by Mayan artisans from Ticul. Each one is unique.
   Tag: 🏺 Artisan Crafted | Made to Order
   Gradient: linear-gradient(135deg, #f5f0e8, #e8d5b0)

4. Conjunto Catrina — $780 MXN — Full Outfit
   Día de Muertos black lace dress with floral skull appliqués and a flower crown.
   Tag: 💀 Limited Edition
   Gradient: linear-gradient(135deg, #2c2c2c, #5c3060)

5. Sudadera Chichen Itzá — $430 MXN — Hoodie
   Cozy fleece hoodie with Chichén Itzá pyramid graphic. Machine washable.
   Colors: 6 colors available | Tag: 🏔️ Year-Round Favorite
   Gradient: linear-gradient(135deg, #d4e8d0, #1a6b5a)

6. Bikini Caribe — $480 MXN — Swimwear
   UV-protective tropical swimwear with flamingo print. Perfect for pool parties.
   Tag: 🌊 Summer Hit
   Gradient: linear-gradient(135deg, #fde8ec, #f4848a)

7. Collar Cenote — $350 MXN — Collar
   Hand-painted leather collar with cenote landscape and gold-plated buckle.
   Tag: 🌊 Artisan Detail
   Gradient: linear-gradient(135deg, #d0eaf5, #1e7ba6)

8. Mochila Paseo — $520 MXN — Carrier Bag
   Vegan leather carrier for small dogs (up to 5 kg). Travel-ready.
   Tag: ✈️ Travel-Ready
   Gradient: linear-gradient(135deg, #e8f0e8, #b8d4b8)

Use the Flamingo Pink (#F4848A) for the price text and the Maya Jade (#1A6B5A)
for the "Add to Cart" button.
```

---

## Phase 4 — Testimonials and Contact (Prompt 4)

```
Now please add the Testimonials section and the Contact section.

TESTIMONIALS — display as cards in a 2×2 grid (or a horizontal row on desktop):

1. ⭐⭐⭐⭐⭐ — @layla_y_coco, Ciudad de México
   "¡Coqueta se ve increíble con su Huipil Bordado! La calidad es espectacular
   y el envío llegó más rápido de lo que esperaba."

2. ⭐⭐⭐⭐⭐ — @taco_chihuahua_mx, Monterrey, NL
   "Mi Chihuahua Taco nunca había recibido tantos comentarios en el parque.
   La Guayabera Canina es simplemente perfecta."

3. ⭐⭐⭐⭐⭐ — @corgi.adventures.sf, San Francisco, CA, USA
   "I ordered the Bikini Caribe from San Francisco. Shipping to the US took
   6 days and the quality is seriously amazing. Worth every peso!"

4. ⭐⭐⭐⭐⭐ — @frenchie_merida_life, Mérida, Yucatán
   "El Collar Cenote es una verdadera obra de arte. Absolutamente todos en
   el parque preguntaron dónde lo conseguí."

Style each card with a subtle drop shadow, rounded corners, and the star rating
in Hacienda Gold (#D4A017).

CONTACT SECTION — include:
- Address: Calle 60 #432, entre 47 y 49, Col. Centro Histórico, Mérida, Yucatán, C.P. 97000
- Phone/WhatsApp: +52 (999) 234-5678
- Email: hola@patitaschic.mx
- Hours: Monday–Saturday 10:00–20:00 / Sunday 11:00–17:00
- A contact form with fields: Name, Email, Dog's name, Message, and a Send button
- The form does not need to submit data — style it and add a simple JavaScript
  validation that shows an alert if any field is empty when the Send button is clicked

Also add a footer with:
- The Patitas Chic name and tagline
- Social media links: Instagram @patitaschic_merida, Facebook /PatitasChicMerida,
  TikTok @patitaschic
- Copyright: © 2024 Patitas Chic — Moda Canina. Mérida, Yucatán, México.
```

---

## Phase 5 — Interactivity and Polish (Prompt 5)

```
The website structure is complete. Now please add the following interactive features:

1. MOBILE HAMBURGER MENU — the navbar should collapse on screens smaller than 768px,
   showing a hamburger icon (☰) that toggles the nav links open and closed when clicked.

2. BACK TO TOP BUTTON — a circular button fixed to the bottom-right corner that
   appears only after the user has scrolled down 300px. Clicking it scrolls smoothly
   back to the top. Style it in Maya Jade (#1A6B5A) with a white arrow (↑).

3. PRODUCT CARD HOVER EFFECT — when the user hovers over a product card, add a
   subtle lift effect (translateY -6px) with a slightly deeper shadow.

4. SECTION FADE-IN ON SCROLL — use the Intersection Observer API to add a
   fade-in animation as each section scrolls into view for the first time.

Please provide the complete updated HTML file including all previous sections and
these new interactive features.
```

---

## Phase 6 — Review and Fix (Prompt 6+)

This is the most important phase for learning. After pasting the final code into a browser and testing it, you will likely find things to fix or improve. Examples of good follow-up prompts:

**Fixing a bug:**
```
The hamburger menu opens when I click ☰ but does not close when I click a
nav link on mobile. Please fix the JavaScript so clicking any nav link also
closes the menu.
```

**Improving layout:**
```
On my phone (375px screen), the product cards are still showing 2 columns
instead of 1. Please fix the CSS media query for the product grid.
```

**Asking Claude to explain code:**
```
Can you explain how the Intersection Observer API works in the scroll
fade-in code you generated? I want to understand what the threshold
and rootMargin options do.
```

**Adding a feature you choose:**
```
I want to add a [feature of your choice — see required features list in the
README]. Please add it and explain what you added.
```

> **Document every exchange.** Each prompt and Claude's response is part of your deliverable. Screenshot or export the full conversation before closing the Claude.ai tab.

---

## Tips for Better Prompts

| ❌ Vague prompt | ✅ Specific prompt |
|----------------|-------------------|
| "Make it look better" | "Increase the spacing between product cards to 24px and add a 1px solid #E0E0E0 border" |
| "Fix the menu" | "The navbar overlaps the hero section on mobile — add `padding-top: 60px` to the hero" |
| "Add animation" | "Add a CSS keyframe animation that fades the hero tagline in from opacity 0 to 1 over 1 second on page load" |
| "Add more stuff" | "Add a Shipping & Services section between Products and Testimonials with a 3-column icon grid showing: Free shipping over $1,500 MXN / Express 3–5 days / International USA & Canada" |

---

## Common Problems and How to Solve Them with Claude

| Problem | What to tell Claude |
|---------|-------------------|
| Layout breaks on mobile | "The layout breaks on screens under 480px — show me the CSS changes needed to make it fully responsive" |
| Font not loading | "Google Fonts is not loading — how do I add Playfair Display and Lato to my HTML file reliably?" |
| JavaScript error in console | "I get this error in the browser console: [paste the error]. Please fix it." |
| Section overlap | "The [section name] section overlaps the next section on scroll — what CSS property fixes this?" |
| Color looks wrong | "The button background color looks lighter than #1A6B5A — can you check the CSS and fix it?" |

---

*Patitas Chic — Moda Canina | Activity 12 Prompting Guide*
*Introduction to Artificial Intelligence*
