# A11 — Plot and Output Analysis Questions
## Natural Language Processing: Sentiment Analysis

**Instructions:**
- Answer every question **after** running `A11_NLP_SentimentAnalysis.ipynb` and confirming all cells show output.
- Every question refers to a specific plot or printed value from the notebook. Keep the notebook open alongside this document.
- Label each answer clearly with its question number (e.g., **Q3.2**).
- Cite exact values from your output wherever a question asks for numbers.
- Submit your answers as a separate document (PDF or Word) — **do not modify the notebook**.

---

## Section 0 — Dataset Overview

**Q0.1.** Step 1.1 prints the class distribution and review length statistics for the 400-review sample. Record the values from your output:

| Metric | Value |
|--------|-------|
| Total reviews sampled | 400 |
| Positive (label = 1) | 203 (50.7%) |
| Negative (label = 0) | |
| Mean review length (words) | |
| Median review length (words) | |
| Longest review (words) | |

**Q0.2.** The sample is drawn from the **test split** of the IMDB dataset using `random_state=11`. Looking at the class distribution (50.7% Positive / 49.2% Negative), is this dataset balanced or imbalanced? If a naive model always predicted "Positive," what accuracy would it achieve? Why is this important context for evaluating VADER and DistilBERT's scores?

**Q0.3.** Three sample reviews are printed at the end of Step 1.1 — one Negative, one Positive, and one Negative. Without looking at the labels, read the first sample review (*"I ran across this movie on a local TV channel last night..."*). Does the opening sentence give an obvious positive or negative signal? What does this tell you about the difficulty of sentiment classification based on the first sentence alone?

---

## Section 1 — Step 1.1: Dataset Exploration

**Q1.1.** The printed output states that the longest review in the sample is **1009 words**. After BERT tokenization, this becomes **512 tokens** (truncated). What information is lost when a review is truncated? Does truncation affect the beginning or the end of the review? In a real product review pipeline, what strategy could you use to reduce the impact of truncation on very long reviews?

**Q1.2.** The token length histogram (Step 1.2) shows the distribution of token counts for 50 sampled reviews. The red dashed line marks the maximum length of **512 tokens**. The printed output states that truncation affects **~70 of the 400** sampled reviews.

- What percentage of the 400 reviews does this represent?
- The token mean is **295** and median is **210**, but the max is **1247**. What does the large gap between the median and max tell you about the shape of this distribution? Is it symmetric or skewed?
- Looking at the histogram, where does the bulk of reviews fall on the x-axis — mostly below or above 512 tokens?

---

## Section 2 — Step 1.2: Tokenization

**Q2.1.** The tokenizer output for *"This product is absolutely brilliant — I could not be happier!"* shows **12 WordPiece tokens**. List the tokens as printed in your output, and then identify the two **special tokens** that are added when the full encoded sequence is shown. What role does each special token play in the DistilBERT model?

**Q2.2.** The WordPiece subword splitting example shows how unusual words are broken into subword units. Complete the table from your output:

| Word | WordPiece tokens |
|------|-----------------|
| unimaginably | ['un', '##ima', '##gina', '##bly'] |
| electroencephalography | |
| disappointing | |
| NLP | |

Why does "disappointing" stay as a single token while "electroencephalography" is split into five pieces? What does the `##` prefix on a token mean?

**Q2.3.** The tokenizer has a vocabulary of **30,522 tokens**. A word that is not in this vocabulary (e.g., a product model name like "RX7500XT") would be split into subword units rather than mapped to a single token. Explain why WordPiece tokenization handles unknown words more gracefully than a simple word-level vocabulary that maps unknown words to a single `[UNK]` token.

**Q2.4.** The notebook states: *"DistilBERT is uncased."* The printed output shows the original sentence and its lowercased version side by side. What does "uncased" mean, and why might this be a limitation for sentiment analysis in a context where capitalization carries meaning (e.g., "AMAZING product" vs. "amazing product")?

---

## Section 3 — Step 1.3: VADER Rule-Based Baseline

**Q3.1.** VADER was run on the first **50 reviews**. Record the accuracy and failure count from your output:
- VADER Accuracy: \_\_\_ % (majority baseline: 50.0%)
- Number of failures: \_\_\_ / 50

**Q3.2.** The printed sample predictions table (first 8 reviews) shows the review text, true label, VADER prediction, and compound score. Look at the first row: *"I ran across this movie on a local TV channel last night..."* with True=NEG, VADER=NEG, Compound=−0.907. The compound score is close to −1.0, indicating strong negative signal. Identify **one specific word or phrase** in that review excerpt that you think VADER's lexicon would assign a strong negative polarity score to.

