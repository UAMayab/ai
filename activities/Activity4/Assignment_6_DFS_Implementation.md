# Assignment 6: Implementing Depth-First Search in Python
**Session 12 - Depth-First Search Algorithm**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand the Depth-First Search (DFS) algorithm implementation
2. Apply DFS to solve real-world graph traversal problems
3. Read and understand commented Python code
4. Modify existing code to create custom applications
5. Visualize and test graph search algorithms

---

## Background

Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It's particularly useful for:
- Finding paths in graphs
- Detecting cycles
- Topological sorting
- Exploring all possible solutions

In this assignment, you'll work with a **course prerequisite graph** (building on your earlier assignments) to understand how DFS works in practice.

---

## Prerequisites

- Basic Python knowledge (variables, lists, dictionaries, functions, loops)
- Understanding of DFS concept from Session 12
- Python 3.x installed on your computer:
  - Jupyter Notebook in Conda

---

## Assignment Instructions

### Part 1: Understanding the DFS Implementation (45 minutes)

#### Step 1: Study the Provided Code

Below is a complete, heavily-commented Python implementation of DFS applied to a university course prerequisite system.

**Read through ALL comments carefully** - they explain every design decision and logic step.

```python
"""
Course Prerequisite Graph - Depth-First Search Implementation
==============================================================
This program implements DFS to analyze course prerequisite relationships.

Author: Miguel Guirao
Date: 14/02/2026 (Happy Valentines!)
Course: AI
"""

# ============================================================================
# PART 1: GRAPH REPRESENTATION
# ============================================================================

class CourseGraph:
    """
    Represents a course prerequisite graph using an adjacency list.

    In this graph:
    - Each course is a node
    - A directed edge from Course A to Course B means:
      "Course A is a prerequisite for Course B"
    """

    def __init__(self):
        """
        Initialize an empty graph.

        We use a dictionary to represent the graph:
        - Keys: course names (strings)
        - Values: lists of courses that have this course as a prerequisite

        Example: {'calculus_1': ['calculus_2', 'physics']}
        means calculus_1 is a prerequisite for both calculus_2 and physics
        """
        self.graph = {}

    def add_course(self, course):
        """
        Add a course to the graph.

        Args:
            course (str): The name of the course to add

        If the course already exists, nothing happens.
        This prevents duplicate entries.
        """
        if course not in self.graph:
            self.graph[course] = []  # Empty list means no courses depend on this one yet

    def add_prerequisite(self, prereq, course):
        """
        Add a prerequisite relationship.

        Args:
            prereq (str): The prerequisite course
            course (str): The course that requires the prerequisite

        This creates a directed edge: prereq -> course
        """
        # Make sure both courses exist in the graph
        self.add_course(prereq)
        self.add_course(course)

        # Add the directed edge
        # If prereq is not already listed as a prerequisite for course, add it
        if course not in self.graph[prereq]:
            self.graph[prereq].append(course)

    def get_courses_requiring(self, prereq):
        """
        Get all courses that directly require a given prerequisite.

        Args:
            prereq (str): The prerequisite course to check

        Returns:
            list: All courses that have prereq as a direct prerequisite
        """
        if prereq in self.graph:
            return self.graph[prereq]
        else:
            return []  # Course has no dependents

    def display_graph(self):
        """
        Display the entire graph in a readable format.
        Useful for debugging and understanding the graph structure.
        """
        print("\n" + "="*60)
        print("COURSE PREREQUISITE GRAPH")
        print("="*60)

        if not self.graph:
            print("Graph is empty!")
            return

        for course in sorted(self.graph.keys()):
            dependents = self.graph[course]
            if dependents:
                print(f"{course:25} -> {', '.join(dependents)}")
            else:
                print(f"{course:25} -> (no dependent courses)")
        print("="*60 + "\n")


# ============================================================================
# PART 2: DEPTH-FIRST SEARCH IMPLEMENTATION
# ============================================================================

def dfs_recursive(graph, start_course, visited=None):
    """
    Perform Depth-First Search using RECURSION.

    This is the classic recursive implementation of DFS.
    It explores as deep as possible before backtracking.

    Args:
        graph (CourseGraph): The course prerequisite graph
        start_course (str): The course to start the search from
        visited (set): Set of already-visited courses (default: None)

    Returns:
        list: All courses reachable from start_course in DFS order

    How it works:
    1. Mark current course as visited
    2. For each course that requires the current course (neighbors):
       a. If not visited, recursively visit it
    3. Return all visited courses
    """

    # Initialize visited set on first call
    # We use a set because it provides O(1) lookup time
    if visited is None:
        visited = set()

    # Mark the current course as visited
    visited.add(start_course)

    # Get all courses that require this course as a prerequisite
    dependent_courses = graph.get_courses_requiring(start_course)

    # Recursively visit each unvisited dependent course
    for course in dependent_courses:
        if course not in visited:
            # RECURSIVE CALL: This is where DFS "goes deep"
            dfs_recursive(graph, course, visited)

    # Return the complete set of visited courses
    return list(visited)


def dfs_iterative(graph, start_course):
    """
    Perform Depth-First Search using ITERATION (with a stack).

    This is the iterative implementation of DFS using an explicit stack.
    It produces the same result as recursive DFS but without recursion.

    Args:
        graph (CourseGraph): The course prerequisite graph
        start_course (str): The course to start the search from

    Returns:
        list: All courses reachable from start_course in DFS order

    How it works:
    1. Push start_course onto stack
    2. While stack is not empty:
       a. Pop a course from stack
       b. If not visited, mark as visited
       c. Push all unvisited dependent courses onto stack
    3. Return all visited courses

    Why use a stack?
    - Stack follows LIFO (Last In, First Out)
    - This ensures we go DEEP before WIDE
    - Compare to BFS which uses a queue (FIFO)
    """

    # Initialize data structures
    visited = set()  # Keeps track of visited courses
    stack = [start_course]  # Stack for DFS (using Python list)

    # Continue until stack is empty
    while stack:
        # Pop from the END of the list (this makes it a stack, not a queue)
        current_course = stack.pop()

        # Only process if we haven't visited this course yet
        if current_course not in visited:
            # Mark as visited
            visited.add(current_course)

            # Get all courses that depend on this one
            dependent_courses = graph.get_courses_requiring(current_course)

            # Add all unvisited dependents to the stack
            # We add them in reverse order to maintain consistent ordering
            for course in reversed(dependent_courses):
                if course not in visited:
                    stack.append(course)

    return list(visited)


def find_all_reachable_courses(graph, start_course):
    """
    Find all courses reachable from a starting course.

    This answers the question: "If I take [start_course], what other
    courses become accessible (directly or indirectly)?"

    Args:
        graph (CourseGraph): The course prerequisite graph
        start_course (str): The starting course

    Returns:
        list: All courses reachable from start_course (excluding start_course itself)
    """

    if start_course not in graph.graph:
        print(f"Error: Course '{start_course}' not found in graph!")
        return []

    # Use DFS to find all reachable courses
    reachable = dfs_recursive(graph, start_course)

    # Remove the starting course from results (we want courses AFTER it)
    reachable.remove(start_course)

    return reachable


def find_prerequisite_path(graph, start_course, target_course):
    """
    Find if there's a path from start_course to target_course.

    This answers: "Is [start_course] a prerequisite (direct or indirect)
    for [target_course]?"

    Args:
        graph (CourseGraph): The course prerequisite graph
        start_course (str): The starting course
        target_course (str): The target course we're trying to reach

    Returns:
        bool: True if path exists, False otherwise
    """

    # Find all reachable courses from start
    reachable = dfs_recursive(graph, start_course)

    # Check if target is in the reachable set
    return target_course in reachable


# ============================================================================
# PART 3: EXAMPLE USAGE AND TESTING
# ============================================================================

def create_sample_graph():
    """
    Create a sample course prerequisite graph for testing.

    This represents a typical Computer Science curriculum structure.

    Graph structure:
    intro_programming -> data_structures -> algorithms -> machine_learning
    intro_programming -> web_development
    calculus_1 -> calculus_2 -> differential_equations
    calculus_1 -> linear_algebra -> machine_learning
    linear_algebra -> computer_graphics
    data_structures -> databases
    """

    graph = CourseGraph()

    # Add prerequisite relationships
    # Format: add_prerequisite(prerequisite_course, dependent_course)

    # Programming track
    graph.add_prerequisite('intro_programming', 'data_structures')
    graph.add_prerequisite('data_structures', 'algorithms')
    graph.add_prerequisite('algorithms', 'machine_learning')
    graph.add_prerequisite('intro_programming', 'web_development')
    graph.add_prerequisite('data_structures', 'databases')

    # Math track
    graph.add_prerequisite('calculus_1', 'calculus_2')
    graph.add_prerequisite('calculus_2', 'differential_equations')
    graph.add_prerequisite('calculus_1', 'linear_algebra')
    graph.add_prerequisite('linear_algebra', 'machine_learning')
    graph.add_prerequisite('linear_algebra', 'computer_graphics')

    return graph


def run_examples():
    """
    Run example queries on the sample graph to demonstrate DFS.
    """

    print("\n" + "="*60)
    print("DEPTH-FIRST SEARCH: COURSE PREREQUISITE ANALYSIS")
    print("="*60 + "\n")

    # Create the sample graph
    graph = create_sample_graph()

    # Display the graph structure
    graph.display_graph()

    # ========================================================================
    # EXAMPLE 1: Find all courses reachable from intro_programming
    # ========================================================================
    print("\n" + "-"*60)
    print("EXAMPLE 1: Courses accessible after intro_programming")
    print("-"*60)

    start = 'intro_programming'
    reachable = find_all_reachable_courses(graph, start)

    print(f"\nStarting from: {start}")
    print(f"Courses you can eventually take: {len(reachable)}")
    print(f"Courses: {', '.join(sorted(reachable))}")

    # ========================================================================
    # EXAMPLE 2: Find all courses reachable from calculus_1
    # ========================================================================
    print("\n" + "-"*60)
    print("EXAMPLE 2: Courses accessible after calculus_1")
    print("-"*60)

    start = 'calculus_1'
    reachable = find_all_reachable_courses(graph, start)

    print(f"\nStarting from: {start}")
    print(f"Courses you can eventually take: {len(reachable)}")
    print(f"Courses: {', '.join(sorted(reachable))}")

    # ========================================================================
    # EXAMPLE 3: Check if a path exists between two courses
    # ========================================================================
    print("\n" + "-"*60)
    print("EXAMPLE 3: Checking prerequisite relationships")
    print("-"*60)

    test_cases = [
        ('intro_programming', 'machine_learning'),
        ('calculus_1', 'machine_learning'),
        ('web_development', 'algorithms'),
        ('data_structures', 'computer_graphics'),
    ]

    for start, target in test_cases:
        path_exists = find_prerequisite_path(graph, start, target)
        result = "YES" if path_exists else "NO"
        print(f"\nIs '{start}' a prerequisite for '{target}'? {result}")

    # ========================================================================
    # EXAMPLE 4: Compare recursive vs iterative DFS
    # ========================================================================
    print("\n" + "-"*60)
    print("EXAMPLE 4: Comparing recursive and iterative DFS")
    print("-"*60)

    start = 'intro_programming'

    recursive_result = dfs_recursive(graph, start)
    iterative_result = dfs_iterative(graph, start)

    print(f"\nStarting course: {start}")
    print(f"\nRecursive DFS result: {recursive_result}")
    print(f"Iterative DFS result: {iterative_result}")
    print(f"\nSame results? {set(recursive_result) == set(iterative_result)}")

    print("\n" + "="*60)
    print("END OF EXAMPLES")
    print("="*60 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    """
    This code runs when you execute the script directly.
    It demonstrates DFS on the course prerequisite graph.
    """
    run_examples()
```

