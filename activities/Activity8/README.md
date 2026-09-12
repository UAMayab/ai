# Activity 8: ShopSmart Assistant — An Expert System for Customer Decisions
## Sessions 15
## Due date (mm/dd/yyyy): 09/27/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

**ShopSmart** is a fictional online store. Every day, it has to make small decisions
automatically: should this customer get a discount? Should this order get free shipping?
Should this account be locked for suspicious activity? Should IT be alerted about an
overheating server?

Instead of a human deciding each case one by one, ShopSmart uses an **expert system**: a fixed
set of IF-THEN rules, written once by a human expert, applied automatically and consistently by
a computer. This activity explores how that works — the same idea shows up in IT (security
rules), business (discount and shipping rules), and any interface that has to *explain itself*
to the people using it (a design/UX concern too).

This activity is a single interactive app — no coding required. Everyone in the class uses the
**same fixed rule base and the same five customer/system profiles** (there is no randomness
anywhere in the app), so your results should match your classmates' exactly.

**App link:** https://uam-aiclass-a8.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has two tabs:

1. **🧠 Knowledge Base & Architecture** — how the five standard components of an expert system
   (knowledge base, inference engine, user interface, knowledge acquisition, explanation
   mechanism) map onto this specific app, plus the full rule base and the five fixed profiles.
2. **⚙️ Run the Inference Engine** — pick one of the five profiles, then click through the
   engine checking each rule against it, one at a time, showing exactly which condition passed
   or failed and why.

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Knowledge Base & Architecture tab.** Note the five components and the four rules.
   💡 *Hint:* You don't need to memorize the rules — you'll look them up as you check each
   profile.

2. **Run each of the five profiles (A through E) through the Inference Engine tab**, one at a
   time, clicking through all four rules for each. Take a screenshot of the **Final Summary**
   for each profile.
   💡 *Hint:* Pay close attention to Profile C — it has 5 failed login attempts (well above the
   threshold of 3), but the Account Lockout rule still does **not** fire. Look carefully at
   *why* in the trace.

3. **Fill out `A8_ReflectionQuestions.md`**, using the exact data from your run, and submit it
   along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity8
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
