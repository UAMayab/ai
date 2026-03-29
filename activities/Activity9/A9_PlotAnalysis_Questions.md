# A9 — Plot and Output Analysis Questions
## Neural Networks: Heart Disease Classification

**Instructions:**
- Answer every question **after** running `A9_NeuralNetworks_HeartDisease.ipynb` and confirming all cells show output.
- Every question refers to a specific plot or printed value from the notebook. Keep the notebook open alongside this document.
- Label each answer clearly with its question number (e.g., **Q3.2**).
- Cite exact values from your output wherever a question asks for numbers.
- Submit your answers as a separate document (PDF or Word) — **do not modify the notebook**.

---

## Section 0 — Dataset Overview

**Q0.1.** The dataset contains 300 patients. Looking at the printed summary statistics, what are the mean values of `age`, `sbp`, and `cholesterol` across all 300 patients? Compare the mean `sbp` (141.68 mmHg) against the clinical reference table in the README. Does the average patient in this dataset fall in the "Healthy" or "At Risk" category for blood pressure?

**Q0.2.** The dataset was generated using a sigmoid-based risk formula combining five biomarkers. Looking at the class distribution printed in Step 1.2, how many patients (count and percentage) belong to each class? Is the dataset balanced or imbalanced? What problems can arise when training a classifier on a highly imbalanced dataset?

---

## Section 1 — Step 1.1: MCP Neuron

**Q1.1.** The printed truth table shows the output of the AND gate (θ = 2) and OR gate (θ = 1) for all four combinations of inputs. Fill in the following from your output:

| x1 | x2 | AND (θ=2) | OR (θ=1) |
|----|----|-----------|---------:|
| 0  | 0  |           |          |
| 0  | 1  |           |          |
| 1  | 0  |           |          |
| 1  | 1  |           |          |

**Q1.2.** The MCP Neuron plot (Step 1.1) shows two scatter plots side by side — one for the AND gate and one for the OR gate. Blue dots represent "No Fire (0)" and red dots represent "Fires (1)". How many red dots appear in the AND gate plot? How many appear in the OR gate plot? Explain in one sentence why the counts differ even though both gates use the same input weights (w₁ = w₂ = 1).

**Q1.3.** The clinical analogy printed in the output states: *"AND gate: flag patient ONLY if BOTH risk factors are present (conservative). OR gate: flag patient if EITHER risk factor is present (sensitive)."* In the context of cardiac screening, which gate strategy would you expect to produce more **False Negatives** (missed at-risk patients)? Justify your answer.

---

## Section 2 — Step 1.2: Exploratory Data Analysis

**Q2.1.** The EDA output prints the **feature means by class**. Complete the following table from your output:

| Feature | Class 0 (No HD) | Class 1 (HD) | Difference |
|---------|-----------------|--------------|-----------|
| age | 49.44 | 55.74 | +6.30 |
| bmi | | | |
| sbp | | | |
| cholesterol | | | |
| resting_hr | | | |

Which feature shows the **largest absolute difference** between the two classes? What does this suggest about its predictive power?

**Q2.2.** The EDA plot (Step 1.2) contains six panels: one bar chart for class distribution and five histograms colored by class (blue = No HD, red = HD). Look at the histogram for `age`. Describe in 1–2 sentences what the distribution tells you: do the two classes overlap heavily, or do they separate cleanly? Which end of the age range (younger vs. older) appears more associated with heart disease?

**Q2.3.** Look at the histogram for `sbp` (Systolic Blood Pressure). The at-risk group (red) tends to concentrate at higher SBP values. At roughly what SBP value do the two distributions appear to diverge most clearly? How does this relate to the clinical reference thresholds (≥ 130 mmHg = At Risk)?

**Q2.4.** The class distribution bar chart shows **43.7% positive** (131 patients with heart disease). If a naive classifier always predicted "No Heart Disease" regardless of the input, what accuracy would it achieve on this dataset? Why does this make accuracy alone an unreliable metric for this problem?

