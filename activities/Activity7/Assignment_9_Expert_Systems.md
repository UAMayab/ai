# Assignment 9: Expert Systems Case Study Analysis
**Session 15 - Expert Systems**
**Estimated Time: 2 hours**

---

## Learning Objectives

By completing this assignment, you will be able to:
1. Analyze and compare architectures of different expert systems
2. Understand various approaches to knowledge representation
3. Evaluate inference engines and reasoning methods
4. Assess strengths and limitations of expert system designs
5. Apply expert system principles to real-world problems

---

## Background

Expert systems are AI programs that emulate the decision-making ability of human experts in specific domains. Since the 1970s, expert systems have been successfully applied in medicine, engineering, finance, and many other fields.

An expert system typically consists of:
- **Knowledge Base**: Domain expertise encoded as facts and rules
- **Inference Engine**: Reasoning mechanism that applies rules
- **User Interface**: How users interact with the system
- **Explanation Facility**: Explains how conclusions were reached
- **Knowledge Acquisition Module**: How expert knowledge is captured

In this assignment, you'll analyze and compare **two classic expert systems** to understand their design philosophies, strengths, weaknesses, and applications.

---

## Assignment Overview

You will:
1. Study two expert systems in depth
2. Compare their architectures, knowledge representation, and inference methods
3. Analyze their real-world impact and limitations
4. Propose improvements based on your analysis

---

## Part 1: Expert System Selection (10 minutes)

Choose **TWO** expert systems from the following list to analyze:

### Option A: MYCIN (Medical Diagnosis)
- **Domain**: Bacterial infection diagnosis and treatment
- **Developed**: Stanford University, 1970s
- **Key Feature**: Certainty factors for handling uncertainty
- **Architecture**: Backward chaining rule-based system
- **Impact**: Pioneered medical expert systems

### Option B: DENDRAL (Chemistry)
- **Domain**: Chemical structure analysis
- **Developed**: Stanford University, 1965-1980
- **Key Feature**: Generate-and-test paradigm
- **Architecture**: Forward and backward chaining
- **Impact**: One of the first expert systems

### Option C: XCON (R1) (Manufacturing Configuration)
- **Domain**: Computer system configuration
- **Developed**: Digital Equipment Corporation, 1978
- **Key Feature**: Constraint satisfaction
- **Architecture**: Forward chaining production system
- **Impact**: Saved millions in manufacturing costs

### Option D: PROSPECTOR (Geology/Mining)
- **Domain**: Mineral exploration and deposit evaluation
- **Developed**: SRI International, 1970s-1980s
- **Key Feature**: Bayesian probability networks
- **Architecture**: Mixed inference strategies
- **Impact**: Successfully discovered molybdenum deposit

### Option E: CLIPS (General Purpose)
- **Domain**: General-purpose expert system shell
- **Developed**: NASA, 1985
- **Key Feature**: Highly portable, flexible architecture
- **Architecture**: Forward chaining rule-based system
- **Impact**: Widely used for building custom expert systems

### Option F: IBM Watson (Modern AI System)
- **Domain**: Question answering, various applications
- **Developed**: IBM, 2011
- **Key Feature**: Natural language processing, machine learning
- **Architecture**: Hybrid system with multiple AI techniques
- **Impact**: Won Jeopardy!, applied to healthcare and business

**Selection Rules:**
- Choose systems from **different eras** (e.g., classic + modern, or two classics from different domains)
- Choose systems with **different architectures** (e.g., forward vs backward chaining)
- Ensure sufficient information is available for analysis

**Recommended Combinations:**
- MYCIN + Watson (medical, classic vs modern)
- DENDRAL + PROSPECTOR (scientific, different domains)
- XCON + CLIPS (practical applications)
- MYCIN + XCON (different inference approaches)

---

## Part 2: Individual System Analysis (45 minutes per system)

For EACH of your two chosen systems, research and document the following:

### Section 1: System Overview (150-200 words)
- What problem does it solve?
- Who developed it and when?
- What was the motivation/need?
- What is its historical significance?

### Section 2: Architecture Analysis (300-400 words)

#### Knowledge Base
- How is knowledge represented? (rules, frames, semantic networks, etc.)
- Give 3-5 example rules or facts
- How many rules/facts does the system contain?
- How is domain knowledge organized?