#### Step 2: Run and Test the Code (15 minutes)

1. Copy the entire code above into a Python file (e.g., `course_dfs.py`)
2. Run the program
3. Study the output carefully
4. Take a **screenshot** of the complete output

**Questions to consider while running:**
- How many courses are reachable from `intro_programming`?
- What's the difference between recursive and iterative DFS output?
- Why does `web_development` not lead to `algorithms`?

---

### Part 2: Create Your Own Scenario (60 minutes)

Now it's your turn! You will modify the code to implement DFS for a **different scenario**.

#### Choose ONE of the following scenarios (or propose your own):

**Scenario A: Social Network Connections**
- Nodes: People
- Edges: Friendships (who knows whom)
- Query: "Find all people reachable through friends-of-friends from person X"

**Scenario B: Software Module Dependencies**
- Nodes: Software modules/libraries
- Edges: Dependencies (Module A requires Module B)
- Query: "Find all modules that must be installed if we install Module X"

**Scenario C: File System Directory Structure**
- Nodes: Folders/Directories
- Edges: Contains relationship (Folder A contains Folder B)
- Query: "Find all subdirectories under a given directory"

**Scenario D: Website Link Structure**
- Nodes: Web pages
- Edges: Hyperlinks (Page A links to Page B)
- Query: "Find all pages reachable from the homepage"

