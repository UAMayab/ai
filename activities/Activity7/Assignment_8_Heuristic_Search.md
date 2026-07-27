# Assignment 8: Heuristic Search Performance Analysis
**Session 14 - Heuristic Search (Greedy Best-First)**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand how Greedy Best-First Search uses heuristics to guide search
2. Implement and measure performance of heuristic search algorithms
3. Compare informed search (heuristic) vs uninformed search (BFS)
4. Analyze the impact of heuristic functions on search efficiency
5. Evaluate trade-offs between optimality and performance

---

## Background

While Breadth-First Search (BFS) explores graphs systematically without any guidance, **Greedy Best-First Search** uses a **heuristic function** to make informed decisions about which nodes to explore next.

### Key Concepts:

**Heuristic Function h(n):**
- Estimates how "promising" a node is
- Guides search toward likely solutions
- Lower values = higher priority

**Greedy Best-First Search:**
- Always explores the most promising node next (based on h(n))
- Uses a priority queue instead of FIFO queue
- Can find solutions faster than BFS
- However, may not explore all nodes (unlike BFS)

**Formula:**
```
f(n) = h(n)
```
Where h(n) estimates distance/cost to goal

**Compare to A*:**
```
f(n) = g(n) + h(n)
```
Where g(n) = cost so far, h(n) = estimated remaining cost

In this assignment, you'll implement Greedy Best-First Search and compare its performance to BFS from Assignment 7.

---

## Prerequisites

- Completed Assignment 7 (BFS Performance Analysis)
- Your BFS performance results from Assignment 7
- Python 3.x with matplotlib
- Understanding of heuristic search from Session 14

---

## Provided Materials

You are provided with:

1. **Same graph files as Assignment 7**:
   - `graph_small.json` (500 nodes)
   - `graph_medium.json` (3,000 nodes)
   - `graph_large.json` (10,000 nodes)

2. **greedy_search.py** - Complete Greedy Best-First Search implementation with heuristic function

3. **bfs_search.py** - For comparison

---

## Understanding the Heuristic Function

The provided heuristic function in `greedy_search.py` works as follows:

### For Spatial Properties (type, region):
```python
# Calculate center of mass for all nodes matching the criteria
avg_x = average x-coordinate of matching nodes
avg_y = average y-coordinate of matching nodes

# Heuristic = Euclidean distance from current node to this center
h(n) = sqrt((node.x - avg_x)² + (node.y - avg_y)²)
```

**Intuition:** Nodes closer to the "center" of matching nodes are explored first.

### For Numerical Properties (capacity, priority):
```python
# Heuristic = absolute difference from target value
h(n) = |node.capacity - target_capacity|
```

**Intuition:** Nodes with values closer to the target are explored first.

This heuristic is **admissible** (never overestimates) and guides the search effectively.

---

## Assignment Instructions

### Part 1: Understanding Greedy Best-First Search (20 minutes)

#### Step 1: Review the Implementation

Open `greedy_search.py` and study the key differences from BFS:

**BFS uses a FIFO queue:**
```python
queue = deque([start_node_id])
current_node_id = queue.popleft()  # Always take the oldest
queue.append(neighbor_id)
```

**Greedy uses a priority queue (min-heap):**
```python
priority_queue = [(heuristic_value, node_id)]
_, current_node_id = heapq.heappop(priority_queue)  # Take lowest heuristic
heapq.heappush(priority_queue, (heuristic, neighbor_id))
```

#### Step 2: Test Greedy Search

Run the greedy search implementation:

```bash
# Search for warehouses
python greedy_search.py small type warehouse

# Search for north region nodes
python greedy_search.py medium region north

# Search for high-capacity nodes
python greedy_search.py large capacity_min 3000
```

**Questions to answer (in your report):**
1. How does the heuristic guide the search?
2. What data structure does Greedy search use? Why?
3. Does Greedy search explore nodes in the same order as BFS?

---

### Part 2: Performance Measurement (40 minutes)

Measure Greedy Best-First Search performance and compare to BFS.

