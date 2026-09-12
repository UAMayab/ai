# Activity 5 — Reflection Questions: The Whispering Cave

Answer every question below based on your own exploration in the app. Submit this file
separately from your screenshots — do not just describe the app, use your actual results.

**Remember: elaborate your answers.** A correct one-word answer with no explanation will not
receive full credit on the interpretive questions.

---

## Part 1 — Facts, Rules, and Recursion (Session 10)

1. Write out one `tunnel(X, Y)` fact directly from the Tunnel Rules tab (any one you like), and
   report whether `reachable(Entrance, Treasure Room)` came back **TRUE** or **FALSE** when you
   asked the Oracle.
2. The rule is: `reachable(X, Y) :- tunnel(X, Y).` and `reachable(X, Y) :- tunnel(X, Z), reachable(Z, Y).`
   Which of these two lines is the **base case**, and which is the **recursive case**? In your own
   words, explain what makes the second line "recursive."

## Part 2 — The Search Space (Session 11)

3. What is the **initial state** and the **goal state** in this activity?
4. According to the app's brute-force count, how many total possible paths exist from the
   Entrance to the Treasure Room? List every path.
5. In your own words, explain the difference between the **search space** (every possible path)
   and the single path a search algorithm like DFS actually finds. Why can these be different?

## Part 3 — Depth-First Search (Session 12)

6. List, in order, every chamber DFS actually **visited** (not skipped) before finding the
   treasure. How many chambers did it visit in total?
7. Name the one chamber where DFS hit a genuine **dead end** and had to backtrack. Separately,
   name the one chamber on the map that was **never visited at all** before the treasure was
   found, and explain why not.
8. What is the exact path DFS used to reach the treasure (the chain of chambers from Entrance to
   Treasure Room, not just the order things were visited)? Is it the same as the *shortest*
   path you listed in Question 4? If not, explain in your own words why Depth-First Search
   doesn't always find the shortest path.

## Part 4 — Synthesis

9. Explain, as if to a 10-year-old, why the recursive `reachable(X, Y)` rule from Session 10 and
   the step-by-step stack-based search from Session 12 are really "the same idea" wearing two
   different costumes.
10. Name one real-world use of Depth-First Search **other than** cave/maze exploration (for
    example: exploring a file system, checking whether a website's links can reach a certain
    page, or solving a puzzle). Briefly explain how "go as deep as possible, then backtrack"
    applies in that example.