**Q3.3.** The Top 3 VADER failures (sorted by |compound| — most confident wrong) are printed. Record them:

| # | True label | VADER predicted | Compound score |
|---|-----------|-----------------|----------------|
| 1 | Negative | Positive | 0.998 |
| 2 | | | |
| 3 | | | |

In failure #1, the review begins: *"The Movie Machine starts in New York during 1899 where Professor Alexander Hartdegen proposes to his beloved girlfriend Emma (Sienna Guillory) who accepts, unfortunatel..."* Despite clearly being a negative review, VADER gave it a compound score of **0.998** — nearly perfectly positive. What type of language in this review excerpt might have caused VADER to misclassify it? (Hint: think about what kinds of words appear in a plot summary.)

**Q3.4.** In failure #2, the review has compound = −0.994 (strongly negative), but the true label is **Positive**. This is a case where irony or mixed tone is present. Explain in one sentence why a lexicon-based model like VADER cannot reliably detect cases where a text uses negative-sounding words to ultimately convey a positive opinion (e.g., a review that says "this film is a beautiful disaster").

---

## Section 4 — Step 1.4: DistilBERT Pipeline

**Q4.1.** The DistilBERT pipeline is loaded with `device=-1` (CPU). The printed output shows inference on 50 reviews takes approximately 30 seconds on CPU. Record the final accuracy:
- DistilBERT Accuracy: \_\_\_ % (VADER: 72.0%)
- Accuracy improvement over VADER: \_\_\_ percentage points

**Q4.2.** The sample predictions table (first 8 reviews) shows that most DistilBERT confidence scores are extremely high — 99%+ even for reviews that are correctly classified. The first review (*"I ran across this movie..."*) is correctly classified as NEG with **100.0%** confidence. What does a confidence score of 100.0% actually mean in the softmax output? Can a model be genuinely 100% certain, or is this a numerical artifact?

**Q4.3.** Hugging Face's `pipeline()` abstraction wraps four steps: tokenization, forward pass, softmax, and label mapping. In plain language, describe what each step does and what information flows between them. Why is it useful to have these four steps abstracted into a single function call for a classroom assignment?

---

## Section 5 — Step 1.5: VADER vs. DistilBERT Comparison

**Q5.1.** The accuracy bar chart (Step 1.5) shows both models against the 50% majority baseline. Fill in the table from your output:

| Model | Accuracy | Improvement over 50% baseline |
|-------|----------|-------------------------------|
| VADER (Rule-Based) | 72.0% | +22.0 pp |
| DistilBERT (Transformer) | | |

**Q5.2.** The agreement breakdown bar chart shows four categories. Record all four values:

| Category | Count | Percentage |
|----------|-------|-----------|
| Both correct | 35 | 70.0% |
| Both wrong | | |
| Only VADER correct | | |
| Only DistilBERT correct | | |

The "Only VADER correct" count is just **1** out of 50. What does this tell you about the cases where VADER succeeds but DistilBERT fails? Is this a meaningful advantage for VADER in practice?

**Q5.3.** The three printed disagreement examples all follow the same pattern: True=Negative, VADER=Positive, DistilBERT=Negative. The first example begins: *"This is another of Hollywood's anti-communist polemics of the golden 1950s. Stalwart American Gene Barry, lovely Englishwoman Valerie French, and three others a..."* Why would VADER assign a **positive** compound score to this text? Which specific words in the excerpt likely contributed most to VADER's false positive prediction?

**Q5.4.** The accuracy gap between DistilBERT (88.0%) and VADER (72.0%) is **16 percentage points**. In a real deployment processing 10,000 TechNest reviews per day, how many additional reviews would DistilBERT tag correctly compared to VADER? If each misclassified review costs the support team 5 minutes to manually correct, how many hours per day could the better model save?

---

## Section 6 — Step 1.6: Confidence Score Distribution

**Q6.1.** The confidence histogram (Step 1.6) separates correct and incorrect predictions by confidence score. Record the statistics from your output:

| | Count | Mean Confidence |
|-|-------|----------------|
| Correct predictions | 44 | |
| Incorrect predictions | 6 | |

**Q6.2.** An unexpected result appears in the printed statistics: the mean confidence of **incorrect** predictions (0.991) is actually *higher* than the mean confidence of **correct** predictions (0.981). What does this tell you about DistilBERT's calibration on this dataset — is it overconfident, underconfident, or well-calibrated? What practical problem does this create when trying to use confidence scores to decide which predictions to trust?

