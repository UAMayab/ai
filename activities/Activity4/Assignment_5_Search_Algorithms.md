# Assignment 5: Search Algorithm Analysis and Comparison
**Session 11 - Problem Solving by Search**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Analyze problem characteristics to select appropriate search algorithms
2. Compare informed vs. uninformed search methods
3. Evaluate trade-offs between optimality, completeness, time, and space complexity
4. Justify algorithm selection based on problem constraints
5. Understand practical applications of different search strategies

---

## Background

In artificial intelligence and computer science, selecting the right search algorithm for a problem is crucial. Different search algorithms have different strengths and weaknesses:

### Uninformed Search Methods (Blind Search)
- **Breadth-First Search (BFS)**: Explores level-by-level, guarantees shortest path
- **Depth-First Search (DFS)**: Explores deeply before backtracking, memory-efficient

### Informed Search Methods (Heuristic Search)
- **A* Algorithm**: Uses heuristic + actual cost, guarantees optimal solution
- **Greedy Best-First Search**: Uses only heuristic, fast but not always optimal

### Key Evaluation Criteria
- **Completeness**: Will it always find a solution if one exists?
- **Optimality**: Will it find the best (shortest/cheapest) solution?
- **Time Complexity**: How many nodes will it explore?
- **Space Complexity**: How much memory does it need?

---

## Assignment Instructions

### Part 1: Algorithm Review (20 minutes)

Review the characteristics of each search algorithm. Fill in the following comparison table:

| Algorithm | Completeness | Optimality | Time Complexity* | Space Complexity* | Best Use Cases |
|-----------|-------------|-----------|-----------------|------------------|----------------|
| BFS | Yes/No | Yes/No | O(?) | O(?) | [Your answer] |
| DFS | Yes/No | Yes/No | O(?) | O(?) | [Your answer] |
| A* | Yes/No | Yes/No | O(?) | O(?) | [Your answer] |
| Greedy | Yes/No | Yes/No | O(?) | O(?) | [Your answer] |

\* Where b = branching factor, d = depth of solution, m = maximum depth

**Include a brief explanation (2-3 sentences) for each algorithm describing:**
- What makes it complete or incomplete?
- What makes it optimal or not optimal?
- When would you choose this algorithm?

---

### Part 2: Problem Scenario Analysis (60 minutes)

You are given **FOUR** problem scenarios. For each scenario:

1. **Analyze the problem characteristics**
2. **Select the most appropriate search algorithm** (BFS, DFS, A*, or Greedy)
3. **Justify your choice** with specific reasoning
4. **Explain why the other algorithms are less suitable**

---

## Scenario 1: University Course Prerequisite Checker

**Context:**
Your university needs a system to verify if a student can enroll in a target course. The system must check if the student has completed all required prerequisites, including indirect prerequisites (prerequisites of prerequisites).

