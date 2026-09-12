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

---

*Anahuac Mayab University — Introduction to Artificial Intelligence — Spring 2026*
