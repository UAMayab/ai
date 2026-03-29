# Activity 10 — K-Means Clustering & Support Vector Machines: Digital Marketing Analytics

**Course:** Introduction to Artificial Intelligence
**Sessions:** 29 (K-Means Algorithm) and 31 (Support Vector Machines)
**Topic:** Unsupervised Clustering · Supervised Classification · Hyperparameter Tuning

---

## Introduction

Welcome to Activity 10. In this assignment you will apply two foundational AI algorithms to a real-world **digital marketing** problem.

You will work as a data scientist at **NovaPulse Media**, a digital marketing agency whose client **StyleHub** — an online fashion retailer — is preparing for its biggest promotional campaign of the year. Your job is to help StyleHub answer two critical business questions:

1. **Who are our customers?** Use **K-Means Clustering** (Session 29) to segment the customer base into behaviorally distinct groups, enabling personalized campaign messaging for each group.

2. **Which customers will click on our retargeting ad?** Use **Support Vector Machines** (Session 31) to build a binary classifier that predicts ad click probability, so the paid advertising budget is focused on high-probability converters.

By the end of this activity you will be able to:

- Explain the K-Means algorithm: centroid initialization, assignment, update, and convergence
- Normalize features and understand why scale matters for distance-based algorithms
- Apply the **Elbow Method** and **Silhouette Score** to choose the optimal number of clusters K
- Visualize high-dimensional clusters using **PCA** (2D projection)
- Interpret cluster profiles and translate them into actionable marketing personas
- Train and evaluate **Linear** and **RBF** SVM classifiers
- Explain the role of the **kernel trick**, **margin**, **support vectors**, and the **C parameter**
- Tune SVM hyperparameters (C, γ) using **Grid Search Cross-Validation**
- Interpret a **confusion matrix** and classification report in a marketing context
- Visualize SVM **decision boundaries** for two features

---

## Background: Why AI for Digital Marketing?

Modern e-commerce companies interact with hundreds of thousands of customers daily. Two of the most impactful AI applications in marketing are:

**Segmentation (Unsupervised):** Rather than treating all customers identically, clustering algorithms discover natural behavioral groups from raw web analytics data — without any predefined labels. Each cluster receives a tailored message: loyalty rewards for high-value customers, discount alerts for bargain hunters, re-engagement offers for inactive browsers.

**Conversion Prediction (Supervised):** Retargeting ads are expensive. A classifier that identifies the 20% of customers most likely to click reduces cost-per-acquisition by concentrating impressions where they are most effective. SVMs are well-suited here because they can handle non-linear relationships between customer attributes and click behavior.

---

## Tasks

| Task | Algorithm | Focus |
|------|-----------|-------|
| **Task 1** | K-Means Clustering | Customer segmentation — discover 3 behavioral personas |
| **Task 2** | Support Vector Machines | Ad click prediction — binary classification with kernel comparison and grid search |

Each task follows a full machine learning pipeline:
1. Generate and explore the dataset
2. Normalize features
3. Build and evaluate the model
4. Visualize results
5. Tune and improve
6. Interpret outputs in business terms
7. Interactive experiment with ipywidgets

---

## Session Coverage

| Session | Topic | Where it appears in the notebook |
|---------|-------|----------------------------------|
| 29 — K-Means Algorithm | Centroid init, assignment, update, elbow, silhouette | Task 1 Steps 1.1–1.8 |
| 31 — Support Vector Machines | Hyperplane, margin, kernel trick, C parameter, Grid Search | Task 2 Steps 2.1–2.8 |

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
jupyter notebook A10_KMeans_SVM_DigitalMarketing.ipynb
```

### 4. Run the cells in order

Start from the top and run each cell sequentially. Both datasets are generated in early cells — all later cells depend on them.

> **Important:** Do not modify the dataset generation cells. The fixed random seed (`10`) ensures every student works with identical data, which is required for consistent results across the class.

### 5. Answer the plot analysis questions

Once **all cells have been executed** and you can see every plot and printed output, open `A10_PlotAnalysis_Questions.md` and answer the questions in a **separate document** (plain text, Word, or PDF — see submission instructions below).

The questions are organized to follow the notebook from top to bottom. Keep the notebook open alongside the question document so you can refer to the exact plots and numbers as you write your answers.

> **Tip:** Do not answer from memory. Every question points to a specific chart or printed value. Your answers should cite those values directly.

---

## Files in This Directory

| File | Description |
|------|-------------|
| `A10_KMeans_SVM_DigitalMarketing.ipynb` | Main assignment notebook. Contains all instructions, code, plots, interactive widgets, and in-notebook reflection questions. **Must be executed before answering the plot analysis questions.** |
| `A10_PlotAnalysis_Questions.md` | Plot and output analysis questions. Answer these **after** running the notebook. Submit your answers as a separate document. |
| `requirements.txt` | List of Python packages required to run the notebook. Install with `pip install -r requirements.txt`. |
| `README.md` | This file. |

---

## Submission

Submit **two files** to the course portal:

1. **`A10_KMeans_SVM_DigitalMarketing.ipynb`** — the executed notebook
   - All code cells must show their output (plots and printed values visible)
   - All in-notebook reflection questions (Q1–Q5 at the end) must be answered in the Markdown cells
   - Do not remove or reorder any cells

2. **`A10_PlotAnalysis_Answers.pdf`** (or `.docx`) — your written answers to the plot analysis questions
   - Answer every question in `A10_PlotAnalysis_Questions.md`
   - Label each answer clearly with its question number (e.g., **Q3.2**, **Q12.3**)
   - Cite specific values from the notebook output in your answers
   - Answers must reflect the plots and numbers produced by **your own executed notebook**

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| Task 1 — Notebook (Steps 1.1 – 1.7) | Code executed, plots visible, step outputs correct | 25 |
| Task 1 — Interactive Experiment | In-notebook reflection answered | 5 |
| Task 2 — Notebook (Steps 2.1 – 2.7) | Code executed, plots visible, step outputs correct | 25 |
| Task 2 — Interactive Experiment | In-notebook reflection answered | 5 |
| Plot Analysis — Sections 0–7 (Task 1) | Written answers to Task 1 plot questions | 20 |
| Plot Analysis — Sections 8–14 (Task 2 & Synthesis) | Written answers to Task 2 and synthesis questions | 20 |
| **Total** | | **100** |

---

*NovaPulse Media — StyleHub Spring Sale Campaign Analytics*
*Activity 10 | Introduction to Artificial Intelligence*
