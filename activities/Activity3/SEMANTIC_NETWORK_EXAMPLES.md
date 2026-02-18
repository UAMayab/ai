# Semantic Networks Examples

This document presents five examples of semantic networks, arranged from simple to complex. Each example builds upon concepts introduced in previous ones, helping you understand how semantic networks can represent knowledge in various domains.

---

## Example 1: Simple Family Relationships (Basic Semantic Network)

### Complexity Level: ⭐ Beginner

### Description
This is the most basic semantic network, representing simple family relationships between four people. It demonstrates the fundamental concept of nodes (representing people) and directed links (representing relationships).

### Network Structure

```
    John ────is_parent_of───→ Mary
      ↓
   is_parent_of
      ↓
    Paul ────is_married_to───→ Susan
```

### Detailed Representation

**Nodes (Concepts):**
- John (Person)
- Mary (Person)
- Paul (Person)
- Susan (Person)

**Links (Relationships):**
- John → is_parent_of → Mary
- John → is_parent_of → Paul
- Paul → is_married_to → Susan

### Key Learning Points
1. **Nodes** represent individual entities or concepts (in this case, people)
2. **Directed links** show the direction of relationships (parent → child, not child → parent)
3. **Relationship labels** give semantic meaning to connections
4. This network allows simple queries like: "Who are John's children?" or "Who is Paul married to?"

### Applications
- Family tree systems
- Genealogy databases
- Social network basics

---

## Example 2: Animal Classification (Hierarchical Semantic Network)

### Complexity Level: ⭐⭐ Elementary

### Description
This example introduces hierarchical organization using "is_a" relationships, demonstrating how semantic networks can represent taxonomies and inheritance of properties. This is a fundamental pattern in knowledge representation.

### Network Structure

```
                    Animal
                   /      \
               is_a        is_a
                /            \
            Mammal          Bird
           /      \        /    \
        is_a    is_a    is_a   is_a
         /        \      /       \
       Dog       Cat   Eagle   Penguin
```

### Detailed Representation

**Nodes (Concepts):**
- Animal (Abstract Category)
- Mammal (Category)
- Bird (Category)
- Dog (Concrete Entity)
- Cat (Concrete Entity)
- Eagle (Concrete Entity)
- Penguin (Concrete Entity)

**Links (Relationships):**
- Dog → is_a → Mammal
- Cat → is_a → Mammal
- Mammal → is_a → Animal
- Eagle → is_a → Bird
- Penguin → is_a → Bird
- Bird → is_a → Animal

**Property Inheritance:**
- Animal: {has_life, can_move, needs_food}
- Mammal: inherits Animal properties + {has_fur, warm_blooded, gives_birth}
- Bird: inherits Animal properties + {has_feathers, has_wings, lays_eggs}
- Dog: inherits all Mammal properties + {barks, loyal}
- Penguin: inherits all Bird properties + {cannot_fly, swims}

### Key Learning Points
1. **Hierarchical structure** organizes knowledge from general (top) to specific (bottom)
2. **Property inheritance** allows lower nodes to inherit characteristics from upper nodes
3. **Transitivity** applies: if Dog is_a Mammal and Mammal is_a Animal, then Dog is_a Animal
4. This structure supports reasoning: "What properties does a Dog have?" includes properties from Mammal and Animal

### Applications
- Biological taxonomies
- Object-oriented programming class hierarchies
- Product categorization in e-commerce

---

## Example 3: University Course Prerequisites (Directed Graph Network)

### Complexity Level: ⭐⭐⭐ Intermediate

### Description
This example shows a more complex directed network representing course prerequisites in a Computer Science program. It introduces multiple relationship types and demonstrates how semantic networks can model dependencies and requirements.

### Network Structure

```
                Introduction to CS (CS101)
                        ↓
                  requires_prerequisite
                   /            \
                  ↓              ↓
        Data Structures        Programming II
            (CS201)               (CS202)
                ↓                    ↓
          requires_prerequisite   requires_prerequisite
                ↓                    ↓
            Algorithms ←─────────────┘
             (CS301)
                ↓
          requires_prerequisite
                ↓
        Artificial Intelligence
             (CS401)
                ↓
          has_specialization
           /          \
          ↓            ↓
   Machine Learning  Natural Language
      (CS450)         Processing (CS451)
```

### Detailed Representation

**Nodes (Courses):**
- CS101: Introduction to CS {credits: 3, level: freshman, semester: 1}
- CS201: Data Structures {credits: 4, level: sophomore, semester: 3}
- CS202: Programming II {credits: 4, level: sophomore, semester: 2}
- CS301: Algorithms {credits: 4, level: junior, semester: 5}
- CS401: Artificial Intelligence {credits: 4, level: senior, semester: 7}
- CS450: Machine Learning {credits: 3, level: senior, semester: 8}
- CS451: Natural Language Processing {credits: 3, level: senior, semester: 8}

