# Activity 7 — Linear Regression: Predicting Systolic Blood Pressure

**Course:** Introduction to Artificial Intelligence
**Sessions:** 20 and 21
**Topic:** Simple and Multiple Linear Regression

---

## Introduction

Welcome to Activity 7. In this assignment you will apply **linear regression** — one of the foundational algorithms in machine learning and statistics — to a real-world health problem: predicting systolic blood pressure (SBP) in hypertension patients.

You will work as a data science consultant for the fictional **Maplewood Regional Health Authority (MRHA)** and its *CardioWatch* program, which monitors patients aged 25–75 who are at risk of developing hypertension. Your job is to build predictive models that estimate a patient's blood pressure from measurable characteristics, and to evaluate how well those models perform.

By the end of this activity you will be able to:

- Perform exploratory data analysis (EDA) on a health dataset
- Build and interpret a **Simple Linear Regression** model (one predictor)
- Build and interpret a **Multiple Linear Regression** model (two predictors)
- Evaluate models using Mean Squared Error (MSE) and R²
- Analyze residuals to verify model assumptions
- Use interactive widgets to experiment with model parameters

---

## Background: Why Blood Pressure?

Hypertension affects roughly 1.28 billion adults worldwide and is a leading cause of heart disease, stroke, and kidney failure. Identifying at-risk patients early — before complications arise — is a major goal of modern preventive medicine. Machine learning models that predict blood pressure from basic patient data (age, weight, lifestyle factors) can help clinicians prioritize screening and intervention.

This assignment uses a **synthetic** dataset that mimics real clinical data, generated from a formula grounded in published medical research:

```
SBP = 105 + 0.55 × Age + 1.10 × BMI + noise
```

---

## Tasks

| Task | Model | Predictor(s) | Goal |
|------|-------|-------------|------|
| **Task 1** | Simple Linear Regression | Age only | Predict SBP from age alone |
| **Task 2** | Multiple Linear Regression | Age + BMI | Predict SBP using two variables |

Each task walks you step by step through the full machine learning pipeline: data exploration → model training → evaluation → visualization → residual analysis → interactive experimentation.

---

## Getting Started

### 1. Install dependencies

Make sure you have Python 3.9 or newer. Then install all required libraries:

```bash
pip install -r requirements.txt
```

### 2. Enable interactive widgets

If you are using **classic Jupyter Notebook**:

```bash
jupyter nbextension enable --py widgetsnbextension
```

If you are using **JupyterLab**:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### 3. Launch the notebook

```bash
jupyter notebook A7_LinearRegression_BloodPressure.ipynb
```

### 4. Run the cells in order

Start from the top and run each cell sequentially. The dataset is generated in an early cell — all later cells depend on it.

> **Important:** Do not modify the dataset generation cell. The fixed random seed ensures every student works with the same 200 patients, which is required for consistent results across the class.

### 5. Answer the plot analysis questions

Once **all cells have been executed** and you can see every plot and printed output, open `A7_PlotAnalysis_Questions.md` and answer the questions in a **separate document** (plain text, Word, or PDF — see submission instructions below).

The questions are organized to follow the notebook from top to bottom. Keep the notebook open alongside the question document so you can refer to the exact plots and numbers as you write your answers.

> **Tip:** Do not answer from memory. Every question points to a specific chart or output value. Your answers should cite those values directly.

---

## Files in This Directory

| File | Description |
|------|-------------|
| `A7_LinearRegression_BloodPressure.ipynb` | Main assignment notebook. Contains all instructions, code, plots, interactive widgets, and in-notebook reflection questions. **Must be executed before answering the plot analysis questions.** |
| `A7_PlotAnalysis_Questions.md` | Plot and output analysis questions. Answer these **after** running the notebook. Submit your answers as a separate document. |
| `requirements.txt` | List of Python packages required to run the notebook. Install with `pip install -r requirements.txt`. |
| `README.md` | This file. |

---

## Submission

Submit **two files** to the course portal:

1. **`A7_LinearRegression_BloodPressure.ipynb`** — the executed notebook
   - All code cells must show their output (plots and printed values visible)
   - All in-notebook reflection questions (Q1–Q6 at the end) must be answered in the Markdown cells
   - Do not remove or reorder any cells

2. **`A7_PlotAnalysis_Answers.pdf`** (or `.docx`) — your written answers to the plot analysis questions
   - Answer every question in `A7_PlotAnalysis_Questions.md`
   - Label each answer clearly with its question number (e.g., **Q1.3**, **Q8.2**)
   - Cite specific values from the notebook output in your answers
   - Answers must reflect the plots and numbers produced by **your own executed notebook**

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| Task 1 — Notebook (Steps 1.1 – 1.6) | Code executed, plots visible, step outputs correct | 25 |
| Task 1 — Interactive Experiment | In-notebook reflection answered | 5 |
| Task 2 — Notebook (Steps 2.1 – 2.8) | Code executed, plots visible, step outputs correct | 25 |
| Task 2 — Interactive Experiment | In-notebook reflection answered | 5 |
| Plot Analysis — Sections 0–5 (Task 1) | Written answers to Q0.1–Q5.5 | 20 |
| Plot Analysis — Sections 6–12 (Task 2 & Synthesis) | Written answers to Q6.1–Q12.5 | 20 |
| **Total** | | **100** |

---

*MRHA CardioWatch Program — Data Science Consulting Report*
*Activity 7 | Introduction to Artificial Intelligence*
