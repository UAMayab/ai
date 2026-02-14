# Assignment 4: Recursive Predicates in Prolog
**Session 10 - Prolog Predicates and Recursion**
**Estimated Time: 1 hour**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand and implement recursive predicates in Prolog
2. Apply recursion to solve complex relational queries
3. Differentiate between base cases and recursive cases
4. Create predicates that traverse relationships transitively
5. Test and debug recursive Prolog programs

---

## Background

In Activity #3 - Session 9, you implemented a semantic network using Prolog facts and rules. However, some relationships in a university course system require **recursion** to fully capture. For example:

- Finding **all** prerequisites for a course (not just direct ones)
- Discovering **all** courses in a prerequisite chain
- Determining if one course is a **distant prerequisite** of another

Recursion in Prolog allows predicates to call themselves, enabling you to traverse relationships of arbitrary depth. This is one of Prolog's most powerful features!

---

## Prerequisites

- Completed Assignment 3 (Prolog Implementation)
- Your working Prolog knowledge base from Assignment 3
- Access to SWISH: https://swish.swi-prolog.org/

---

## Understanding Recursion in Prolog

### The Pattern: Base Case + Recursive Case

Every recursive predicate follows this pattern:

```prolog
% BASE CASE: Direct relationship
predicate(X, Y) :- direct_fact(X, Y).

% RECURSIVE CASE: Indirect relationship through intermediate step
predicate(X, Y) :-
    direct_fact(X, Z),      % X relates to some intermediate Z
    predicate(Z, Y).        % Z recursively relates to Y
```

### Example: Ancestor Relationship

```prolog
% Facts about family
parent(john, mary).
parent(mary, susan).
parent(susan, alice).

% Base case: Someone is your ancestor if they're your parent
ancestor(X, Y) :- parent(X, Y).

% Recursive case: Someone is your ancestor if they're the parent
% of someone who is your ancestor
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
```

**How it works:**
- Query: `?- ancestor(john, alice).`
- Prolog finds: john → parent → mary → ancestor → susan → parent → alice
- Result: `true`

---

## Assignment Instructions

### Part 1: Extend Your Knowledge Base (30 minutes)

Open your Prolog file from Activity #3 - Session 9 in SWISH and add the following recursive predicates.

#### Example 1: All Prerequisites (Provided)

This predicate finds both **direct** and **indirect** prerequisites for a course.

```prolog
% ============================================
% RECURSIVE PREDICATE 1: All Prerequisites
% ============================================

% Base case: Direct prerequisite
all_prerequisites(Course, Prereq) :-
    is_prerequisite_of(Prereq, Course).

% Recursive case: Prerequisite of a prerequisite
all_prerequisites(Course, Prereq) :-
    is_prerequisite_of(DirectPrereq, Course),
    all_prerequisites(DirectPrereq, Prereq).

% Example usage:
% If: calculus_1 is_prerequisite_of calculus_2
%     calculus_2 is_prerequisite_of differential_equations
% Then: ?- all_prerequisites(differential_equations, X).
% Returns: X = calculus_2 ; X = calculus_1
```

#### Example 2: Course Accessibility (Provided)

This predicate checks if a course is eventually accessible from another course (following any length of prerequisite chain).

```prolog
% ============================================
% RECURSIVE PREDICATE 2: Course Leads To
% ============================================

% Base case: One course directly leads to another
course_leads_to(Course1, Course2) :-
    is_prerequisite_of(Course1, Course2).

% Recursive case: Course1 leads to Course2 through intermediate courses
course_leads_to(Course1, Course2) :-
    is_prerequisite_of(Course1, IntermediateCourse),
    course_leads_to(IntermediateCourse, Course2).

% Example usage:
% If: intro_programming → data_structures → algorithms → machine_learning
% Then: ?- course_leads_to(intro_programming, machine_learning).
% Returns: true
```

#### Example 3: Courses in Same Learning Path (Provided)

This predicate finds courses that are in the same learning path (they share prerequisites or lead to the same course).