---

## Section 3 — Step 1.3: Feature Normalization

**Q3.1.** The notebook prints feature statistics **before** and **after** applying `StandardScaler`. The raw `sbp` feature has mean = 141.68 mmHg and std = 24.67, while `bmi` has mean = 28.33 and std = 5.52. After scaling, what are the mean and standard deviation of each feature in the training set? Why is this transformation essential for neural network training?

**Q3.2.** The normalization plot (Step 1.3) shows four panels: the raw and scaled distributions for `age` and `sbp`. The raw `sbp` histogram spans from roughly 100 to 200 mmHg, while the scaled `sbp` histogram spans from about −1.5 to +2.5. Describe one visual difference between the raw and scaled histograms. Does the **shape** of the distribution change after scaling, or only the axis values?

**Q3.3.** The notebook note states: *"We fit the scaler **only on the training set** and then apply it to both train and test sets."* If instead we had fit the scaler on the full dataset (train + test) before splitting, what subtle problem would this introduce? This problem has a specific name — what is it?

**Q3.4.** The train/test split used `test_size=0.20` and `random_state=9`. How many samples ended up in the training set and test set respectively? Express both as absolute counts and percentages.

---

## Section 4 — Step 1.4: Train / Test Split

**Q4.1.** The output for Step 1.4 prints the class balance within each split. Fill in the values:

| Split | Class 0 (No HD) | Class 1 (HD) |
|-------|-----------------|--------------|
| Training (240) | 133 (55.4%) | 107 (44.6%) |
| Test (60) | | |

Does the class ratio in the test set closely reflect the overall dataset ratio (56.3% / 43.7%)? Why is it important for both splits to preserve the overall class distribution?

---

## Section 5 — Step 1.5: MLP Architecture and Training

**Q5.1.** The network summary printed in Step 1.5 reports the architecture as **5 → 100 → 50 → 1**. Identify what each number in this sequence represents. Then confirm from the printout how many total trainable parameters the network has. Show the breakdown layer by layer:
- Input → Hidden 1: \_\_\_ parameters
- Hidden 1 → Hidden 2: \_\_\_ parameters
- Hidden 2 → Output: \_\_\_ parameters
- **Total: \_\_\_ parameters**

**Q5.2.** The printout shows `Activation: relu` and `Solver: adam`. In one sentence each, explain what the ReLU activation function does and why the Adam optimizer is preferred over basic gradient descent for training neural networks.

**Q5.3.** The model ran for 500 iterations but the printout shows `Converged: False`. What does convergence mean in the context of neural network training? What would you change in the code to give the model a better chance of converging?

---

## Section 6 — Step 1.6: Confusion Matrix

**Q6.1.** The confusion matrix heatmap (Step 1.6) and the printed output report four values. Read them directly from your output and fill in the table:

|  | Predicted: No HD (0) | Predicted: HD (1) |
|--|---------------------|-----------------|
| **Actual: No HD (0)** | TN = \_\_ | FP = \_\_ |
| **Actual: HD (1)** | FN = \_\_ | TP = \_\_ |

**Q6.2.** The printed accuracy is 50.0%. Compare this to the "naive classifier" baseline you calculated in Q2.4 (always predicting the majority class). Is 50% better, equal to, or worse than the naive baseline? What does this tell you about the Task 1 model's performance?

**Q6.3.** The output states: *"14 at-risk patients missed (FN) — most dangerous: no intervention given."* In your own words, explain why False Negatives are considered the most dangerous clinical error in cardiac screening. How does this compare to the cost of a False Positive?

**Q6.4.** Using only the confusion matrix values (TN=20, FP=16, FN=14, TP=10), verify the accuracy formula manually:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Show your calculation and confirm it matches the printed value of 50.0%.

---

## Section 7 — Step 1.7: Classification Report

