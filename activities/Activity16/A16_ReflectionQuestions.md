# Activity 16 — Reflection Questions: Customer Groups (k-means)

Answer every question using the app's **default settings**, unless a question tells you to change
something. Submit this file together with your labeled screenshots — do not just describe the app,
use your actual results.

---

## Part A — The data and the algorithm

1. **Before running anything**, look at the chart in the *Meet the Customers* tab. How many groups
   of customers do you see by eye? Describe each group in plain words (for example, "people who
   visit often but spend little").

2. In the *Step by Step* tab with the default settings (k = 4, Random customers, seed 4, maximum
   iterations 30, tolerance 0), run k-means to the end. Report:
   (a) how many iterations it took,
   (b) which stopping rule stopped it, and
   (c) the final WCSS.

3. In your own words, explain what the **assignment step** and the **update step** do. Then look at
   the WCSS column of your iteration log: what happened to WCSS from one iteration to the next?
   Explain why it can never go up.

4. Keep the default settings, but:
   (a) set **maximum iterations to 3**, and
   (b) set maximum iterations back to 30 and the **tolerance to 0.1**.

   For each run, report the stopping rule, the number of iterations, and the final WCSS. Compare
   them with your answer to Question 2. What is the risk of stopping k-means early? (Hint: look at
   the "largest centroid move" column of the full run's log.)

## Part B — Starting centroids

5. With **Random customers** and k = 4, try different random seeds until you find one whose final
   WCSS is clearly worse than in Question 2. Report the seed and its final WCSS, include a
   screenshot, and describe what went wrong (look at where the centroids ended up).

6. In the *Restarts* tab (k = 4, 20 runs), report:
   (a) the best WCSS found,
   (b) how many random starts reached it,
   (c) how many k-means++ starts reached it, and
   (d) the worst random-start WCSS.

   The lecture says that when k-means converges, it "has reached an optimal and stable result."
   Every one of these runs converged. Based on your numbers, is the lecture's statement completely
   true? Explain.

7. Choose **Pick my own** and deliberately choose 4 bad starting customers. Report the 4 customer
   numbers you chose and the final WCSS, include a screenshot of the final clusters, and describe
   what the final clusters got wrong.

## Part C — Choosing k and making business decisions

8. In the *Choosing k & Segments* tab, which k does the **elbow method** suggest, and which k does
   the **silhouette score** suggest? Do they agree with your guess in Question 1?

9. In the segment report with k = 4:
   (a) give each cluster a business name,
   (b) say which cluster brings in the largest share of total monthly revenue, and report that
   cluster's share of customers and its share of revenue, and
   (c) propose one specific marketing action for each cluster.

## Part D — Limits of k-means

10. In the *Where k-means Fails* tab, for **each** of the two datasets, report the percentage of
    points k-means put in their true group, the WCSS of k-means' answer, and the WCSS of the true
    groups. What does comparing the two WCSS values tell you about *why* k-means fails on these
    datasets?

## Part E — Another application

11. In the *Bonus: Photo Compression* tab, with the coffee photo (k-means++, seed 0), report the
    bits per pixel and the uncompressed size for **k = 4, 16, and 32**, along with the original's
    size. What is the smallest k at which the photo still looks acceptable to you, and why?

12. Describe **one other real-world use of k-means** (not customers or photos). What would each data
    point be, which features would you cluster on, how would you choose k, and what would you do
    with the clusters once you had them?
