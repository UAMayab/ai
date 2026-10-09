# Activity 17: Second Opinion — Support Vector Machines for Breast-Cancer Diagnosis
## Session 31
## Due date (mm/dd/yyyy): 11/08/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

When a breast mass is found, a doctor can take a tiny sample of cells with a fine needle and
examine it under a microscope. In the early 1990s, researchers at the University of Wisconsin
measured 30 properties of the cell nuclei in those images (size, shape, texture...) for 569
patients whose diagnosis was later confirmed. Can a computer learn to tell **malignant** (cancer)
from **benign** masses from those measurements, as a "second opinion" for the doctor?

You will answer that with a **Support Vector Machine (SVM)**. First you will see exactly how an SVM
works on small 2D examples: the "widest street", support vectors, the **C** parameter, and
**kernels**. Then you will apply it to the real medical data and decide how you would tune it and
whether you would trust it.

**No programming background is required.** Everything happens by clicking, moving sliders, and
reading charts in the app.

> ⚠️ **This app is a teaching tool, not a medical device.** It uses a public research dataset from the
> 1990s and must never be used for decisions about real patients.

**App link:** https://uam-aiclass-a17.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

Six tabs:

1. **🛣️ The Widest Street** — the decision boundary, the margin, and the support vectors on a simple
   2D example.
2. **🎚️ C and the Soft Margin** — the same idea on data with one mislabeled point (an *outlier*);
   move C and watch the margin, the errors, and the test accuracy.
3. **🌀 Kernels** — curved boundaries with the polynomial, RBF, and sigmoid kernels on three shapes
   that no straight line can separate.
4. **🎨 Multi-class** — two ways to handle four classes: one-vs-one and one-vs-rest.
5. **🩺 Second Opinion: Diagnosis** — the real breast-cancer data, with recall, precision, F1, a
   confusion matrix, and a **grid search with cross-validation** to choose C and gamma.
6. **⚖️ SVM vs. Logistic Regression** — the same patients with logistic regression (Activity 14),
   side by side.

> 💡 **Hint:** When the app first opens, wait until it finishes loading (the running indicator in
> the top-right corner disappears) before switching tabs.

### Your Tasks

1. **In The Widest Street**, read the explanation, then switch on **"Retrain the SVM using only the
   support vectors"**. Take a screenshot with the switch on.

   > 💡 **Hint:** The yellow circles are the support vectors. Watch the green lines when you flip
   > the switch, and read the green message next to the chart.

2. **In C and the Soft Margin**, set C to **0.001**, then **1**, then **10000**, and take a
   screenshot of each. Also look at the "Every C at once" chart.

   > 💡 **Hint:** Find the star (the mislabeled point) in each picture. Is the SVM treating it as a
   > mistake to ignore, or is it bending the street to get it right? Compare training accuracy with
   > test accuracy.

3. **In Kernels**, with the Circles dataset, C = 1, gamma = 1, and degree = 2, try all four kernels.
   Then use the RBF kernel and raise gamma (and C) until the boundary overfits. Take a screenshot of
   the overfitting case.

   > 💡 **Hint:** Overfitting looks like small "islands" around single points. Turn on **Show the
   > test points** and compare training accuracy with test accuracy.

4. **In Multi-class**, keep the linear kernel and C = 1. Take a screenshot showing all three charts
   and the table.

   > 💡 **Hint:** Look at the blue *Middle* class. Can a single straight line separate it from all
   > three other classes at once?

5. **In Second Opinion: Diagnosis**, read the results with the default settings, then switch to
   **All 30 features**. Take a screenshot of each, including the confusion matrix.

   > 💡 **Hint:** In medicine, the two kinds of mistakes are not equally bad. The confusion matrix
   > spells them out: *missed cancers* and *false alarms*.

6. **Still in the Diagnosis tab (all 30 features)**, scroll to the grid search. Choose by
   **Accuracy**, then by **Recall**, and take a screenshot of each heatmap and its test results.

   > 💡 **Hint:** The heatmap is computed only from the training patients. The test patients are used
   > once, at the end, for the winning combination.

7. **In SVM vs. Logistic Regression**, look at both the two-feature and the 30-feature comparisons,
   and the circles example at the bottom. Take a screenshot of the 30-feature table.

   > 💡 **Hint:** Read the blue message under the table: it says which model won on these patients,
   > and by how many patients.