**Q6.3.** The pie chart (Step 1.6) shows the breakdown of 50 reviews by confidence bucket. The **High (0.90–1.00)** bucket contains **96%** of all predictions. The Low and Medium buckets each contain roughly **2%**. What does this extreme concentration in the high-confidence bucket tell you about DistilBERT's behavior on IMDB reviews? Would you expect the same pattern on a harder dataset (e.g., product reviews with mixed sentiment or sarcasm)?

**Q6.4.** The printed output states: **Reviews with conf > 0.90: 48/50** and **Reviews with conf > 0.95: 47/50**. If you set a confidence threshold of 0.90 for auto-tagging on these 50 Task 1 reviews, how many would be auto-tagged? Of the 6 incorrect predictions, how many likely fall above the 0.90 threshold? Use the histogram to support your answer.

---

## Section 7 — Step 1.7: Interactive Sentiment Analyzer

**Q7.1.** Using the interactive widget (Step 1.7), test the four suggested challenging cases. For each one, record the VADER compound score and DistilBERT label + confidence:

| Text | VADER compound | DistilBERT label | DistilBERT confidence |
|------|---------------|------------------|-----------------------|
| Sarcasm: *"Oh great, another product that breaks in a week. Just what I needed."* | | | |
| Mixed: *"The camera is phenomenal but the battery life is a disaster."* | | | |
| Negation: *"This is not bad at all — I was pleasantly surprised."* | | | |
| Formal praise: *"The engineering is impeccably refined..."* | | | |

**Q7.2.** For the **sarcasm** example, which model gives the correct sentiment prediction? Explain in 1–2 sentences *why* the incorrect model fails on this specific sentence. Reference the specific mechanism (lexicon lookup vs. contextual representation) that causes the failure.

**Q7.3.** For the **mixed sentiment** example (*"The camera is phenomenal but the battery life is a disaster"*), there are strong positive words ("phenomenal") and strong negative words ("disaster"). What does DistilBERT predict for this sentence? What does VADER predict? Which do you think better reflects a typical customer's overall feeling after reading this review? In a real product feedback system, how might you handle reviews with genuinely mixed sentiment that a binary classifier cannot capture?

---

## Section 8 — Step 2.1: Full Evaluation Dataset

**Q8.1.** The Task 2 evaluation set uses reviews 200–399 — a fresh set not touched in Task 1. Record the distribution:

| | Count | Percentage |
|-|-------|-----------|
| Positive reviews | 108 | 54.0% |
| Negative reviews | | |
| **Total** | 200 | 100% |

**Q8.2.** The printed output shows:
- DistilBERT Accuracy: **88.5%**
- Majority Baseline: **54.0%**
- Improvement over baseline: **+34.5 pp**

The Task 1 accuracy (50 reviews) was 88.0% and Task 2 accuracy (200 reviews) is 88.5%. These two estimates are very close. What does the consistency between these two sample sizes tell you about the stability of DistilBERT's performance on this type of data? Why is it generally better to evaluate on 200 examples than on 50?

---

## Section 9 — Step 2.2: Confusion Matrix and Classification Report

**Q9.1.** The confusion matrix (Step 2.2) reports four values. Read them from your output:

|  | Predicted: Negative | Predicted: Positive |
|--|--------------------|--------------------|
| **Actual: Negative** | TN = 85 | FP = 7 |
| **Actual: Positive** | FN = | TP = |

**Q9.2.** Using only the confusion matrix values (TN=85, FP=7, FN=16, TP=92), verify the accuracy formula manually:
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
Show your calculation and confirm it matches the printed value of **88.5%** (rounded to 89% in the report).

**Q9.3.** The classification report shows that precision and recall are **not equal** for either class. Fill in the table from your output:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Negative | 0.84 | 0.92 | 0.88 | 92 |
| Positive | | | | |

The model has **higher precision for Positive** (0.93) but **lower recall for Positive** (0.85). In plain language: when the model predicts "Positive," it is right 93% of the time, but it misses 15% of truly Positive reviews. In TechNest's use case (flagging positive reviews for marketing testimonials), which error — low precision or low recall — is more damaging? Explain your reasoning.

**Q9.4.** The model produces **16 False Negatives** (actual Positive reviews predicted as Negative) but only **7 False Positives** (actual Negative reviews predicted as Positive). What asymmetry in the dataset or the model's decision boundary might explain why FN > FP? Consider the class distribution (108 Positive vs. 92 Negative) in your answer.

---

