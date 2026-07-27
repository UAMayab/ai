

# Assignment 7: BFS Performance Analysis
**Session 13 - Breadth-First Search**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand how Breadth-First Search (BFS) explores graphs
2. Analyze the performance of BFS on graphs of different sizes
3. Measure and compare running times across different graph scales
4. Create visualizations of algorithm performance
5. Interpret computational complexity in practice

---

## Background

Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores nodes level-by-level, visiting all neighbors at the current depth before moving deeper. BFS is particularly important because:

- It guarantees finding the shortest path in unweighted graphs
- It explores the graph systematically and completely
- It has well-defined time complexity: **O(V + E)** where V = vertices, E = edges

In this assignment, you'll analyze how BFS performs on graphs of different sizes, measuring actual running times and comparing them to theoretical predictions.

---

## Prerequisites

- Python 3.x installed
- Basic command line knowledge
- Understanding of BFS concept from Session 13
- Libraries: `matplotlib` for plotting (install with: `pip install matplotlib`)

---

## Provided Materials

You are provided with three pre-generated graph files and a working BFS implementation:

### Graph Files (JSON format):
1. **graph_small.json** - 500 nodes, ~3,000 edges
2. **graph_medium.json** - 3,000 nodes, ~38,000 edges
3. **graph_large.json** - 10,000 nodes, ~126,000 edges

### Python Files:
1. **bfs_search.py** - Complete BFS implementation
2. **graph_generator.py** - Graph generator (for reference)

### Graph Structure: Transportation/Logistics Network

The graphs represent a transportation network where:
- **Nodes** represent distribution centers, warehouses, retail stores, hubs, and depots
- **Edges** represent shipping routes (directed, with weights representing distances)

**Node Properties:**
- `id`: Unique identifier (e.g., "node_42")
- `name`: Human-readable name (e.g., "warehouse_north_42")
- `type`: One of: warehouse, distribution_center, retail_store, hub, depot
- `region`: One of: north, south, east, west, central
- `capacity`: Storage capacity (100-5000 units)
- `priority`: Priority level (1-5)
- `coordinates`: x,y position for spatial calculations

**Edge Properties:**
- `source`: Source node ID
- `target`: Target node ID
- `weight`: Distance/cost (integer)

---

## Assignment Instructions

### Part 1: Understanding the BFS Implementation (20 minutes)

#### Step 1: Review the Code

Open `bfs_search.py` and read through the implementation carefully. The file contains:

1. **Graph loading function** - Reads JSON graph files
2. **Adjacency list builder** - Converts graph to efficient format
3. **Search criteria matcher** - Checks if nodes match search properties
4. **BFS search function** - Main algorithm implementation
5. **Results display** - Formatted output

**Key Algorithm Components:**
```python
queue = deque([start_node_id])  # FIFO queue for BFS
visited = set([start_node_id])   # Track visited nodes

while queue:
    current_node_id = queue.popleft()  # Dequeue (FIFO)
    nodes_explored += 1

    neighbors = adjacency_list.get(current_node_id, [])

    for neighbor_id in neighbors:
        if neighbor_id not in visited:
            visited.add(neighbor_id)
            queue.append(neighbor_id)  # Enqueue neighbors
```

#### Step 2: Test the Implementation

Run the BFS implementation with different search criteria:

```bash
# Search for warehouses in small graph
python bfs_search.py small type warehouse

# Search for nodes in the north region (medium graph)
python bfs_search.py medium region north

# Search for high-capacity nodes (large graph)
python bfs_search.py large capacity_min 3000
```

**Questions to answer (in your report):**
1. How many nodes of type "warehouse" exist in the small graph?
2. How does BFS explore the graph? (level-by-level? depth-first?)
3. What data structure does BFS use? Why is it important?

---

### Part 2: Performance Measurement (40 minutes)

Now you'll measure BFS performance across the three graph sizes.

#### Step 1: Create Performance Measurement Script

Create a file called `bfs_performance.py`:

