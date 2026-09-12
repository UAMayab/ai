# Activity 7: YucaExpress — The Fastest Route Challenge
## Sessions 14
## Due date (mm/dd/yyyy): 09/27/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

You dispatch deliveries for **YucaExpress**, a last-mile courier service in Mérida. A courier
needs to get from the **Depot** to the **Client Office** using the *cheapest total distance* —
every extra kilometer costs the company time and fuel.

You know the straight-line ("as the crow flies") distance from any junction to the client's
office — that's easy to read off a map. But real roads don't always go in a straight line.
This activity is about **Heuristic Search**: using that straight-line estimate to guide your
search, without letting it fool you.

This activity is a single interactive app — no coding required. Everyone in the class uses the
**same fixed delivery map** (there is no randomness anywhere in the app), so your results should
match your classmates' exactly.

**App link:** https://uam-aiclass-a7.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has three tabs:

1. **🗺️ The Map** — the problem definition, the full road network with real distances, and a
   table of straight-line distances (the heuristic, h) from every junction to the goal.
2. **🎯 Greedy Best-First** — click through a search that always drives toward whichever
   junction *looks* closest to the goal, ignoring how far it has already driven.
3. **⭐ A\* Search** — click through a search that balances real distance driven (g) *and* the
   straight-line estimate (h), using f(n) = g(n) + h(n).

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Map tab.** Note the initial state, the goal state, and the heuristic formula
   f(n) = g(n) + h(n). Look at the straight-line-distance table.
   💡 *Hint:* Notice that "Retorno del Lago" has one of the *smallest* straight-line distances
   to the goal of any junction. Keep an eye on it.

2. **Step through the Greedy Best-First tab, one click at a time, until you arrive.** Take a
   screenshot of the final result.
   💡 *Hint:* At every step, Greedy always jumps to whichever junction in the frontier has the
   *smallest* h — watch the "Frontier, sorted by h" panel to predict its next move before you
   click.

3. **Step through the A\* tab, one click at a time, until you arrive.** Take a screenshot of
   the final result, including the comparison message.
   💡 *Hint:* Watch how A\* sometimes picks a junction with a *larger* h than another option in
   the frontier — that's because its f (g + h) is smaller overall.

4. **Find the one road in this map that costs noticeably more than a straight line between its
   two junctions would suggest.** Take a screenshot of it (visible as an edge label on the map,
   or in either trace table).

5. **Fill out `A7_ReflectionQuestions.md`**, using the exact data from your run, and submit it
   along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity7
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