## Section 10 — Step 2.3: Error Analysis

**Q10.1.** The error analysis output reports:
- Total errors: **23 / 200 (11.5%)**
- False Positives (predicted POS, actually NEG): **7**
- False Negatives (predicted NEG, actually POS): **16**

The printed bar chart shows the four prediction categories. Compute the following from the confusion matrix values:
- What percentage of the 200 reviews were correctly classified as Negative (TN rate)?
- What percentage were correctly classified as Positive (TP rate)?

**Q10.2.** The top 5 most confident wrong predictions are printed. Record the true label, predicted label, and confidence for each:

| # | True label | Predicted | Confidence |
|---|-----------|-----------|-----------|
| 1 | Negative | Positive | 99.8% |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

All five errors have confidence above **99%**. What does it mean for the deployment system when the model's worst errors are also its most confident predictions? How does this affect the usefulness of the confidence threshold as a quality filter?

**Q10.3.** Error #1 (True: Negative, Predicted: Positive, 99.8% confidence) is a review that begins: *"I'm Mike Sedlak. I co-wrote the score for this movie. And proud of it."* This is a behind-the-scenes review written by a crew member, not a typical viewer opinion. Identify two reasons why this type of review is particularly difficult for a model fine-tuned on standard viewer sentiment data. What does this tell you about the importance of training data diversity?

**Q10.4.** Error #2 (True: Positive, Predicted: Negative, 99.7%) begins: *"All right, I'll grant you that some of the science in 'Doppelganger' (or 'Journey To The Far Side Of The Sun') is kind of dopey."* The review appears to start with a concession (acknowledging a flaw) before presumably praising the film. Explain how this **rhetorical structure** (concede-then-praise) can fool a transformer model that processes text sequentially and may weight the beginning of a review heavily due to truncation.

---

## Section 11 — Step 2.4: Calibration — Accuracy vs. Confidence

**Q11.1.** The calibration chart (Step 2.4) shows accuracy and review count for five confidence buckets. Complete the table from your output:

| Bucket | Count | Accuracy | Cumulative Coverage |
|--------|-------|----------|---------------------|
| 0.50–0.60 | 3 | 66.7% | 1.5% |
| 0.60–0.70 | 2 | 50.0% | 2.5% |
| 0.70–0.80 | | | |
| 0.80–0.90 | | | |
| 0.90–1.00 | | | |

**Q11.2.** The **0.70–0.80 bucket** has **0%** accuracy (n=2). This is the worst-performing bucket — worse even than the 0.50–0.60 bucket. Does this mean the model is reliably wrong in this range? What statistical limitation makes this observation unreliable, and how would you need to change the experiment to draw a robust conclusion about accuracy in this bucket?

**Q11.3.** The **0.90–1.00 bucket** contains **189 out of 200 reviews (94.5%)** with an accuracy of **89.9%**. This single bucket dominates the dataset. A student argues: *"Since nearly all predictions fall in the high-confidence bucket, the confidence score isn't useful for filtering — most reviews will be auto-tagged anyway."* Do you agree or disagree? Use the specific numbers from the calibration table to support your answer. What is the difference in accuracy between auto-tagging at threshold 0.90 vs. threshold 0.50?

**Q11.4.** The calibration chart title is *"Accuracy vs. Confidence."* A perfectly calibrated model would show a **monotonically increasing** accuracy as confidence increases (higher confidence always means higher accuracy). Looking at your chart, does DistilBERT show this pattern across all five buckets? Point to any bucket where the pattern breaks down and suggest why.

---

## Section 12 — Step 2.5: Business Deployment — Auto-Tagging Threshold

**Q12.1.** The threshold analysis chart (Step 2.5) plots % auto-tagged (blue) and auto-tag accuracy (green) as the confidence threshold increases from 0.50 to 1.00. Describe the general shape of each curve:
- As the threshold increases, does the % auto-tagged go up or down?
- As the threshold increases, does the auto-tag accuracy go up or down overall?
- At what approximate threshold does the accuracy line start to rise steeply?

**Q12.2.** The printed operating point comparison shows:

| Threshold | Auto-tagged | Human review | Auto accuracy | Time saved |
|-----------|-------------|--------------|---------------|------------|
| Default (0.50) | 200/200 (100%) | 0/200 (0%) | 88.5% | ~16.7 hours |
| High-precision (0.90) | 189/200 (94.5%) | 11/200 (5.5%) | 89.9% | ~15.8 hours |