**Scenario E: Your Own** (Get creative!)
- Choose a domain relevant to your engineering major
- Must have at least 10 nodes and 12 edges
- Must demonstrate a meaningful graph structure

#### Step 1: Design Your Graph (20 minutes)

Before coding, design your graph on paper:

1. **List at least 10 nodes** (courses, people, files, etc.)
2. **Define at least 12 directed edges** (relationships)
3. **Draw the graph structure** (simple diagram is fine)
4. **Identify interesting queries** to test (at least 3)

**Example for Social Network:**
```
Nodes: Alice, Bob, Carol, David, Eve, Frank, Grace, Henry, Iris, Jack

Edges (friendships):
- Alice -> Bob, Carol
- Bob -> David, Eve
- Carol -> Eve, Frank
- David -> Grace
- Eve -> Henry
- Frank -> Henry, Iris
- Grace -> Jack
- Henry -> Jack
```

#### Step 2: Modify the Code (30 minutes)

Modify the provided Python code to implement your scenario:

1. **Rename the class** (e.g., `CourseGraph` -> `SocialNetworkGraph`)
2. **Update all comments** to reflect your new domain
3. **Update variable names** to match your scenario
4. **Create your graph** in `create_sample_graph()`
5. **Modify the examples** to demonstrate your scenario

