# Activity 9 — Artificial Neural Networks: Heart Disease Classification

**Course:** Introduction to Artificial Intelligence
**Sessions:** 25, 26, 27, and 28
**Topic:** Artificial Neural Networks · Backpropagation · Debugging & Improvement

---

## Introduction

Welcome to Activity 9. In this assignment you will build and train **Artificial Neural Networks (ANNs)** to solve a real-world health problem: classifying whether a patient will develop cardiovascular heart disease within the next five years.

You will continue working as a data science consultant for the **Maplewood Regional Health Authority (MRHA)** and its *CardioWatch* program — the same organization from Activity 7. The MRHA has now extended its dataset to include additional biomarkers and has tasked you with moving beyond regression (Activity 7) into **classification** using neural networks.

By the end of this activity you will be able to:

- Explain how a McCulloch-Pitts (MCP) neuron computes logical operations
- Normalize features and understand why this step is critical for neural network training
- Build, train, and evaluate a **Multi-Layer Perceptron (MLP)** using scikit-learn
- Interpret a **confusion matrix** and classification metrics (precision, recall, F1-score)
- Read a **training loss curve** and identify convergence and overfitting
- Demonstrate and remedy **overfitting** using L2 regularization
- Apply **cross-validation** correctly using a scikit-learn Pipeline
- Interpret a **ROC curve** and AUC score
- Use interactive widgets to experiment with neural network hyperparameters

---

## Background: From Regression to Classification

In Activity 7 you predicted *how high* a patient's blood pressure would be — a **regression** task. In this activity you answer a different question: will this patient *develop heart disease or not?* — a **classification** task.

This is a more direct clinical question. Physicians don't just want to know a number; they want to know whether to intervene. Neural networks are particularly well suited to classification because they can learn non-linear decision boundaries that simpler models like logistic regression cannot.

The dataset is generated from a clinically grounded risk formula inspired by established cardiovascular risk models:

```
risk = f(age, BMI, systolic BP, cholesterol, resting heart rate)
P(heart_disease = 1) = sigmoid(risk)
```

---

## Dataset

| Column | Description | Units |
|--------|-------------|-------|
| `age` | Patient age | years |
| `bmi` | Body Mass Index | kg/m² |
| `sbp` | Systolic Blood Pressure | mmHg |
| `cholesterol` | Total cholesterol | mg/dL |
| `resting_hr` | Resting heart rate | bpm |
| `heart_disease` | **Target** — develops heart disease within 5 years | 0 = No / 1 = Yes |

**Reference ranges:**

| Metric | Healthy | At Risk |
|--------|---------|---------|
| Total Cholesterol | < 200 mg/dL | ≥ 240 mg/dL |
| Resting Heart Rate | 60–100 bpm | > 100 bpm |
| SBP | < 120 mmHg | ≥ 130 mmHg |

---

## Tasks

| Task | Model | Focus |
|------|-------|-------|
| **Task 1** | Simple MLP (1–2 hidden layers) | Build, train, evaluate — confusion matrix, loss curve |
| **Task 2** | Deeper MLP + Debugging | Overfitting, regularization, cross-validation, ROC curve |

Each task follows the same pipeline:
1. Build intuition (MCP neuron) / Demonstrate a problem (overfitting)
2. Prepare the data
3. Build and train the model
4. Evaluate with multiple metrics
5. Visualize results
6. Interactive experiment with ipywidgets

---

## Session Coverage

| Session | Topic | Where it appears in the notebook |
|---------|-------|----------------------------------|
| 25 — Artificial Neural Networks | MCP neuron, architectures, learning | Task 1 Steps 1.1–1.5 |
| 26 — Backpropagation | Loss function, gradient descent, epochs | Task 1 Steps 1.5, 1.8 |
| 27 — 21st Century Applications | Medical diagnosis, clinical predictions | Task 2 Step 2.5 |
| 28 — Debugging & Improvement | Overfitting, regularization, CV, confusion matrix | Task 2 Steps 2.1–2.4 |

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
jupyter notebook A9_NeuralNetworks_HeartDisease.ipynb
```

### 4. Run the cells in order

Start from the top and run each cell sequentially. The dataset is generated in an early cell — all later cells depend on it.

> **Important:** Do not modify the dataset generation cell. The fixed random seed (`9`) ensures every student works with the same 300 patients, which is required for consistent results across the class.

### 5. Answer the plot analysis questions

Once **all cells have been executed** and you can see every plot and printed output, open `A9_PlotAnalysis_Questions.md` and answer the questions in a **separate document** (plain text, Word, or PDF — see submission instructions below).

The questions are organized to follow the notebook from top to bottom. Keep the notebook open alongside the question document so you can refer to the exact plots and numbers as you write your answers.

> **Tip:** Do not answer from memory. Every question points to a specific chart or output value. Your answers should cite those values directly.

---

## Files in This Directory

| File | Description |
|------|-------------|
| `A9_NeuralNetworks_HeartDisease.ipynb` | Main assignment notebook. Contains all instructions, code, plots, interactive widgets, and in-notebook reflection questions. **Must be executed before answering the plot analysis questions.** |
| `A9_PlotAnalysis_Questions.md` | Plot and output analysis questions. Answer these **after** running the notebook. Submit your answers as a separate document. |
| `requirements.txt` | List of Python packages required to run the notebook. Install with `pip install -r requirements.txt`. |
| `README.md` | This file. |

---

## Submission

Submit **two files** to the course portal:

1. **`A9_NeuralNetworks_HeartDisease.ipynb`** — the executed notebook
   - All code cells must show their output (plots and printed values visible)
   - All in-notebook reflection questions (Q1–Q6 at the end) must be answered in the Markdown cells
   - Do not remove or reorder any cells

2. **`A9_PlotAnalysis_Answers.pdf`** (or `.docx`) — your written answers to the plot analysis questions
   - Answer every question in `A9_PlotAnalysis_Questions.md`
   - Label each answer clearly with its question number (e.g., **Q1.3**, **Q8.2**)
   - Cite specific values from the notebook output in your answers
   - Answers must reflect the plots and numbers produced by **your own executed notebook**

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| Task 1 — Notebook (Steps 1.1 – 1.8) | Code executed, plots visible, step outputs correct | 25 |
| Task 1 — Interactive Experiment | In-notebook reflection answered | 5 |
| Task 2 — Notebook (Steps 2.1 – 2.6) | Code executed, plots visible, step outputs correct | 25 |
| Task 2 — Interactive Experiment | In-notebook reflection answered | 5 |
| Plot Analysis — Sections 0–5 (Task 1) | Written answers to Task 1 plot questions | 20 |
| Plot Analysis — Sections 6–12 (Task 2 & Synthesis) | Written answers to Task 2 and synthesis questions | 20 |
| **Total** | | **100** |

---

*MRHA CardioWatch Program — Neural Network Clinical Risk Assessment*
*Activity 9 | Introduction to Artificial Intelligence*