**Links (Relationships):**

*Prerequisites (requires_prerequisite):*
- CS201 → requires_prerequisite → CS101
- CS202 → requires_prerequisite → CS101
- CS301 → requires_prerequisite → CS201
- CS301 → requires_prerequisite → CS202
- CS401 → requires_prerequisite → CS301

*Specializations (has_specialization):*
- CS401 → has_specialization → CS450
- CS401 → has_specialization → CS451

*Co-requisites (can_take_together):*
- CS450 ↔ can_take_together ↔ CS451

### Key Learning Points
1. **Multiple relationship types** create a richer knowledge representation
2. **Path analysis** can determine course sequences: to take CS450, you must complete CS101 → CS201/CS202 → CS301 → CS401
3. **Constraint modeling** represents academic rules and requirements
4. **Symmetric vs. asymmetric relationships**: co-requisites are symmetric (bidirectional), while prerequisites are asymmetric (unidirectional)
5. Enables queries like: "What courses can I take after completing CS201 and CS202?"

### Applications
- Academic planning systems
- Course registration systems
- Skill dependency mapping
- Project task scheduling

---

## Example 4: Restaurant Recommendation System (Multi-Relational Network)

### Complexity Level: ⭐⭐⭐⭐ Advanced

### Description
This semantic network models a restaurant recommendation system with multiple entity types (restaurants, cuisines, dishes, users, locations) and diverse relationship types. It demonstrates how semantic networks can represent complex real-world domains with heterogeneous information.

### Network Structure

```
        [Users]              [Restaurants]           [Cuisines]

    Alice ──likes──→ Italian Bistro ──serves──→ Italian
      ↓                     ↓                      ↓
   visited              located_in            is_type_of
      ↓                     ↓                      ↓
   Sushi Place ←─rated(4.5)─┘              Mediterranean
      ↓                     ↓
   serves               has_price_range
      ↓                     ↓
   Japanese            Moderate ($$$)
      ↓
   offers_dish
      ↓
   [Dishes]
   - Sushi Roll
   - Ramen
      ↓
   contains_ingredient
      ↓
   [Ingredients]
   - Rice, Fish, Seaweed
```

### Detailed Representation

**Node Types and Instances:**

*Users:*
- Alice {age: 28, dietary_preference: vegetarian}
- Bob {age: 35, dietary_preference: none}
- Carol {age: 42, dietary_preference: gluten_free}

*Restaurants:*
- Italian Bistro {rating: 4.7, price_range: moderate, capacity: 50}
- Sushi Place {rating: 4.5, price_range: expensive, capacity: 30}
- Taco Corner {rating: 4.2, price_range: cheap, capacity: 40}

*Cuisines:*
- Italian {origin: Italy, popularity: high}
- Japanese {origin: Japan, popularity: high}
- Mexican {origin: Mexico, popularity: medium}

*Dishes:*
- Margherita Pizza {calories: 800, is_vegetarian: true}
- Sushi Roll {calories: 350, is_vegetarian: false}
- Ramen {calories: 450, is_vegetarian: false}
- Fish Tacos {calories: 520, is_vegetarian: false}

*Ingredients:*
- Tomato, Mozzarella, Basil (for pizza)
- Rice, Fish, Seaweed (for sushi)
- Noodles, Broth, Pork (for ramen)

**Relationship Types:**

1. **User ↔ Restaurant:**
   - Alice → visited → Italian Bistro, Sushi Place
   - Alice → rated(5.0) → Italian Bistro
   - Alice → rated(4.5) → Sushi Place
   - Bob → likes → Taco Corner

2. **Restaurant → Cuisine:**
   - Italian Bistro → serves → Italian
   - Sushi Place → serves → Japanese
   - Taco Corner → serves → Mexican

3. **Restaurant → Dish:**
   - Italian Bistro → offers_dish → Margherita Pizza
   - Sushi Place → offers_dish → Sushi Roll, Ramen
   - Taco Corner → offers_dish → Fish Tacos

4. **Dish → Ingredient:**
   - Margherita Pizza → contains_ingredient → Tomato, Mozzarella, Basil
   - Sushi Roll → contains_ingredient → Rice, Fish, Seaweed

5. **Restaurant → Location:**
   - Italian Bistro → located_in → Downtown
   - Sushi Place → located_in → Westside
   - Taco Corner → located_in → Downtown

6. **Dish ↔ Dietary Properties:**
   - Margherita Pizza → suitable_for → Vegetarian
   - Sushi Roll → contains_allergen → Fish, Seaweed