#### Step 1: Create Performance Measurement Script

Create `greedy_performance.py`:

```python
"""
Greedy Best-First Search Performance Measurement
=================================================
Measures Greedy search performance and compares to BFS.
"""

import json
import time
import statistics
from greedy_search import load_graph, greedy_search_all_components
from bfs_search import bfs_search_all_components


def measure_greedy_performance(graph_size, search_property, search_value, num_runs=10):
    """
    Measure Greedy Best-First Search performance over multiple runs.
    """
    filename = f"graph_{graph_size}.json"
    graph = load_graph(filename)

    times = []
    nodes_explored_list = []
    found_nodes_list = []

    print(f"\nRunning Greedy Best-First Search on {graph_size} graph ({num_runs} runs)...")
    print(f"Search: {search_property} = {search_value}")

    for run in range(num_runs):
        found_nodes, nodes_explored, time_taken = greedy_search_all_components(
            graph, search_property, search_value
        )

        times.append(time_taken)
        nodes_explored_list.append(nodes_explored)
        found_nodes_list.append(len(found_nodes))

        print(f"  Run {run+1}/{num_runs}: {time_taken:.6f} seconds")

    return {
        "graph_size": graph_size,
        "num_nodes": graph["metadata"]["num_nodes"],
        "num_edges": graph["metadata"]["num_edges"],
        "avg_time": statistics.mean(times),
        "std_time": statistics.stdev(times) if len(times) > 1 else 0,
        "min_time": min(times),
        "max_time": max(times),
        "nodes_explored": nodes_explored_list[0],
        "nodes_found": found_nodes_list[0]
    }


def measure_bfs_performance(graph_size, search_property, search_value, num_runs=10):
    """
    Measure BFS performance for comparison.
    """
    filename = f"graph_{graph_size}.json"
    graph = load_graph(filename)

    times = []
    nodes_explored_list = []

    print(f"\nRunning BFS on {graph_size} graph ({num_runs} runs)...")
    print(f"Search: {search_property} = {search_value}")

    for run in range(num_runs):
        found_nodes, nodes_explored, time_taken = bfs_search_all_components(
            graph, search_property, search_value
        )

        times.append(time_taken)
        nodes_explored_list.append(nodes_explored)

        print(f"  Run {run+1}/{num_runs}: {time_taken:.6f} seconds")

    return {
        "graph_size": graph_size,
        "avg_time": statistics.mean(times),
        "nodes_explored": nodes_explored_list[0]
    }


def main():
    """
    Compare Greedy Best-First Search and BFS performance.
    """
    # Define search criteria
    search_property = "type"
    search_value = "warehouse"

    print("="*70)
    print("GREEDY BEST-FIRST SEARCH vs BFS PERFORMANCE COMPARISON")
    print("="*70)

    greedy_results = []
    bfs_results = []

    # Measure both algorithms on each graph size
    for size in ["small", "medium", "large"]:
        print(f"\n{'='*70}")
        print(f"TESTING: {size.upper()} GRAPH")
        print('='*70)

        greedy_result = measure_greedy_performance(size, search_property, search_value, num_runs=10)
        bfs_result = measure_bfs_performance(size, search_property, search_value, num_runs=10)

        greedy_results.append(greedy_result)
        bfs_results.append(bfs_result)

    # Display comparison
    print("\n" + "="*70)
    print("PERFORMANCE COMPARISON SUMMARY")
    print("="*70)

    for greedy, bfs in zip(greedy_results, bfs_results):
        speedup = bfs["avg_time"] / greedy["avg_time"]
        nodes_ratio = bfs["nodes_explored"] / greedy["nodes_explored"]

        print(f"\nGraph Size: {greedy['graph_size'].upper()}")
        print(f"  Nodes: {greedy['num_nodes']:,}")
        print(f"  Edges: {greedy['num_edges']:,}")
        print(f"\n  BFS Time:    {bfs['avg_time']:.6f} seconds")
        print(f"  Greedy Time: {greedy['avg_time']:.6f} seconds")
        print(f"  Speedup:     {speedup:.2f}x")
        print(f"\n  BFS Nodes Explored:    {bfs['nodes_explored']:,}")
        print(f"  Greedy Nodes Explored: {greedy['nodes_explored']:,}")
        print(f"  Exploration Ratio:     {nodes_ratio:.2f}x")

    # Save results
    comparison_data = {
        "greedy_results": greedy_results,
        "bfs_results": bfs_results
    }

    with open("search_comparison_results.json", "w") as f:
        json.dump(comparison_data, f, indent=2)

    print("\n" + "="*70)
    print("Results saved to search_comparison_results.json")
    print("="*70)


if __name__ == "__main__":
    main()
```

