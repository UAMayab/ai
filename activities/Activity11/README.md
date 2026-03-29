# Activity 11 — Natural Language Processing: Sentiment Analysis

**Course:** Introduction to Artificial Intelligence
**Session:** 33 — Natural Language Processing
**Topic:** Tokenization · Rule-Based NLP · Transformer Models · Sentiment Classification

---

## Introduction

Welcome to Activity 11. In this assignment you will build an **AI-powered sentiment analysis pipeline** grounded in the NLP concepts from Session 33 — from the historical evolution of language processing systems all the way to modern transformer models.

You will work as a junior data scientist at **ReviewIQ**, an analytics company whose client **TechNest** — an online electronics retailer — receives thousands of product reviews every day. Your job is to help TechNest answer two critical questions:

1. **How do rule-based and transformer-based NLP models compare?** Use **VADER** (a lexicon-based analyzer) and **DistilBERT** (a Hugging Face transformer) on the same review dataset, understand the tokenization process, and measure the accuracy gap.

2. **How can we deploy sentiment analysis in a real business pipeline?** Evaluate DistilBERT on 200 held-out reviews, interpret the confusion matrix and error patterns, and design a **confidence-threshold system** that auto-tags high-confidence predictions while routing uncertain cases to human review.

By the end of this activity you will be able to:

- Explain **WordPiece tokenization** and the role of `[CLS]`, `[SEP]`, and `##` tokens
- Describe how **VADER** uses a sentiment lexicon and why it struggles with sarcasm and negation
- Load a pre-trained **DistilBERT** model via the Hugging Face `pipeline()` API
- Interpret **confidence scores** from a softmax classifier
- Compute and interpret a **confusion matrix**, precision, recall, and F1-score in a business context
- Perform **error analysis** by inspecting confident wrong predictions
- Read a **calibration chart** (accuracy vs. confidence bucket)
- Design a **human-in-the-loop deployment** strategy using a confidence threshold

---

## Background: Why Transformers Changed NLP

Session 33 traces NLP's evolution from rule-based systems (ELIZA, 1966) through statistical models (HMMs, SVMs) to deep learning. The critical breakthrough was the **transformer architecture** (Vaswani et al., 2017), which introduced self-attention — allowing the model to weigh every word in the context of every other word simultaneously.

**BERT** (Bidirectional Encoder Representations from Transformers, Google 2018) applied this architecture to language understanding by pre-training on massive text corpora. **DistilBERT** (Hugging Face, 2019) is a distilled version of BERT — 40% smaller, 60% faster, and 97% as accurate on benchmarks — making it ideal for classroom use on standard laptops.

---

## Tasks

| Task | Algorithm | Focus |
|------|-----------|-------|
| **Task 1** | VADER vs. DistilBERT | Tokenization, pipeline, model comparison on 50 reviews |
| **Task 2** | DistilBERT full evaluation | Confusion matrix, error analysis, calibration, auto-tagging deployment |

Each task follows the same pipeline:
1. Load and explore the data
2. Run the model / analyze outputs
3. Visualize results
4. Interpret in business terms
5. Interact with ipywidgets

---

## Session Coverage

| Session | Topic | Where it appears in the notebook |
|---------|-------|----------------------------------|
| 33 — Natural Language Processing | Tokenization, rule-based NLP, transformer models, sentiment analysis | All steps (Task 1 Steps 1.1–1.7, Task 2 Steps 2.1–2.6) |

---

## Model and Data

**Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- Available for free from the [Hugging Face Hub](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- Downloaded automatically by `transformers` on first run (~268 MB, cached locally)
- **No Hugging Face account or API key required**

**Dataset:** IMDB Movie Reviews
- Loaded automatically via the `datasets` library (~80 MB, cached locally)
- 400 reviews sampled from the test split with fixed random seed (`11`)
- Binary labels: Positive (1) / Negative (0)

---

## Before You Begin — Disk Space and Download Time

> **Important — please read before installing.**
>
> This assignment uses large pre-trained models and datasets that are downloaded automatically on first run. Make sure you have:
>
> | Download | Size | Cached location |
> |----------|------|-----------------|
> | PyTorch (CPU-only) | ~250 MB | Python environment |
> | Hugging Face `transformers` + `datasets` | ~100 MB | Python environment |
> | DistilBERT model weights | ~268 MB | `~/.cache/huggingface/hub` |
> | IMDB dataset | ~80 MB | `~/.cache/huggingface/datasets` |
> | **Total (first run)** | **~700 MB** | |
>
> - **Free disk space required:** at least **1.5 GB** (environment + cache + notebook outputs)
> - **Download time:** 10–30 minutes on a typical university Wi-Fi connection
> - **After the first run**, everything is cached locally — re-running the notebook takes only a few seconds for setup cells
>
> If you are on a metered connection or have limited disk space, complete the installation **before** class.

---

## Getting Started

### 1. Check Python version

This assignment requires **Python 3.9 or newer**. Open a terminal (Command Prompt or PowerShell on Windows) and verify:

```bash
python --version
```

If your version is older than 3.9, download the latest Python installer from [python.org](https://www.python.org/downloads/).

> **Windows users:** During Python installation, check the box **"Add Python to PATH"**. Without this, the `pip` and `python` commands will not be found in the terminal.

### 2. Install dependencies

Open a terminal in the folder that contains `requirements.txt` and run:

```bash
pip install -r requirements.txt
```

> **Windows users — PowerShell execution policy:** If you see an error like *"running scripts is disabled on this system"*, run PowerShell as Administrator and execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then retry the `pip install` command.

> **PyTorch note:** `torch` is required as the backend for `transformers`. The CPU-only version is sufficient — no GPU needed. The `requirements.txt` file installs the standard CPU build automatically. If the download stalls or fails, you can install PyTorch manually using the command generator at [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) — select: Stable, Windows, Pip, Python, CPU.

> **Estimated install time:** 10–20 minutes depending on your internet speed. The PyTorch package alone is ~250 MB. Do not close the terminal while installation is running.

### 3. Enable interactive widgets

If you are using **classic Jupyter Notebook**:

```bash
jupyter nbextension enable --py widgetsnbextension
```

If you are using **JupyterLab**:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

> **Windows users:** Run these commands in the same terminal window where you ran `pip install`. If you see a `jupyter: command not found` error, close and reopen the terminal so the updated PATH takes effect.

### 4. Launch the notebook

Navigate to the Activity 11 folder and run:

```bash
jupyter notebook A11_NLP_SentimentAnalysis.ipynb
```

> **Windows users:** If Jupyter does not open automatically in your browser, copy the URL printed in the terminal (it looks like `http://localhost:8888/?token=...`) and paste it into your browser manually.

### 5. Run the cells in order

Start from the top and run each cell sequentially. The dataset and model are downloaded in early cells — all later cells depend on them.

> **Important:** Do not modify the dataset sampling cell. The fixed random seed (`11`) ensures every student works with identical reviews, which is required for consistent results across the class.

> **Runtime note:** The first time you run the notebook, two cells will trigger large downloads:
> - The **IMDB dataset** cell (~80 MB) — expect 1–5 minutes
> - The **DistilBERT model** cell (~268 MB) — expect 2–10 minutes
>
> Subsequent runs load both from local cache and complete in seconds. Cells that run inference on batches of reviews take an additional **1–3 minutes on CPU** — this is expected behavior.

> **Windows antivirus note:** Some antivirus programs (Windows Defender, etc.) may slow down the first model download by scanning the cache files as they are written. If the download seems unusually slow, this is a common cause. It resolves itself once the files are fully cached.

### 6. Answer the plot analysis questions

Once **all cells have been executed** and you can see every plot and printed output, open `A11_PlotAnalysis_Questions.md` and answer the questions in a **separate document** (plain text, Word, or PDF — see submission instructions below).

The questions are organized to follow the notebook from top to bottom. Keep the notebook open alongside the question document so you can refer to the exact plots and numbers as you write your answers.

> **Tip:** Do not answer from memory. Every question points to a specific chart or printed value. Your answers should cite those values directly.

---

## Files in This Directory

| File | Description |
|------|-------------|
| `A11_NLP_SentimentAnalysis.ipynb` | Main assignment notebook. Contains all instructions, code, plots, interactive widgets, and in-notebook reflection questions. **Must be executed before answering the plot analysis questions.** |
| `A11_PlotAnalysis_Questions.md` | Plot and output analysis questions. Answer these **after** running the notebook. Submit your answers as a separate document. |
| `requirements.txt` | List of Python packages required to run the notebook. Install with `pip install -r requirements.txt`. |
| `README.md` | This file. |

---

## Submission

Submit **two files** to the course portal:

1. **`A11_NLP_SentimentAnalysis.ipynb`** — the executed notebook
   - All code cells must show their output (plots and printed values visible)
   - All in-notebook reflection questions (Q1–Q5 at the end) must be answered in the Markdown cells
   - Do not remove or reorder any cells

2. **`A11_PlotAnalysis_Answers.pdf`** (or `.docx`) — your written answers to the plot analysis questions
   - Answer every question in `A11_PlotAnalysis_Questions.md`
   - Label each answer clearly with its question number (e.g., **Q2.3**, **Q11.1**)
   - Cite specific values from the notebook output in your answers
   - Answers must reflect the plots and numbers produced by **your own executed notebook**

---

## Grading

| Component | Description | Points |
|-----------|-------------|--------|
| Task 1 — Notebook (Steps 1.1 – 1.6) | Code executed, plots visible, step outputs correct | 25 |
| Task 1 — Interactive Experiment | In-notebook reflection Q1 answered | 5 |
| Task 2 — Notebook (Steps 2.1 – 2.5) | Code executed, plots visible, step outputs correct | 25 |
| Task 2 — Interactive Experiment | In-notebook reflection Q2 answered | 5 |
| Plot Analysis — Sections 0–7 (Task 1) | Written answers to Task 1 plot questions | 20 |
| Plot Analysis — Sections 8–14 (Task 2 & Synthesis) | Written answers to Task 2 and synthesis questions | 20 |
| **Total** | | **100** |

---

*ReviewIQ — TechNest Customer Review Analytics Pipeline*
*Activity 11 | Introduction to Artificial Intelligence*