**Key changes needed:**
```python
# Change class name and docstrings
class SocialNetworkGraph:  # Was: CourseGraph
    """Represents a social network using an adjacency list."""

    # Update method names and comments
    def add_person(self, person):  # Was: add_course
        """Add a person to the network."""
        if person not in self.graph:
            self.graph[person] = []

    def add_friendship(self, person1, person2):  # Was: add_prerequisite
        """Add a friendship connection."""
        # ... implementation ...
```

#### Step 3: Test Your Implementation (10 minutes)

Run your modified code and verify it works correctly:

1. **Run the program** and check for errors
2. **Verify the graph structure** displays correctly
3. **Test your queries** - do the results make sense?
4. **Take screenshots** of your output

---

### Part 3: Analysis and Reflection (15 minutes)

Answer the following questions about your implementation:

**Question 1: Graph Structure (100 words)**
- Describe your graph: What do nodes and edges represent?
- How many nodes and edges does your graph have?
- Why did you choose this particular structure?

**Question 2: DFS Behavior (100 words)**
- What does DFS find in your scenario?
- Give an example query and explain the result
- How does the "depth-first" nature affect the exploration?

**Question 3: Practical Application (100 words)**
- Where could this be used in real life?
- What insights does DFS provide for your scenario?
- What are the limitations of using DFS here?