```prolog
% ============================================
% RECURSIVE PREDICATE 3: Same Learning Path
% ============================================

% Two courses are in the same learning path if they share a common prerequisite
same_learning_path(Course1, Course2) :-
    all_prerequisites(Course1, CommonPrereq),
    all_prerequisites(Course2, CommonPrereq),
    Course1 \= Course2.

% Alternative: Two courses are in the same path if they both lead to a common course
same_learning_path(Course1, Course2) :-
    course_leads_to(Course1, CommonTarget),
    course_leads_to(Course2, CommonTarget),
    Course1 \= Course2.

% Example usage:
% If both "linear_algebra" and "probability" are prerequisites for "machine_learning"
% Then: ?- same_learning_path(linear_algebra, probability).
% Returns: true
```

### Part 2: Test the Recursive Predicates (15 minutes)

Test each of the three provided recursive predicates with **at least 2 queries each**.

Document your queries and results:

**Template:**
```
Predicate: all_prerequisites/2

Query 1: ?- all_prerequisites(algorithms, X).
Result: [List all results]
Explanation: [What does this tell you about the course?]

Query 2: ?- all_prerequisites(X, calculus_1).
Result: [List all results]
Explanation: [What does this query find?]
```

**Important Testing Tips:**
- Use specific course names from YOUR knowledge base
- Try queries with variables in different positions
- Test edge cases (courses with no prerequisites, long chains)
- Include at least one query that returns `false`

### Part 3: Create Your Own Recursive Predicate (10 minutes)

Design and implement **ONE** custom recursive predicate that would be useful for the university course system.

**Ideas for your custom predicate:**

1. **required_for_graduation(Major, Course)** - Find all courses in a major that require a specific course
2. **prerequisite_depth(Course, Depth)** - Calculate how many levels of prerequisites a course has
3. **courses_at_level(StartCourse, Level, Course)** - Find courses at a certain distance in the prerequisite chain
4. **common_foundation(Course1, Course2, Foundation)** - Find common foundational courses for two advanced courses
5. **builds_toward(Topic, Course)** - Recursively find courses that cover a topic or lead to courses that do

**Your predicate must:**
- Include both a base case and recursive case
- Use at least one recursive call
- Be testable with your existing knowledge base
- Be well-commented explaining what it does

**Template:**
```prolog
% ============================================
% YOUR CUSTOM RECURSIVE PREDICATE
% Name: [predicate_name]
% Purpose: [What does it do?]
% ============================================

% Base case:
[your_predicate] :- [base_case_definition].

% Recursive case:
[your_predicate] :- [recursive_case_definition].
```

### Part 4: Test Your Custom Predicate (5 minutes)

Test your custom recursive predicate with **at least 3 different queries** that demonstrate it works correctly.

---

## Deliverables

Submit **ONE document** (PDF) containing:

1. **Extended Prolog Code** (copy-paste from SWISH)
   - All three provided recursive predicates
   - Your one custom recursive predicate
   - Well-commented code

2. **Testing Results for Provided Predicates**
   - 2 queries per predicate (6 total)
   - Results for each query
   - Brief explanation of what each query finds

3. **Custom Predicate Documentation**
   - Name and purpose
   - Explanation of base case and recursive case
   - 3 test queries with results
   - Brief description (50-100 words) of when this predicate would be useful

4. **Screenshots** (2 required)
   - Screenshot showing one successful recursive query in SWISH
   - Screenshot showing your custom predicate working

**Total Length: 2-3 pages**

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Provided Predicates** | All 3 implemented correctly | 2-3 implemented, minor issues | 1-2 working | Missing or incorrect | /25 |
| **Testing of Provided Predicates** | 6+ queries, thorough testing | 5-6 queries, good testing | 4 queries, basic testing | <4 or incomplete | /20 |
| **Custom Predicate** | Sophisticated, correct, well-designed | Good predicate, works correctly | Basic but functional | Doesn't work or missing | /30 |
| **Testing Custom Predicate** | 3+ queries, demonstrates functionality | 3 queries, adequate testing | 2 queries | <2 or incomplete | /15 |
| **Documentation & Comments** | Excellent comments and explanations | Good documentation | Basic documentation | Poor or missing | /10 |
| **TOTAL** | | | | | /100 |

---

## Common Pitfalls & Debugging Tips

### Pitfall 1: Infinite Recursion
```prolog
% WRONG - This will loop forever!
related(X, Y) :- related(Y, X).

% RIGHT - Add a base case
related(X, Y) :- direct_relation(X, Y).
related(X, Y) :- direct_relation(Y, X).
```

