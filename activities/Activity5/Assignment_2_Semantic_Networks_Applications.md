# Assignment 2: Applying and Expanding Semantic Networks
**Session 8 - Examples of Construction and Use of Semantic Networks**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Enhance existing semantic networks with hierarchical structures
2. Apply semantic network concepts to real-world applications
3. Analyze and identify different types of knowledge representation
4. Design inference rules based on semantic relationships
5. Prepare a semantic network for implementation in a programming language

---

## Background

Building on Assignment 1, you will now expand and refine your university course semantic network. This assignment focuses on making your network more sophisticated and preparing it for implementation in Prolog (Assignment 3).

In real-world applications, semantic networks must not only represent explicit knowledge (facts) but also support inference and reasoning (rules). For example, if Course A is a prerequisite for Course B, and Course B is a prerequisite for Course C, then implicitly, Course A is required before Course C.

---

## Prerequisites

- **Completed Assignment 1** 
- Your semantic network diagram from Assignment 1
- Understanding of hierarchical vs. flat networks (Session 7 material)

---

## Assignment Instructions

### Part 1: Network Enhancement (45 minutes)

Take your semantic network from Assignment 1 and enhance it by adding the following:

#### 1.1 Hierarchical Organization (15 minutes)

Add hierarchical levels to your network:
- **Level 0 (Root)**: University or College
- **Level 1**: Departments
- **Level 2**: Course Categories (e.g., "Core Courses", "Electives", "Lab Courses")
- **Level 3**: Individual Courses
- **Level 4**: Topics/Concepts covered in courses

**Example:**
```
[University]
    |
    |--belongs_to--> [Computer Science Dept]
    |                       |
    |                       |--offers--> [Core Courses]
    |                       |                |
    |                       |                |--includes--> [Data Structures]
    |                       |                |--includes--> [Algorithms]
    |                       |
    |                       |--offers--> [Elective Courses]
    |                                        |
    |                                        |--includes--> [AI]
    |                                        |--includes--> [Machine Learning]
```

#### 1.2 Add Temporal Relationships (15 minutes)

Include time-based information:
- **academic_level**: (100-level, 200-level, 300-level, 400-level)
- **typical_semester**: (Fall, Spring, Both)
- **credit_hours**: (1, 2, 3, 4 credits)

Create at least 5 new relationships showing:
- Which courses are typically taken in which year
- Which courses should be taken in sequence

#### 1.3 Add Attribute Nodes (15 minutes)

Add nodes representing attributes:
- Difficulty level (Beginner, Intermediate, Advanced)
- Course format (Lecture, Lab, Hybrid, Online)
- Skills acquired (e.g., "Programming", "Problem Solving", "Critical Thinking")

Connect these attributes to appropriate courses.

**Your enhanced network should now have:**
- **Minimum 20-25 nodes**
- **Minimum 25-30 relationships**
- **Clear hierarchical structure**
- **At least 5 different relationship types**

### Part 2: Knowledge Representation Analysis (30 minutes)

#### 2.1 Declarative Knowledge (15 minutes)

Identify and list **10 declarative facts** from your network. Declarative knowledge represents static facts.

**Format:**
```
Fact 1: Data Structures belongs_to Computer Science Department
Fact 2: Data Structures is_taught_by Dr. Martinez
Fact 3: Data Structures covers_topic Trees
...
```

#### 2.2 Procedural Knowledge (15 minutes)

Identify and create **5 inference rules** (procedural knowledge) that can be derived from your network. These rules show HOW to derive new knowledge from existing facts.

**Format:**
```
Rule 1: A student can_enroll_in Course X IF:
        - Student has_completed all prerequisites of Course X

Rule 2: Course X is_advanced_course IF:
        - Course X academic_level is 300 or higher

Rule 3: Student meets_requirements_for Department D IF:
        - Student has_completed at least 3 courses that belong_to Department D

Rule 4: Course X is_foundational_for Course Y IF:
        - Course X is_prerequisite_of Course Y
        OR
        - Course X is_prerequisite_of some Course Z AND Course Z is_prerequisite_of Course Y

Rule 5: Professor P is_expert_in Topic T IF:
        - Professor P teaches Course C AND Course C covers_topic Topic T
```

**Your rules should follow this format:**
- IF [conditions based on relationships in your network]
- THEN [new knowledge that can be inferred]

### Part 3: Application Design (30 minutes)

#### 3.1 Use Case Scenarios (15 minutes)

Describe **3 practical use cases** for your semantic network in a university system:

**Example Use Case:**
```
Use Case 1: Course Prerequisite Checker

Actor: Student advisor
Scenario: A student wants to enroll in "Machine Learning" course.
System uses the semantic network to:
1. Find all courses that are prerequisites for "Machine Learning"
2. Check which prerequisites have prerequisites themselves
3. Generate a complete prerequisite chain
4. Compare with student's completed courses
5. Inform if student is eligible or what courses are still needed

Benefits: Saves time, prevents enrollment errors, helps with academic planning
```

Create similar descriptions for 3 different use cases such as:
- Course recommendation system
- Professor expertise finder
- Degree requirement tracker
- Course schedule optimizer
- Academic path planner

#### 3.2 Query Examples (15 minutes)

For each use case above, write **2-3 specific queries** that the system would need to answer:

**Example for Use Case 1:**
```
Query 1: What are all prerequisites for [Course X]?
Query 2: Has student [Student Y] completed all prerequisites for [Course X]?
Query 3: What is the shortest path of courses from [Course A] to [Course C]?
```

### Part 4: Preparation for Implementation (15 minutes)

You will implement this network in Prolog in Assignment 3. To prepare:

#### 4.1 Fact Representation

Choose 5 facts from your network and write them in a **pseudo-code format** that looks like Prolog:

**Example:**
```
belongs_to(data_structures, computer_science).
is_prerequisite_of(calculus_1, calculus_2).
taught_by(algorithms, dr_smith).
covers_topic(data_structures, trees).
academic_level(data_structures, 200).
```

Notice the format: `relationship_name(entity1, entity2).`

#### 4.2 Rule Representation

Choose 2 rules from Part 2.2 and express them in pseudo-code:

**Example:**
```
can_enroll(Student, Course) IF
    prerequisite(PrereqCourse, Course) AND
    completed(Student, PrereqCourse).

is_advanced_course(Course) IF
    academic_level(Course, Level) AND
    Level >= 300.
```

---

## Deliverables

Submit the following in a **single document** (PDF):

1. **Enhanced Semantic Network Diagram**
   - Clearly showing hierarchical levels
   - With legend for all symbols and relationship types
   - Properly labeled

2. **Knowledge Representation Analysis**
   - 10 declarative facts listed
   - 5 inference rules with clear explanations
   - Explanation of how each rule derives new knowledge

3. **Application Design Section**
   - 3 detailed use case descriptions
   - 6-9 query examples (2-3 per use case)

4. **Implementation Preparation**
   - 5 facts in pseudo-code format
   - 2 rules in pseudo-code format
   - Brief explanation (100 words) of your notation choices

5. **Reflection** (200-250 words)
   - How did adding hierarchy change your understanding?
   - What was challenging about creating inference rules?
   - How might this network be used in AI applications?

**Total Length: 4-6 pages including diagram**

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Enhanced Network** | 25+ nodes, clear hierarchy, 30+ relationships | 20-24 nodes, good structure, 25-29 relationships | 18-19 nodes, basic hierarchy, 20-24 relationships | Missing requirements | /25 |
| **Declarative Facts** | 10 clear, accurate facts, well-formatted | 8-9 facts, minor issues | 6-7 facts, some unclear | <6 or incorrect facts | /10 |
| **Inference Rules** | 5 sophisticated rules, logically sound | 4-5 rules, mostly sound | 3 rules, basic logic | <3 or illogical rules | /15 |
| **Use Cases** | 3 detailed, practical use cases with clear benefits | 3 use cases, good detail | 3 use cases, basic detail | <3 or vague use cases | /15 |
| **Query Examples** | 6+ specific, well-designed queries | 6 queries, mostly clear | 4-5 queries | <4 or unclear queries | /10 |
| **Implementation Prep** | Excellent pseudo-code, ready for Prolog | Good pseudo-code, minor issues | Basic pseudo-code | Incorrect or missing | /15 |
| **Reflection** | Insightful, demonstrates learning | Good reflection | Basic reflection | Superficial | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

1. **Build on Feedback**: Incorporate any feedback from Assignment 1
2. **Think About Inference**: Ask yourself "What new information can I derive from existing facts?"
3. **Be Specific**: Vague rules like "IF something THEN something" are not useful
4. **Test Your Logic**: Walk through your rules with examples to ensure they work
5. **Keep Assignment 3 in Mind**: The clearer your pseudo-code now, the easier Assignment 3 will be
6. **Use Consistent Naming**: Use underscores instead of spaces (e.g., `data_structures` not `data structures`)

---

## Common Pitfalls to Avoid

- **Circular Logic**: Make sure rules don't reference themselves
- **Ambiguous Rules**: Be specific about conditions and outcomes
- **Inconsistent Relationships**: Use the same relationship name for similar connections
- **Over-complication**: Start with simple rules and add complexity as needed
- **Ignoring Hierarchy**: Make sure your hierarchical structure is meaningful

---

## Resources

- Session 8 lecture notes
- Your Assignment 1 network and feedback
- Prolog syntax reference (preview for next assignment): https://www.swi-prolog.org/pldoc/man?section=quickstart
- Online diagram tools:
  - draw.io: https://app.diagrams.net/
  - Lucidchart: https://www.lucidchart.com/

---

## Connection to Assignment 3

In the next assignment, you will:
- Convert your pseudo-code into actual Prolog code
- Implement your network in SWISH (online Prolog environment)
- Query your knowledge base
- Test your inference rules

**The better prepared you are now, the smoother Assignment 3 will be!**

---

## Example of Quality Work

**Good Inference Rule:**
```
Rule: A professor is_expert_in a topic IF:
      - The professor teaches a course
      - That course covers the topic

Example:
- dr_martinez teaches data_structures
- data_structures covers_topic trees
- Therefore: dr_martinez is_expert_in trees
```

**Poor Inference Rule (Don't do this):**
```
Rule: Courses are related if they are similar
Example: Some courses are connected somehow
```

The first rule is specific, testable, and implementable. The second is vague and unusable.

---

**Due Date**: Sunday, Feb 22th 2026 before midnight
**Submission**: Brightspace

Remember: This assignment bridges conceptual understanding and practical implementation. Take your time to create logical, well-structured rules that will translate smoothly into Prolog code!

Good luck!