```python
"""
BFS Performance Measurement Script
===================================
Measures BFS running time across multiple runs and graph sizes.
"""

import json
import time
import statistics
from bfs_search import load_graph, bfs_search_all_components


def measure_bfs_performance(graph_size, search_property, search_value, num_runs=10):
    """
    Measure BFS performance over multiple runs.

    Args:
        graph_size (str): 'small', 'medium', or 'large'
        search_property (str): Property to search
        search_value (str): Value to search for
        num_runs (int): Number of times to run the search

    Returns:
        dict: Performance statistics
    """
    filename = f"graph_{graph_size}.json"
    graph = load_graph(filename)

    times = []
    nodes_explored_list = []
    found_nodes_list = []

    print(f"\nRunning BFS on {graph_size} graph ({num_runs} runs)...")
    print(f"Search: {search_property} = {search_value}")

    for run in range(num_runs):
        found_nodes, nodes_explored, time_taken = bfs_search_all_components(
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


def main():
    """
    Run performance measurements on all graph sizes.
    """
    # Define search criteria (same for all graphs for fair comparison)
    search_property = "type"
    search_value = "warehouse"

    print("="*70)
    print("BFS PERFORMANCE ANALYSIS")
    print("="*70)

    results = []

    # Measure performance on each graph size
    for size in ["small", "medium", "large"]:
        result = measure_bfs_performance(size, search_property, search_value, num_runs=10)
        results.append(result)

    # Display summary
    print("\n" + "="*70)
    print("PERFORMANCE SUMMARY")
    print("="*70)

    for result in results:
        print(f"\nGraph Size: {result['graph_size'].upper()}")
        print(f"  Nodes: {result['num_nodes']:,}")
        print(f"  Edges: {result['num_edges']:,}")
        print(f"  Average Time: {result['avg_time']:.6f} seconds")
        print(f"  Std Dev: {result['std_time']:.6f} seconds")
        print(f"  Min Time: {result['min_time']:.6f} seconds")
        print(f"  Max Time: {result['max_time']:.6f} seconds")
        print(f"  Nodes Explored: {result['nodes_explored']:,}")
        print(f"  Nodes Found: {result['nodes_found']}")

    # Save results to JSON
    with open("bfs_performance_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "="*70)
    print("Results saved to bfs_performance_results.json")
    print("="*70)


if __name__ == "__main__":
    main()
```

#### Step 2: Run Performance Measurements

Execute your performance measurement script:

```bash
python bfs_performance.py
```

This will run BFS 10 times on each graph size and calculate average times.

**Expected output:** A JSON file `bfs_performance_results.json` with timing data.

---

### Part 3: Data Visualization (30 minutes)

Create visualizations to analyze BFS performance.

#### Create Plotting Script

Create a file called `plot_bfs_performance.py`:

