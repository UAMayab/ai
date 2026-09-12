# Session 18 Class Demo: Supervised vs. Unsupervised Learning

**This is a classroom teaching tool, not a graded activity. There is nothing to submit.**

An interactive, animated Streamlit app for presenting Session 18 (Supervised and Unsupervised
Learning) in class, with a brief closing look at threats facing ML systems.

**App link:** https://uam-aiclass-a11-demo.streamlit.app/

## What's in it

Three tabs:

1. **🎯 Supervised Learning** — real-life examples, plus two animated demos you can press play
   on: a regression line learning to fit ice-cream-sales-vs-temperature data via gradient
   descent, and a classification boundary learning to separate "pass"/"fail" students by hours
   studied and attendance.
2. **🧩 Unsupervised Learning** — real-life examples, plus an animated K-Means clustering demo
   grouping fictional customers by income and spending score, starting from deliberately bad
   initial guesses so the convergence is visible.
3. **⚠️ ML Threats 101** — four brief, real-world-grounded cards: adversarial examples, data
   poisoning, bias & discrimination, and privacy leakage.

## Design notes

- All three demos use a **fixed random seed** (see `ml_demos.py`), so the animations look and
  converge the same way every time — useful for a live class demo you don't want to behave
  differently between takes.
- The K-Means demo intentionally starts from bad initial centroid guesses (not near the real
  cluster centers) so the "walking into place" animation is visually obvious.
- Animations use Plotly's built-in Play/Pause + step slider controls (`updatemenus` /
  `sliders`), embedded via `st.plotly_chart`.

## Running It Yourself

```bash
conda activate ai_uam
cd class_demos/Session18_MachineLearning
pip install -r requirements.txt
streamlit run app.py
```
