# Activity 6: Six Degrees to Katún — A Breadth-First Search Networking Challenge
## Sessions 13
## Due date (mm/dd/yyyy): 09/27/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

You're a Business Development Associate at **Meridian Consulting Group**, trying to land a
meeting with **Elena Ruiz, CFO of Grupo Katún**. You don't know her directly — but maybe someone
you know, knows someone, who knows her. In business networking this is often called **"degrees
of separation"**: how many introductions stand between you and someone you want to meet. It's
exactly the idea behind LinkedIn's "2nd connection" / "3rd connection" labels.

You don't just want *a* chain of introductions — you want the **shortest one**. That's exactly
the problem **Breadth-First Search (BFS)** solves.

This activity is a single interactive app — no coding required. Everyone in the class uses the
**same fixed professional network** (there is no randomness anywhere in the app), so your
results should match your classmates' exactly.

**App link:** https://uam-aiclass-a6.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

The app has two tabs:

1. **🕸️ The Network** — the problem definition (initial state, goal state, actions, search
   space) and the full map of your professional network.
2. **🔎 BFS Path Finder** — click "Process next person in line" to watch Breadth-First Search
   work through the network one person at a time, using a first-in-first-out line (queue), until
   it reaches Elena Ruiz.

### Your Tasks

No programming background is required — just follow each step and use the hints if you get stuck.

1. **Read the Network tab.** Note the initial state, the goal state, and open "Who is who?" to
   understand each contact.
   💡 *Hint:* You don't need to memorize anything — you'll look people up as you go.

2. **Step through the BFS Path Finder tab, one click at a time, until Elena Ruiz is reached.**
   Don't skip ahead — read each message as it appears.
   💡 *Hint:* Watch the "Line to be processed" panel. It only ever grows from the back and
   shrinks from the front — that's what "first in, first out" means.

3. **Find the step where someone had no new contacts to offer.** Take a screenshot of that
   exact step's message.
   💡 *Hint:* One contact in this network only knows one other person — and that person was
   already reached before we got to them.

4. **Take a screenshot of the final success message**, showing the shortest chain of
   introductions and how many hops it took.

5. **Open "What would last session's DFS have done here?"** and take a screenshot of the
   comparison.

6. **Fill out `A6_ReflectionQuestions.md`**, using the exact data from your run, and submit it
   along with your labeled screenshots.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the
shared link:

```bash
conda activate ai_uam
cd Activity6
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
