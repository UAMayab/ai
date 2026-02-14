# Assignment 1: Understanding Semantic Networks
**Session 7 - Introduction to Semantic Networks**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Understand the fundamental concepts of semantic networks
2. Identify nodes and relationships in a knowledge domain
3. Design a semantic network for a real-world scenario
4. Differentiate between various types of relationships (hierarchical, associative, causal)
5. Represent knowledge in a structured, visual format

---

## Background

Semantic networks are powerful tools for representing knowledge through interconnected concepts. In this assignment, you will design a semantic network for a **University Course Management System**. This domain includes courses, professors, departments, prerequisites, and student requirements - all of which are interconnected through various relationships.

As future engineers, understanding how to model knowledge systematically will help you design better databases, AI systems, and information architectures regardless of your engineering specialty.

---

## Assignment Instructions

### Part 1: Domain Analysis (30 minutes)

Before creating your semantic network, you need to understand the domain. Consider the following elements of a university course system:

**Entities (Nodes):**
- Courses (e.g., "Introduction to AI", "Data Structures", "Calculus I")
- Departments (e.g., "Computer Science", "Mathematics", "Engineering")
- Professors (e.g., "Dr. Smith", "Prof. Johnson")
- Topics/Concepts (e.g., "Machine Learning", "Algorithms", "Probability")
- Academic Levels (e.g., "Undergraduate", "Graduate", "100-level", "200-level")

**Relationships (Links):**
- **is_prerequisite_of**: One course must be taken before another
- **belongs_to_department**: A course is offered by a specific department
- **taught_by**: A professor teaches a course
- **covers_topic**: A course includes specific topics
- **requires_knowledge_of**: A course assumes certain background knowledge
- **is_corequisite_of**: Two courses must be taken together
- **is_part_of**: A course belongs to a program or track

### Part 2: Design Your Semantic Network (60 minutes)

Create a semantic network that includes **at minimum**:
- **12-15 nodes** representing different entities
- **15-20 relationships** (directed links) connecting these nodes
- **At least 3 different types of relationships**

**Guidelines:**
1. Use circles or boxes to represent nodes
2. Use labeled arrows to represent relationships (the label describes the relationship)
3. Make sure arrows point in the correct direction (e.g., "Calculus I" → is_prerequisite_of → "Calculus II")
4. Include a legend explaining your node types and relationship types

**Example Fragment:**

```
[Data Structures] --is_prerequisite_of--> [Algorithms]
       |                                        |
       |                                        |
  belongs_to                               belongs_to
       |                                        |
       v                                        v
[Computer Science Dept] <----------- [Computer Science Dept]

[Data Structures] --taught_by--> [Dr. Martinez]

[Data Structures] --covers_topic--> [Trees]
[Data Structures] --covers_topic--> [Graphs]
[Data Structures] --covers_topic--> [Hash Tables]
```

**Your network should tell a story.** For example:
- Which courses lead to which?
- What knowledge builds upon other knowledge?
- How are departments and professors connected?
- What topics span multiple courses?

### Part 3: Network Analysis (20 minutes)

Answer the following questions about your semantic network:

1. **Hierarchical Structures**: Identify at least one hierarchical relationship chain in your network (e.g., foundational course → intermediate course → advanced course)

2. **Network Properties**:
   - Which node has the most connections? Why?
   - Are there any isolated nodes? Should there be?
   - Identify one transitive relationship (if A→B and B→C, then A→C)

3. **Practical Applications**: Describe two practical queries or questions that could be answered using your semantic network. For example:
   - "What are all the prerequisites I need before taking Course X?"
   - "Which courses does Professor Y teach?"

4. **Improvements**: What additional nodes or relationships would make your network more complete and useful?

### Part 4: Reflection (10 minutes)

Write a brief paragraph (150-200 words) reflecting on:
- What was challenging about representing this knowledge?
- How might this semantic network be useful in a real university system?
- How does organizing information this way differ from traditional databases or lists?

---

## Deliverables

Submit the following:

1. **Semantic Network Diagram** (PDF, PNG, or JPG)
   - Can be hand-drawn and scanned, or created digitally
   - Must be clear and legible
   - Must include a legend

2. **Written Analysis** (PDF or Word document)
   - Answers to Part 3 questions
   - Reflection from Part 4
   - 1-2 pages maximum

3. **Node and Relationship List** (in your written document)
   - List all nodes with brief descriptions
   - List all relationships with their meanings

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **Network Completeness** | 15+ nodes, 20+ relationships, diverse types | 12-14 nodes, 15-19 relationships | 10-11 nodes, 12-14 relationships | <10 nodes or <12 relationships | /25 |
| **Accuracy & Logic** | All relationships are logical and correctly directed | Most relationships correct, minor errors | Some illogical connections | Many errors in relationships | /20 |
| **Visual Clarity** | Clear, organized, easy to follow with legend | Mostly clear, minor organization issues | Somewhat cluttered but understandable | Difficult to read or understand | /15 |
| **Network Analysis** | Thorough, insightful answers with specific examples | Good answers with some detail | Basic answers, lacking depth | Incomplete or superficial answers | /20 |
| **Practical Application** | Excellent examples of queries and use cases | Good examples with some detail | Basic examples | Weak or missing examples | /10 |
| **Reflection** | Thoughtful, demonstrates deep understanding | Good reflection with some insight | Basic reflection | Superficial or missing | /10 |
| **TOTAL** | | | | | /100 |

---

## Tips for Success

1. **Start Simple**: Begin with 5-6 core courses and their obvious relationships, then expand
2. **Think Like a Student**: What information would YOU want to know about courses?
3. **Use Real Examples**: Base your network on actual courses from your program
4. **Check Directions**: Make sure arrow directions make sense (prerequisites point forward in time)
5. **Be Consistent**: Use the same relationship names for similar connections
6. **Don't Overcomplicate**: A clear, simple network is better than a cluttered complex one

---


## Connection to Next Assignments

This semantic network will serve as the foundation for your next two assignments. In Assignment 2, you'll analyze and expand this network with more sophisticated features. In Assignment 3, you'll implement this network in Prolog, transforming your visual representation into executable code.

**Save your work carefully - you'll need it for the next assignments!**

---

**Due Date**: Sunday, Feb 22th 2026 before midnight.
**Submission**: Brightspace	

Good luck! Remember, the goal is to learn how to represent knowledge systematically. There's no single "correct" network - creativity and logical thinking are both valued.