#### Inference Engine
- What reasoning strategy is used? (forward chaining, backward chaining, mixed)
- Explain how the inference process works with an example
- How does it handle uncertainty? (if applicable)
- What conflict resolution strategies are used?

#### User Interface
- How do users interact with the system?
- What inputs does it require?
- How are results/recommendations presented?
- Does it provide explanations for its conclusions?

### Section 3: Knowledge Representation Example (200-300 words)

Provide a detailed example of how the system represents and uses knowledge:

**Example Template:**
```
IF-THEN Rule Example:
IF [condition 1]
AND [condition 2]
THEN [conclusion] with [certainty/confidence]

How it works:
[Explain the reasoning process]

Example Case:
[Walk through a specific example]
```

### Section 4: Performance and Impact (200-300 words)
- How well does/did the system perform?
- What real-world problems has it solved?
- What are its successes?
- What are its limitations or failures?
- How is it used today (if still in use)?

### Section 5: Strengths and Weaknesses (200-300 words)

**Strengths:**
- What does this system do particularly well?
- What innovations did it introduce?
- What advantages does its architecture provide?

**Weaknesses:**
- What are its limitations?
- What types of problems can't it handle well?
- What assumptions does it make?
- How does it deal with incomplete or incorrect information?

---

## Part 3: Comparative Analysis (30 minutes)

Now compare your two systems across multiple dimensions:

### Comparison Table

Create a comprehensive comparison table:

| Aspect | System 1: [Name] | System 2: [Name] |
|--------|-----------------|-----------------|
| **Domain** | | |
| **Era/Year** | | |
| **Knowledge Representation** | | |
| **Inference Method** | | |
| **Handling Uncertainty** | | |
| **Number of Rules** | | |
| **User Interaction** | | |
| **Explanation Capability** | | |
| **Knowledge Acquisition** | | |
| **Performance** | | |
| **Current Status** | | |

### Detailed Comparison Questions (300-400 words)

Answer the following:

**Question 1: Architecture Differences**
- How do their architectures differ fundamentally?
- Why did each choose their particular approach?
- Which architecture is more suitable for its domain? Why?

**Question 2: Knowledge Representation**
- How do they represent expert knowledge differently?
- What are the advantages of each approach?
- Which is more flexible? Which is more efficient?

**Question 3: Reasoning Approach**
- Compare their inference/reasoning strategies
- Why does each use forward/backward chaining (or mixed)?
- How does this affect their problem-solving capabilities?

**Question 4: Practical Application**
- Which system had greater real-world impact?
- Which architecture is more maintainable/scalable?
- Which better handles complex, uncertain environments?

---

## Part 4: Critical Evaluation and Future Directions (25 minutes)

### Section 1: Lessons Learned (200-300 words)
- What can we learn from these systems about expert system design?
- What principles from these systems are still relevant today?
- What approaches have been superseded by modern AI?
- How have modern ML/AI techniques addressed their limitations?

### Section 2: Design a Hybrid System (250-350 words)

Imagine you're designing a NEW expert system that combines the best features of both systems you studied.

**Describe:**
- What domain would it target?
- What would you take from System 1?
- What would you take from System 2?
- What modern AI techniques would you add?
- How would knowledge be represented?
- What inference method would you use?
- How would it handle uncertainty?

**Justify your design choices.**

### Section 3: Modern Relevance (150-200 words)
- Are rule-based expert systems still relevant in the age of machine learning?
- Where do traditional expert systems excel compared to ML models?
- Where does ML outperform expert systems?
- What's the role of hybrid systems combining both approaches?

---

## Deliverables

Submit **ONE PDF document** containing:

1. **Title Page**
   - Assignment title
   - Your name
   - Systems analyzed
   - Date

2. **Introduction** (1 page)
   - Brief overview of expert systems
   - Why you chose these two systems
   - What you'll analyze

3. **System 1 Analysis** (3-4 pages)
   - All sections from Part 2
   - Include diagrams if helpful

4. **System 2 Analysis** (3-4 pages)
   - All sections from Part 2
   - Include diagrams if helpful

5. **Comparative Analysis** (2-3 pages)
   - Comparison table
   - Detailed comparison questions

6. **Critical Evaluation** (2-3 pages)
   - All sections from Part 4

7. **Conclusion** (1 page)
   - Summary of key insights
   - Personal reflections

