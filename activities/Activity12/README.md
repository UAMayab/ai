# Activity 12 — Generative AI for App Development
## Build a Website with Claude.ai: Patitas Chic Dog Fashion

**Course:** Introduction to Artificial Intelligence
**Session:** 36 — App Development with GenAI
**Topic:** Prompt Engineering · Code Generation · Iterative Development · GenAI as a Development Partner

---

## Introduction

Welcome to Activity 12 — the final and most hands-on assignment of the course.

In Session 36 you learned how Generative AI is transforming software development: from code generation and debugging to refactoring and documentation. In this activity you will experience that transformation firsthand.

You are hired as a **web developer at ReviewIQ's sister agency**, and your first client is **Patitas Chic** — a dog fashion boutique based in Mérida, Yucatán, México. Patitas Chic needs a modern, single-page website to showcase their products, tell their brand story, and let customers get in touch.

The catch: **you will not write the code yourself**. You will use **Claude.ai** — Anthropic's conversational AI assistant — as your development partner. Your job is to craft the prompts, review the output, iterate, and produce a working, polished website.

This activity teaches a core skill of modern software development: **communicating with AI effectively**. The quality of your website is a direct reflection of the quality of your prompts.

---

## What You Will Build

A **single-page website** (`index.html`) for Patitas Chic that includes:

| Section | Required content |
|---------|-----------------|
| **Navigation bar** | Sticky, with logo and smooth-scroll links to all sections |
| **Hero** | Full-width banner with company tagline and "Shop Now" CTA button |
| **About Us** | Company story, 3 brand value cards, shelter partnership mention |
| **Products** | 8 product cards in a responsive grid with names, prices, descriptions, badges |
| **Testimonials** | 4 customer reviews with star ratings in card layout |
| **Contact** | Address, phone, email, hours, and a validated contact form |
| **Footer** | Social media links, copyright |

**Required interactive features (JavaScript):**
- Mobile hamburger menu (collapses on screens < 768px)
- Back-to-top button (appears after scrolling 300px)
- Scroll-triggered fade-in animations (Intersection Observer API)
- Contact form validation (alert if any field is empty on submit)
- **One feature of your own choice** (see suggestions below)

**Suggested additional features:**
- Product image lightbox / modal
- Animated counter (e.g., "1,200+ happy dogs")
- A sticky "WhatsApp us" floating button
- Dark mode toggle
- Product category filter (show only Clothing / Accessories)
- A simple image carousel in the Hero section
- Testimonial auto-scroll / slider

---

## What GenAI Teaches in This Activity

| GenAI concept from Session 36 | Where you apply it |
|-------------------------------|-------------------|
| **Code generation from prompts** | Each phase of the Prompting Guide produces a functional code section |
| **Iterative refinement** | Phase 6 — debugging and improving Claude's output |
| **Code review / explanation** | Asking Claude to explain generated code you don't understand |
| **Debugging assistance** | Pasting browser console errors back to Claude for fixes |
| **Documentation** | Asking Claude to comment your final code |

---

## Files in This Assignment

| File | Description |
|------|-------------|
| `A12_CompanyBrief.md` | **Read this first.** Contains all fictional company data: brand identity, colors, team, products, testimonials, contact info, and FAQ. This is your "brief" — everything you need to prompt Claude effectively. |
| `A12_PromptingGuide.md` | Step-by-step guide with 6 phased prompts to build the website from scratch. Follow these in order. Also includes tips for better prompts and common problem solutions. |
| `README.md` | This file — overview, requirements, getting started, and grading. |

---

## Getting Started

### Step 1 — Read the company brief

Open `A12_CompanyBrief.md` and read it completely before writing your first prompt. The brief contains:
- Brand colors (you must use these)
- All 8 product names, prices, descriptions, and badge tags
- Team bios and the company story
- All 4 customer testimonials (exact quotes)
- Contact details and store hours

The richer your understanding of the brand, the better your prompts will be.

### Step 2 — Open Claude.ai