**Problem Characteristics:**
- **Graph Structure**: Directed acyclic graph (DAG) - courses and prerequisites
- **Goal**: Determine if there's a valid path from completed courses to target course
- **Constraints**:
  - Some courses have multiple prerequisites
  - Prerequisite chains can be 5-6 levels deep
  - Need to check ALL possible prerequisite paths
  - Must be reliable (can't miss any requirement)
- **Size**: ~200 courses, average 2-3 prerequisites per course
- **Priority**: Correctness is critical; speed is secondary

**Your Task:**
- **Which algorithm would you choose?** [Your answer]
- **Justification** (150-200 words):
  - Why is this algorithm best for this problem?
  - What specific characteristics make it suitable?
  - How does it handle the problem constraints?
- **Why NOT the other algorithms?** (50-75 words each):
  - Why would [Algorithm 2] be less suitable?
  - Why would [Algorithm 3] be less suitable?
  - Why would [Algorithm 4] be less suitable?

---

## Scenario 2: GPS Navigation in Urban Area

**Context:**
You're building a GPS navigation app for a delivery service. Drivers need the fastest route from their current location to a delivery address during rush hour.

**Problem Characteristics:**
- **Graph Structure**: Road network with thousands of intersections
- **Goal**: Find the shortest (fastest) path from start to destination
- **Constraints**:
  - Real-time traffic information available
  - Can estimate time to destination from any point (heuristic available)
  - Must find optimal route (time is money for delivery service)
  - City has ~10,000 intersections, ~25,000 road segments
  - Average trip involves 50-100 intersections
- **Priority**: Must be fast AND optimal

**Additional Information:**
- You have a good heuristic: straight-line distance to destination
- Traffic conditions can make some short routes slower
- Solution must be optimal to minimize delivery time

**Your Task:**
- **Which algorithm would you choose?** [Your answer]
- **Justification** (150-200 words)
- **Why NOT the other algorithms?** (50-75 words each)

---

## Scenario 3: Solving a Sliding Puzzle Game

**Context:**
You're creating an AI to solve 15-puzzle games (4x4 grid with 15 numbered tiles and one empty space). Players want hints when stuck.

**Problem Characteristics:**
- **State Space**: Each configuration of tiles is a state
- **Goal**: Reach the solved configuration
- **Constraints**:
  - State space is enormous (over 10 trillion possible configurations)
  - Only 4 moves possible from each state (up, down, left, right)
  - Must find a solution, but doesn't need to be shortest
  - Limited memory (mobile device)
  - Need to provide hint within 2-3 seconds
- **Priority**: Find ANY solution quickly with minimal memory

**Additional Information:**
- Good heuristics exist (Manhattan distance, misplaced tiles)
- Solution depth can be 50+ moves
- Some puzzles are unsolvable (not all configurations can reach goal)

**Your Task:**
- **Which algorithm would you choose?** [Your answer]
- **Justification** (150-200 words)
- **Why NOT the other algorithms?** (50-75 words each)

---

## Scenario 4: Social Network Connection Finder

**Context:**
A social media platform wants to implement a "Degrees of Separation" feature that shows how two users are connected through mutual friends.

**Problem Characteristics:**
- **Graph Structure**: Undirected social network graph
- **Goal**: Find ANY connection path between two users
- **Constraints**:
  - Network is huge: millions of users
  - Average user has 200-300 connections
  - Paths are typically short (3-4 degrees of separation)
  - Users want fast responses (under 1 second)
  - Don't need the shortest path, just want to show "how you're connected"
  - Memory is limited (can't load entire graph)
- **Priority**: Speed over optimality

**Additional Information:**
- Most connections are found within 4-5 hops
- No good heuristic available (can't estimate distance between users)
- If path exists, it's usually short
- If no path exists, we need to know that too

**Your Task:**
- **Which algorithm would you choose?** [Your answer]
- **Justification** (150-200 words)
- **Why NOT the other algorithms?** (50-75 words each)

---

### Part 3: Comparative Analysis (30 minutes)

Answer the following questions based on your analysis of all four scenarios:

**Question 1: Informed vs. Uninformed Search (100-150 words)**
- In which scenarios were informed search methods (A*, Greedy) better than uninformed methods (BFS, DFS)?
- What problem characteristics favor informed search?
- When might uninformed search be preferable despite being "blind"?

**Question 2: Optimality vs. Speed Trade-off (100-150 words)**
- In which scenarios did you prioritize finding the optimal solution?
- In which scenarios was speed more important than optimality?
- How did this trade-off influence your algorithm choice?

**Question 3: Real-World Considerations (100-150 words)**
- How do memory constraints affect algorithm selection?
- How does problem size (graph size) influence your choice?
- What role do heuristics play in making informed search practical?

**Question 4: Your Own Scenario (150-200 words)**
- Describe a problem from your engineering discipline where search algorithms could be applied
- What would you be searching for?
- Which algorithm would be most appropriate and why?
- What are the key constraints and priorities?

---

### Part 4: Critical Thinking (10 minutes)

Choose **ONE** scenario where your algorithm choice was most difficult. Explain:

1. What made this decision challenging? (50 words)
2. What was your second-choice algorithm and why didn't you choose it? (75 words)
3. Under what changed conditions would you choose differently? (75 words)

---

## Deliverables

Submit **ONE document** (PDF) containing:

1. **Algorithm Review Table** (from Part 1)
   - Completed comparison table
   - Brief explanations for each algorithm

2. **Four Scenario Analyses** (from Part 2)
   - Each scenario should have:
     - Your algorithm choice clearly stated
     - Detailed justification (150-200 words)
     - Explanation of why other algorithms aren't suitable (3 × 50-75 words)

3. **Comparative Analysis** (from Part 3)
   - Answers to all 4 questions
   - Total: ~500-650 words

4. **Critical Thinking** (from Part 4)
   - Analysis of your most difficult decision
   - ~200 words total

**Total Length: 6-8 pages**

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Algorithm Review Table** | Complete, accurate, insightful | Complete, mostly accurate | Basic completion | Incomplete or inaccurate | /10 |
| **Scenario 1 Analysis** | Excellent choice with strong justification | Good choice, solid reasoning | Reasonable choice, basic reasoning | Poor choice or weak reasoning | /15 |
| **Scenario 2 Analysis** | Excellent choice with strong justification | Good choice, solid reasoning | Reasonable choice, basic reasoning | Poor choice or weak reasoning | /15 |
| **Scenario 3 Analysis** | Excellent choice with strong justification | Good choice, solid reasoning | Reasonable choice, basic reasoning | Poor choice or weak reasoning | /15 |
| **Scenario 4 Analysis** | Excellent choice with strong justification | Good choice, solid reasoning | Reasonable choice, basic reasoning | Poor choice or weak reasoning | /15 |
| **Comparative Analysis** | Thoughtful, demonstrates deep understanding | Good insights and connections | Basic understanding | Superficial or incomplete | /15 |
| **Critical Thinking** | Sophisticated analysis of trade-offs | Good consideration of alternatives | Basic analysis | Weak or missing | /10 |
| **Writing Quality** | Clear, well-organized, professional | Good clarity and organization | Adequate communication | Unclear or disorganized | /5 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

### Analyzing Problems
1. **Identify the goal**: What are you trying to find?
2. **Understand the graph**: Directed? Weighted? How big?
3. **Check for heuristics**: Is there a way to estimate distance to goal?
4. **Consider constraints**: Memory? Time? Optimality required?
5. **Prioritize criteria**: What matters most for this specific problem?

### Writing Strong Justifications
**Good Justification:**
> "BFS is ideal for this problem because it guarantees finding the shortest path, which is critical for the course prerequisite checker. Since the prerequisite graph is relatively small (~200 courses) and acyclic, BFS's O(b^d) space complexity is manageable. The level-by-level exploration ensures we find the minimum prerequisite chain, providing students with the most efficient path to their target course. The completeness guarantee is essential because missing a prerequisite would cause registration errors."

**Weak Justification:**
> "BFS is good because it searches everything and finds the answer. It works well for graphs and is a popular algorithm."

**What makes it strong?**
- Specific problem characteristics mentioned
- Connects algorithm properties to problem needs
- Discusses trade-offs explicitly
- Shows understanding of complexity

### Common Mistakes to Avoid
- **Don't just describe the algorithm** - explain WHY it fits THIS problem
- **Don't ignore trade-offs** - acknowledge drawbacks even for your chosen algorithm
- **Don't be vague** - use specific problem details in your reasoning
- **Don't forget to eliminate other options** - explain why you didn't choose them
- **Don't confuse complexity** - O(b^d) vs. O(bd) matters!

---

## Algorithm Quick Reference

### Breadth-First Search (BFS)
- **Strategy**: Explore all neighbors before going deeper
- **Data Structure**: Queue (FIFO)
- **Strengths**: Finds shortest path, complete
- **Weaknesses**: High memory usage for large graphs
- **Best For**: Shortest path in unweighted graphs, small to medium graphs

### Depth-First Search (DFS)
- **Strategy**: Explore as deep as possible before backtracking
- **Data Structure**: Stack (LIFO)
- **Strengths**: Low memory usage, explores deep paths
- **Weaknesses**: Not optimal, can get stuck in deep paths
- **Best For**: Memory-constrained problems, exploring all paths

### A* Algorithm
- **Strategy**: Use f(n) = g(n) + h(n) to prioritize nodes
- **Data Structure**: Priority queue
- **Strengths**: Optimal (with admissible heuristic), efficient
- **Weaknesses**: Requires good heuristic, higher memory than DFS
- **Best For**: Pathfinding with heuristics, needs optimal solution

### Greedy Best-First Search
- **Strategy**: Use only h(n) heuristic to prioritize
- **Data Structure**: Priority queue
- **Strengths**: Fast, follows promising paths
- **Weaknesses**: Not optimal, not always complete
- **Best For**: Quick solutions when optimality not required

**Key Terms:**
- **g(n)**: Actual cost from start to node n
- **h(n)**: Estimated cost from node n to goal (heuristic)
- **f(n)**: Total estimated cost through node n

---

## Resources

- Session 11 lecture notes
- Introduction to Algorithms (Cormen et al.) - Chapter 22 (Graph Algorithms)
- AI: A Modern Approach (Russell & Norvig) - Chapter 3 (Search)
- Visualizations:
  - Pathfinding Visualizer: https://qiao.github.io/PathFinding.js/visual/
  - Algorithm Visualizer: https://algorithm-visualizer.org/

---

## Example Analysis (for reference only)

**Scenario:** Robot navigating a warehouse to pick items

**Algorithm Choice:** A*

**Justification:**
"A* is optimal for warehouse robot navigation because it combines the benefits of guaranteed shortest path (like BFS) with the efficiency of heuristic guidance. The warehouse environment provides a clear heuristic (Euclidean distance to target), and finding the shortest path minimizes both time and battery usage. Unlike Greedy search, A* won't sacrifice optimality for speed, which is important for efficiency. Unlike BFS, A* uses the heuristic to avoid exploring unnecessary areas. The warehouse graph (~1000 locations) is small enough that A*'s memory requirements are manageable, and the O(b^d) complexity is acceptable given the importance of optimal paths for operational efficiency."

**Why NOT Greedy?**
"Greedy might find suboptimal paths, causing the robot to travel further and waste battery. In a warehouse with obstacles and aisles, the straight-line heuristic can be misleading, and Greedy would follow it blindly without considering actual path cost."

---

## Frequently Asked Questions

**Q: Is there always one "correct" algorithm for each scenario?**
A: Not always! Sometimes multiple algorithms could work. Your justification is more important than the specific choice.

**Q: Can I suggest using multiple algorithms together?**
A: Yes, if you justify it well! For example, using DFS for initial exploration then A* for optimization.

**Q: What if I disagree with the problem characteristics?**
A: State your assumptions clearly and analyze based on them.

**Q: Do I need to calculate exact complexity?**
A: No, but you should understand relative complexity (which is faster/uses less memory).

**Q: Can I use algorithms not in the main four?**
A: Stick to BFS, DFS, A*, and Greedy for consistency, but you can mention others in your discussion.

---

## Connection to Other Assignments

- **Activity 3 (Prolog)**: You've been working with course prerequisite graphs - now you're analyzing how to search them efficiently!
- **This Activity #4 (DFS Implementation)**: You'll implement one of these algorithms in Python
- **Real-World**: These concepts apply to robotics, game AI, route planning, and network analysis

---

**Due Date:** Sunday, March 1st, 2026 by midnight
**Submission:** Brightspace

---

Good luck! Remember: there's no single "right" answer, but there are well-reasoned answers and poorly-reasoned answers. Focus on demonstrating your understanding of algorithm trade-offs and problem characteristics.

**Think like an engineer**: What constraints matter? What are you optimizing for? What trade-offs are you willing to make?