```python
"""
BFS Performance Visualization
==============================
Creates plots showing BFS performance across graph sizes.
"""

import json
import matplotlib.pyplot as plt


def load_results():
    """Load performance results from JSON file."""
    with open("bfs_performance_results.json", "r") as f:
        return json.load(f)


def plot_time_vs_size(results):
    """
    Plot average running time vs graph size.
    """
    sizes = [r["graph_size"] for r in results]
    num_nodes = [r["num_nodes"] for r in results]
    avg_times = [r["avg_time"] for r in results]
    std_times = [r["std_time"] for r in results]

    plt.figure(figsize=(10, 6))

    # Bar plot with error bars
    plt.bar(sizes, avg_times, yerr=std_times, capsize=10,
            color=['#3498db', '#e74c3c', '#2ecc71'], alpha=0.7)

    plt.xlabel("Graph Size", fontsize=12, fontweight='bold')
    plt.ylabel("Average Time (seconds)", fontsize=12, fontweight='bold')
    plt.title("BFS Running Time vs Graph Size", fontsize=14, fontweight='bold')

    # Add node count labels
    for i, (size, nodes, time) in enumerate(zip(sizes, num_nodes, avg_times)):
        plt.text(i, time, f"{nodes:,} nodes\n{time:.4f}s",
                ha='center', va='bottom', fontsize=10)

    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("bfs_time_vs_size.png", dpi=300)
    print("Saved: bfs_time_vs_size.png")
    plt.close()


def plot_time_per_node(results):
    """
    Plot time per node explored.
    """
    sizes = [r["graph_size"] for r in results]
    num_nodes = [r["num_nodes"] for r in results]
    avg_times = [r["avg_time"] for r in results]

    # Calculate time per node
    time_per_node = [t / n * 1000000 for t, n in zip(avg_times, num_nodes)]  # microseconds

    plt.figure(figsize=(10, 6))

    plt.plot(num_nodes, time_per_node, 'o-', linewidth=2, markersize=10,
            color='#9b59b6', label='Time per node')

    plt.xlabel("Number of Nodes", fontsize=12, fontweight='bold')
    plt.ylabel("Time per Node (microseconds)", fontsize=12, fontweight='bold')
    plt.title("BFS Efficiency: Time per Node", fontsize=14, fontweight='bold')

    # Add value labels
    for nodes, time in zip(num_nodes, time_per_node):
        plt.text(nodes, time, f"{time:.2f} μs", ha='center', va='bottom', fontsize=10)

    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("bfs_time_per_node.png", dpi=300)
    print("Saved: bfs_time_per_node.png")
    plt.close()


def plot_scalability(results):
    """
    Plot nodes explored vs graph size to show linear scaling.
    """
    num_nodes = [r["num_nodes"] for r in results]
    num_edges = [r["num_edges"] for r in results]
    avg_times = [r["avg_time"] for r in results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Time vs Nodes
    ax1.plot(num_nodes, avg_times, 'o-', linewidth=2, markersize=10,
            color='#e67e22', label='Measured time')
    ax1.set_xlabel("Number of Nodes (V)", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Time (seconds)", fontsize=12, fontweight='bold')
    ax1.set_title("BFS Time Complexity: O(V + E)", fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Plot 2: Time vs (V + E)
    v_plus_e = [v + e for v, e in zip(num_nodes, num_edges)]
    ax2.plot(v_plus_e, avg_times, 'o-', linewidth=2, markersize=10,
            color='#16a085', label='Measured time')
    ax2.set_xlabel("V + E (Nodes + Edges)", fontsize=12, fontweight='bold')
    ax2.set_ylabel("Time (seconds)", fontsize=12, fontweight='bold')
    ax2.set_title("BFS Linear Scaling: Time vs (V + E)", fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.savefig("bfs_scalability.png", dpi=300)
    print("Saved: bfs_scalability.png")
    plt.close()


def main():
    """
    Generate all plots.
    """
    print("="*70)
    print("GENERATING BFS PERFORMANCE PLOTS")
    print("="*70)
    print()

    results = load_results()

    plot_time_vs_size(results)
    plot_time_per_node(results)
    plot_scalability(results)

    print()
    print("="*70)
    print("ALL PLOTS GENERATED SUCCESSFULLY")
    print("="*70)


if __name__ == "__main__":
    main()
```

#### Generate Plots

```bash
python plot_bfs_performance.py
```

This will create three PNG files:
1. `bfs_time_vs_size.png` - Bar chart of running times
2. `bfs_time_per_node.png` - Efficiency analysis
3. `bfs_scalability.png` - Complexity verification

---

### Part 4: Analysis and Interpretation (30 minutes)

Answer the following questions in your report:

#### Question 1: Performance Scaling (150-200 words)
- How does BFS running time change as graph size increases?
- Is the relationship linear, quadratic, or something else?
- Does your data match the theoretical O(V + E) complexity? Explain.

#### Question 2: Graph Structure Impact (150-200 words)
- The medium graph has 6x more nodes than small, but how much longer does it take?
- The large graph has 20x more nodes than small. Is the time increase also 20x?
- What factors besides number of nodes affect running time?

#### Question 3: BFS Characteristics (150-200 words)
- Why does BFS explore ALL nodes even when searching for a specific property?
- What are the advantages of BFS's level-by-level exploration?
- In what scenarios would BFS be preferred over other search algorithms?

#### Question 4: Practical Observations (150-200 words)
- Were there variations in running time across the 10 runs? Why?
- How does the number of edges affect performance?
- If you had a graph with 100,000 nodes, estimate how long BFS would take.

#### Question 5: Search Property Comparison (100-150 words)
Run BFS with different search properties (type, region, capacity_min) on the same graph. Do they take different amounts of time? Why or why not?

---

## Deliverables

Submit **ONE ZIP file** containing:

1. **Performance Scripts**
   - `bfs_performance.py` (your measurement script)
   - `plot_bfs_performance.py` (your plotting script)

2. **Results**
   - `bfs_performance_results.json` (timing data)
   - All three PNG plot files

