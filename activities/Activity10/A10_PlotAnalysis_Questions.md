# A10 — Plot and Output Analysis Questions
## K-Means Clustering & Support Vector Machines: Digital Marketing Analytics

**Instructions:**
- Answer every question **after** running `A10_KMeans_SVM_DigitalMarketing.ipynb` and confirming all cells show output.
- Every question refers to a specific plot or printed value from the notebook. Keep the notebook open alongside this document.
- Label each answer clearly with its question number (e.g., **Q3.2**).
- Cite exact values from your output wherever a question asks for numbers.
- Submit your answers as a separate document (PDF or Word) — **do not modify the notebook**.

---

## Section 0 — Dataset Overview

**Q0.1.** The notebook generates two separate datasets — one for each task. Complete the following summary table using the printed output at the top of each task:

| | Task 1 — K-Means | Task 2 — SVM |
|-|------------------|--------------|
| Number of customers | 200 | |
| Number of features | 6 | |
| Supervised or Unsupervised? | | |
| Random seed | 10 | |

**Q0.2.** Task 1 is an **unsupervised** learning problem and Task 2 is a **supervised** learning problem. Explain in one sentence each what "unsupervised" and "supervised" mean in the context of digital marketing: what kind of data does each approach require, and what kind of output does it produce?

**Q0.3.** The notebook note in Step 1.1 states: *"Do not modify the dataset generation cells. The fixed random seed (10) ensures every student works with identical data."* Why is reproducibility important when a whole class is analyzing the same assignment? What would happen to the elbow plot and cluster sizes if each student used a different random seed?

---

## Section 1 — Step 1.1 & 1.2: Exploratory Data Analysis (K-Means)

**Q1.1.** The printed summary statistics for the K-Means dataset describe six behavioral features. Complete the table from your output:

| Feature | Mean | Std Dev | Min | Max |
|---------|------|---------|-----|-----|
| session_duration (min) | 10.99 | 4.62 | | |
| pages_per_session | | | | |
| avg_order_value ($) | 70.94 | 40.90 | | |
| purchase_frequency (per month) | | | | |
| email_ctr (%) | 23.36 | 11.84 | | |
| recency_days | 7.76 | 6.55 | | |

**Q1.2.** The EDA bar chart (Step 1.1) shows the mean value of each of the six features across all 200 customers. Looking at the chart, which feature has the **highest mean value** on the original (unnormalized) scale? Which has the **lowest**? Why does this scale difference make it impossible to run K-Means directly on the raw features?

**Q1.3.** The Step 1.2 scatter matrix (or pair-plot panel) visualizes relationships between behavioral features. Identify one pair of features that appears to show a **positive correlation** (both tend to be high or low together). What business logic explains why these two features would move together for StyleHub customers?

---

## Section 2 — Step 1.3: Feature Normalization (K-Means)

**Q2.1.** The normalization output (Step 1.3) prints the statistics **before** and **after** applying `StandardScaler`. After scaling, what are the mean and standard deviation of every feature? Why must all features share the same scale before computing Euclidean distances in K-Means?

**Q2.2.** The normalization comparison plot (Step 1.3) shows the raw and scaled distributions for two features side by side. Describe one visual change between the raw and scaled histograms. Does the **shape** of the distribution change after scaling, or only the axis range and tick values?

**Q2.3.** In Task 1 (K-Means), `StandardScaler` is fit on the **entire 200-customer dataset** — there is no train/test split. In Task 2 (SVM), the scaler is fit only on the **training set**. Explain why these two approaches are correct for their respective tasks. What problem would arise if the SVM scaler were fit on the full 300-customer dataset before splitting?

**Q2.4.** K-Means uses **Euclidean distance** to assign customers to centroids. Without normalization, `avg_order_value` (range ≈ \$15–\$175) would dominate the distance calculation compared to `email_ctr` (range ≈ 2–51%). Compute the maximum raw gap between two customers on each of these two features, and explain in one sentence why the order-value gap would effectively "drown out" the email-CTR gap in an unnormalized distance calculation.

