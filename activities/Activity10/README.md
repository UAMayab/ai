# Activity 10: SmartWash — A Fuzzy Logic Laundry Controller
## Sessions 17
## Due date (mm/dd/yyyy): 10/04/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

Real washing machines don't ask "is this load big or small?" as a strict Yes/No question — a
4 kg load isn't cleanly "small" or "medium," it's a bit of both. **Fuzzy Logic**, first proposed
by Lotfi Zadeh in 1965, lets a controller reason with exactly that kind of real-world
ambiguity, and still land on one precise decision. It's the same idea behind smart washers,
dryers, thermostats, and camera autofocus systems.

In this activity, you'll explore **SmartWash**, a small fuzzy controller that reads a load's
**size** and **dirtiness** and decides how many minutes to wash for.

This activity is a single interactive app — no coding required. Everyone in the class uses the
**same fixed rule base and membership functions, tested on the same five profiles** (there is no
randomness anywhere in the app), so your results should match your classmates' exactly.

**App link:** https://uam-aiclass-a10.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has two tabs:

1. **🧺 The Fuzzy Controller** — the four-step fuzzy pipeline (fuzzification, inference,
   aggregation, defuzzification), the membership function curves for Load Size and Dirtiness,
   and the full 9-rule rule base.
2. **🔬 Test the Controller** — pick one of five fixed profiles and see every step of the
   reasoning process, from raw numbers to final wash time. A sandbox at the bottom (ungraded)
   lets you try your own values just to build intuition.

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Fuzzy Controller tab.** Look at the membership function charts and note that a
   value near the middle of the range belongs to *two* terms at once.
   💡 *Hint:* Try to find the load value where "Small" and "Medium" are exactly equal (look at
   where the two lines cross on the chart).

2. **Run all five profiles (P1 through P5) in the Test the Controller tab.** Take a screenshot
   of the full breakdown for each one.
   💡 *Hint:* For P2, only one single rule fires at full strength (1.0) — that's the easiest one
   to double-check by hand.

3. **Compare P4 and P5.** Take a screenshot showing both of their final wash times side by side.

4. **Fill out `A10_ReflectionQuestions.md`**, using the exact data from your run, and submit it
   along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity10
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