**Question 4: Comparison to BFS (100 words)**
- How would Breadth-First Search behave differently on your graph?
- For your scenario, which algorithm (DFS or BFS) is more appropriate? Why?
- Give a specific example where the difference matters

**Question 5: Code Understanding (100 words)**
- What was the most challenging part of understanding the provided code?
- What was the most challenging part of modifying it?
- What did you learn about DFS implementation?

---

## Deliverables

Submit **ONE PDF document** containing:

1. **Part 1: Original Code Understanding**
   - Screenshot of running the original course prerequisite code
   - Output showing all examples working

2. **Part 2: Your Custom Scenario**
   - **Graph Design**: Hand-drawn or digital diagram of your graph structure
   - **Modified Code**: Complete Python code (copy-paste into document or attach as separate .py file)
   - **Screenshots**: At least 3 screenshots showing:
     - Your graph structure display
     - At least 2 different query results
     - Successful execution without errors
   - **Test Results**: Document at least 3 test queries with their outputs

3. **Part 3: Written Analysis**
   - Answers to all 5 questions (total ~500 words)

**Total Package: PDF document + optional Python file**

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Original Code Execution** | Successfully runs, understands output | Runs with minor issues | Runs but incomplete understanding | Does not run or major issues | /10 |
| **Custom Graph Design** | Well-designed, 10+ nodes, 12+ edges, meaningful | Good design, meets minimum requirements | Basic design, barely meets requirements | Incomplete or poor design | /20 |
| **Code Modification** | Excellent adaptation, all names/comments updated | Good modifications, mostly complete | Basic modifications, some issues | Incomplete or incorrect | /25 |
| **Testing & Screenshots** | 3+ tests, clear screenshots, thorough | 2-3 tests, good documentation | Minimal testing, basic screenshots | Insufficient or missing | /15 |
| **Written Analysis** | Thoughtful, detailed, demonstrates understanding | Good analysis with some depth | Basic answers, superficial | Weak or incomplete | /20 |
| **Code Quality** | Clean, well-commented, follows conventions | Good quality, mostly clear | Basic quality, some issues | Poor quality or unclear | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

### Understanding the Code
1. **Read top to bottom** - Don't skip the comments!
2. **Run it first** - See what it does before modifying
3. **Trace execution** - Follow what happens step-by-step
4. **Experiment** - Try adding print statements to see intermediate values

### Modifying the Code
1. **Change one thing at a time** - Test after each change
2. **Update ALL references** - If you rename something, change it everywhere
3. **Keep the structure** - Don't change the overall algorithm, just the domain
4. **Test frequently** - Don't wait until everything is changed to test

### Debugging Common Issues
```python
# Issue: KeyError when accessing graph
# Fix: Make sure you add nodes before adding edges
graph.add_person('Alice')  # Do this first
graph.add_friendship('Alice', 'Bob')  # Then this

# Issue: Infinite loop in DFS
# Fix: Make sure you're marking nodes as visited
if node not in visited:
    visited.add(node)  # This line is crucial!

# Issue: Edges going the wrong direction
# Fix: Think carefully about the relationship direction
# "A requires B" means edge from B -> A
# "A contains B" means edge from A -> B
```

### Python Beginner Tips
```python
# List vs Set
my_list = [1, 2, 2, 3]  # Can have duplicates
my_set = {1, 2, 3}      # No duplicates, fast lookup

# Dictionary (used for the graph)
graph = {}              # Empty dictionary
graph['A'] = ['B', 'C'] # Key 'A' maps to list ['B', 'C']

# List operations
stack = []
stack.append('A')       # Push 'A' onto stack
item = stack.pop()      # Pop from stack (removes and returns)

# Checking membership
if 'A' in visited:      # Fast for sets, slower for lists
    print("Already visited")
```

---

## Common Mistakes to Avoid

