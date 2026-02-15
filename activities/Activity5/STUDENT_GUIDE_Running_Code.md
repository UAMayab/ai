# Student Guide: Running BFS and Greedy Search Code
**Assignments 7 & 8 - Complete Setup and Execution Guide**

---

## Table of Contents
1. [Before You Start](#before-you-start)
2. [Environment Setup](#environment-setup)
3. [File Organization](#file-organization)
4. [Assignment 7: Running BFS](#assignment-7-running-bfs)
5. [Assignment 8: Running Greedy Search](#assignment-8-running-greedy-search)
6. [Troubleshooting](#troubleshooting)
7. [Quick Reference](#quick-reference)

---

## Before You Start

### What You'll Need
- Python 3.7 or higher installed
- Basic command line/terminal knowledge
- Text editor or IDE (VS Code, PyCharm, or even Notepad++)
- ~100 MB of free disk space for graph files

### Time Estimates
- Initial setup: 10-15 minutes
- Assignment 7: 2 hours
- Assignment 8: 2 hours

---

## Environment Setup

### Step 1: Check Python Installation

Open your terminal/command prompt and check Python version:

**Windows:**
```bash
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

You should see something like: `Python 3.9.7` or higher.

**If Python is not installed:**
- Windows: Download from https://www.python.org/downloads/
- Mac: Use Homebrew: `brew install python3`
- Linux: `sudo apt-get install python3`

### Step 2: Install Required Libraries

You need `matplotlib` for creating plots.

**Install matplotlib:**

**Windows:**
```bash
pip install matplotlib
```

**Mac/Linux:**
```bash
pip3 install matplotlib
```

**Verify installation:**
```bash
python -c "import matplotlib; print('matplotlib installed successfully!')"
```

If you see the success message, you're ready!

---

## File Organization

### Step 1: Create Project Folder

Create a folder for your assignments:

**Windows:**
```bash
mkdir C:\AI_Assignments
cd C:\AI_Assignments
```

**Mac/Linux:**
```bash
mkdir ~/AI_Assignments
cd ~/AI_Assignments
```

### Step 2: Download/Copy Required Files

Your instructor should provide these files. Place them all in your project folder:

```
AI_Assignments/
├── graph_generator.py          (provided)
├── bfs_search.py               (provided)
├── greedy_search.py            (provided)
├── graph_small.json            (will be generated)
├── graph_medium.json           (will be generated)
└── graph_large.json            (will be generated)
```

**Check you have the three Python files:**
```bash
# Windows
dir *.py

# Mac/Linux
ls *.py
```

You should see:
- `graph_generator.py`
- `bfs_search.py`
- `greedy_search.py`

---

## Assignment 7: Running BFS

### Phase 1: Generate Graph Files (One-time Setup)

**Step 1:** Run the graph generator

```bash
python graph_generator.py
```

**Expected output:**
```
============================================================
GRAPH GENERATION FOR BFS AND HEURISTIC SEARCH ASSIGNMENTS
============================================================

Generating SMALL graph (500 nodes)...
Generating 500 nodes...
Generating edges...
Generated 500 nodes and 3065 edges
Graph saved to graph_small.json

Generating MEDIUM graph (3000 nodes)...
[... similar output ...]

Generating LARGE graph (10000 nodes)...
[... similar output ...]

============================================================
ALL GRAPHS GENERATED SUCCESSFULLY
============================================================
```

**⏱️ Time:** Small: ~1 sec, Medium: ~5 sec, Large: ~15 sec

**Step 2:** Verify graph files were created

```bash
# Windows
dir *.json

# Mac/Linux
ls -lh *.json
```

You should see three JSON files:
- `graph_small.json` (~5 MB)
- `graph_medium.json` (~35 MB)
- `graph_large.json` (~120 MB)

**✅ Checkpoint:** If you have these files, you're ready for both assignments!

---

### Phase 2: Test BFS Search

**Step 1:** Run a simple BFS search on the small graph

```bash
python bfs_search.py small type warehouse
```

**What this does:**
- Searches the **small** graph
- Looks for nodes where **type** equals **warehouse**
- Uses BFS algorithm

**Expected output:**
```
Loading graph from graph_small.json...
Loaded graph with 500 nodes and 3065 edges

Searching for nodes where type = warehouse...

======================================================================
BFS SEARCH RESULTS
======================================================================
Graph: small (500 nodes)
Search Property: type
Search Value: warehouse
Nodes Explored: 500
Nodes Found: 112
Time Taken: 0.001098 seconds
======================================================================

Found 112 matching nodes:
  1. warehouse_central_4 (ID: node_4)
      Type: warehouse, Region: central, Capacity: 1561, Priority: 1
  2. warehouse_east_5 (ID: node_5)
      Type: warehouse, Region: east, Capacity: 2546, Priority: 2
  [... more results ...]
```

**✅ Success!** BFS is working correctly.

**Step 2:** Try different search criteria

Search by region:
```bash
python bfs_search.py small region north
```

Search by minimum capacity:
```bash
python bfs_search.py small capacity_min 3000
```

Search by priority:
```bash
python bfs_search.py small priority 5
```

**Step 3:** Test on larger graphs

Medium graph:
```bash
python bfs_search.py medium type warehouse
```

Large graph (this will take longer!):
```bash
python bfs_search.py large type warehouse
```

**⏱️ Expected times:**
- Small: <0.01 seconds
- Medium: ~0.1 seconds
- Large: ~0.5 seconds

---

### Phase 3: Performance Measurement (Assignment 7)

**Step 1:** Create your performance measurement script

Create a new file called `bfs_performance.py` and copy the code from Assignment 7 instructions (Part 2, Step 1).

**Step 2:** Run performance measurements

```bash
python bfs_performance.py
```

**What this does:**
- Runs BFS 10 times on each graph size
- Measures average time, standard deviation, min, max
- Saves results to `bfs_performance_results.json`

**Expected output:**
```
======================================================================
BFS PERFORMANCE ANALYSIS
======================================================================

Running BFS on small graph (10 runs)...
Search: type = warehouse
  Run 1/10: 0.001045 seconds
  Run 2/10: 0.001023 seconds
  [... more runs ...]

Running BFS on medium graph (10 runs)...
[... similar output ...]

Running BFS on large graph (10 runs)...
[... similar output ...]

======================================================================
PERFORMANCE SUMMARY
======================================================================

Graph Size: SMALL
  Nodes: 500
  Edges: 3,065
  Average Time: 0.001056 seconds
  Std Dev: 0.000023 seconds
  [... more stats ...]
```

**⏱️ Time:** This will take ~2-3 minutes to complete (30 total runs).

**Step 3:** Verify results file

```bash
# Windows
type bfs_performance_results.json

# Mac/Linux
cat bfs_performance_results.json
```

You should see JSON data with timing results.

---

### Phase 4: Create Plots (Assignment 7)

**Step 1:** Create your plotting script

Create a new file called `plot_bfs_performance.py` and copy the code from Assignment 7 instructions (Part 3).

**Step 2:** Generate plots

```bash
python plot_bfs_performance.py
```

**Expected output:**
```
======================================================================
GENERATING BFS PERFORMANCE PLOTS
======================================================================

Saved: bfs_time_vs_size.png
Saved: bfs_time_per_node.png
Saved: bfs_scalability.png

======================================================================
ALL PLOTS GENERATED SUCCESSFULLY
======================================================================
```

**Step 3:** View your plots

The PNG files should now exist in your folder. Open them with any image viewer.

**✅ Assignment 7 Complete!** You now have all data and plots needed.

---

## Assignment 8: Running Greedy Search

### Phase 1: Test Greedy Search

**Step 1:** Run a simple greedy search

```bash
python greedy_search.py small type warehouse
```

**Expected output:**
```
Loading graph from graph_small.json...
Loaded graph with 500 nodes and 3065 edges

Searching for nodes where type = warehouse...
Using Greedy Best-First Search with heuristic guidance...

======================================================================
GREEDY BEST-FIRST SEARCH RESULTS
======================================================================
Graph: small (500 nodes)
Search Property: type
Search Value: warehouse
Nodes Explored: 500
Nodes Found: 112
Time Taken: 0.029433 seconds
======================================================================
```

**Notice:** Greedy finds the same 112 warehouses but takes slightly longer per node (due to heuristic calculation and priority queue overhead).

**Step 2:** Test on different graph sizes

```bash
python greedy_search.py medium type warehouse
python greedy_search.py large type warehouse
```

---

### Phase 2: Compare BFS and Greedy (Assignment 8)

**Step 1:** Create comparison script

Create `greedy_performance.py` from Assignment 8 instructions (Part 2, Step 1).

**Step 2:** Run comparison

```bash
python greedy_performance.py
```

**What this does:**
- Runs BOTH BFS and Greedy on all three graph sizes
- Compares: running time, nodes explored, speedup
- Saves to `search_comparison_results.json`

**Expected output:**
```
======================================================================
GREEDY BEST-FIRST SEARCH vs BFS PERFORMANCE COMPARISON
======================================================================

======================================================================
TESTING: SMALL GRAPH
======================================================================

Running Greedy Best-First Search on small graph (10 runs)...
[... output ...]

Running BFS on small graph (10 runs)...
[... output ...]

[... similar for medium and large ...]

======================================================================
PERFORMANCE COMPARISON SUMMARY
======================================================================

Graph Size: SMALL
  Nodes: 500
  Edges: 3,065

  BFS Time:    0.001056 seconds
  Greedy Time: 0.029145 seconds
  Speedup:     0.04x  ← Note: Greedy might be slower on small graphs!

  BFS Nodes Explored:    500
  Greedy Nodes Explored: 500
  Exploration Ratio:     1.00x
```

**⏱️ Time:** ~5-6 minutes (60 total runs).

**Important Note:** Greedy might be slower than BFS on these complete searches because:
- We're searching for ALL matching nodes (not stopping at first)
- Heuristic calculation has overhead
- Priority queue operations are slower than simple queue

In your analysis, explain this observation!

---

### Phase 3: Create Comparison Plots (Assignment 8)

**Step 1:** Create plotting script

Create `plot_search_comparison.py` from Assignment 8 instructions (Part 3).

**Step 2:** Generate comparison plots

```bash
python plot_search_comparison.py
```

**Expected output:**
```
======================================================================
GENERATING SEARCH ALGORITHM COMPARISON PLOTS
======================================================================

Saved: search_time_comparison.png
Saved: greedy_speedup.png
Saved: nodes_explored_comparison.png
Saved: efficiency_comparison.png

======================================================================
ALL COMPARISON PLOTS GENERATED SUCCESSFULLY
======================================================================
```

**✅ Assignment 8 Complete!** You have all comparison data and plots.

---

## Troubleshooting

### Problem 1: "Python is not recognized" or "command not found"

**Solution:**
- **Windows:** Add Python to PATH during installation, or use full path: `C:\Python39\python.exe`
- **Mac/Linux:** Use `python3` instead of `python`

### Problem 2: "No module named 'matplotlib'"

**Solution:**
```bash
# Try with pip3
pip3 install matplotlib

# Or with specific Python version
python -m pip install matplotlib
```

### Problem 3: "FileNotFoundError: graph_small.json"

**Solution:**
- Make sure you ran `graph_generator.py` first
- Check you're in the correct directory: `pwd` (Mac/Linux) or `cd` (Windows)
- Verify files exist: `ls *.json` or `dir *.json`

### Problem 4: "Permission denied" or "Access denied"

**Solution:**
- Don't run as administrator/sudo unless required
- Check file permissions
- Try a different directory (like Documents or Desktop)

### Problem 5: "Invalid syntax" errors

**Solution:**
- Make sure you copied the entire code from the assignment
- Check for missing quotes, colons, or parentheses
- Use a proper text editor (not Microsoft Word!)

### Problem 6: Code runs but plots don't appear

**Solution:**
- Check if PNG files were created: `ls *.png` or `dir *.png`
- Open them manually with image viewer
- If using remote server, download files to view locally

### Problem 7: Performance measurement takes forever

**Solution:**
- This is normal for large graph (10,000 nodes)
- Don't interrupt - let it complete
- Large graph with 10 runs should take 5-10 minutes
- If stuck for >15 minutes, stop and restart

### Problem 8: "ModuleNotFoundError: No module named 'bfs_search'"

**Solution:**
- Make sure all Python files are in the same directory
- Don't rename the files
- Check spelling: it's `bfs_search.py` not `bfs_searches.py`

### Problem 9: JSON file is corrupted or won't load

**Solution:**
- Delete all JSON files: `rm *.json` or `del *.json`
- Run graph generator again: `python graph_generator.py`
- Don't manually edit JSON files!

### Problem 10: Numbers/times look different from examples

**Solution:**
- **This is normal!** Performance varies by computer
- What matters: relative differences (small vs medium vs large)
- Focus on trends, not exact values

---

## Quick Reference

### Commands Cheat Sheet

```bash
# Generate graphs (do this once)
python graph_generator.py

# Test BFS
python bfs_search.py small type warehouse
python bfs_search.py medium region north
python bfs_search.py large capacity_min 3000

# Test Greedy
python greedy_search.py small type warehouse
python greedy_search.py medium region north
python greedy_search.py large capacity_min 3000

# Assignment 7: Measure BFS performance
python bfs_performance.py
python plot_bfs_performance.py

# Assignment 8: Compare BFS and Greedy
python greedy_performance.py
python plot_search_comparison.py

# Check what files you have
ls *.json    # Mac/Linux
dir *.json   # Windows

ls *.png     # Mac/Linux
dir *.png    # Windows
```

### Search Property Options

| Property | Values | Example |
|----------|--------|---------|
| `type` | warehouse, distribution_center, retail_store, hub, depot | `type warehouse` |
| `region` | north, south, east, west, central | `region north` |
| `capacity_min` | Any number (100-5000) | `capacity_min 3000` |
| `capacity_max` | Any number (100-5000) | `capacity_max 2000` |
| `priority` | 1, 2, 3, 4, 5 | `priority 5` |

### File Checklist

**After graph generation:**
- [ ] `graph_small.json` (~5 MB)
- [ ] `graph_medium.json` (~35 MB)
- [ ] `graph_large.json` (~120 MB)

**After Assignment 7:**
- [ ] `bfs_performance.py` (your code)
- [ ] `plot_bfs_performance.py` (your code)
- [ ] `bfs_performance_results.json` (results)
- [ ] `bfs_time_vs_size.png` (plot)
- [ ] `bfs_time_per_node.png` (plot)
- [ ] `bfs_scalability.png` (plot)

**After Assignment 8:**
- [ ] `greedy_performance.py` (your code)
- [ ] `plot_search_comparison.py` (your code)
- [ ] `search_comparison_results.json` (results)
- [ ] `search_time_comparison.png` (plot)
- [ ] `greedy_speedup.png` (plot)
- [ ] `nodes_explored_comparison.png` (plot)
- [ ] `efficiency_comparison.png` (plot)

---

## Tips for Success

### General Tips
1. **Start early** - Don't wait until the deadline
2. **Test incrementally** - Run each step before moving on
3. **Save your work** - Back up your files regularly
4. **Read error messages** - They usually tell you what's wrong
5. **Ask for help** - If stuck for >30 minutes, ask instructor

### Performance Tips
1. **Close other programs** while measuring performance
2. **Run multiple times** if results seem inconsistent
3. **Don't trust first run** - Python JIT compilation affects timing
4. **Use same computer** for both assignments for fair comparison

### Plotting Tips
1. **Check plots immediately** - Make sure they look right
2. **Regenerate if needed** - Just run the script again
3. **Adjust figure size** - If text is too small, edit `figsize=(10, 6)` to larger values
4. **Save high resolution** - Plots are saved at 300 dpi (good quality)

### Report Writing Tips
1. **Include plots in report** - Don't just submit PNG files separately
2. **Explain your plots** - What does each one show?
3. **Compare to theory** - Do results match O(V+E)?
4. **Discuss anomalies** - If something looks weird, explain why

---

## Getting Help

### If You're Stuck

1. **Check this guide** - Read the troubleshooting section
2. **Read error messages carefully** - They often tell you exactly what's wrong
3. **Google the error** - Add "python" to your search
4. **Check file locations** - Make sure all files are in same folder
5. **Try on different computer** - Could be environment issue

### Resources

**Python Help:**
- Python documentation: https://docs.python.org/3/
- Stack Overflow: https://stackoverflow.com/questions/tagged/python

**matplotlib Help:**
- matplotlib documentation: https://matplotlib.org/stable/index.html
- matplotlib gallery: https://matplotlib.org/stable/gallery/index.html

**Command Line Help:**
- Windows CMD: https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/
- Mac Terminal: https://support.apple.com/guide/terminal/welcome/mac
- Linux Terminal: https://ubuntu.com/tutorials/command-line-for-beginners

### Contact Information

**If you need help:**
- Office hours: [Check syllabus]
- Email: [Instructor email]
- Discussion board: [Course platform]

**Before asking for help, include:**
- What command you ran
- Full error message (copy/paste)
- What you've tried already
- Screenshots if relevant

---

## Summary: Steps to Success

### Assignment 7 (BFS) - Complete Workflow
1. ✅ Install Python and matplotlib
2. ✅ Run `graph_generator.py` to create graph files
3. ✅ Test `bfs_search.py` with various parameters
4. ✅ Create `bfs_performance.py` script
5. ✅ Run performance measurements (saves JSON)
6. ✅ Create `plot_bfs_performance.py` script
7. ✅ Generate plots (creates 3 PNG files)
8. ✅ Write report analyzing results
9. ✅ Submit ZIP with scripts, plots, and report

### Assignment 8 (Greedy) - Complete Workflow
1. ✅ Use same graph files from Assignment 7
2. ✅ Test `greedy_search.py` with various parameters
3. ✅ Create `greedy_performance.py` script (compares BFS and Greedy)
4. ✅ Run comparison measurements (saves JSON)
5. ✅ Create `plot_search_comparison.py` script
6. ✅ Generate comparison plots (creates 4 PNG files)
7. ✅ Write report comparing both algorithms
8. ✅ Submit ZIP with scripts, plots, and report

---

## Final Checklist

Before you start Assignment 7:
- [ ] Python 3.7+ installed and working
- [ ] matplotlib installed
- [ ] All three `.py` files downloaded (generator, bfs, greedy)
- [ ] Graph files generated (3 JSON files created)
- [ ] Tested at least one BFS search successfully

Before you start Assignment 8:
- [ ] Assignment 7 completed
- [ ] Tested at least one Greedy search successfully
- [ ] Have BFS results from Assignment 7 available

Before submitting Assignment 7:
- [ ] `bfs_performance.py` runs without errors
- [ ] `plot_bfs_performance.py` creates all 3 plots
- [ ] Plots are clear and readable
- [ ] Report written and explains results
- [ ] All files in ZIP

Before submitting Assignment 8:
- [ ] `greedy_performance.py` runs without errors
- [ ] `plot_search_comparison.py` creates all 4 plots
- [ ] Report compares both algorithms
- [ ] References Assignment 7 results
- [ ] All files in ZIP

---

**Good luck with your assignments! 🚀**

Remember: The code is already written and working - your job is to run it, measure performance, create plots, and analyze the results. Focus on understanding **why** the algorithms behave the way they do!

If you follow this guide step-by-step, you'll have everything you need for successful assignments. Happy coding! 💻📊