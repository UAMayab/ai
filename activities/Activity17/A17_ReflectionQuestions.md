# Activity 17 — Reflection Questions: Second Opinion (Support Vector Machines)

Answer every question using the app's **default settings**, unless a question tells you to change
something. Submit this file together with your labeled screenshots — do not just describe the app,
use your actual results.

---

## Part A — The widest street (margin and support vectors)

1. In *The Widest Street* tab, report the number of **support vectors**, the **margin width**, and
   the **test accuracy**. Then turn on **"Retrain the SVM using only the support vectors"**: how
   many training points were used, and how much did the line change?

2. In your own words, what is a **support vector**, and why does the result of Question 1 explain
   the name "*support* vector machine"?

## Part B — C and the soft margin

3. In the *C and the Soft Margin* tab, report the following for **C = 0.001**, **C = 1**, and
   **C = 10000**: margin width, number of support vectors, training points on the wrong side,
   training accuracy, test accuracy, and how the outlier is classified.

4. The lecture says: *"A larger value of C can be beneficial when the data points are not
   well-separated or when there is a significant presence of noise or outliers."* Using your numbers
   from Question 3, do you agree? Which C would you choose for this data, and why?

## Part C — Kernels

5. In the *Kernels* tab, with the **Circles** dataset, C = 1, gamma = 1, and degree = 2, report the
   **test accuracy** of the linear, polynomial, RBF, and sigmoid kernels. Why does the linear kernel
   fail on this dataset?

6. Using the **RBF** kernel, find settings (dataset, C, gamma) that clearly **overfit**: training
   accuracy much higher than test accuracy. Report your settings and both accuracies, include a
   screenshot, and describe what the boundary looks like.

## Part D — More than two classes

7. In the *Multi-class* tab (linear kernel, C = 1), how many binary SVMs does **one-vs-one** train,
   and how many does **one-vs-rest** train? Report the **Middle** class's test accuracy for each
   strategy, and explain why one-vs-rest has trouble with the class in the middle.

## Part E — The practical case: breast-cancer diagnosis

8. In the *Second Opinion: Diagnosis* tab, with the default settings (two features: worst radius and
   worst concave points; RBF kernel; C = 1; gamma = scale), report the **accuracy, recall,
   precision, F1 score**, the number of **missed cancers** (false negatives), and the number of
   **false alarms** (false positives).

9. Switch to **All 30 features** (same kernel, C, and gamma). Report the same six values. Did the
   extra features help? Which numbers changed the most?

10. In the grid search (with **all 30 features**), report the best C, the best gamma, and the
    cross-validation score when choosing by **accuracy**, and again when choosing by **recall**. For
    each choice, report how many cancers the model missed and how many false alarms it raised on
    the test patients. Which of the two would you rather use as a screening aid, and why? Why must
    the test patients not be used to choose C and gamma?

11. In the *SVM vs. Logistic Regression* tab with **All 30 features** and the default settings,
    report both models' accuracy and number of missed cancers. Which model did better on these
    patients? Then look at the **circles** example at the bottom of the tab. The lecture says SVMs
    "excel" compared with methods like logistic regression. Based on *both* results, when is that
    true, and when isn't it?

## Part F — Responsible use

12. Name one other application of SVMs mentioned in the lecture and explain why an SVM suits it. Then
    describe **two safeguards** a hospital should require before using a model like the one in this
    app to support real diagnoses.
