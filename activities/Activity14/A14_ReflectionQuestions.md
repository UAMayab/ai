# Activity 14 — Reflection Questions: ShopSmart Churn Prediction

Answer every question below using the **Canonical Model** sections only (not the playground),
unless a question specifically asks about your own playground exploration. Submit this file
separately from your screenshots — do not just describe the app, use your actual results.

---

1. For the **plain (unregularized) model**, report the train accuracy, test accuracy, train
   loss, and test loss.

2. Report all 8 coefficients of the **Canonical L2 (Ridge) Model**.

3. Report the **Canonical L2 Model's** train and test accuracy. How do they compare to the
   plain model's from Question 1?

4. Report all 8 coefficients of the **Canonical L1 (Lasso) Model**, and name exactly which
   feature(s) were driven to zero.

5. Report the **Canonical L1 Model's** train and test accuracy.

6. In your own words, explain the key difference between how **L2** and **L1** treat
   coefficients as λ grows, based on what you saw in the bar charts.

7. True or False: the unregularized model's 100% training accuracy means it's the best model to
   actually deploy for predicting churn on new customers. Justify your answer using the actual
   numbers from Question 1.

8. Name one **real business or IT scenario** (other than churn prediction) where a
   classification model could overfit due to too many irrelevant features. Which
   regularization type (L1 or L2) would you reach for first, and why?