---

## Section 3 — Step 1.4: Elbow Method

**Q3.1.** The Elbow Method table and plot (Step 1.4) show the **Within-Cluster Sum of Squares (WCSS / Inertia)** and **Silhouette Score** for K = 1 through 8. Complete the table from your output:

| K | Inertia (WCSS) | Silhouette Score |
|---|----------------|-----------------|
| 1 | 1200.00 | — |
| 2 | 478.98 | 0.5346 |
| 3 | 286.68 | 0.5097 |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |

**Q3.2.** The printed output computes the **inertia reduction** between consecutive K values. Fill in the three key reductions:
- K=1 → K=2: \_\_\_ (\_\_\_ % reduction)
- K=2 → K=3: \_\_\_ (\_\_\_ % reduction)
- K=3 → K=4: \_\_\_ (\_\_\_ % reduction)

At which step does the reduction drop below 15%? What does this "kink" tell you about the optimal number of clusters?

**Q3.3.** The elbow plot annotation marks **K=3 as the elbow**. Looking at the silhouette scores, K=2 actually achieves a higher silhouette score (0.5346) than K=3 (0.5097). The notebook still recommends K=3. Give one business reason why three customer segments is more useful than two for StyleHub's personalized campaign strategy, even if K=2 produces slightly tighter clusters.

**Q3.4.** The silhouette score measures how well each point fits its own cluster compared to neighboring clusters, ranging from −1 to +1. The score at K=3 is **0.5097**. Interpret this value: does it indicate strong, moderate, or weak cluster separation? What would a score near 0.0 tell you about the cluster structure?

---

## Section 4 — Step 1.5: K-Means Fit (K=3)

**Q4.1.** After fitting K-Means with K=3, the printed output reports three key values. Record them:
- Final Inertia (WCSS): \_\_\_
- Number of iterations to converge: \_\_\_
- Silhouette Score: \_\_\_

**Q4.2.** K-Means converged in only **3 iterations** on this dataset. In the context of the K-Means algorithm, what does convergence mean? Describe the two alternating steps (assignment and update) that the algorithm repeats, and explain what condition causes it to stop.

**Q4.3.** The printed cluster size distribution shows:

| Cluster | Count | Percentage |
|---------|-------|-----------|
| 0 | 42 | 21.0% |
| 1 | 75 | 37.5% |
| 2 | 83 | 41.5% |

The three clusters are **not equally sized**. Is unequal cluster size a problem with K-Means, or is it an expected and valid outcome? What would it mean for StyleHub's campaign planning if one cluster contained 95% of all customers?

