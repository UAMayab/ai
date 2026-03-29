# Activity 7 — Plot & Output Analysis: Understanding the Story in the Data

**Course:** Introduction to Artificial Intelligence
**Assignment:** A7 — Linear Regression: Predicting Systolic Blood Pressure

> **Instructions:** Answer every question directly from the plots and numerical outputs produced when you run the notebook. Every question refers to a specific figure or printed result. Your answers should be concrete — cite values, describe visual patterns, and explain what those patterns mean in the context of blood pressure prediction.

---

## Section 0 — Dataset Overview

**Refer to:** Summary statistics table (`df.describe()` output)

**Q0.1** — The mean SBP across all 200 patients is **162.55 mmHg**. Using the clinical reference table from the notebook introduction, which hypertension category does the average patient in this dataset fall into? What does this tell you about the population being monitored by the MRHA CardioWatch program?

**Q0.2** — The minimum SBP in the dataset is **133.1 mmHg** and the maximum is **185.0 mmHg**. No patient has a "Normal" SBP (below 120 mmHg). Is this surprising given the program's purpose? Explain why the dataset was designed this way.

**Q0.3** — The standard deviation of SBP is **11.29 mmHg**. In your own words, what does this tell you about the spread of blood pressure values among the patients? Does a standard deviation of ~11 mmHg feel clinically significant to you?

---

## Section 1 — Task 1: Exploratory Data Analysis

**Refer to:** Plot titled *"Task 1 — Exploratory Data Analysis"* (two side-by-side charts)

### Left chart: Distribution of Patient Age

**Q1.1** — Describe the shape of the age distribution histogram. Is it skewed to the left, skewed to the right, or approximately uniform? What does a uniform distribution of ages mean for the quality of our dataset?

**Q1.2** — The mean age is marked at **49.5 years** with a red dashed line. Looking at the histogram bars, does the mean appear to split the distribution roughly in half? Would the median be significantly different from the mean in this case? Explain your reasoning.

### Right chart: Age vs. Systolic Blood Pressure (Scatter Plot)

**Q1.3** — Three horizontal dashed lines are drawn at 120 mmHg (gold), 130 mmHg (orange), and 140 mmHg (red). Looking at the scatter plot, approximately what fraction of the patients appear to fall **above** the Stage 2 threshold (140 mmHg)? Does this match your expectation for a hypertension-monitoring program?

**Q1.4** — The scatter plot shows a general upward trend from left to right. Describe this trend in plain language: what happens to SBP as patients get older? Are all older patients guaranteed to have high SBP? What does the scatter around the trend tell us?

**Q1.5** — The Pearson correlation computed is **r = 0.676**. The notebook classifies this as a "moderate positive linear relationship."
- What would the scatter plot look like if r were close to **1.0**?
- What would it look like if r were close to **0.0**?
- Based on the actual scatter plot, does r = 0.676 seem like an accurate description of the relationship you see?

---

## Section 2 — Task 1: Model Training & Coefficients

**Refer to:** Printed output from Step 1.3

```
Intercept  b0 : 137.2003 mmHg
Slope      b1 : 0.5114 mmHg per year
Equation: SBP = 137.20 + 0.51 x Age
```

**Q2.1** — The slope β₁ = **0.51 mmHg per year**. Translate this number into a clinical statement that a physician could put in a patient report. Avoid all mathematical notation — write it as a plain sentence.

**Q2.2** — The intercept β₀ = **137.20 mmHg**. Mathematically, this is the predicted SBP when Age = 0.
- Is this a clinically meaningful prediction?
- What is the real purpose of the intercept in a linear regression model?

**Q2.3** — Using the equation `SBP = 137.20 + 0.51 × Age`, manually calculate the predicted SBP for a **45-year-old** patient and a **70-year-old** patient. Show your arithmetic. What clinical category would each patient fall into?

---

## Section 3 — Task 1: Model Evaluation

**Refer to:** Printed output from Step 1.4

```
Mean Squared Error  (MSE)  : 65.943 mmHg²
Root MSE            (RMSE) : 8.121 mmHg
R-squared           (R²)   : 0.515
The model explains 51.5% of the variance in SBP.
On average, predictions are off by about 8.1 mmHg.
```

**Q3.1** — The RMSE is **8.121 mmHg**. In practical terms, if the model predicts a patient's SBP as 155 mmHg, what is a reasonable range for the true SBP? Is this level of error acceptable for making clinical decisions? Why or why not?

**Q3.2** — The R² is **0.515**. This means the model explains **51.5%** of the variability in SBP. What does the remaining **48.5%** represent? Give at least two specific examples of factors that might account for unexplained variability in blood pressure.