### Pitfall 2: Missing Base Case
```prolog
% WRONG - No way to stop!
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% RIGHT - Base case stops the recursion
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

### Pitfall 3: Incorrect Variable Binding
```prolog
% WRONG - Variables don't connect properly
chain(X, Y) :- rel(A, B), chain(C, D).

% RIGHT - Variables must link correctly
chain(X, Y) :- rel(X, Z), chain(Z, Y).
```

### Debugging Strategy:
1. **Test base case first** - Make sure it works independently
2. **Use trace in SWISH** - Watch how Prolog evaluates your predicate
3. **Start with simple queries** - Use specific values before variables
4. **Check for cycles** - Make sure recursion terminates
5. **Add print statements** - Use `write()` to see what's happening

---

## Examples of Good Queries to Test

```prolog
% Find all prerequisites for a specific course
?- all_prerequisites(machine_learning, X).

% Find all courses that require a specific prerequisite
?- all_prerequisites(X, calculus_1).

% Check if a specific course is a prerequisite for another
?- all_prerequisites(algorithms, data_structures).

% Find learning paths
?- course_leads_to(intro_programming, X).

% Find related courses
?- same_learning_path(algorithms, X).

% Test your custom predicate
?- [your_custom_predicate with various arguments].
```

---

## Tips for Success

1. **Build on Assignment 3**: Use your existing knowledge base - don't start from scratch
2. **Understand Before Coding**: Make sure you understand how each provided predicate works
3. **Test Incrementally**: Add one predicate at a time and test it before moving on
4. **Think About Real Use Cases**: Your custom predicate should solve a real problem
5. **Comment Generously**: Explain what your code does, especially the recursive logic
6. **Use Meaningful Names**: Choose predicate names that clearly describe what they do

---

## Understanding Recursion: A Visual Example

Consider this prerequisite chain:
```
intro_programming → data_structures → algorithms → machine_learning
```

**Query:** `?- all_prerequisites(machine_learning, X).`

**How Prolog solves it:**
1. Base case finds: `algorithms` (direct prerequisite)
2. Recursive call on `algorithms` finds: `data_structures`
3. Recursive call on `data_structures` finds: `intro_programming`
4. Recursive call on `intro_programming` finds: nothing (base case ends)
5. Returns all: `algorithms, data_structures, intro_programming`

**This is the power of recursion!** Without it, you'd need separate predicates for:
- direct prerequisites
- prerequisites of prerequisites
- prerequisites of prerequisites of prerequisites
- ... and so on

---

## Resources

- SWISH Online: https://swish.swi-prolog.org/
- SWI-Prolog Recursion Guide: https://www.swi-prolog.org/pldoc/man?section=recursion
- Learn Prolog Now - Recursion Chapter: http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse23

---

## Frequently Asked Questions

**Q: Can I modify the provided predicates?**
A: No, use them as-is for Parts 1-2. Your creativity goes into Part 3 (custom predicate).

**Q: My recursive predicate gives duplicate results. Is that okay?**
A: Yes, that's normal in Prolog. You can use `setof` or `bagof` to remove duplicates if needed (optional).

**Q: How do I know if my recursion will terminate?**
A: Make sure your base case doesn't require recursion, and each recursive call gets "closer" to the base case.

**Q: Can my custom predicate use the provided recursive predicates?**
A: Absolutely! Building on existing predicates is encouraged.

**Q: What if I don't have enough courses in my knowledge base?**
A: Add more facts! You should have at least 5-6 courses with prerequisite relationships to make recursion meaningful.

---

## Connection to Previous & Future Work

- **From Activity 3**: You created facts and rules - now you're adding the power of recursion
- **Real-World Application**: Recursive queries are used in course registration systems, degree audit tools, and academic planning software
- **Beyond This Course**: Recursion is fundamental in AI for tree traversal, game strategies, and problem-solving

---

**Due Date:** Sunday, March 1st, 2026 by midnight
**Submission:** Brightspace

---

Good luck! Recursion might feel tricky at first, but once it "clicks," you'll see how elegant and powerful it is. Take your time to understand the examples, and don't hesitate to ask questions!

Remember: **Base case + Recursive case = Recursive magic!** ✨
