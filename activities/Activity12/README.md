# Activity 12: Mérida Homes — Predicting Property Prices
## Sessions 20, 21
## Due date (mm/dd/yyyy): 10/11/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

**Mérida Homes** is a fictional real-estate agency. Before listing a property, agents want a
quick, data-driven price estimate — a job perfectly suited to **Linear Regression**: learning a
straight-line (or flat-plane) relationship between a house's features and its price, from 60
real past sales.

- **Session 20** covers **one-variable** regression: predicting price from size alone.
- **Session 21** extends it to **multi-variable** regression: adding bedrooms, age, and distance
  to downtown.

This activity is more hands-on than earlier ones: instead of just clicking through a fixed
trace, you can freely **drag sliders to change the learning rate and iteration count, toggle
which features the model uses, and type in your own house specs to get a live price
prediction.** Try breaking things — a learning rate that's too high will make the model
*diverge* instead of learn, and the app will tell you so.

**App link:** *(your instructor will post the shared Streamlit Community Cloud link here)*

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has three tabs:

1. **🏠 The Dataset** — the 60-sale dataset and a scatter plot of each feature against price.
2. **📈 One-Variable Regression (Session 20)** — an animated gradient-descent playground (your
   own learning rate/iterations), a **canonical model** with fixed settings, and a live
   price-prediction tool.
3. **📊 Multi-Variable Regression (Session 21)** — a feature-toggle playground, a canonical
   4-feature model, a live prediction tool, and a side-by-side comparison against Session 20's
   model.

### ⚠️ Important: Playground vs. Canonical Model

The learning-rate sliders, iteration sliders, and feature checkboxes are **playgrounds for your
own exploration** — they do not affect your grade. Every reflection question below is about the
**Canonical Model** sections (clearly labeled in the app, using a fixed learning rate of 0.3 and
200 iterations), so your answers will match your classmates' exactly.

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Dataset tab.** Note which feature looks most strongly related to price just from
   the scatter plots.

2. **In the One-Variable tab, try at least 3 different learning rates in the playground**,
   including one large enough to make the model diverge. Take a screenshot of the divergence
   warning.
   💡 *Hint:* Try 1.0 or higher.

3. **Record the Canonical Model's slope, intercept, R², and MSE** from the One-Variable tab.
   Take a screenshot.

4. **In the Multi-Variable tab, toggle features on and off in the playground** and watch R²
   change. Take a screenshot showing at least two different feature combinations and their R²
   values.

5. **Record the Canonical (all 4 features) Model's coefficients, R², and MSE.** Take a
   screenshot.

6. **Use both canonical prediction tools** to predict the price of the **same house**: 150 m²,
   3 bedrooms, 5 years old, 4 km from downtown. Take a screenshot of both predictions.

7. **Fill out `A12_ReflectionQuestions.md`**, using the exact numbers from your Canonical Model
   screenshots, and submit it along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity12
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