**Q3.3** — MSE is reported in **mmHg²** while RMSE is in **mmHg**. Why do we often prefer RMSE over MSE when interpreting model performance? Which one is easier to communicate to a physician, and why?

---

## Section 4 — Task 1: Regression Line Plot

**Refer to:** Plot titled *"Task 1 — Simple Linear Regression: SBP vs. Age"*

**Q4.1** — The plot shows **gray dots** (training patients) and **blue dots** (test patients), with a **red regression line**. Why are the training patients shown in a lighter color? Why is it important to visually distinguish training from test data in this plot?

**Q4.2** — Look at the regression line carefully. At approximately what age does the predicted SBP cross the **Stage 2 threshold** (140 mmHg dashed red line)? Show how you would estimate this from the equation `SBP = 137.20 + 0.51 × Age`.

**Q4.3** — Some blue dots (test patients) are **far above** the regression line (up to ~15 mmHg above), while others are **far below** it. What do these distant points represent mathematically? What might explain clinically why some patients have much higher or lower SBP than the model predicts for their age?

**Q4.4** — The regression line spans the full age range from ~25 to ~75 years. Would you trust this model to predict SBP for a **20-year-old** or an **85-year-old**? What is the statistical term for using a model beyond its training range, and why is it risky?

---

## Section 5 — Task 1: Residual Analysis

**Refer to:** Plot titled *"Task 1 — Residual Analysis"* and the printed residual summary

```
Residual summary:
  Mean   : 0.2590  (should be close to 0)
  Std    : 8.1164 mmHg
  Min    : -14.11 mmHg
  Max    : 15.83 mmHg
```

### Left chart: Residuals vs. Fitted Values

**Q5.1** — The residuals are scattered around the **red dashed zero line** with no obvious curve or funnel shape. Which two assumptions of linear regression does this random scatter support — **linearity** or **homoscedasticity**? Explain what each assumption means and how the plot confirms it.

**Q5.2** — If the residuals vs. fitted plot showed a **U-shaped curve** (residuals negative in the middle, positive at the extremes), what would that tell you about the model? What corrective action could you take?

**Q5.3** — The residuals range from **-14.11 to +15.83 mmHg**. The largest positive residual (+15.83) means the model predicted a patient's SBP was 15.83 mmHg **lower** than it actually was. In clinical terms, what is the consequence of systematically underestimating a patient's blood pressure?

### Right chart: Distribution of Residuals (RMSE = 8.12 mmHg)

**Q5.4** — The residual histogram shows a roughly **bell-shaped distribution** centered near zero (mean residual = 0.26). Which assumption of linear regression does this support? What would a severely skewed residual histogram suggest about the model?

**Q5.5** — The mean residual is **0.2590**, which the notebook says "should be close to 0." Why must the mean residual be approximately zero in a correctly fitted OLS model? What mathematical property guarantees this?

---

## Section 6 — Task 2: Exploratory Data Analysis

**Refer to:** Plot titled *"Task 2 — Exploratory Data Analysis"* (2×2 grid of charts)

### Top-left: Distribution of BMI

**Q6.1** — The BMI distribution shows vertical dotted lines at **25 kg/m²** (Overweight) and **30 kg/m²** (Obese). The mean BMI is **28.4 kg/m²**, which falls in the Overweight category. Looking at the histogram, roughly what fraction of the 200 patients have a BMI ≥ 30 (Obese)? Is this a concern for this hypertension-monitoring population?

### Top-right: BMI vs. Systolic Blood Pressure

**Q6.2** — Compare this scatter plot (BMI vs. SBP) to the one in Task 1 (Age vs. SBP). In which plot do the points form a tighter, more linear pattern? The Pearson correlations are **r = 0.676** (Age vs. SBP) and **r = 0.514** (BMI vs. SBP). Is this ranking consistent with what you see visually in the two scatter plots?

**Q6.3** — Despite the weaker correlation, adding BMI to the model improved R² from 0.515 to 0.763. How is it possible for a predictor with a relatively weak individual correlation (r = 0.514) to cause such a large improvement in the combined model?

### Bottom-left: Age vs. BMI (Multicollinearity Check)

**Q6.4** — The Age vs. BMI scatter plot shows **r = -0.009**, essentially zero. The points form a completely random cloud with no pattern. Why did the notebook include this specific plot? What problem would arise if Age and BMI had a correlation of r = 0.95 instead of -0.009?

### Bottom-right: Correlation Matrix

