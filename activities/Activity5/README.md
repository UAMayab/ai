# Activity 5: The Whispering Cave — A Depth-First Search Adventure
## Sessions 10, 11, 12
## Due date (mm/dd/yyyy): 09/20/2026
## Delivery Format: [X] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

You are a cave explorer standing at the mouth of the **Whispering Cave**. Somewhere inside,
past ten chambers and winding tunnels, sits a chest of treasure. You only have one flashlight,
so you can only look down **one tunnel at a time** — and if it's a dead end, you have to walk
all the way back before you can try a different one.

That's exactly how a computer explores a graph with **Depth-First Search (DFS)**: go as deep
as you can down one path, and only turn back when you truly have to.

This activity is a single interactive app — no coding required, but you will click, step, and
query your way through it. Everyone in the class uses the **same fixed cave map** (there is no
randomness anywhere in the app), so your results should match your classmates' exactly.

**App link:** *(your instructor will post the shared Streamlit Community Cloud link here)*

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has three tabs, each mapping to one of this unit's sessions:

1. **🧭 The Search Space (Session 11)** — the vocabulary of problem-solving-by-search: initial
   state, goal state, actions, and the full search space. Shows every possible route through
   the cave to the treasure.
2. **🔗 Tunnel Rules (Session 10)** — the cave map written as Prolog-style facts and one
   recursive rule, `reachable(X, Y)`. Pick any two chambers and "Ask the Oracle" whether one can
   reach the other, and watch the recursive derivation happen step by step.
3. **🔦 Depth-First Explorer (Session 12)** — the main event. Click "Take one step" repeatedly
   to watch DFS explore the cave one move at a time, with a live stack, a visited list, and a
   highlighted map.

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Search Space tab.** Note the initial state, the goal state, and how many total
   paths exist from the Entrance to the Treasure Room.
   💡 *Hint:* The app counts this for you under "The Entire Search Space, Brute-Force" — you
   don't need to count by hand.

2. **Use the Tunnel Rules tab.** Ask the Oracle whether `Entrance` can reach `Treasure Room`.
   Then pick a different pair of your choosing and ask again. Take a screenshot of one full
   derivation trace.
   💡 *Hint:* Read the trace top to bottom — each indented line is one recursive call of
   `reachable(X, Y) :- tunnel(X, Z), reachable(Z, Y)`, one tunnel deeper than the line above it.

3. **Step through the entire Depth-First Explorer tab, one click at a time, until the treasure
   is found.** Don't skip ahead — read each message as it appears.
   💡 *Hint:* Watch the stack panel. Every time a chamber gets added to the top, that's DFS
   "going deeper." Every time the *same* chamber gets popped and immediately skipped, that's DFS
   noticing it already explored this chamber (this is what stops it from looping forever around
   the Torch Hallway – Echo Chamber – Bat Roost – Entrance loop!).

4. **Find the dead end.** Somewhere in your step-through, DFS will hit a chamber with nowhere
   new to go and have to backtrack. Take a screenshot of that exact step's message.
   💡 *Hint:* There are two candidate dead-end chambers in this cave. Only one of them actually
   gets *visited* during the search — the other is never reached before the treasure is found.

5. **Take a screenshot of the final message** once the treasure is found (step count and the
   path DFS actually walked will be shown).

6. **Fill out `A5_ReflectionQuestions.md`** and submit it along with your labeled screenshots.

7. **Record your 5-minute video** (see below) and include the link/file with your submission.

### Your 5-Minute Video

Record a video, **5 minutes or less**, explaining Depth-First Search **as if you were teaching
it to a 10-year-old** — simple words, no jargon, use the cave/treasure story as your example.

Because a spoken explanation can't be graded with a single "correct answer" the way a number
can, your video will instead be graded against a **checklist**: your grade depends on whether
you clearly cover each of the following points, not on production quality or eloquence.

**Your video must, in your own words:**
1. Explain what a **stack** is and why DFS uses one (LIFO — last in, first out).
2. Walk through **your own run** of the Depth-First Explorer tab: name the exact order of
   chambers DFS visited, in order.
3. Point out the **one dead-end chamber** your run actually hit, and explain what "backtracking"
   meant at that moment.
4. Explain, using the Torch Hallway – Echo Chamber – Bat Roost – Entrance loop as your example,
   why a search algorithm needs to remember which chambers it has already **visited**.
5. State whether the path DFS found to the treasure was the **shortest possible** path, and
   explain how you know (hint: compare it to what the Search Space tab told you).

Submit either a **YouTube link** (unlisted is fine) or an **MP4 file**.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity5
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