The accuracy gain from raising the threshold from 0.50 to 0.90 is only **+1.4 percentage points** (from 88.5% to 89.9%), while the coverage drops by **5.5%** (11 reviews sent to human review). For TechNest's pipeline processing 10,000 reviews per day, calculate:
- How many reviews per day would require human review at threshold 0.90?
- How many additional correct predictions per day does the 0.90 threshold produce compared to 0.50?

Is the +1.4 pp accuracy gain worth routing 550 extra reviews per day to human reviewers? Make a recommendation and justify it.

**Q12.3.** The time-saved calculation assumes **5 minutes per review** for a human analyst. At threshold 0.50 (all reviews auto-tagged), the model saves **~16.7 hours** per 200 reviews — but only if the auto-tagged predictions are accepted without verification. In a real enterprise deployment, a quality assurance team would spot-check a random sample of auto-tagged reviews. How would you design a spot-checking protocol that balances efficiency and quality assurance? What sample size would you check, and how would you use the confidence score to prioritize which reviews to spot-check?

---

## Section 13 — Step 2.6: Interactive Batch Analysis Widget

**Q13.1.** Run the five default reviews in the batch widget (Step 2.6) at threshold **0.50**. Record the Sentiment and Action for each:

| # | Review (first 5 words) | Sentiment | Confidence | Action |
|---|------------------------|-----------|------------|--------|
| 1 | "This product exceeded every..." | | | |
| 2 | "Arrived damaged and customer..." | | | |
| 3 | "It works fine, nothing..." | | | |
| 4 | "Five stars. Best purchase..." | | | |
| 5 | "Stopped working after two..." | | | |

**Q13.2.** Now raise the threshold to **0.90** and run the same five reviews again. Which reviews, if any, change from AUTO to HUMAN? What does the confidence score for those reviews tell you about the model's certainty on ambiguous text (e.g., review #3: *"It works fine, nothing special, would probably buy again"*)?

**Q13.3.** Review #3 (*"It works fine, nothing special, would probably buy again"*) is deliberately neutral/lukewarm. What sentiment does DistilBERT predict for it, and what is the confidence score? A binary (positive/negative) classifier is forced to assign one label to every review. What class of sentiment does it fail to represent, and how could a **three-class model** (Positive / Neutral / Negative) improve the ReviewIQ pipeline for TechNest?

---

## Section 14 — Cross-Task Synthesis

**Q14.1.** Task 1 demonstrates a **16-percentage-point accuracy gap** between VADER (72.0%) and DistilBERT (88.0%) on the same 50 reviews. The agreement breakdown shows that in 9 out of 50 cases (18%), only DistilBERT is correct while VADER fails. Using what you learned about tokenization (Section 2) and VADER's lexicon limitations (Section 3), explain in 2–3 sentences *why* contextual representations give DistilBERT a fundamental advantage over lexicon lookup for reviews that contain negation, sarcasm, or plot-summary language.

**Q14.2.** In Task 2, the model produces **23 errors out of 200**, with all 5 top errors having confidence above 99%. The calibration chart shows the model is extremely confident on nearly all predictions, yet still wrong 11.5% of the time. Compare this behavior to what you would expect from a **well-calibrated** model: how should confidence and accuracy relate in a well-calibrated classifier? Use the phrase "overconfident" in your answer.

**Q14.3.** The threshold analysis (Step 2.5) shows that raising the threshold from 0.50 to 0.90 only improves accuracy by 1.4 pp while routing 5.5% of reviews to human review. This limited gain happens because 94.5% of predictions already fall above 0.90. This is a direct consequence of the overconfidence observed in Section 6 (Q6.2). Explain the connection: how does extreme confidence concentration make the threshold an ineffective quality filter for this model on this dataset?

**Q14.4.** The notebook evaluated DistilBERT — which was fine-tuned on **SST-2** (Rotten Tomatoes snippets) — on full **IMDB** reviews. The conclusions section warns that deploying on **TechNest's actual product reviews** would likely reduce accuracy. List **three specific differences** between IMDB movie reviews and electronics product reviews that would cause the model to struggle, and for each one explain whether it affects VADER or DistilBERT more severely.

**Q14.5.** Throughout both tasks, **feature normalization** was not required — unlike K-Means (Activity 10) or neural networks (Activity 9). Explain why transformer models like DistilBERT do not require the explicit normalization step that distance-based and gradient-descent-based algorithms need. What internal mechanism in the transformer architecture makes it robust to the scale differences between input features?

---

*ReviewIQ — TechNest Customer Review Analytics Pipeline*
*Activity 11 | Introduction to Artificial Intelligence*