**Q7.1.** The classification report prints precision, recall, and F1-score for both classes. Complete the following table from your output:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| No Heart Disease (0) | 0.59 | 0.56 | 0.57 | 36 |
| Heart Disease (1) | | | | |

**Q7.2.** The manual verification section prints:
- `Precision = TP/(TP+FP) = 10/(10+16) = 0.3846`
- `Recall = TP/(TP+FN) = 10/(10+14) = 0.4167`
- `F1-score = 2*P*R/(P+R) = 0.4000`

In clinical terms, the model catches **41.7%** of true heart disease cases. Suppose you are a cardiologist reviewing this model for the MRHA CardioWatch program. Would you consider 41.7% recall acceptable for a cardiac screening tool? What is the clinical risk of deploying a model with recall this low?

**Q7.3.** The macro average F1-score is 0.49. The weighted average F1-score is 0.50. Explain in one sentence why these two averages differ for this dataset. Which one better reflects performance on the minority class (Heart Disease)?

---

## Section 8 — Step 1.8: Training Loss Curve

**Q8.1.** The loss curve plot (Step 1.8) shows the cross-entropy loss over 500 training epochs. Read the following values from the printed output and the chart:
- Starting loss (epoch 1): \_\_\_
- Final loss (epoch 500): \_\_\_
- Total loss reduction: \_\_\_

**Q8.2.** The curve has a characteristic steep drop in the early epochs followed by a gradual flattening. The annotation on the plot labels this early rapid descent as *"Rapid learning (early epochs)"*. Explain in 1–2 sentences why the loss drops so steeply at first and then slows down as training continues. What does this shape indicate about the optimizer's behavior?

**Q8.3.** The plot includes a **green shaded region** in the last 10% of epochs (approximately epochs 450–500) and a **red dashed horizontal line** at the final loss value of 0.1271. The printed output says "Status: DID NOT CONVERGE." Looking at the curve shape in this shaded region, does the loss appear to have actually plateaued? What would a fully converged curve look like compared to what you see?

**Q8.4.** The loss curve only shows the **training loss**. Why is this a limitation? What additional curve would you need to detect overfitting, and where in the notebook does Task 2 address this limitation?

---

## Section 9 — Step 2.1: Overfitting Demonstration

**Q9.1.** The grouped bar chart (Step 2.1) compares three architectures on train and test accuracy. Read the values from the chart and fill in the table:

| Architecture | Train Accuracy | Test Accuracy | Gap (pp) |
|--------------|---------------|--------------|---------|
| Underfitting (5,) | 70.0% | 63.3% | 6.7 |
| Good Fit (100,50) | | | |
| Overfitting (300,300,200) | | | |

**Q9.2.** The "Good Fit" architecture (100,50) achieves 99.6% training accuracy but only 51.7% test accuracy — a gap of 47.9 percentage points. This is a clear sign of overfitting even though this is called the "good fit" model. Explain why a model can memorize training data almost perfectly (99.6%) yet perform near-randomly on the test set (51.7%).

**Q9.3.** The Underfitting architecture (5,) achieves only 70.0% train accuracy and 63.3% test accuracy, with a small gap of 6.7 pp. Is a small train/test gap alone sufficient to call a model "good"? What is the problem with this underfitting model, and why is it insufficient for clinical deployment?

**Q9.4.** The Overfitting model (300,300,200) achieves **100.0%** training accuracy. What does it mean for a neural network to achieve perfect training accuracy? What is happening to the model's weights when this occurs, and why does it fail to generalize to the test set?

---

## Section 10 — Step 2.2: L2 Regularization

**Q10.1.** The three confusion matrix panels (Step 2.2) show the effect of increasing L2 regularization (alpha). Read the comparison table printed below the plot:

| Alpha | Accuracy | FN (missed) | FP (false alarm) |
|-------|----------|-------------|-----------------|
| 0.0001 (very weak) | 50.0% | 14 | 16 |
| 0.01 (moderate) | | | |
| 0.5 (strong) | | | |

