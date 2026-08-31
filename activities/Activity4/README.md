# Activity 4: ReelWave Recommendation Meltdown
## Sessions 7, 8, 9
## Due date (mm/dd/yyyy): 09/13/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Case

ReelWave, a streaming platform, woke up to a wave of complaints: kids' profiles are getting horror-movie recommendations, and horror fans are getting cooking shows. You've been hired as an **AI Detective** to find out where in ReelWave's AI pipeline the fault lives — is it bad **Data**, bad **Information**, or bad **Knowledge**?

This activity is a single interactive app — no coding required, but you will make a few precise, guided edits and observe what changes. Everyone in the class uses the **same shared link** (your instructor will post it), so there's nothing to install.

**App link:** https://esgbtzjappjhcnqvn9s5jbm.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see **Running It Yourself** below.

### The App

The app has four tabs, each mapping to one of this unit's sessions:

1. **🗂️ Data (Session 7)** — Raw, unprocessed interaction logs. Use the filters to explore, then click "Show data quality report" to see how much of the data is corrupted (duplicates, missing values).
2. **📊 Information (Session 7)** — The same data, cleaned and aggregated into per-genre averages. Switch the profile type and look for anything that seems out of place.
3. **🕸️ Knowledge Graph (Session 8)** — The actual knowledge the recommendation engine relies on: a network of content, genres, and age groups connected by relationships. One relationship in this graph is wrong, and it's the real root cause of the meltdown.
4. **🔎 Interrogation Room (Session 9)** — A small fact/rule/query engine (in the spirit of Prolog) that reasons about who or what caused the bug. Run a query, then add one new fact and run it again.

### Your Tasks

No programming, AI, or Prolog background is required — just follow each step and use the hints below if you get stuck.

1. **Investigate the Data tab.** Take a screenshot of the data quality report.
   💡 *Hint:* "Corrupted" rows are either exact duplicates (the same log entry logged twice) or rows missing a rating. You don't need to count anything by hand — just click "Show data quality report."

2. **Investigate the Information tab.** Find the profile type + genre combination with a suspiciously high match score. Take a screenshot.
   💡 *Hint:* Switch the dropdown between kids / teen / adult and compare the bars. Ask yourself: does it make sense for a *kids* profile to score high on any particular genre? One bar shouldn't be there at all.

3. **Investigate the Knowledge Graph tab.** Identify the one `similar_to` edge that doesn't belong. Take a screenshot of the "Top 3 Recommended" list *before* you touch anything.
   💡 *Hint:* Node colors tell you what kind of thing each node is (blue = content, orange = genre, green = age group). Find the "Bunny Buddies" node and look at every line coming out of it — one of them connects it to something clearly not made for kids.

4. **Fix it.** Use the "Fix an Edge" control to remove that one bad edge. Take a screenshot of the "Top 3 Recommended" list *after* the fix.
   💡 *Hint:* The dropdown under "Fix an Edge" lists every `similar_to` edge by name — just pick the one you spotted in Step 3.

5. **Investigate the Interrogation Room.** Run a query against each suspect. Take a screenshot of the reasoning trace and verdict for the suspect you believe is responsible.
   💡 *Hint:* Query all four suspects, not just one — seeing a GUILTY trace next to a NOT GUILTY trace makes it much easier to see what the rule is actually checking. Pay attention to two things in each trace: did the suspect have access, and did their edit happen "overnight"?

6. **Add one new fact.** Use the "Add a New Fact" form to give the engine one additional piece of evidence, then re-run a query and see whether the verdict changes. Take a screenshot of the new result.
   💡 *Hint:* The engine only cares about the hour of the time you type in. Pick a suspect who came back NOT GUILTY, give them a new edit time somewhere between 00:00 and 05:59, and re-run the query.

7. **Write your report.** Answer every question in `A4_ReflectionQuestions.md` and submit it, along with your labeled screenshots, as your deliverable.

### Running It Yourself (optional)

If you already completed Activity 2's setup and prefer to run this locally instead of using the shared link:

```bash
conda activate ai_uam
cd Activity4
pip install -r requirements.txt
streamlit run app.py
```

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