8. **References** (1-2 pages)
   - At least 6-8 scholarly sources
   - Properly formatted (APA or IEEE style)

**Total Length: 12-16 pages**
**Filename:** `LastName_Assignment9_ExpertSystems.pdf`

---

## Grading Rubric (100 points)

| Criterion | Excellent (90-100%) | Good (75-89%) | Satisfactory (60-74%) | Needs Improvement (<60%) | Points |
|-----------|-------------------|---------------|---------------------|------------------------|---------|
| **System 1 Analysis** | Thorough, detailed, insightful | Good coverage, solid understanding | Basic analysis | Superficial or incomplete | /20 |
| **System 2 Analysis** | Thorough, detailed, insightful | Good coverage, solid understanding | Basic analysis | Superficial or incomplete | /20 |
| **Comparative Analysis** | Excellent comparison, clear insights | Good comparison with detail | Basic comparison | Weak comparison | /20 |
| **Critical Evaluation** | Sophisticated, forward-thinking | Good insights and proposals | Basic evaluation | Limited critical thinking | /15 |
| **Understanding** | Demonstrates mastery of concepts | Good understanding | Basic understanding | Limited understanding | /10 |
| **Research Quality** | Excellent sources, well-cited | Good sources, properly cited | Adequate sources | Poor or missing sources | /10 |
| **Writing & Organization** | Professional, clear, well-structured | Good organization | Basic structure | Poor organization | /5 |
| **TOTAL** | | | | | /100 |

---

## Research Resources

### Primary Sources

**Classic Papers:**
- Buchanan & Shortliffe (1984) - "Rule-Based Expert Systems: The MYCIN Experiments"
- McDermott (1982) - "R1: A Rule-Based Configurer of Computer Systems"
- Duda, Hart & Nilsson (1976) - "Subjective Bayesian Methods for Rule-Based Inference Systems"

**Books:**
- Jackson, P. (1998). "Introduction to Expert Systems"
- Giarratano & Riley (2005). "Expert Systems: Principles and Programming"
- Luger & Stubblefield (1993). "Artificial Intelligence: Structures and Strategies"

### Online Resources

**Academic Databases:**
- IEEE Xplore: https://ieeexplore.ieee.org/
- ACM Digital Library: https://dl.acm.org/
- Google Scholar: https://scholar.google.com/

**Expert System Information:**
- MYCIN: https://pmc.ncbi.nlm.nih.gov/articles/PMC2464549/
- MYCIN: https://www.britannica.com/technology/MYCIN
- MYCIN: https://en.wikipedia.org/wiki/Mycin
- DENDRAL: https://web.mit.edu/6.034/www/6.s966/dendral-history.pdf
- DENDRAL: https://www.britannica.com/technology/artificial-intelligence
- DENDRAL: https://profiles.nlm.nih.gov/spotlight/bb/feature/ai
- CLIPS: http://www.clipsrules.net/
- IBM Watson: https://www.ibm.com/watson

**Wikipedia** (starting point only, not as primary source):
- Expert System: https://en.wikipedia.org/wiki/Expert_system
- Specific system pages for overview

### University Libraries
- Check the university library for access to academic journals
- Many classic AI papers are freely available online

---

## Tips for Success

### Research Strategy
1. **Start broad**: Wikipedia/textbooks for overview
2. **Go deep**: Find original papers and case studies
3. **Find examples**: Look for concrete rule examples
4. **Check citations**: Follow references to find more sources
5. **Use recent sources**: Find modern perspectives on classic systems

### Analysis Strategy
1. **Understand before comparing**: Analyze each system thoroughly first
2. **Look for patterns**: What design choices repeat? Why?
3. **Think critically**: Don't just describe - evaluate and critique
4. **Connect to theory**: Relate to concepts from Session 15
5. **Be specific**: Use concrete examples, not generalizations

### Writing Tips
1. **Use clear headings**: Make structure obvious
2. **Include diagrams**: Visualize architectures and processes
3. **Provide examples**: Rule examples, reasoning traces
4. **Cite properly**: Give credit for all sources
5. **Proofread**: Check for clarity and errors

### Common Pitfalls to Avoid
- **Don't just summarize**: Analyze and critique
- **Don't ignore weaknesses**: Every system has limitations
- **Don't skip examples**: Concrete examples demonstrate understanding
- **Don't forget citations**: All facts need sources
- **Don't compare superficially**: Go beyond surface differences

