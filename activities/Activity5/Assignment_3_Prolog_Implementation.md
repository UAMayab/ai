# Assignment 3: Implementing Semantic Networks in Prolog
**Session 9 - Logic Programming and Prolog Language**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand the basics of logic programming and Prolog syntax
2. Translate a semantic network into Prolog facts and rules
3. Implement predicates to represent relationships
4. Query a knowledge base to retrieve information
5. Create inference rules that derive new knowledge from existing facts
6. Use an online Prolog environment (SWISH) effectively

---

## Background

Welcome to practical logic programming! In Assignments 1 and 2, you designed and analyzed a semantic network for a university course system. Now, you'll bring it to life by implementing it in **Prolog** - a logic programming language perfect for representing and reasoning about knowledge.

Unlike traditional programming languages that tell the computer HOW to do something (step-by-step instructions), Prolog lets you declare WHAT you know (facts and rules), and then ask questions. Prolog figures out the answers using logical inference.

**Think of it this way:**
- **Facts** = Things you know to be true (like your semantic network nodes and links)
- **Rules** = Logical patterns for deriving new knowledge (like your inference rules from Assignment 2)
- **Queries** = Questions you ask Prolog to answer

---

## Prerequisites

- Completed Assignments 1 and 2
- Access to SWISH online Prolog environment: https://swish.swi-prolog.org/
- Your semantic network diagram and pseudo-code from Assignment 2

---

## Getting Started with SWISH

### Step 1: Open SWISH
1. Go to https://swish.swi-prolog.org/
2. You'll see a code editor on the left and a query panel on the right
3. Click "Create a new program" or start typing in the editor

### Step 2: Understand Prolog Syntax Basics

**Facts** look like this:
```prolog
parent(john, mary).      % John is a parent of Mary
likes(mary, pizza).      % Mary likes pizza
```

**Rules** look like this:
```prolog
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
% X is a grandparent of Y if X is parent of Z and Z is parent of Y
```

**Queries** look like this:
```prolog
?- parent(john, mary).           % Is John a parent of Mary? (yes/no)
?- parent(john, Who).            % Who are John's children? (finds all)
?- grandparent(X, Y).            % Find all grandparent relationships
```