3. **Written Report (PDF)**
   - Introduction (what you're testing)
   - Methodology (how you measured performance)
   - Results section with all three plots embedded
   - Answers to all 5 analysis questions
   - Conclusion summarizing findings
   - 4-6 pages total

4. **Screenshots**
   - Screenshot of running `bfs_performance.py`
   - Screenshot of one successful BFS search

**Filename:** `LastName_Assignment7_BFS.zip`

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Performance Scripts** | Both scripts run correctly, well-structured | Scripts run with minor issues | Scripts have some problems | Scripts don't work | /20 |
| **Measurements** | 10+ runs per size, accurate data collection | 5-9 runs, mostly accurate | <5 runs or inconsistent data | Incomplete measurements | /15 |
| **Plots** | All 3 plots clear, labeled, professional | 2-3 plots, good quality | 1-2 plots, basic quality | Poor or missing plots | /20 |
| **Analysis Questions** | Thorough, insightful answers with data | Good answers with some depth | Basic answers | Superficial or incomplete | /25 |
| **Report Quality** | Well-organized, clear, professional | Good organization | Basic structure | Poor organization | /10 |
| **Understanding** | Demonstrates deep understanding of BFS | Good understanding | Basic understanding | Limited understanding | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

### Performance Measurement
1. **Close other programs** while measuring to reduce noise
2. **Run multiple times** (10+) and average the results
3. **Check consistency** - if times vary wildly, investigate why
4. **Document system specs** (CPU, RAM) in your report

### Creating Plots
1. **Label everything** - axes, title, units
2. **Use appropriate scales** - consider log scale for large ranges
3. **Add data labels** - show exact values on plots
4. **Choose good colors** - accessible, professional
5. **High resolution** - save at 300 dpi minimum

### Writing Analysis
1. **Reference your plots** - "As shown in Figure 1..."
2. **Use specific numbers** - cite actual measurements
3. **Compare to theory** - does O(V+E) match your data?
4. **Be critical** - discuss limitations and sources of error

### Common Issues
- **matplotlib not installed**: `pip install matplotlib`
- **JSON file not found**: Make sure graphs are generated first
- **Import errors**: Ensure all files are in the same directory
- **Slow on large graph**: This is expected! That's what you're measuring

---

## Search Property Reference

You can search for nodes using these properties:

### type
Values: warehouse, distribution_center, retail_store, hub, depot
```bash
python bfs_search.py small type warehouse
```

### region
Values: north, south, east, west, central
```bash
python bfs_search.py medium region north
```

### capacity_min
Value: integer (e.g., 3000)
```bash
python bfs_search.py large capacity_min 3000
```

### priority
Value: 1, 2, 3, 4, or 5
```bash
python bfs_search.py small priority 5
```

---

## Connection to Assignment 8

In Assignment 8, you'll implement **Greedy Best-First Search** (a heuristic search algorithm) and compare its performance to BFS. Save your results from this assignment - you'll need them for comparison!

**Key comparison points:**
- Running time: Which is faster?
- Nodes explored: Which explores fewer nodes?
- Optimality: Which guarantees finding all matches?

---

## Resources

- Session 13 lecture notes
- BFS Algorithm Visualization: https://visualgo.net/en/dfsbfs
- Python heapq documentation: https://docs.python.org/3/library/heapq.html
- matplotlib tutorial: https://matplotlib.org/stable/tutorials/index.html

---

## Frequently Asked Questions

**Q: Do I need to modify bfs_search.py?**
A: No, use it as provided. You only write the measurement and plotting scripts.

**Q: How many runs should I do for averaging?**
A: Minimum 10, but more is better (20-30 gives more stable averages).

**Q: Can I test on different search properties?**
A: Yes! In fact, Question 5 asks you to do this.

**Q: What if the large graph takes too long?**
A: It should take <1 second. If it takes much longer, check your system resources.

**Q: My times are in milliseconds, is that normal?**
A: Yes! Small graph should be <10ms, medium ~100ms, large ~500ms (varies by system).

---

**Due Date:** Saturday, March 8th, 2026 by midnight
**Submission:** Brightspace (upload ZIP file)

---

Good luck! Remember: the goal is not just to measure performance, but to **understand why** BFS performs the way it does and how it relates to the theoretical complexity O(V + E).

**Think scientifically:** Make predictions, measure carefully, analyze critically, and draw evidence-based conclusions! 🔬📊