8. **Fill out `A17_ReflectionQuestions.md`**, using the exact numbers from your screenshots, and
   submit it along with your labeled screenshots (a `.zip` with the `.md` file and the images is
   fine).

   > 💡 **Hint:** Before submitting, check each answer against **How Your Grade Is Calculated**
   > below. It lists exactly what earns full points on every question.

### How Your Grade Is Calculated

Your grade is out of **100 points**, split across the 12 reflection questions. There are three
kinds of questions, and each kind is graded differently:

- **Exact answers** (Q1, Q3, Q5, Q8, Q9, and the numbers in Q7, Q10, Q11): there is one correct
  value, read from the app. With the settings the question gives, everyone sees exactly the same
  numbers. You get full points for correct values and partial credit when some parts are right.
  Small rounding differences are accepted.
- **Your own experiment** (Q6): every student's settings are different, so there is no single right
  number. But the app always gives exactly the same result for the same settings, so any setting you
  report can be re-run and checked. Numbers that no setting can reproduce get no credit.
- **Explain in your own words** (Q2, Q4, Q12, and the explanations in Q5, Q7, Q9, Q10, Q11): graded
  on four levels.
  - **Excellent:** complete, correct, and supported by your own numbers.
  - **Proficient:** correct, but missing a required part or not tied to your own numbers.
  - **Developing:** vague, incomplete, or partly wrong.
  - **Insufficient:** missing or wrong.

| # | Question | Points | Full points if you… | Partial credit |
|---|---|---:|---|---|
| 1 | Support vectors and margin | 6 | report the support vectors, margin width, and test accuracy, and what changed when retraining on the support vectors only | 3–4: some values right |
| 2 | What a support vector is | 6 | define support vectors in your own words and connect the definition to your Q1 result | Proficient 4–5 · Developing 2–3 · Insufficient 0–1 |
| 3 | Three values of C | 12 | report all six values for each of the three C values | 5–9: most values right, or one C missing |
| 4 | Judging the lecture's claim about C | 8 | take a clear position on the claim, support it with your Q3 numbers, and justify your choice of C | Proficient 5–7 · Developing 2–4 · Insufficient 0–1 |
| 5 | Four kernels on the circles | 8 | report all four test accuracies and explain why a straight line can't work | 4–6: values right but weak explanation, or one value wrong |
| 6 | An overfitting RBF | 6 | report reproducible settings with both accuracies, a screenshot, and a description of the boundary | Proficient 4–5 · Developing 2–3 · Insufficient 0–1 |
| 7 | One-vs-one vs. one-vs-rest | 8 | report both numbers of SVMs and both Middle-class accuracies, and explain the difference | 4–6: numbers right but weak explanation |
| 8 | Diagnosis, two features | 8 | report all six values correctly | 3–6: some values right |
| 9 | Diagnosis, 30 features | 6 | report all six values and say what changed most | 3–4: values right but no comparison |
| 10 | Grid search: accuracy vs. recall | 12 | report both winners (C, gamma, cross-validation score) with their missed cancers and false alarms, choose one with a clinical reason, and explain why the test set can't be used for tuning | Proficient 8–10 · Developing 4–7 · Insufficient 0–3 |
| 11 | SVM vs. logistic regression | 10 | report both models' accuracy and missed cancers, name the winner, and use both results to judge the lecture's claim | Proficient 6–8 · Developing 3–5 · Insufficient 0–2 |
| 12 | Applications and safeguards | 10 | give a lecture application with a reason an SVM suits it, plus two specific, realistic safeguards | Proficient 6–8 · Developing 3–5 · Insufficient 0–2 |
| | **Total** | **100** | | |

**Delivery format:** your answers must be in a Markdown file (`A17_ReflectionQuestions.md`); a `.zip`
with that file and your screenshots is fine. Answers delivered in another format (PDF, Word, `.txt`)
lose **5 points** from the total.

### Running It Yourself (optional)

```bash
conda activate ai_uam
cd Activity17
pip install -r requirements.txt
streamlit run app.py
```

### About the Data

- **Breast Cancer Wisconsin (Diagnostic)**, W. Wolberg, O. Mangasarian, N. Street, and W. Street, UCI
  Machine Learning Repository (1993), DOI [10.24432/C5DW2B](https://doi.org/10.24432/C5DW2B),
  licensed CC BY 4.0. Introductory paper: W. N. Street, W. H. Wolberg, and O. L. Mangasarian,
  "Nuclear feature extraction for breast tumor diagnosis" (1993). The app uses the copy included in
  scikit-learn.
- The 2D examples in the first four tabs are fictional, generated with a fixed random seed so that
  everyone sees exactly the same data.

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [scikit-learn: Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