**Q6.5** — The correlation matrix shows three cells: age/sbp = **0.68**, bmi/sbp = **0.51**, and age/bmi = **-0.01**. The color scale runs from red (−1) to green (+1).
- Why are all diagonal cells equal to **1.00**?
- Why is the matrix **symmetric** (the cell at row=age, col=bmi equals the cell at row=bmi, col=age)?
- Based on the colors alone, which predictor has the strongest relationship with SBP?

---

## Section 7 — Task 2: Multiple Regression Coefficients

**Refer to:** Printed output from Step 2.3

```
Intercept  b0 : 107.0487 mmHg
Age coef.  b1 : 0.5392 mmHg per year
BMI coef.  b2 : 1.0241 mmHg per kg/m²
Equation: SBP = 107.05 + 0.54*Age + 1.02*BMI
```

**Q7.1** — In Task 1, the age coefficient was **β₁ = 0.5114**. In Task 2, it is **β₁ = 0.5392**. The value changed when BMI was added. Explain why adding a second predictor changes the coefficient of the first predictor. (Hint: think about what "holding BMI constant" means.)

**Q7.2** — The BMI coefficient is **β₂ = 1.02 mmHg per kg/m²**. Write a plain-language sentence for a clinical report explaining what this coefficient means for a patient who gains 5 kg/m² of BMI while staying the same age.

**Q7.3** — Using the equation `SBP = 107.05 + 0.54 × Age + 1.02 × BMI`, manually verify the prediction for **Patient A** (age=35, bmi=22.4). Show your full arithmetic. Does your result match the notebook output of **148.90 mmHg**?

---

## Section 8 — Task 2: Model Comparison

**Refer to:** Comparison table from Step 2.4

```
Metric          Simple LR    Multiple LR
Predictors      Age only     Age + BMI
MSE (mmHg²)     65.943       32.191
RMSE (mmHg)      8.121        5.674
R-squared        0.515        0.763

R² improvement from adding BMI: +0.248 (24.8 percentage points)
MSE reduction from adding BMI : -33.752 mmHg²
```

**Q8.1** — The RMSE dropped from **8.121 mmHg** (Simple LR) to **5.674 mmHg** (Multiple LR). In practical terms: if you were a physician using these two models to screen patients, how much more accurate are your predictions with the multiple regression model? Express this as an absolute improvement in mmHg and explain whether this difference matters clinically.

**Q8.2** — R² jumped from **0.515 to 0.763** — an increase of **24.8 percentage points**. Yet BMI's individual correlation with SBP is only r = 0.514. Why does BMI add so much explanatory power to the model even though it has only a moderate individual correlation with SBP?

**Q8.3** — The MSE dropped by **33.752 mmHg²** when BMI was added. MSE penalizes large errors more than small ones (because errors are squared). What does a large MSE reduction tell you specifically — is it the small errors that got better, or the large errors?

---

## Section 9 — Task 2: Actual vs. Predicted Plot

**Refer to:** Plot titled *"Task 2 — Actual vs. Predicted Systolic Blood Pressure"* (two side-by-side charts)

**Q9.1** — Both plots have an identical **red dashed diagonal line**. What does a point that falls exactly on this diagonal represent? What does a point that falls **far above** the diagonal represent? What about a point that falls **far below** it?

**Q9.2** — Compare the spread of dots around the diagonal in the **left plot** (Simple LR, blue) vs. the **right plot** (Multiple LR, orange). Describe the visual difference between the two. Which model would you choose based on this plot alone, and why?

**Q9.3** — In the **Simple LR plot** (left), several blue dots appear in the lower-left area with actual SBP around 140–150 mmHg but predicted SBP around 150–155 mmHg. The model is **overestimating** these patients' blood pressure. What is the clinical consequence of overestimating a patient's SBP — could it lead to unnecessary treatment?

**Q9.4** — Both plots use the **same axis limits** (set using `lo` and `hi` from the combined data). Why is it important that both subplots share identical axis scales when comparing two models side by side?

---

## Section 10 — Task 2: Residual Analysis (Multiple Regression)

**Refer to:** Plot titled *"Task 2 — Residual Analysis (Multiple Regression)"* and printed summary

```
Residual summary (Multiple LR):
  Mean   : -1.3174  (should be close to 0)
  Std    : 5.5186 mmHg
  Min    : -15.82 mmHg
  Max    :   7.24 mmHg
```

### Left chart: Residuals vs. Fitted

**Q10.1** — The residuals in the Multiple LR model are more tightly packed around zero compared to Task 1 (Std dropped from 8.12 to 5.52 mmHg). This is visible in the narrower vertical spread in this plot. What does a smaller residual standard deviation mean for the usefulness of the model?