1. **Not updating comments** - If you change code, change comments too!
2. **Reversing edge direction** - Think carefully about what edges mean
3. **Forgetting to mark visited** - This causes infinite loops
4. **Not testing enough** - Test edge cases (single node, no edges, etc.)
5. **Inconsistent naming** - If you use `person`, don't mix with `course`
6. **Not explaining your graph** - Make it clear what nodes and edges represent

---


## Resources

### Python Resources
- Python Official Tutorial: https://docs.python.org/3/tutorial/
- Python Lists: https://docs.python.org/3/tutorial/datastructures.html
- Python Dictionaries: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

### DFS Resources
- Session 12 lecture notes
- Visualize DFS: https://visualgo.net/en/dfsbfs
- DFS Algorithm Explanation: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

### Graph Theory
- Graph basics: https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/describing-graphs
- When to use DFS vs BFS: https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-dfs-vs-bfs

---

## Example Scenarios (for inspiration)

### Social Network Example
```python
def create_sample_graph():
    graph = SocialNetworkGraph()

    # Add friendships
    graph.add_friendship('Alice', 'Bob')
    graph.add_friendship('Alice', 'Carol')
    graph.add_friendship('Bob', 'David')
    graph.add_friendship('Carol', 'Eve')
    # ... more friendships ...

    return graph

# Query: Find all people Alice can reach through friends
reachable = find_all_reachable_people(graph, 'Alice')
print(f"Alice's extended network: {reachable}")
```

### Software Dependencies Example
```python
def create_sample_graph():
    graph = DependencyGraph()

    # Module dependencies
    graph.add_dependency('express', 'node')
    graph.add_dependency('mongoose', 'mongodb')
    graph.add_dependency('myapp', 'express')
    graph.add_dependency('myapp', 'mongoose')
    # ... more dependencies ...

    return graph

# Query: Find all dependencies needed for 'myapp'
deps = find_all_dependencies(graph, 'myapp')
print(f"Installing myapp requires: {deps}")
```

---

## Frequently Asked Questions

**Q: Can I use a different programming language?**
A: No, please stick to Python for consistency. The code is designed for beginners.

**Q: Do I need to implement both recursive and iterative DFS?**
A: The provided code has both. For your scenario, you only need to keep one (preferably recursive as it's simpler).

**Q: Can my graph have cycles?**
A: Yes, but make sure your DFS handles them correctly (marking visited prevents infinite loops).

**Q: What if I don't know much Python?**
A: The provided code is heavily commented. Read through it slowly, run it, and the comments will guide you. You're mostly doing find-and-replace!

**Q: How detailed should my graph diagram be?**
A: Simple is fine! Just clearly show nodes and directed edges. Hand-drawn is acceptable.

**Q: Can I make my scenario simpler than the examples?**
A: It must have at least 10 nodes and 12 edges to demonstrate meaningful graph structure, but it doesn't need to be complex.

---

## Connection to Previous Assignments

- You've been working with course prerequisites conceptually (semantic networks) and in Prolog - now you're seeing a concrete algorithmic implementation!
- You analyzed when to use DFS - now you're implementing it!
- **Real-World Impact**: DFS is used in compilers, AI game playing, maze solving, and network analysis

---

**Due Date:** Sunday, March 1st, 2026 by midnight
**Submission:** Brightspace (PDF)

---

## Final Checklist

Before submitting, verify:
- [ ] Original code runs successfully (screenshot included)
- [ ] Custom scenario has 10+ nodes and 12+ edges
- [ ] Graph diagram is clear and labeled
- [ ] Modified code runs without errors
- [ ] At least 3 test queries documented with screenshots
- [ ] All 5 analysis questions answered (~ 500 words total)
- [ ] Code is well-commented and properly renamed
- [ ] Screenshots are clear and readable
- [ ] PDF is properly formatted and complete

---

Good luck! Remember: the goal isn't just to make the code work, but to **understand how DFS explores graphs**. Take your time to read the comments, experiment with the code, and think about how depth-first exploration affects the results.

**Have fun exploring graphs!**