#### Step 2: Run Performance Comparison

```bash
python greedy_performance.py
```

---

### Part 3: Comparative Visualization (30 minutes)

Create plots comparing Greedy Best-First Search and BFS.

#### Create Comparison Plotting Script

Create `plot_search_comparison.py`:

```python
"""
Search Algorithm Comparison Visualization
==========================================
Creates plots comparing Greedy Best-First Search and BFS.
"""

import json
import matplotlib.pyplot as plt
import numpy as np


def load_results():
    """Load comparison results from JSON file."""
    with open("search_comparison_results.json", "r") as f:
        return json.load(f)


def plot_time_comparison(data):
    """
    Compare running times of both algorithms.
    """
    greedy_results = data["greedy_results"]
    bfs_results = data["bfs_results"]

    sizes = [r["graph_size"] for r in greedy_results]
    greedy_times = [r["avg_time"] for r in greedy_results]
    bfs_times = [r["avg_time"] for r in bfs_results]

    x = np.arange(len(sizes))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))

    bars1 = ax.bar(x - width/2, bfs_times, width, label='BFS (Uninformed)',
                   color='#3498db', alpha=0.8)
    bars2 = ax.bar(x + width/2, greedy_times, width, label='Greedy (Heuristic)',
                   color='#e74c3c', alpha=0.8)

    ax.set_xlabel('Graph Size', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Time (seconds)', fontsize=12, fontweight='bold')
    ax.set_title('Running Time Comparison: BFS vs Greedy Best-First Search',
                fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([s.capitalize() for s in sizes])
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.4f}s', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig("search_time_comparison.png", dpi=300)
    print("Saved: search_time_comparison.png")
    plt.close()


def plot_speedup(data):
    """
    Plot speedup achieved by Greedy over BFS.
    """
    greedy_results = data["greedy_results"]
    bfs_results = data["bfs_results"]

    sizes = [r["graph_size"] for r in greedy_results]
    num_nodes = [r["num_nodes"] for r in greedy_results]
    speedups = [bfs["avg_time"] / greedy["avg_time"]
               for bfs, greedy in zip(bfs_results, greedy_results)]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(sizes, speedups, color=['#2ecc71', '#f39c12', '#9b59b6'], alpha=0.7)

    ax.set_xlabel('Graph Size', fontsize=12, fontweight='bold')
    ax.set_ylabel('Speedup Factor', fontsize=12, fontweight='bold')
    ax.set_title('Greedy Best-First Search Speedup over BFS',
                fontsize=14, fontweight='bold')
    ax.set_xticklabels([s.capitalize() for s in sizes])

    # Add horizontal line at 1.0 (no speedup)
    ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='No speedup')

    # Add value labels
    for i, (bar, speedup, nodes) in enumerate(zip(bars, speedups, num_nodes)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{speedup:.2f}x\n({nodes:,} nodes)',
               ha='center', va='bottom', fontsize=10)

    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("greedy_speedup.png", dpi=300)
    print("Saved: greedy_speedup.png")
    plt.close()


def plot_nodes_explored(data):
    """
    Compare number of nodes explored by both algorithms.
    """
    greedy_results = data["greedy_results"]
    bfs_results = data["bfs_results"]

    sizes = [r["graph_size"] for r in greedy_results]
    greedy_explored = [r["nodes_explored"] for r in greedy_results]
    bfs_explored = [r["nodes_explored"] for r in bfs_results]

    x = np.arange(len(sizes))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))

    bars1 = ax.bar(x - width/2, bfs_explored, width, label='BFS',
                   color='#3498db', alpha=0.8)
    bars2 = ax.bar(x + width/2, greedy_explored, width, label='Greedy',
                   color='#e74c3c', alpha=0.8)

    ax.set_xlabel('Graph Size', fontsize=12, fontweight='bold')
    ax.set_ylabel('Nodes Explored', fontsize=12, fontweight='bold')
    ax.set_title('Nodes Explored: BFS vs Greedy Best-First Search',
                fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([s.capitalize() for s in sizes])
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig("nodes_explored_comparison.png", dpi=300)
    print("Saved: nodes_explored_comparison.png")
    plt.close()


def plot_efficiency_analysis(data):
    """
    Analyze efficiency (time per node) for both algorithms.
    """
    greedy_results = data["greedy_results"]
    bfs_results = data["bfs_results"]

    num_nodes = [r["num_nodes"] for r in greedy_results]
    greedy_efficiency = [r["avg_time"] / r["nodes_explored"] * 1000000
                        for r in greedy_results]  # microseconds per node
    bfs_efficiency = [b["avg_time"] / b["nodes_explored"] * 1000000
                     for b in bfs_results]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(num_nodes, bfs_efficiency, 'o-', linewidth=2, markersize=10,
           color='#3498db', label='BFS')
    ax.plot(num_nodes, greedy_efficiency, 's-', linewidth=2, markersize=10,
           color='#e74c3c', label='Greedy')

    ax.set_xlabel('Number of Nodes', fontsize=12, fontweight='bold')
    ax.set_ylabel('Time per Node Explored (microseconds)', fontsize=12, fontweight='bold')
    ax.set_title('Efficiency: Time per Node Explored', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("efficiency_comparison.png", dpi=300)
    print("Saved: efficiency_comparison.png")
    plt.close()


def main():
    """
    Generate all comparison plots.
    """
    print("="*70)
    print("GENERATING SEARCH ALGORITHM COMPARISON PLOTS")
    print("="*70)
    print()

    data = load_results()

    plot_time_comparison(data)
    plot_speedup(data)
    plot_nodes_explored(data)
    plot_efficiency_analysis(data)

    print()
    print("="*70)
    print("ALL COMPARISON PLOTS GENERATED SUCCESSFULLY")
    print("="*70)


if __name__ == "__main__":
    main()
```