Go to [claude.ai](https://claude.ai) and sign in or create a free account.

> **Free tier is sufficient for this assignment.** Claude's free tier allows enough messages to complete all six prompting phases. If you hit a rate limit, wait a few minutes and continue in the same conversation.

### Step 3 — Follow the Prompting Guide

Open `A12_PromptingGuide.md` and work through the six phases **in order**:

| Phase | What you build | Approximate prompts |
|-------|---------------|---------------------|
| 1 | HTML skeleton + navbar + hero | 1 |
| 2 | About Us section | 1 |
| 3 | Products grid | 1 |
| 4 | Testimonials + Contact + Footer | 1 |
| 5 | Interactivity (hamburger, back-to-top, animations) | 1 |
| 6 | Review, fix, and your own feature | 2–5 |

Each time Claude generates code, **copy it into a file called `index.html`** on your computer and open it in Chrome or Edge to test it.

### Step 4 — Save your chat transcript

Before closing Claude.ai, **export or screenshot your entire conversation**. This is a required deliverable.

To export: click the **three-dot menu (⋯)** next to the conversation → "Export" or take full-page screenshots of the conversation.

### Step 5 — Write your reflection

After completing the website, write a **200–300 word reflection** (see submission instructions below).

---

## Submission

Submit **three items** to the course portal:

### 1. `index.html` — Your completed website file
- Must be a single self-contained HTML file (CSS and JavaScript embedded inside the file)
- Must be openable by double-clicking — no server required
- All six required sections must be present
- All required JavaScript features must work
- Brand colors from the brief must be used consistently
- All product names, prices, and company information must match the `A12_CompanyBrief.md`

### 2. Chat transcript — Your Claude.ai conversation
- Export as PDF **or** submit a folder of full-page screenshots (one per exchange)
- Must show at least **6 distinct prompting exchanges** (one per phase)
- Must include at least **2 iterative exchanges** — prompts where you corrected or improved something from a previous response
- You must have at least **one prompt asking Claude to explain** a piece of code it generated

### 3. Reflection document (200–300 words) — PDF or Word
Answer these four questions:
1. **What worked best?** — Which of your prompts produced the best code with the least correction? Why do you think it worked?
2. **What required the most iteration?** — Which part of the website took the most back-and-forth with Claude? What did you have to correct?
3. **What did Claude struggle with?** — Was there anything Claude got consistently wrong or that you had to fix manually?
4. **What does this experience tell you about using GenAI for software development?** — Connect your experience to at least one concept from Session 36 (e.g., code generation, iterative refinement, the role of the human developer).

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| **Website — Completeness** | All 6 required sections present with correct Patitas Chic content | 20 |
| **Website — Visual Design** | Brand colors used correctly; clean, professional layout; responsive on mobile | 20 |
| **Website — Interactivity** | All 4 required JS features work; self-chosen feature implemented | 20 |
| **Prompt Quality** | Chat transcript shows at least 6 phases; includes 2+ iterative refinements; includes 1+ explanation request | 20 |
| **Reflection** | 200–300 words; answers all 4 questions; connects to Session 36 concepts | 15 |
| **Content Accuracy** | Products, prices, team, testimonials match the company brief | 5 |
| **Total** | | **100** |

### Grading notes
- A website that is visually polished but missing interactive features caps at 60 points
- A chat transcript showing only 1–2 prompts (no iteration) caps the Prompt Quality score at 10
- The reflection must reference **your own experience** — generic answers not grounded in your chat transcript will not receive full credit
- You **do not need to write any code yourself** — the goal is to direct Claude effectively, not to be a web developer

---

## Academic Integrity

This assignment is designed to be completed with Claude.ai. Using Claude is not only allowed — it is **required**. However:

- The company data, color palette, and section structure are fixed (from the company brief) — do not substitute a different company
- Your chat transcript must reflect **your own prompts and your own iteration** — you may not copy another student's prompt sequence
- Your reflection must describe **your own experience** with Claude

---

## Tips for Success

**Before you prompt:**
- Read the entire `A12_CompanyBrief.md` — you cannot prompt well from memory
- Have the hex colors ready to paste (#1A6B5A, #1E7BA6, etc.)

**While prompting:**
- Work in phases — do not ask for the entire website in one prompt
- If you don't like the output, say so specifically: *"The hero section is too tall on mobile — reduce the min-height to 60vh for screens under 768px"*
- If Claude's code has an error, paste the browser console error message directly into the chat

**Testing:**
- Test in both desktop and mobile view (Chrome DevTools → Ctrl+Shift+M toggles mobile view)
- Test all JavaScript features before submitting

---

*Patitas Chic — Moda Canina | Mérida, Yucatán, México*
*Activity 12 | Introduction to Artificial Intelligence*