### Key Learning Points
1. **Heterogeneous networks** combine different types of entities
2. **Weighted relationships** (e.g., ratings) add quantitative information
3. **Multi-hop reasoning** enables complex queries: "Find vegetarian dishes at highly-rated restaurants Alice has visited"
4. **Attribute-based filtering** on nodes (price range, dietary restrictions)
5. **Recommendation logic**: Users who liked Restaurant A also liked Restaurant B
6. **Temporal relationships** (visited implies past action)

### Applications
- E-commerce recommendation engines
- Social media platforms
- Content recommendation systems
- Personalized search engines

---

## Example 5: Medical Diagnosis System (Complex Expert System Network)

### Complexity Level: ⭐⭐⭐⭐⭐ Expert

### Description
This is the most complex example, representing a medical diagnosis system. It includes multiple entity types (patients, symptoms, diseases, tests, treatments), probabilistic relationships, temporal sequences, and causal links. This demonstrates how semantic networks can model expert knowledge in critical domains.

### Network Structure

```
                        [Patient]
                            ↓
                     presents_symptom
                      /     |      \
                     ↓      ↓       ↓
               [Symptoms]
        Fever(38.5°C)  Cough  Fatigue
             ↓          ↓        ↓
        suggests    suggests  suggests
      (prob=0.7)   (prob=0.8) (prob=0.6)
             ↓          ↓        ↓
             └──────→ [Disease] ←──────┘
                        ↓
                 Influenza (Type A)
                   /    |    \
                  ↓     ↓     ↓
         requires_test  caused_by  treated_with
                ↓         ↓          ↓
            [Tests]   [Pathogens] [Treatments]
        PCR Test    Influenza    Antiviral
        Blood Test    Virus      Rest
                        ↓          ↓
                   transmitted_  has_duration
                      via           ↓
                        ↓        7-10 days
                   Airborne         ↓
                   Droplets    monitored_by
                                    ↓
                               [Follow-up]
                          Symptom tracking
                          Temperature logs
```

### Detailed Representation

**Node Types and Instances:**

*Patients:*
- Patient_001 {
    age: 45,
    gender: female,
    medical_history: [asthma, hypertension],
    current_medications: [albuterol, lisinopril],
    admitted_date: 2024-01-15
  }

*Symptoms:*
- Fever {value: 38.5°C, duration: 3_days, severity: moderate}
- Dry Cough {frequency: persistent, duration: 4_days, severity: high}
- Fatigue {level: severe, duration: 5_days}
- Muscle Aches {location: generalized, severity: moderate}
- Headache {type: frontal, severity: mild}

*Diseases:*
- Influenza Type A {
    prevalence: seasonal,
    incubation_period: 1-4_days,
    contagious_period: 1_day_before_to_7_days_after,
    mortality_rate: 0.1%
  }
- COVID-19 {
    prevalence: pandemic,
    incubation_period: 2-14_days,
    contagious_period: variable,
    mortality_rate: 1-2%
  }
- Common Cold {
    prevalence: endemic,
    incubation_period: 1-3_days,
    severity: mild
  }

*Diagnostic Tests:*
- Rapid Influenza Test {accuracy: 70%, time: 15_minutes, cost: low}
- PCR Test {accuracy: 95%, time: 24_hours, cost: moderate}
- Chest X-ray {purpose: rule_out_pneumonia, cost: high}
- Blood Test {measures: [WBC, CRP], indicates: infection_severity}

*Treatments:*
- Oseltamivir (Tamiflu) {
    type: antiviral,
    effectiveness: 70%_if_early,
    duration: 5_days,
    side_effects: [nausea, headache]
  }
- Rest {type: supportive, duration: 7-10_days}
- Hydration {type: supportive, importance: high}
- Acetaminophen {type: symptomatic, for: fever_pain}

*Pathogens:*
- Influenza Virus Type A {
    family: Orthomyxoviridae,
    transmission: airborne_droplets,
    survival_outside_host: 24_hours
  }

**Relationship Types and Semantics:**

1. **Patient → Symptoms** (presents_symptom, temporal):
   - Patient_001 → presents_symptom → Fever [onset: day_1]
   - Patient_001 → presents_symptom → Cough [onset: day_1]
   - Patient_001 → presents_symptom → Fatigue [onset: day_0]

2. **Symptoms → Disease** (suggests, probabilistic):
   - (Fever + Cough + Fatigue) → suggests → Influenza [probability: 0.75]
   - (Fever + Cough + Fatigue) → suggests → COVID-19 [probability: 0.60]
   - (Fever + Cough) → suggests → Common Cold [probability: 0.40]