### Middle chart: Residuals vs. Age

**Q10.2** — This plot shows residuals on the y-axis and **Age** on the x-axis. The points appear randomly scattered with no trend — no curve, no fan shape. What specific assumption does this confirm? If instead you saw a clear downward slope in this plot (residuals decreasing as age increases), what would that mean?

### Right chart: Residual Distribution (RMSE = 5.67)

**Q10.3** — The residual histogram for the Multiple LR model shows a mean of **-1.3174**, which is slightly off zero (compared to 0.26 in Task 1). The histogram also appears left-skewed, with a longer tail toward negative residuals (the minimum is -15.82 while the maximum is only 7.24). What does this asymmetry suggest? Does it seriously threaten the validity of the model?

**Q10.4** — Compare the two RMSE values: **8.12 mmHg** (Task 1) vs. **5.67 mmHg** (Task 2). Express the improvement as a percentage reduction. Then express it clinically: if you are predicting a patient is at Stage 1 hypertension (130–139 mmHg), how much does the reduced RMSE improve your confidence in that classification?

---

## Section 11 — Task 2: Clinical Predictions

**Refer to:** Patient risk screening output from Step 2.7

```
Patient    age   bmi   Predicted SBP   Classification
Patient A   35  22.40         148.90   High Stage 2
Patient B   58  30.10         169.10   High Stage 2
Patient C   67  27.80         171.60   High Stage 2
```

**Q11.1** — All three patients are classified as **High Stage 2** (SBP ≥ 140 mmHg). Patient A is only 35 years old with a normal-weight BMI (22.4). Why does the model predict such a high SBP of 148.90 mmHg for a relatively young patient with a healthy BMI? Is this prediction plausible, or does it reveal a potential issue with the dataset?

**Q11.2** — Patient B (age=58, bmi=30.1) is predicted at **169.10 mmHg** and Patient C (age=67, bmi=27.8) is predicted at **171.60 mmHg**. Patient C is older but has a lower BMI. Yet their predicted SBP is only slightly higher (+2.5 mmHg). Walk through the arithmetic using the equation `SBP = 107.05 + 0.54*Age + 1.02*BMI` to explain why the predictions are so close.

**Q11.3** — The model predicts SBP but does not measure it directly. Given the RMSE of 5.67 mmHg, what is a reasonable confidence interval around Patient A's predicted SBP of 148.90 mmHg? Does the lower bound of that interval change the clinical classification?

**Q11.4 — Ethics & Critical Thinking:** The MRHA wants to use these predictions to automatically schedule patients for mandatory medication without a physician review. Based on the model's RMSE and residual range (min = -15.82, max = +7.24 mmHg), identify at least **two concrete risks** of automating this decision. What safeguards should be in place?

---

## Section 12 — Cross-Task Synthesis

These questions require you to think across both tasks and the full notebook.

**Q12.1** — The notebook uses a fixed **random seed of 7** for data generation and train/test splits. What would happen to the model's MSE and R² values if you changed the seed? Would the equation (coefficients) change? Would the conclusions about which model is better change? Explain.

**Q12.2** — The interactive widget lets you change the **noise level (σ)** from 2 to 25 mmHg. Predict (without running the widget) what R² and the regression line would look like at σ = 2 vs. σ = 25. Explain your prediction using the definition of R².

**Q12.3** — Looking at both the **regression line plot** (Task 1) and the **actual vs. predicted plot** (Task 2), which visualization do you find more informative for evaluating model quality? Justify your choice — what information does one provide that the other does not?

**Q12.4** — The true data-generating formula used in the notebook is:
```
SBP = 105 + 0.55 × Age + 1.10 × BMI + noise (σ=6)
```
The multiple regression model recovered:
```
SBP = 107.05 + 0.54 × Age + 1.02 × BMI
```
The recovered coefficients (0.54 vs 0.55; 1.02 vs 1.10) are close but not identical to the true values. Why doesn't the model recover the exact coefficients? What two sources of imprecision prevent a perfect recovery?

**Q12.5 — Big Picture:** A colleague suggests replacing both linear regression models with a single rule: *"Classify every patient as Stage 2 hypertension, since the dataset mean is 162.55 mmHg."*
- What would be the MSE and R² of this "always predict the mean" rule?
- How much better is the Simple LR model (R²=0.515) compared to this baseline?
- How much better is the Multiple LR model (R²=0.763)?
- What is the formal name for this baseline in statistics?

---

*MRHA CardioWatch Program — Plot & Output Analysis Evaluation*
*Activity 7 | Introduction to Artificial Intelligence*