---

## Example Rule Representations

To help you understand how to present expert system rules, here are examples:

### MYCIN-style Rule (Medical Diagnosis):
```
RULE037
IF:
  (1) The infection is primary-bacteremia, AND
  (2) The site of the culture is blood, AND
  (3) The suspected portal of entry is the gastrointestinal tract, AND
  (4) The patient's age is greater than 10 years
THEN:
  There is evidence (0.7) that the identity of the organism is
  bacteroides
```

### XCON-style Rule (Configuration):
```
IF:
  The system requires a disk drive, AND
  The available space in the cabinet is at least 5.25 inches, AND
  The budget allows for additional storage
THEN:
  Configure an RD53 disk drive in the available slot
```

### PROSPECTOR-style Rule (with probabilities):
```
IF:
  Quartz content is high (P=0.8), AND
  Rock alteration is moderate (P=0.6)
THEN:
  Probability of porphyry copper deposit = 0.7
```

---

## Sample Comparison Questions

To guide your comparative analysis:

**Architecture:**
- Why did MYCIN use backward chaining while XCON used forward chaining?
- How does the choice of chaining strategy affect system behavior?

**Knowledge Representation:**
- Why did MYCIN use certainty factors while PROSPECTOR used Bayesian probabilities?
- Which approach to uncertainty is more intuitive? More mathematically sound?

**Scalability:**
- Which system architecture scales better to thousands of rules?
- How do maintenance requirements differ?

**Explanation:**
- How does MYCIN explain its reasoning to users?
- Why is explanation important in medical systems but less so in configuration systems?

---

## Assignment Checklist

Before submitting, verify you have:

- [ ] Analyzed two different expert systems in depth
- [ ] Included all required sections for each system
- [ ] Provided concrete examples of rules/knowledge representation
- [ ] Created comprehensive comparison table
- [ ] Answered all comparative analysis questions
- [ ] Proposed a hybrid system design
- [ ] Discussed modern relevance and future directions
- [ ] Included 6-8 properly cited scholarly sources
- [ ] Proofread for clarity and correctness
- [ ] PDF is 12-16 pages
- [ ] Followed formatting guidelines

---

## Connection to Previous Assignments

While this assignment doesn't involve programming, it connects to earlier work:

- **Assignments 1-4 (Semantic Networks, Prolog)**: Expert systems use similar knowledge representation techniques
- **Assignments 5-6 (Search Algorithms)**: Inference engines use search strategies
- **Assignments 7-8 (BFS, Heuristic Search)**: Expert systems reason through solution spaces

**Key Insight**: Expert systems combine knowledge representation (like your semantic networks) with reasoning strategies (like your search algorithms) to solve real problems.

---

## Frequently Asked Questions

**Q: Can I analyze two modern AI systems instead of classic expert systems?**
A: You should include at least one classic rule-based expert system. Pairing a classic with a modern system (like Watson) makes an excellent comparison.

**Q: How technical should my analysis be?**
A: Be specific about architectures and algorithms, but explain concepts clearly. Use diagrams to help.

**Q: Where can I find actual rules from these systems?**
A: Original papers, textbooks, and online archives. See Resources section.

**Q: What if I can't find complete information about a system?**
A: That's okay - do your best with available sources. Document what you couldn't find and explain why.

**Q: Can I interview an expert who has used these systems?**
A: Absolutely! This would be an excellent primary source. Document it in your references.

**Q: Should I focus more on one system than the other?**
A: No - give equal attention to both systems.

---

**Due Date:** Saturday, March 8th, 2026 by midnight
**Submission:** Brightspace (upload PDF)

---

## Final Thoughts

Expert systems represent a crucial chapter in AI history. While modern machine learning dominates current AI research, the principles of expert systems - knowledge representation, reasoning, explanation - remain fundamental to AI.

By analyzing these systems, you'll understand:
- How AI was successfully applied before deep learning
- The value of explicit knowledge and reasoning
- Why explainability matters (something ML often lacks)
- How to combine human expertise with computational reasoning

**Approach this assignment with curiosity**: These systems solved real problems and saved lives, money, and time. What can we learn from them?

Good luck with your analysis!