**Q4.4.** K-Means uses **random centroid initialization**, which means different random seeds can produce different cluster assignments. The notebook uses `random_state=10` to ensure reproducibility. If you ran K-Means with `random_state=42` instead, would you necessarily get the same three clusters? What technique (mentioned in scikit-learn's `n_init` parameter) is typically used to mitigate sensitivity to initialization?

---

## Section 5 — Step 1.6: Cluster Profiles

**Q5.1.** The cluster profile table (Step 1.6) reports the mean value of each feature per cluster. Complete the table from your output:

| Feature | Cluster 0 | Cluster 1 | Cluster 2 |
|---------|-----------|-----------|-----------|
| session_duration (min) | ~5.2 | ~14.2 | |
| pages_per_session | ~3.2 | ~6.1 | |
| avg_order_value ($) | ~56 | ~118 | ~36 |
| purchase_frequency | ~1.5 | ~3.9 | ~0.5 |
| email_ctr (%) | ~22 | ~36 | ~12 |
| recency_days | ~15.8 | ~2.6 | |

**Q5.2.** The notebook assigns a **marketing persona name** to each cluster. Match each cluster to its persona by circling/underlining the correct name and explaining the single most important feature that drove the assignment:

- **Cluster 0** (avg_order=\$56, freq=1.5/mo, recency=15.8 days): Budget Browsers / Loyal High-Value / Bargain Hunters
- **Cluster 1** (avg_order=\$118, freq=3.9/mo, recency=2.6 days): Budget Browsers / Loyal High-Value / Bargain Hunters
- **Cluster 2** (avg_order=\$36, freq=0.5/mo, recency=9.4 days): Budget Browsers / Loyal High-Value / Bargain Hunters

**Q5.3.** The profile bar chart (Step 1.6) plots normalized cluster centers across all six features. **Cluster 1** (Loyal High-Value) shows the highest bars on most features. Which specific feature shows the **largest positive spike** for Cluster 1? Which feature shows the **smallest value** for Cluster 2? What does this combination tell you about Cluster 2 customers' relationship with the StyleHub brand?

**Q5.4.** Using the cluster profile data, design a one-sentence personalized campaign message for **each** of the three personas. Your message should directly reference at least one numerical statistic from the cluster profile (e.g., average order value, email CTR, or recency).

**Q5.5.** K-Means cluster labels (0, 1, 2) are **arbitrary** — they are assigned by the algorithm based on centroid initialization order, not by behavioral ranking. Why is it important to always inspect the cluster profiles (Step 1.6) rather than assuming Cluster 0 is the "worst" or "best" segment? What could go wrong in a marketing campaign if a team acted on cluster numbers without reading the profiles?

---

## Section 6 — Step 1.7: PCA Visualization

**Q6.1.** PCA is applied in Step 1.7 to project the 6-dimensional normalized data into 2 dimensions for visualization. The printed output reports the **variance explained** by each component. Record the values:
- PC1 variance explained: \_\_\_ %
- PC2 variance explained: \_\_\_ %
- **Total (2-component) variance explained: \_\_\_ %**

**Q6.2.** The PCA scatter plot (Step 1.7) shows 200 customers colored by K-Means cluster label. Describe the spatial arrangement of the three clusters in the 2D projection:
- Are the clusters visually distinct, or do they overlap heavily?
- Which two clusters appear to be **closest to each other** in the PCA space?
- Is there a clear empty region separating any pair of clusters?

**Q6.3.** The 2-component PCA projection captures **84.7%** of the total variance in the original 6 features. The remaining 15.3% is discarded. What does this mean for interpreting the PCA scatter plot — can you fully trust the cluster separations you see in 2D? Why is PCA used only for *visualization* here and not as a preprocessing step before K-Means?

**Q6.4.** The PCA plot annotation prints the cluster centroids in the 2D space as colored "×" markers. In PCA space, the centroid of **Cluster 1** (Loyal High-Value) appears in the upper-right region of the plot, while **Cluster 2** (Budget Browsers) appears in the lower-left. What does the horizontal distance between these two centroids along the PC1 axis tell you about which original features most distinguish these two groups? (Hint: PC1 captures 68.3% of variance — which behavioral differences most likely dominate PC1?)

---

## Section 7 — Step 1.8: Interactive K-Means Widget

**Q7.1.** The interactive widget (Step 1.8) lets you drag the **K slider** from 2 to 8 and observe how the PCA scatter plot and cluster profiles change. Run the widget and experiment with at least three values of K. Complete the following table from your observations:

| K | Visual impression of cluster separation | Biggest change from K=3 |
|---|----------------------------------------|------------------------|
| 2 | | |
| 3 | (baseline) | — |
| 5 | | |

**Q7.2.** When you increase K to 6 or 7, some clusters become very small (fewer than 10 customers). What does this indicate about the true underlying structure of the data? In a real marketing campaign, what is the practical minimum cluster size below which a dedicated campaign message becomes economically unviable?

**Q7.3.** Based on your widget experiments, does the PCA scatter plot at K=4 show meaningfully better-separated clusters than K=3, or does one of K=3's clusters simply get split into two similar-looking halves? Use this observation to justify (or challenge) the K=3 choice recommended by the elbow method.

---

## Section 8 — Step 2.1 & 2.2: SVM Dataset and Normalization

**Q8.1.** The SVM dataset (Step 2.1) contains 300 customers with a binary label: **clicked the retargeting ad (1)** or **did not click (0)**. Record the class distribution from your output:

| Class | Count | Percentage |
|-------|-------|-----------|
| 0 — Did Not Click | 169 | 56.3% |
| 1 — Clicked | | |

Is this dataset balanced or imbalanced? If a naive model always predicted "did not click," what accuracy would it achieve?

**Q8.2.** The EDA output (Step 2.1) prints **feature means by class**. Complete the table:

| Feature | Class 0 (No Click) | Class 1 (Clicked) | Difference |
|---------|-------------------|-------------------|-----------|
| income_k (\$000) | 59.35 | 78.97 | +19.62 |
| pages_viewed | 10.64 | | |
| prev_purchases | | | |
| age | | | |
| browsing_hours | | | |

Which feature shows the **largest absolute difference** between clickers and non-clickers? What does this suggest about the most predictive customer behavior for ad click prediction?

**Q8.3.** The scatter plot (Step 2.1) shows `income_k` vs `pages_viewed` colored by class (blue = no click, red = clicked). Looking at the plot, do the two classes appear to be **linearly separable** (i.e., could a straight line cleanly divide them), or do they overlap significantly? How does your visual assessment here help predict whether a Linear SVM or RBF SVM will perform better?

**Q8.4.** Step 2.2 applies `StandardScaler` and performs an 80/20 train/test split with `random_state=10`. Record the split sizes:
- Training set: \_\_\_ customers (\_\_\_%)
- Test set: \_\_\_ customers (\_\_\_%)

The scaler is fit **only on the training set**. Explain why fitting the scaler on the test set too would constitute data leakage, even though the scaler only computes means and standard deviations.

---

## Section 9 — Step 2.3: Linear SVM

**Q9.1.** The Linear SVM (Step 2.3) is trained with default `C=1.0`. Record the performance values from your output:
- Training accuracy: \_\_\_ %
- Test accuracy: \_\_\_ %
- Train–test gap: \_\_\_ percentage points
- Number of support vectors (Class 0 / Class 1): \_\_\_ / \_\_\_

**Q9.2.** The confusion matrix (Step 2.3) for the Linear SVM shows:

|  | Predicted: No Click (0) | Predicted: Clicked (1) |
|--|------------------------|----------------------|
| **Actual: No Click (0)** | TN = 21 | FP = 13 |
| **Actual: Clicked (1)** | FN = 12 | TP = 14 |

Using these four values, manually compute:
- **Precision** = TP / (TP + FP) = \_\_\_
- **Recall** = TP / (TP + FN) = \_\_\_
- **Accuracy** = (TP + TN) / Total = \_\_\_

Show your calculations and confirm they match the printed output.

**Q9.3.** The train–test gap for the Linear SVM is approximately **20 percentage points** (78.8% train vs. 58.3% test). What does this large gap indicate about the model's behavior? Name the concept this illustrates, and describe one change to the model or training procedure that could reduce this gap.

**Q9.4.** The printed output states the Linear SVM has **69 support vectors for Class 0 and 68 for Class 1** — a total of 137 out of 240 training points. In the SVM framework, what is a **support vector**? If the number of support vectors is close to the total training set size, what does this tell you about the quality of the linear decision boundary for this dataset?

---

## Section 10 — Step 2.4: Kernel Comparison

**Q10.1.** Step 2.4 compares three SVM kernels with default hyperparameters. Record the results from the printed output and grouped bar chart:

| Kernel | Train Accuracy | Test Accuracy | Gap (pp) | Support Vectors |
|--------|---------------|--------------|---------|----------------|
| Linear | 78.8% | 58.3% | 20.5 | 137 (69/68) |
| RBF | | | | |
| Polynomial | | | | |

**Q10.2.** The **Polynomial kernel** achieves the highest test accuracy of the three in the comparison. Yet the notebook cautions against declaring it the "winner" based on this comparison alone. Why? What is missing from this single train/test split evaluation that would be needed to confidently select a kernel?

**Q10.3.** The **RBF kernel** has **82 + 76 = 158 support vectors** compared to the Linear kernel's 137. Why might the RBF kernel require more support vectors than a linear kernel on this dataset? What does a larger number of support vectors generally imply about the complexity of the learned decision boundary?

**Q10.4.** The kernel trick allows SVMs to operate in very high-dimensional feature spaces without explicitly computing the transformation. In plain language, explain what the **RBF (Radial Basis Function) kernel** measures between two data points. Why is this kernel well suited for customer behavioral data where the relationship between features and click probability may not be linear?

---

## Section 11 — Step 2.5: Grid Search Cross-Validation

**Q11.1.** The Grid Search (Step 2.5) tests a 5 × 5 grid of C and γ values. Record the best hyperparameters and CV score from your output:
- Best C: \_\_\_
- Best γ (gamma): \_\_\_
- Best cross-validation accuracy: \_\_\_ %
- Total model fits evaluated: \_\_\_ (5 C values × 5 γ values × 5 folds)

**Q11.2.** The Grid Search heatmap (Step 2.5) plots CV accuracy as a color gradient across all 25 (C, γ) combinations. Describe the general pattern you observe: at which corner of the grid (high C / low γ, low C / high γ, etc.) does the best performance cluster? What does this tell you about the preferred trade-off between regularization strength and kernel bandwidth for this dataset?

**Q11.3.** The best CV accuracy from Grid Search is **76.67%**, but the test set accuracy of the best model (Step 2.6) is lower. Why can CV accuracy be higher than the final test accuracy? Does this mean Grid Search "cheated"? Explain in 1–2 sentences.

**Q11.4.** The notebook uses a `Pipeline([('scaler', StandardScaler()), ('svm', SVC(...))])` inside the Grid Search. Why is it essential to include the scaler inside the Pipeline rather than scaling the data once before calling `GridSearchCV`? What leakage problem would the single pre-scaling approach introduce?

**Q11.5.** The Grid Search evaluated **25 combinations × 5 folds = 125 model fits**. The notebook's reflection question Q4 asks what problems this would face on 10 million customers with 50 features. Name at least **two** scalability bottlenecks that would emerge, and describe one alternative to exhaustive grid search that is more computationally efficient.

---

## Section 12 — Step 2.6: Best Model Evaluation

**Q12.1.** The best model (Grid Search winner, Step 2.6) is evaluated on the 60-customer test set. Record the full evaluation from the printed output:

| Metric | Value |
|--------|-------|
| Test Accuracy | 58.3% |
| Precision (Class 1) | |
| Recall (Class 1) | |
| F1-score (Class 1) | |

Confusion matrix:

|  | Predicted: No Click | Predicted: Clicked |
|--|--------------------|--------------------|
| **Actual: No Click** | TN = 21 | FP = 13 |
| **Actual: Clicked** | FN = 12 | TP = 14 |

**Q12.2.** The best model's test accuracy (58.3%) is **not significantly better** than the baseline Linear SVM (also 58.3%). Yet the Grid Search found C=100 and γ=0.001 as the optimal hyperparameters with a CV accuracy of 76.67%. Explain this apparent contradiction: why might hyperparameter tuning improve cross-validation accuracy without improving held-out test accuracy?

**Q12.3.** In the marketing context, **False Negatives (FN = 12)** represent customers who *would have clicked* but were not targeted by the retargeting ad. **False Positives (FP = 13)** represent customers who were shown the ad but did not click, wasting ad budget. For StyleHub's campaign, which error is more costly: missing a likely-clicker (FN) or wasting a budget impression (FP)? Justify your answer using the business context.

**Q12.4.** The model's **Recall for Class 1 is 53.85%** — it detects just over half of the customers who will actually click. If StyleHub's campaign budget allows targeting 40% of all customers, would you recommend using this SVM to *select* that 40%, or would you use a **probability threshold** lower than 0.5 to increase recall? Explain the trade-off.

---

## Section 13 — Step 2.7: Decision Boundary Visualization

**Q13.1.** The decision boundary plot (Step 2.7) visualizes the SVM boundary using only **two features**: `income_k` and `pages_viewed`. The printed output shows:

| Kernel | 2-Feature Test Accuracy | Support Vectors |
|--------|------------------------|----------------|
| Linear | 61.7% | 77 / 77 |
| RBF | 61.7% | 76 / 74 |

The 2-feature test accuracy (61.7%) differs from the 5-feature test accuracy (58.3% for Linear). Why can a 2-feature model sometimes outperform a 5-feature model? What does this suggest about the other three features (`prev_purchases`, `age`, `browsing_hours`) for this particular dataset and split?

**Q13.2.** The Linear SVM decision boundary plot shows a **straight line** separating the two classes, while the RBF SVM shows a **curved boundary**. Describe one specific region in the plot where the RBF boundary captures a cluster of red points (clicked) that the linear boundary misclassifies. What does this tell you about the non-linearity in the relationship between income, page views, and ad click behavior?

**Q13.3.** In the decision boundary plot, the **support vectors** are highlighted with circles around the data points nearest to the margin boundary. Looking at the Linear SVM plot, are the support vectors concentrated near the boundary line, or are they scattered throughout the plot? What does the margin width (distance between the two dashed margin lines) tell you about how confident the SVM is in its classification near the decision boundary?

**Q13.4.** The decision boundary visualization uses only `income_k` and `pages_viewed` because it is impossible to visualize a 5-dimensional boundary in 2D. In a real deployment, the model would use all 5 features. Identify one customer type that might be correctly classified by the full 5-feature model but incorrectly placed by the 2-feature visualization — for example, a customer with low income and few page views but very high `prev_purchases`. Why can such a customer appear in the "wrong" region of the 2D plot?

---

## Section 14 — Cross-Task Synthesis

**Q14.1.** In Task 1, K-Means discovered three customer behavioral segments **without any labels**. In Task 2, the SVM learned to predict ad clicks **from labeled examples**. The notebook's conclusions table (Section 3.10) summarizes the difference. Using the comparison table as a guide, explain in 2–3 sentences why a marketing team would need *both* techniques — not just one — to run a fully AI-driven campaign for StyleHub's spring sale.

**Q14.2.** The K-Means cluster labels (0, 1, 2) from Task 1 could theoretically be added as a new feature to the SVM in Task 2 — giving the click predictor a "customer segment" input. Describe one potential **benefit** of this combined approach and one **risk** you would need to watch for. (Hint: think about when the K-Means model was trained and what happens when new customers arrive who were not in the original 200.)

**Q14.3.** Feature normalization was required in **both** tasks. However, the reason differs:
- In K-Means, normalization prevents high-range features from dominating **Euclidean distance**.
- In SVM, normalization helps the optimizer find the **maximum-margin hyperplane** efficiently.

Explain in one sentence each why unnormalized features cause problems in each of these two specific mechanisms. Use the actual feature ranges from this notebook to make your explanation concrete (e.g., avg_order_value ≈ \$15–\$175 vs. email_ctr ≈ 2–51% for Task 1; income_k ≈ \$30–\$110k vs. age ≈ 18–65 for Task 2).

**Q14.4.** The Elbow Method (Task 1) and Grid Search CV (Task 2) are both **model selection** techniques — they help choose the best hyperparameter value (K for K-Means; C and γ for SVM). Compare the two approaches: what is each one optimizing for, and what is the key difference in how they evaluate candidate hyperparameters? (Hint: one uses a held-out validation set; the other uses a within-sample metric.)

**Q14.5.** The SVM test accuracy plateaued around **58–65%** across all kernels and hyperparameter settings. Yet the dataset was generated from a known logistic formula with five features. List two possible explanations for why the SVM cannot achieve higher accuracy despite having access to the correct features. Your answer should reference at least one concept from Session 31 (e.g., sample size, noise, class overlap, or the limitation of the kernel chosen).

---

*NovaPulse Media — StyleHub Spring Sale Campaign Analytics*
*Activity 10 | Introduction to Artificial Intelligence*