3. **Disease → Tests** (requires_test, diagnostic):
   - Influenza → confirmed_by → Rapid Influenza Test
   - Influenza → confirmed_by → PCR Test
   - Suspected_Influenza → requires_test → Chest X-ray [if: severe_symptoms]

4. **Disease → Pathogen** (caused_by, etiological):
   - Influenza → caused_by → Influenza Virus Type A

5. **Disease → Treatment** (treated_with, therapeutic):
   - Influenza → treated_with → Oseltamivir [condition: within_48h_symptom_onset]
   - Influenza → treated_with → Rest [always]
   - Influenza → treated_with → Hydration [always]

6. **Disease → Complications** (may_lead_to, causal):
   - Influenza → may_lead_to → Pneumonia [risk_factor: age>65 OR immunocompromised]
   - Influenza → may_lead_to → Bronchitis [probability: 0.15]

7. **Treatment → Outcome** (produces_outcome, consequential):
   - Oseltamivir → reduces_duration → [1-2_days]
   - Oseltamivir → reduces_severity → [moderate_effect]
   - Rest → supports_recovery → [essential]

8. **Pathogen → Transmission** (transmitted_via, epidemiological):
   - Influenza Virus → transmitted_via → Airborne Droplets
   - Influenza Virus → transmitted_via → Contact [contaminated_surfaces]

9. **Risk Factors** (increases_susceptibility):
   - Age>65 → increases_risk_of → Severe Influenza
   - Asthma → increases_risk_of → Complications
   - Immunosuppression → increases_risk_of → Severe Disease

**Complex Inference Rules:**

1. **Differential Diagnosis Rule:**
   ```
   IF Patient presents (Fever AND Cough AND Fatigue)
   AND Season = Winter
   AND Rapid_Test = Positive
   THEN Diagnosis = Influenza [confidence: 0.90]
   ```

2. **Treatment Selection Rule:**
   ```
   IF Diagnosis = Influenza
   AND Symptom_Onset < 48_hours
   AND No_Contraindications
   THEN Prescribe = Oseltamivir
   ELSE Prescribe = Supportive_Care_Only
   ```

3. **Complication Risk Assessment:**
   ```
   IF Patient.age > 65 OR Patient.has(Chronic_Condition)
   AND Diagnosis = Influenza
   THEN Risk_Level = High
   AND Recommend = Close_Monitoring + Consider_Hospitalization
   ```

### Key Learning Points
1. **Probabilistic relationships** represent uncertainty in medical diagnosis
2. **Temporal sequences** model disease progression and treatment timelines
3. **Conditional relationships** capture expert rules (e.g., "IF... THEN...")
4. **Multi-level reasoning** combines symptoms → diseases → tests → treatments
5. **Risk stratification** uses patient attributes to modify recommendations
6. **Causal networks** represent disease mechanisms and complications
7. **Decision support** enables automated reasoning for diagnosis and treatment
8. **Semantic richness** includes quantitative values, temporal information, and probabilities
9. **Interoperability** demonstrates how semantic networks connect diverse medical concepts

### Applications
- Clinical decision support systems
- Electronic health records (EHR)
- Medical diagnosis expert systems
- Drug interaction databases
- Epidemiological modeling
- Medical education and training systems

---

## Summary: Progression of Complexity

| Example | Nodes | Relationship Types | Key Feature | Complexity |
|---------|-------|-------------------|-------------|------------|
| 1. Family | 4 | 2 | Basic directed links | ⭐ |
| 2. Animals | 7 | 1 | Hierarchy & inheritance | ⭐⭐ |
| 3. Courses | 7 | 3 | Dependencies & constraints | ⭐⭐⭐ |
| 4. Restaurants | 15+ | 8+ | Heterogeneous multi-relational | ⭐⭐⭐⭐ |
| 5. Medical | 25+ | 10+ | Probabilistic, temporal, causal | ⭐⭐⭐⭐⭐ |

## Key Takeaways for Students

1. **Start Simple**: Begin with basic node-link structures before adding complexity
2. **Choose Appropriate Relationships**: The type of relationship matters as much as the nodes
3. **Consider Directionality**: Some relationships are symmetric (bidirectional), others are not
4. **Add Attributes When Needed**: Node and edge properties enrich the semantic network
5. **Think About Queries**: Design networks to answer the questions you need to ask
6. **Use Hierarchies**: Organize knowledge from general to specific when appropriate
7. **Handle Uncertainty**: In real-world applications, probabilistic relationships are common
8. **Model Temporal Aspects**: Time-dependent relationships are crucial in many domains
9. **Enable Inference**: Good semantic networks support reasoning and knowledge discovery
10. **Scale Thoughtfully**: Complex networks require careful design to remain manageable

