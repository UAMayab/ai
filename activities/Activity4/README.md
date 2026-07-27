# Activity 4 — Python Code Comprehension Lab
## Reading, Understanding, and Adapting Python Code (Session 6)

**Course:** Introduction to Artificial Intelligence
**Session:** 6
**Topic:** Programming Languages and Paradigms for AI

---

## Introduction

Session 6 compared programming languages used in AI and introduced three programming paradigms: **imperative**, **functional**, and **logic/rule-based**. Starting with the next activities, you'll be reading, running, and adapting Python code that other people wrote — so before that happens, this activity checks that you can actually do that.

This is a hands-on lab, not a written assignment. You'll run pre-written Python code in **JupyterLab** (using the `ai_uam` environment you set up in Activity 2), answer comprehension questions about what the code does, and then make small, specific modifications to it yourself.

---

## What You Will Do

The notebook solves **one small problem** — deciding what action a device needs based on its battery level — three different ways, one per paradigm:

| Section | Paradigm | What it demonstrates |
|---|---|---|
| 1 | Imperative | Loops and `if`/`elif`/`else` branches that build up a result step by step |
| 2 | Functional | A named function applied across a list with `map`, plus `filter` |
| 3 | Logic / Rule-Based | A table of `(condition, result)` rules checked in order — the style behind expert systems |

For each section you will: run the code, answer comprehension questions about it, and complete a **"Now You Adapt It"** task that requires you to modify the code yourself and re-run it.

---

## Files in This Assignment

| File | Description |
|------|-------------|
| `A4_PythonComprehensionLab.ipynb` | The notebook — read the instructions in its first cell, then work through it top to bottom. |
| `README.md` | This file. |

---

## Getting Started

### Step 1 — Activate your environment

Open a terminal, activate the `ai_uam` conda environment from Activity 2:

```bash
conda activate ai_uam
```

### Step 2 — Launch JupyterLab

```bash
jupyter lab
```

### Step 3 — Open the notebook

Open `A4_PythonComprehensionLab.ipynb` and work through it **in order, top to bottom**. Do not skip cells.

### Step 4 — Answer questions and complete the adapt tasks

Each section has comprehension questions (answer directly in the markdown cell) and one "Now You Adapt It" task (edit the section's code cell directly, then re-run it).

### Step 5 — Submit

See **Submission** below.

---

## Submission

Submit **one item** to the course portal:

### Executed Notebook — `A4_PythonComprehensionLab.ipynb`

- Every code cell must show its output (run top to bottom without errors).
- Every comprehension question must be answered in its markdown cell.
- All three "Now You Adapt It" tasks must be completed, with the modified code cell showing correct output.
- Do not remove or reorder any cells.

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| **Imperative Section** | Code runs; comprehension questions (Q1.1–Q1.2) answered correctly | 20 |
| **Functional Section** | Code runs; comprehension questions (Q2.1–Q2.3) answered correctly | 20 |
| **Logic/Rule-Based Section** | Code runs; comprehension questions (Q3.1–Q3.3) answered correctly | 20 |
| **"Now You Adapt It" Tasks** | All three modifications (Task 1, 2, 3) correctly implemented and re-run | 25 |
| **Reflection (Q4)** | Specific, references your own experience with the adapt tasks | 15 |
| **Total** | | **100** |

### Grading notes

- "Correct" for the adapt tasks means the modified cell actually produces the right output when run — not just an attempted edit.
- Comprehension answers should reflect your own understanding of the code, not a copied definition of the paradigm.

---

## Tips for Success

- Read each code cell fully before running it, and try to predict the output first — that's the whole point of the comprehension questions.
- If a "Now You Adapt It" task isn't working, re-read the section's original code carefully before changing anything else — the fix is almost always a small, localized change.
- This notebook uses only Python's standard library — no `pip install` needed beyond what Activity 2 already set up.

---

*Activity 4 | Introduction to Artificial Intelligence*
