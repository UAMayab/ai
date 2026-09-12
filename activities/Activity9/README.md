# Activity 9: Pack for the Trip — A Genetic Algorithm Challenge
## Sessions 16
## Due date (mm/dd/yyyy): 10/04/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

You're heading out on a business trip with one **8 kg carry-on bag**. You have 8 items you'd
like to bring — a laptop, a client gift, a camera, and more — each with its own weight and
usefulness score, but they don't all fit. Which combination should you pack to get the **most
total usefulness** without going over the weight limit?

This is the classic **Knapsack Problem** — the same kind of decision behind choosing which
projects to fund with a limited budget, which items to stock in limited warehouse space, or
which features to build with limited developer time. Today you'll solve it the way nature
solves survival: with a **Genetic Algorithm** — evolving a population of candidate packing plans
across generations using selection, crossover, and mutation.

This activity is a single interactive app — no coding required. Everyone in the class uses the
**same fixed items and the same fixed genetic algorithm run** (the "randomness" is seeded, so it
produces identical results every time), so your results should match your classmates' exactly.

**App link:** https://uam-aiclass-a9.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has two tabs:

1. **🧳 The Packing Problem** — the 8 candidate items, the weight limit, and a glossary of
   genetic algorithm vocabulary (chromosome, gene, population, fitness, generation, selection,
   crossover, mutation) mapped onto this specific problem.
2. **🧬 Run the Genetic Algorithm** — click through 12 generations, one at a time, watching the
   population's fitness values evolve, and finally compare the algorithm's best-ever answer
   against the true optimal packing (found by checking all 256 possible combinations).

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Packing Problem tab.** Note the 8 items, the weight limit, and the vocabulary
   table.
   💡 *Hint:* You don't need to memorize the vocabulary — you'll see each term in action in the
   next tab.

2. **Step through all 12 generations in the Run the Genetic Algorithm tab, one click at a
   time.** Take a screenshot of Generation 1, and another of the generation where "Best-ever"
   first reaches its final value.
   💡 *Hint:* Watch the "Best in Generation" number — it doesn't always go up! That's expected:
   this is a **non-elitist** algorithm, so a good solution can disappear from the population in
   a later generation. That's exactly why "Best-ever" is tracked separately.

3. **Take a screenshot of the Final Result**, showing whether the algorithm found the true
   optimal packing.

4. **Fill out `A9_ReflectionQuestions.md`**, using the exact data from your run, and submit it
   along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity9
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