#### Generate Comparison Plots

```bash
python plot_search_comparison.py
```

This creates four PNG files comparing the algorithms.

---

### Part 4: Analysis and Interpretation (30 minutes)

Answer the following questions in your report:

#### Question 1: Algorithm Comparison (200-250 words)
- Which algorithm is faster? By how much?
- Which algorithm explores fewer nodes? Why?
- Do both algorithms find the same number of matching nodes?
- How does the speedup change with graph size?

#### Question 2: Heuristic Effectiveness (200-250 words)
- How does the heuristic function guide the search?
- For which search properties (type, region, capacity) is the heuristic most effective?
- Would a different heuristic function produce different results?
- What makes a heuristic "good"?

#### Question 3: Trade-offs (200-250 words)
- What does Greedy search sacrifice for speed?
- In what scenarios would you choose BFS over Greedy?
- In what scenarios would you choose Greedy over BFS?
- Does Greedy guarantee finding all matching nodes? Why or why not?

#### Question 4: Computational Complexity (150-200 words)
- BFS has complexity O(V + E). What about Greedy Best-First Search?
- Why does Greedy take longer per node but finish faster overall?
- How does using a priority queue affect performance?
- What is the complexity of heap operations?

#### Question 5: Real-World Application (150-200 words)
Imagine you're building a GPS navigation system:
- Would you use BFS or Greedy search? Why?
- What heuristic would you use?
- What if you needed the absolute shortest path?
- How would A* (which combines both) be better?

---

## Deliverables

Submit **ONE ZIP file** containing:

