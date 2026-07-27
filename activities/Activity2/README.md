# Activity 2 — Development Environment Setup
## Installing Anaconda, Creating Your `ai_uam` Environment, and Verifying JupyterLab

**Course:** Introduction to Artificial Intelligence
**Topic:** Setting Up Your Python Development Environment

---

## Introduction

Starting with this activity, you'll be working hands-on with Python and Jupyter notebooks for the rest of the semester. Before any of that can happen, you need a working development environment on your own computer.

This activity has no code and no theory questions — it's a hands-on setup lab. You'll install **Anaconda**, use it to create a dedicated conda environment named **`ai_uam`**, confirm Python is installed inside it, install **JupyterLab**, and submit screenshots proving each step worked. Every later activity in this course assumes this environment already exists, so it's worth doing carefully now.

---

## What You Will Set Up

| Component | Purpose |
|-----------|---------|
| Anaconda | The distribution that provides Python, conda, and JupyterLab together |
| Conda environment `ai_uam` | An isolated environment for this course, so packages here never conflict with anything else on your machine |
| Python 3.11 | Installed automatically inside `ai_uam` when you create it |
| JupyterLab | The notebook interface you'll use for Activities 7, 9, 10, and 11 |

---

## Files in This Assignment

| File | Description |
|------|-------------|
| `A2_SetupGuide.md` | Step-by-step installation instructions for Windows, Mac, and Linux, with expected output and a troubleshooting table. Read this first — it's where the actual work happens. |
| `README.md` | This file — overview, submission instructions, and grading. |

---

## Getting Started

1. Open `A2_SetupGuide.md` and follow it step by step, in order, on your own computer.
2. Along the way you'll take **5 screenshots** — the guide tells you exactly when and what to capture.
3. Combine all 5 screenshots into a single PDF or Word document, each one labeled with which step it proves (Screenshot 1, Screenshot 2, etc.).
4. Submit that document — see **Submission** below.

**Quick checklist of what you're proving:**
- [ ] Anaconda is installed
- [ ] The `ai_uam` conda environment exists and activates correctly
- [ ] Python 3.11 is installed inside `ai_uam`
- [ ] JupyterLab is installed inside `ai_uam`
- [ ] JupyterLab launches and runs a notebook cell with your name and a timestamp

---

## Submission

Submit **one item** to the course portal:

### Screenshot Evidence Document (PDF or Word)

A single document containing all 5 required screenshots from `A2_SetupGuide.md`, each one clearly labeled. Screenshots must be legible — if a grader can't read the terminal output or notebook output, that screenshot won't count as evidence.

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| **Anaconda Installation Proof** | `conda --version` / `conda info` output shown | 15 |
| **Conda Environment `ai_uam` Created & Activated** | `conda env list` shows `ai_uam`; prompt shows `(ai_uam)` active | 20 |
| **Python 3.11 Verified Inside `ai_uam`** | `python --version` shows 3.11.x with `ai_uam` active | 15 |
| **JupyterLab Installed & Verified Inside `ai_uam`** | `jupyter lab --version` shown with `ai_uam` active | 15 |
| **JupyterLab Launched + Personalized Proof Cell** | Browser screenshot of JupyterLab running a notebook cell with the student's own name and a timestamp | 25 |
| **Screenshots Labeled & Legible** | All 5 screenshots present, clearly labeled, and readable | 10 |
| **Total** | | **100** |

### Grading notes

- The personalized proof cell in Screenshot 5 exists so that each submission is verifiably the student's own environment — a screenshot without your own name and a current timestamp will not receive credit for that component, even if JupyterLab is clearly running.
- If you hit an error not covered by the Troubleshooting table in `A2_SetupGuide.md`, ask for help early rather than submitting incomplete screenshots.

---

## Academic Integrity

- Every screenshot must come from your own computer and your own installation — screenshots copied or shared between students are easy to detect once the proof cell requirement is in place.
- If you already have Anaconda installed from before this course, you still need to create the `ai_uam` environment specifically and take fresh screenshots for this activity.

---

## Troubleshooting

Common installation issues (wrong Mac chip installer, `conda` not found, environment already exists, etc.) are covered in the **Troubleshooting** table at the end of `A2_SetupGuide.md`. Check there first before asking for help.

---

*Activity 2 | Introduction to Artificial Intelligence*
