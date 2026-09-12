# Anahuac Mayab University
## Introduction to Artificial Intelligence
### Fall 2026
### Prof. Miguel A. Guirao Aguilera

---

## Activities

| # | Activity | Sessions | Topic | Tools |
|---|----------|----------|-------|-------|
| 1 | [Activity 1](activities/Activity1/) | 1–3 | AI Foundations — Definitions, History & Interdisciplinary Roots | PowerPoint, Video |
| 2 | [Activity 2](activities/Activity2/) | — | Development Environment Setup — Anaconda, conda, and JupyterLab | Anaconda, conda, Python, JupyterLab |
| 3 | [Activity 3](activities/Activity3/) | 4–5 | AI Applications & Ethics Briefing — Real Applications, Real Ethics, Real Law | PowerPoint, Video |
| 4 | [Activity 4](activities/Activity4/) | 6 | Python Code Comprehension Lab — Reading & Adapting Python Code | Python, JupyterLab |
| 5 | [Activity 5](activities/Activity5/) | 10–12 | The Whispering Cave — Depth-First Search Adventure | Prolog-style Logic |
| 6 | [Activity 6](activities/Activity6/) | 13 | Six Degrees to Katún — Breadth-First Search Networking Challenge | — |
| 7 | [Activity 7](activities/Activity7/) | 14 | YucaExpress — The Fastest Route Challenge (Heuristic Search) | — |
| 8 | [Activity 8](activities/Activity8/) | 15 | ShopSmart Assistant — An Expert System for Customer Decisions | — |
| 9 | [Activity 9](activities/Activity9/) | 16 | Pack for the Trip — A Genetic Algorithm Challenge | — |
| 10 | [Activity 10](activities/Activity10/) | 17 | SmartWash — A Fuzzy Logic Laundry Controller | — |

---

## Activity Summaries

### Activity 1 — AI Foundations Briefing
Working in teams, students act as outside AI consultants hired by **Katún Manufactura**, a fictional Mérida precision-parts manufacturer, to independently evaluate an AI vendor's pitch before the board signs a three-year contract. Covers plain-language AI classification (weak vs. strong AI), a historical lesson drawn from AI's hype cycles, and the interdisciplinary expertise real AI adoption requires. The deliverable is an 8–10 slide PowerPoint plus a 5–7 minute English-language video presenting the team's findings, recommendation, and personal reflection.

### Activity 2 — Development Environment Setup
Students install Anaconda, create a dedicated conda environment named `ai_uam` with Python 3.11, and install JupyterLab — the toolchain every later Python activity in the course depends on. Covers installation on Windows, Mac, and Linux, with a personalized proof-of-installation notebook cell to verify each student's own setup. The deliverable is a single document of labeled screenshots evidencing each installation step.

### Activity 3 — AI Applications & Ethics Briefing
Working in teams, students pick one real-world AI domain (healthcare, agriculture, energy, manufacturing, logistics, finance, environmental conservation, or cybersecurity) from a curated list, describe a real current AI application in it, and analyze its ethical and legal implications, citing a real regulatory framework such as GDPR or Mexico's data-protection law. Unlike Activity 1's fictional scenario, this activity is grounded entirely in real applications and real law. The deliverable is the same PowerPoint + English-language video format as Activity 1.

### Activity 4 — Python Code Comprehension Lab
Students work through a JupyterLab notebook that solves one small problem three different ways, matching the three programming paradigms introduced in Session 6: imperative, functional, and logic/rule-based. For each paradigm, students answer code-comprehension questions and complete a required "Now You Adapt It" task where they modify the code themselves and re-run it — directly building the code-reading and code-adapting skills the rest of the semester's Python activities depend on.

### Activity 5 — The Whispering Cave: A Depth-First Search Adventure
Students explore a fixed, deterministic cave map through an interactive Streamlit app across three tabs matching Sessions 10–12: problem-space vocabulary (initial/goal state, search space), Prolog-style facts and a recursive `reachable(X, Y)` rule, and a click-through Depth-First Search stepper showing the stack, visited set, and live graph. The deliverable is a reflection markdown file, screenshots, and a 5-minute video explaining DFS in kid-friendly terms — graded against a fixed checklist tied to the app's deterministic Answer Key.

### Activity 6 — Six Degrees to Katún: A Breadth-First Search Networking Challenge
Students use an interactive Streamlit app to find the shortest chain of professional introductions to **Elena Ruiz, CFO of Grupo Katún**, through a fixed, deterministic business network. Covers problem-space vocabulary, a click-through Breadth-First Search stepper (queue/FIFO, distance-by-level discovery), and an optional side-by-side comparison against Session 12's Depth-First Search on the same network. Unlike Activity 5, this is a single-session activity with no video component — every reflection question is answered directly from the app's deterministic output, keeping grading fast and consistent.

### Activity 7 — YucaExpress: The Fastest Route Challenge
Students use an interactive Streamlit app to route a delivery courier across a fixed, coordinate-based city map, comparing **Greedy Best-First Search** (which only looks at straight-line distance to the goal) against **A\*** (which balances real distance driven with the straight-line estimate, f(n) = g(n) + h(n)). The map is deliberately built with a provably admissible heuristic and one "mirage" junction that reliably misleads Greedy into a costlier route while A\* finds the true optimum — verified against Dijkstra's algorithm. Same single-session, no-video format as Activity 6.

### Activity 8 — ShopSmart Assistant: An Expert System for Customer Decisions
Students use an interactive Streamlit app modeling a fictional online store's rule-based expert system, mapping the five classic expert-system components (knowledge base, inference engine, user interface, knowledge acquisition, explanation mechanism) onto a concrete IT + business rule base. Students step through the inference engine against five fixed customer/server profiles, seeing exactly which IF-THEN rules fire and why. Per the instructor's request, this activity's reflection questions are weighted heavily toward closed-ended, fixed-answer items rather than open-ended analysis.

### Activity 9 — Pack for the Trip: A Genetic Algorithm Challenge
Students use an interactive Streamlit app to solve a classic Knapsack Problem (which items to pack in a weight-limited bag for maximum usefulness) with a Genetic Algorithm — population, fitness, roulette selection, one-point crossover, and mutation, stepped through generation by generation. The algorithm is stochastic by nature but made fully deterministic via a fixed random seed, chosen (after testing many candidates) to show genuine improvement across generations and to demonstrate the non-elitist property: the best-in-generation score can dip even after the true optimum (verified by brute force) has already been found. Same single-session, no-video format as Activities 6–8.

### Activity 10 — SmartWash: A Fuzzy Logic Laundry Controller
Students use an interactive Streamlit app to explore a fuzzy logic controller (the same "fuzzy washing machine" example from the course material) that decides wash time from load size and dirtiness. Covers the full four-step fuzzy pipeline — fuzzification, rule-based inference, aggregation, and weighted-average defuzzification — with membership function charts and a 9-rule rule base. Because fuzzy logic's inputs are naturally continuous, grading is restricted to five fixed, pre-verified profiles; an explicitly-labeled, ungraded slider sandbox is offered separately for free exploration. Same single-session, no-video format as Activities 6–9.

---

## Class Demos (not graded — nothing to submit)

| Session | Demo | Topic |
|---------|------|-------|
| 18 | [Session 18 ML Demo](class_demos/Session18_MachineLearning/) | Supervised vs. Unsupervised Learning — animated, interactive teaching app, plus a brief intro to ML threats (adversarial examples, data poisoning, bias, privacy leakage) |

---

*Anahuac Mayab University — Introduction to Artificial Intelligence — Spring 2026*