1. **Performance Scripts**
   - `greedy_performance.py`
   - `plot_search_comparison.py`

2. **Results**
   - `search_comparison_results.json`
   - All four PNG comparison plot files

3. **Written Report (PDF)**
   - Introduction (building on Assignment 7)
   - Methodology (how you compared the algorithms)
   - Results section with all plots embedded
   - Answers to all 5 analysis questions
   - Comparison table summarizing key differences
   - Conclusion about when to use each algorithm
   - 5-7 pages total

4. **Screenshots**
   - Screenshot of running `greedy_performance.py`
   - Screenshot of one Greedy search execution

**Filename:** `LastName_Assignment8_HeuristicSearch.zip`

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Performance Scripts** | Both scripts work perfectly, clean code | Scripts work with minor issues | Scripts have some problems | Scripts don't work properly | /20 |
| **Measurements** | Accurate comparison, 10+ runs each | Good comparison, 5-9 runs | Basic comparison | Incomplete measurements | /15 |
| **Comparison Plots** | All 4 plots clear, insightful | 3-4 plots, good quality | 2 plots, basic quality | Poor or missing plots | /20 |
| **Analysis Questions** | Excellent insights, deep comparison | Good analysis with detail | Basic answers | Superficial or incomplete | /25 |
| **Algorithm Understanding** | Demonstrates mastery of both | Good understanding | Basic understanding | Limited understanding | /10 |
| **Report Quality** | Professional, well-integrated with Assignment 7 | Good organization | Basic structure | Poor organization | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

### Understanding the Difference
```
BFS:  Always explores closest nodes first (by depth)
      No knowledge of where goal might be
      Explores everything systematically

Greedy: Explores most promising nodes first (by heuristic)
        Uses knowledge to guide search
        Can skip unpromising areas
```

### Key Comparison Points
1. **Speed**: Which finishes faster?
2. **Nodes Explored**: Which explores fewer?
3. **Completeness**: Does each find all solutions?
4. **Optimality**: Does each find the best solution?
5. **Memory**: Which uses more memory?

### Common Observations
- Greedy is usually faster for finding first solution
- BFS explores more nodes but systematically
- Heuristic quality matters greatly
- Per-node time may differ due to heap operations

---

## Connection to Assignment 7

This assignment builds directly on Assignment 7:

**From Assignment 7 you learned:**
- How BFS works
- BFS performance characteristics
- O(V + E) complexity in practice

**In this assignment you're learning:**
- How heuristics improve search
- Trade-offs between informed and uninformed search
- When to use which algorithm

**Together they show:**
- The value of problem knowledge (heuristics)
- Performance vs optimality trade-offs
- Different algorithms for different scenarios

---

## Resources

- Session 14 lecture notes
- Assignment 7 BFS results (for comparison)
- A* Algorithm: https://www.redblobgames.com/pathfinding/a-star/introduction.html
- Python heapq documentation: https://docs.python.org/3/library/heapq.html
- Heuristic Functions: https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

---

## Frequently Asked Questions

**Q: Should Greedy always be faster than BFS?**
A: Usually yes, if the heuristic is good. But per-node overhead might be higher.

**Q: Do both algorithms find the same nodes?**
A: Yes! Both find all matching nodes, but in different orders and exploring different total nodes.

**Q: Why does Greedy explore ALL nodes sometimes?**
A: The provided implementation searches all components. Pure greedy might stop early.

**Q: Can I modify the heuristic function?**
A: For the assignment, use the provided heuristic. But in your analysis, you can discuss alternatives!

**Q: What if Greedy is slower than BFS?**
A: Document this! Explain why (graph structure, heuristic quality, heap overhead).

---

**Due Date:** Saturday, March 8th, 2026 by midnight
**Submission:** Brightspace (upload ZIP file)

---

Remember: The goal is to understand **why** heuristics help and **when** to use informed vs uninformed search. Don't just measure - **analyze and explain**!

**Think critically:** Does your heuristic actually help? How much? Why? What could make it better? 🎯🔍