**Q10.2.** As alpha increases from 0.0001 to 0.5, the accuracy improves from 50.0% to 58.3%, and the number of FN decreases from 14 to 13. However, the FP count also changes. Explain in 1–2 sentences the trade-off that L2 regularization makes: what does it sacrifice, and what does it gain in terms of model behavior?

**Q10.3.** The notebook explains that L2 regularization adds a penalty term α∑w² to the loss. In plain language, what effect does this penalty have on the model's weights during training? Why does pushing weights toward zero make the model **less likely to overfit**?

**Q10.4.** Looking at the confusion matrices for alpha=0.0001 and alpha=0.5, the strong regularization (alpha=0.5) reduces both FN (14→13) and FP (16→12) compared to the baseline. However, if alpha were increased too far (e.g., alpha=10.0), what would likely happen to the model's training accuracy and test accuracy? What is this failure mode called?

---

## Section 11 — Step 2.3: Cross-Validation with a Pipeline

**Q11.1.** The 5-fold cross-validation bar chart (Step 2.3) shows the accuracy for each fold and a dashed red line at the mean. Read the five fold scores and compute the spread:

| Fold | Accuracy |
|------|---------|
| 1 | 53.33% |
| 2 | 55.00% |
| 3 | 60.00% |
| 4 | 58.33% |
| 5 | 58.33% |

What are the **mean accuracy** and **standard deviation** printed in the output? What is the 95% confidence interval? Based on this interval, what range of accuracies might we expect if we deployed this model on a new patient group?

**Q11.2.** The cross-validation mean accuracy is 57.00%, which is higher than the single train/test split accuracy of 50.0% (Step 1.6). Why can a single train/test split give a misleading estimate of performance? What advantage does K-fold cross-validation provide over a single split?

**Q11.3.** The notebook uses a `Pipeline([('scaler', StandardScaler()), ('mlp', MLPClassifier(...))])` instead of applying the scaler and model separately. The printed explanation states: *"In each of the 5 folds, StandardScaler is fit ONLY on the 4 training folds. The validation fold is scaled with those parameters but never influences them."* Why would it be incorrect (data leakage) to fit the scaler on the full dataset before running cross-validation? Describe in 1–2 sentences what information would "leak" into the training process.

---

## Section 12 — Step 2.4: ROC Curve and AUC

**Q12.1.** The ROC curve plot (Step 2.4) shows the MLP classifier curve against the random classifier diagonal. Read the following values from the plot title and legend:
- **AUC** of the MLP classifier: \_\_\_
- At the default threshold (0.5), the **True Positive Rate (TPR)**: \_\_\_
- At the default threshold (0.5), the **False Positive Rate (FPR)**: \_\_\_

**Q12.2.** The printed output states: *"AUC = 0.550 is poor for a screening tool."* The AUC scale goes from 0.5 (random) to 1.0 (perfect). The red dot on the curve marks the default operating point (threshold = 0.5). At this operating point, the model flags 44.4% of healthy patients as at-risk (FPR = 0.444). Would you prefer to accept a higher or lower FPR if you moved the threshold to increase sensitivity for mass screening? What is the clinical cost of the change?

**Q12.3.** A perfect classifier would have an AUC of 1.0 and its ROC curve would pass through the top-left corner of the plot (FPR=0, TPR=1). The MLP's curve of AUC=0.550 barely rises above the random classifier diagonal. What does this tell you about this model's ability to distinguish between heart disease and non-heart disease patients? Based on the AUC alone, is this model ready for clinical deployment?

**Q12.4.** The ROC curve is described as "threshold-independent." Explain in one sentence what this means: how does the ROC curve show information that a single confusion matrix (at threshold = 0.5) does not?

---

## Section 13 — Step 2.5: Clinical Predictions for New MRHA Patients