**Important Syntax Rules:**
- Atoms (constants) start with lowercase: `data_structures`, `dr_smith`
- Variables start with uppercase: `X`, `Course`, `Student`
- Every statement ends with a period `.`
- Commas `,` mean AND
- Semicolons `;` mean OR (but we won't use these much)
- `:-` means IF (used in rules)
- `%` starts a comment

### Step 3: Test with a Simple Example

Copy this into SWISH and press the "Run" button after typing in the query box:

```prolog
% Simple facts
parent(john, mary).
parent(mary, susan).

% Simple rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
```

Then in the query box at the bottom, type:
```prolog
?- grandparent(john, susan).
```

Press Enter. Prolog should respond with `true`.

---

## Assignment Instructions

### Part 1: Implement Your Semantic Network (60 minutes)

Now you'll implement YOUR university course semantic network in Prolog!

#### 1.1 Create Your Prolog File (40 minutes)

Create a new Prolog program with the following structure:

```prolog
% ============================================
% UNIVERSITY COURSE SEMANTIC NETWORK
% Assignment 3 - Introduction to Prolog
% Student Name: [Your Name]
% Date: [Date]
% ============================================

% ============================================
% SECTION 1: BASIC FACTS (Minimum 10 required)
% ============================================

% Courses and Departments
belongs_to(data_structures, computer_science).
belongs_to(algorithms, computer_science).
belongs_to(calculus_1, mathematics).
belongs_to(calculus_2, mathematics).

% Prerequisites
is_prerequisite_of(data_structures, algorithms).
is_prerequisite_of(calculus_1, calculus_2).

% Professors and Courses
taught_by(data_structures, dr_martinez).
taught_by(algorithms, dr_smith).
taught_by(calculus_1, prof_johnson).

% Course Topics
covers_topic(data_structures, trees).
covers_topic(data_structures, graphs).
covers_topic(algorithms, sorting).
covers_topic(algorithms, searching).

% Academic Levels
academic_level(data_structures, 200).
academic_level(algorithms, 300).
academic_level(calculus_1, 100).

% ADD YOUR OWN FACTS HERE
% Add at least 5 more facts from your semantic network
% Examples: credit_hours, course_format, difficulty_level, etc.


% ============================================
% SECTION 2: INFERENCE RULES (Minimum 5 required)
% ============================================

% Rule 1: A course is advanced if it's level 300 or higher
is_advanced_course(Course) :-
    academic_level(Course, Level),
    Level >= 300.

% Rule 2: Find indirect prerequisites (if A is prereq of B, and B is prereq of C,
%         then A is an indirect prerequisite of C)
indirect_prerequisite(Course1, Course2) :-
    is_prerequisite_of(Course1, IntermediateCourse),
    is_prerequisite_of(IntermediateCourse, Course2).

% Rule 3: Two courses are related if they belong to the same department
related_courses(Course1, Course2) :-
    belongs_to(Course1, Department),
    belongs_to(Course2, Department),
    Course1 \= Course2.  % Make sure they're different courses

% Rule 4: A professor is an expert in a topic if they teach a course covering that topic
is_expert_in(Professor, Topic) :-
    taught_by(Course, Professor),
    covers_topic(Course, Topic).

% Rule 5: A course is a prerequisite chain if it has prerequisites and is itself a prerequisite
is_in_prerequisite_chain(Course) :-
    is_prerequisite_of(_, Course),
    is_prerequisite_of(Course, _).

% ============================================
% SECTION 3: YOUR CUSTOM PREDICATES (3 required)
% ============================================

% TODO: Add 3 of your own inference rules here!
% Use the rules you designed in Assignment 2 as inspiration
%
% Ideas:
% - can_enroll(Student, Course) - check if student can enroll
% - courses_in_sequence(Course1, Course2) - check course ordering
% - same_topic_courses(Topic, Course1, Course2) - find courses with same topic
% - department_expert(Professor, Department) - professor teaches multiple courses in dept
% - foundation_course(Course) - course that is prerequisite for many courses
%
% Your Rule 1:


% Your Rule 2:


% Your Rule 3:


% ============================================
% END OF KNOWLEDGE BASE
% ============================================
```

**Your complete knowledge base must include:**
- **Minimum 15 total facts** (10 provided + 5 you add)
- **Minimum 8 total rules** (5 provided + 3 you create)
- **Facts must cover at least 4 different relationship types** (e.g., belongs_to, is_prerequisite_of, taught_by, covers_topic)

#### 1.2 Guidelines for Your Custom Predicates (20 minutes)

Your 3 custom rules should:
1. **Be useful** - answer practical questions about the course system
2. **Use logical inference** - combine multiple facts to derive new knowledge
3. **Be different from each other** - don't just repeat the same pattern
4. **Be testable** - you should be able to demonstrate they work

**Example of a GOOD custom predicate:**
```prolog
% Find courses that have the same prerequisite (might be offered in parallel)
share_prerequisite(Course1, Course2, Prereq) :-
    is_prerequisite_of(Prereq, Course1),
    is_prerequisite_of(Prereq, Course2),
    Course1 \= Course2.
```

**Example of a POOR custom predicate (Don't do this):**
```prolog
% Too simple - just restates a fact
course_exists(Course) :- belongs_to(Course, _).
```

### Part 2: Test Your Knowledge Base (30 minutes)

#### 2.1 Basic Queries (10 minutes)

Test your Prolog program with at least **8 different queries**. Include:

**Type 1: Simple fact checking (Yes/No questions)**
```prolog
?- belongs_to(data_structures, computer_science).
?- taught_by(algorithms, dr_jones).  % This should be false
```

**Type 2: Finding values (Who/What questions)**
```prolog
?- belongs_to(Course, computer_science).  % Find all CS courses
?- taught_by(data_structures, Who).       % Who teaches this course?
?- covers_topic(data_structures, Topic).  % What topics are covered?
```

**Type 3: Pattern matching (Find all matching cases)**
```prolog
?- is_prerequisite_of(X, Y).              % Find all prerequisite pairs
?- related_courses(algorithms, X).        % Find courses related to algorithms
```

**Type 4: Testing your rules**
```prolog
?- is_advanced_course(algorithms).        % Is this an advanced course?
?- is_expert_in(dr_martinez, trees).     % Is professor expert in this topic?
?- indirect_prerequisite(X, algorithms).  % What are indirect prerequisites?
```

#### 2.2 Test Your Custom Rules (10 minutes)

For each of your 3 custom predicates, create **2 different queries** that demonstrate it works:

**Example:**
```prolog
% Testing share_prerequisite predicate:
?- share_prerequisite(Course1, Course2, data_structures).
% Expected: Find all pairs of courses that have data_structures as prerequisite

?- share_prerequisite(algorithms, artificial_intelligence, X).
% Expected: Find prerequisites shared by these two courses
```

#### 2.3 Document Your Results (10 minutes)

For each query, record:
- The query you entered
- The result Prolog returned
- Brief explanation of what the query does

---

### Part 3: Analysis and Reflection (30 minutes)

#### 3.1 Query Analysis (15 minutes)

Answer the following:

1. **Most Useful Query**: Which query provides the most useful information for a student or advisor? Why?

2. **Unexpected Results**: Did any query produce surprising results? Explain what happened and why.

3. **Limitations**: What information from your semantic network diagram couldn't be easily represented in Prolog? Why?

4. **Comparison to Traditional Programming**: How is writing Prolog different from programming in languages like Python or Java? Give specific examples.

#### 3.2 Reflection (15 minutes)

Write a reflection (250-300 words) addressing:

- What was most challenging about implementing your semantic network in Prolog?
- How did Prolog's logical inference help you derive new knowledge?
- How could this type of knowledge representation be useful in AI applications?
- What would you do differently if you had to design the semantic network again from scratch?
- How does the declarative nature of Prolog compare to imperative programming you've done before?

---

## Deliverables

Submit the following:

1. **Prolog Source Code File** (`.pl` file)
   - Save your program from SWISH
   - File → Download
   - Name it: `YourLastName_Assignment3.pl`
   - Must include all required facts and rules
   - Must be well-commented

2. **Query Testing Document** (PDF)
   - All 8+ basic queries with results
   - All 6 custom predicate test queries with results
   - Screenshots from SWISH showing queries working
   - Include at least 2 screenshots of successful queries

3. **Analysis and Reflection Document** (PDF)
   - Answers to all Part 3.1 questions
   - Your reflection essay
   - 2-3 pages total

4. **Updated Semantic Network Diagram** (Optional but recommended)
   - If you made changes during implementation
   - Annotated with Prolog predicate names

**Total Package: 3-4 documents in a single ZIP file**

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Facts Completeness** | 15+ facts, diverse, accurate | 12-14 facts, mostly accurate | 10-11 facts, some issues | <10 facts or many errors | /15 |
| **Provided Rules** | All 5 rules work correctly | 4 rules work, 1 has issues | 3 rules work correctly | <3 working rules | /15 |
| **Custom Predicates** | 3 sophisticated, working rules | 3 rules, minor issues | 2-3 basic rules | <2 or non-functional | /20 |
| **Query Testing** | 8+ queries, well-documented, screenshots | 6-7 queries, good docs | 5-6 queries, basic docs | <5 or poor documentation | /15 |
| **Code Quality** | Clean, well-commented, organized | Good structure, some comments | Basic organization | Messy or uncommented | /10 |
| **Analysis** | Thorough, insightful answers | Good analysis | Basic answers | Superficial or incomplete | /15 |
| **Reflection** | Thoughtful, demonstrates learning | Good reflection | Basic reflection | Superficial | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

### Debugging Prolog Programs

**Common Error 1: Syntax errors**
```prolog
% WRONG:
belongs_to(Data Structures, Computer Science).  % Spaces in atoms!

% RIGHT:
belongs_to(data_structures, computer_science).  % Use underscores
```

**Common Error 2: Missing periods**
```prolog
% WRONG:
parent(john, mary)  % Missing period

% RIGHT:
parent(john, mary).
```

**Common Error 3: Variable/Atom confusion**
```prolog
% WRONG:
taught_by(Course, dr_smith) :- belongs_to(course, computer_science).
% 'Course' and 'course' are different! One is variable, one is atom

% RIGHT:
taught_by(Course, dr_smith) :- belongs_to(Course, computer_science).
```

### Testing Strategy

1. **Start Simple**: Test basic facts before complex rules
2. **One at a Time**: Add one rule, test it, then add the next
3. **Use Specific Cases**: Test with specific values first, then try variables
4. **Check Edge Cases**: What if there are no results? Does it handle that?

### Prolog Tips

- **Use meaningful names**: `is_prerequisite_of` is better than `prereq`
- **Comment your code**: Explain what each rule does
- **Test incrementally**: Don't write everything then test
- **Use the trace feature**: In SWISH, you can trace how Prolog finds answers
- **Variables are your friend**: Use them to find all possible answers

---

## Common Pitfalls to Avoid

1. **Don't use spaces in atom names** - use underscores: `data_structures` not `data structures`
2. **Don't forget the period** - every fact and rule ends with `.`
3. **Don't confuse atoms and variables** - atoms start lowercase, variables start uppercase
4. **Don't create circular rules** - `a :- b. b :- a.` will cause infinite loops
5. **Don't forget to test** - a rule that looks right might not work as expected
6. **Don't plagiarize** - your custom rules should be YOUR OWN work

---

## Resources

### Official Resources
- SWISH Online: https://swish.swi-prolog.org/
- SWI-Prolog Documentation: https://www.swi-prolog.org/pldoc/
- Prolog Tutorial: https://www.swi-prolog.org/pldoc/man?section=quickstart

### Helpful Tutorials
- Learn Prolog Now: http://www.learnprolognow.org/
- Prolog Syntax Quick Reference: https://www.swi-prolog.org/pldoc/man?section=syntax

### From Previous Assignments
- Your Assignment 2 pseudo-code (use as starting point!)
- Your semantic network diagram (reference for relationships)
- Session 9 lecture notes

---

## Example of Complete Work

Here's an example of a well-implemented custom predicate:

```prolog
% Custom Rule: Find all courses a student needs before taking a target course
% This includes both direct and indirect prerequisites
all_prerequisites(TargetCourse, Prereq) :-
    is_prerequisite_of(Prereq, TargetCourse).

all_prerequisites(TargetCourse, Prereq) :-
    is_prerequisite_of(DirectPrereq, TargetCourse),
    all_prerequisites(DirectPrereq, Prereq).
```

**Wait!** This rule uses recursion, which we're not requiring for this assignment. But it shows what's possible! For your assignment, simpler non-recursive rules are perfectly fine.

**Here's a simpler example without recursion:**

```prolog
% A course is foundational if it's a prerequisite for at least 2 other courses
is_foundational_course(Course) :-
    is_prerequisite_of(Course, Course1),
    is_prerequisite_of(Course, Course2),
    Course1 \= Course2.
```

---

## Frequently Asked Questions

**Q: Can I use my exact facts from Assignment 2's pseudo-code?**
A: Yes! That's exactly what you should do. Just make sure the syntax is correct Prolog.

**Q: What if my rules don't work?**
A: Use SWISH's trace feature, check your syntax, make sure facts exist to test the rule with, and start with simpler versions.

**Q: Can I add more than the minimum requirements?**
A: Absolutely! Extra facts and rules (if correct) can earn bonus points.

**Q: Do all my queries need to return results?**
A: No. Showing that a query returns `false` or `no results` is also valuable testing.

**Q: Can I work with a partner?**
A: You can discuss concepts, but all code must be your own. Your custom predicates must be original.

**Q: What if I want to use recursion?**
A: You're welcome to try it for extra credit, but it's not required and won't be graded.

**Q: How do I download my code from SWISH?**
A: File → Download, or copy/paste into a text editor and save as `.pl`

---


## Connection to Future Learning

This assignment introduces you to:
- **Logic-based AI**: Many AI systems use logical reasoning
- **Expert Systems**: Knowledge bases like yours are used in medical diagnosis, legal systems, etc.
- **Semantic Web**: Technologies like RDF and OWL extend these concepts to the entire internet
- **Database Query Languages**: SQL and SPARQL share concepts with Prolog
- **Constraint Satisfaction**: Prolog is excellent for solving scheduling and planning problems

Understanding how to represent and reason about knowledge is a fundamental AI skill that applies across many domains!

---

**Due Date**: Sunday, Feb 22th by midnight
**Submission**: Brightspace


---

## Final Checklist

Before submitting, make sure you have:
- [ ] At least 15 facts in your knowledge base
- [ ] All 5 provided rules are present and working
- [ ] 3 custom predicates that YOU created
- [ ] At least 8 basic test queries documented
- [ ] 6 queries testing your custom predicates (2 per predicate)
- [ ] Screenshots showing successful queries in SWISH
- [ ] Answers to all analysis questions
- [ ] Reflection essay (250-300 words)
- [ ] Code is well-commented and organized
- [ ] All files named correctly
- [ ] Everything in a single ZIP file

**Good luck! Welcome to the world of logic programming!**

Remember: Prolog might feel strange at first, but it's incredibly powerful for knowledge representation. You're not just learning a programming language - you're learning a new way to think about problems and solutions. Enjoy the journey!
