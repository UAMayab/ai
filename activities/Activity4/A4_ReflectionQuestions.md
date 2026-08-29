# Activity 4 — Reflection Questions: ReelWave Recommendation Meltdown

Answer every question below based on your own investigation in the app. Submit this file separately from your screenshots — do not just describe the app, use your actual results.

**Remember: elaborate your answers.** A correct one-word answer with no explanation will not receive full credit on the interpretive questions.

---

## Part 1 — Data, Information, Knowledge (Session 7)

1. In the Data tab, how many total rows are in the raw log, how many are exact duplicates, and how many are missing a rating?
2. In the Information tab, which profile type + genre combination showed a suspiciously high average genre-match score, and what was the value?
3. In your own words, classify what you saw in the Data tab, the Information tab, and the Knowledge Graph tab as **Data**, **Information**, or **Knowledge**, using the DIKW distinctions from Session 7. Why does the actual bug only become *explainable* once you reach the Knowledge Graph tab, even though a hint of it was already visible in the Information tab?

## Part 2 — Knowledge Representation (Session 8)

4. Which single `similar_to` edge in the knowledge graph was the root cause, and what were its two endpoints?
5. Report the "Top 3 Recommended" list *before* you removed the bad edge, and the list *after*. What changed?
6. Using Session 8 terminology (nodes, edges, relationship types, inference), explain why a single wrong edge in a semantic network can cause a bad downstream recommendation even when the underlying raw Data was completely correct.

## Part 3 — Facts, Rules, and Queries (Session 9)

7. Before you added your own fact, which suspect(s) did the engine mark GUILTY when you ran a query, and what did the reasoning trace show?
8. After you added one new fact in the Interrogation Room, did any verdict change? Report the suspect, the fact you added, and the new result.
9. In your own words — not a memorized textbook definition — explain what a **fact**, a **rule**, and a **query** are, using this activity's suspect(X) rule as your example.

## Part 4 — Synthesis

10. Real recommendation systems (Netflix, Spotify, YouTube) occasionally go viral for hilariously bad recommendations. Based on what you found in this activity, where in the Data → Information → Knowledge → Inference pipeline do you think most real-world AI failures actually originate, and why?