**Q13.1.** Five new patients were assessed by the model. Read the predictions from the printed output and complete the table:

| Patient | Age | BMI | SBP | Chol | HR | P(HD) | Prediction | Clinical Flag |
|---------|-----|-----|-----|------|----|-------|-----------|--------------|
| A | 45 | 22.1 | 118 | 185 | 68 | | | |
| B | 62 | 30.5 | 155 | 260 | 88 | | | |
| C | 55 | 27.0 | 135 | 215 | 74 | | | |
| D | 38 | 19.2 | 108 | 160 | 62 | | | |
| E | 70 | 35.8 | 175 | 300 | 98 | | | |

**Q13.2.** Patient E (age 70, BMI 35.8, SBP 175, Chol 300, HR 98) received a predicted probability of **100.0%** for heart disease. Looking at their clinical profile, identify at least three risk factors that are elevated beyond the healthy reference ranges provided in the dataset documentation. Does the model's extreme confidence match what a clinician would expect for this patient?

**Q13.3.** Patient A (age 45, BMI 22.1, SBP 118, Chol 185, HR 68) received a probability of only **2.6%**. Compare their biomarkers to the healthy reference ranges. Do their values justify a low-risk prediction? What does this tell you about the model's ability to capture the joint effect of multiple risk factors being simultaneously healthy?

**Q13.4.** The probability bar chart (Step 2.5) shows a dashed line at 50% with a blue "Low risk zone" below and a red "High risk zone" above. Patients B, C, and E are all flagged as HIGH RISK, but their probabilities differ: 95.9%, 59.0%, and 100.0% respectively. Why is the **probability score** more clinically useful than the hard binary prediction alone? How might a physician treat a patient with P(HD)=59% differently from one with P(HD)=100%?

**Q13.5.** The notebook warns: *"In a real deployment, we would use the full Pipeline (scaler + model) trained on all available data, not just the 80% training split."* Why would training on all 300 patients (instead of only 240) likely produce better predictions for new patients like those in Step 2.5?

---

## Section 14 — Cross-Task Synthesis

**Q14.1.** Task 1 achieved 50.0% test accuracy on the single train/test split. Task 2's cross-validation reported a mean accuracy of 57.00%. These two numbers describe the same base architecture (100,50). Why do they differ? Which estimate is more reliable for reporting model performance, and why?

**Q14.2.** Compare the **confusion matrices** from Step 1.6 (baseline, alpha=0.0001) and Step 2.2 (alpha=0.5). The stronger regularization improves accuracy from 50.0% to 58.3%. However, the FN count only decreases by 1 (from 14 to 13). From a clinical standpoint, is a 1-patient improvement in missed cases meaningful for a program monitoring hundreds of patients per year? What additional techniques (beyond regularization) could further reduce FN?

**Q14.3.** The training loss curve (Step 1.8) shows the loss starting at **0.712** and ending at **0.127** — a reduction of 0.585. Yet the model achieves only 50% test accuracy. Explain the disconnect: why can a low training loss coexist with poor generalization performance? What concept from Session 28 describes this situation?

**Q14.4.** Throughout the notebook, the importance of **feature normalization** is emphasized. In Step 1.3, the raw `sbp` range is [100–200] while `bmi` is [18.5–37.9] — a scale difference of roughly 5×. Explain in 1–2 sentences why this scale difference would cause problems for the gradient descent optimizer if normalization were skipped.

**Q14.5.** The MRHA CardioWatch program (introduced in Activity 7) originally used **linear regression** to predict systolic blood pressure. Activity 9 now uses a **neural network** to predict whether a patient will develop heart disease. List one advantage of the neural network approach over logistic regression for this classification problem, and one situation where a simpler, interpretable model might still be preferred in a clinical setting.

---

*MRHA CardioWatch Program — Neural Network Clinical Risk Assessment*
*Activity 9 | Introduction to Artificial Intelligence*
