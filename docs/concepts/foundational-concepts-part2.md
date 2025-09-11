# Foundational Concepts of Generative AI - Part 2: Numerical Representations

## 📚 Previously in Part 1

We established the foundation by covering:

- **Tokens**: The building blocks of AI text processing (LEGO brick analogy)
- **Tokenization**: Breaking text into manageable chunks (cake slicing analogy)
- **Processing Pipeline**: Raw text → Tokenization → (You are here)

*Catch up: [foundational-concepts-part1.md](./foundational-concepts-part1.md)*

## 🎯 Learning Objectives

By the end of this part, you'll understand:

- How encoding transforms tokens into numbers machines can process
- What embeddings are and why they're revolutionary for AI
- How semantic relationships are captured in vector space
- The mathematical foundation that powers modern AI understanding

---

## 🔢 3. Encoding: From Text to Numbers

### What Is Encoding?

**Encoding transforms tokens into numeric IDs that machines can process.** It's like creating a universal translator between human language and computer language.

### The Encoding Process

```text
Step 1: Tokens (from tokenization)
["The", " AI", " model", " processes", " text"]

Step 2: Vocabulary Lookup
Vocabulary Dictionary:
"The" → ID: 278
" AI" → ID: 15837
" model" → ID: 2746
" processes" → ID: 8149
" text" → ID: 2420

Step 3: Encoded Sequence
[278, 15837, 2746, 8149, 2420]
```

### Encoding Example: Real-World Scenario

```text
Input Text: "Generative AI transforms creativity"

Tokenization: ["Gener", "ative", " AI", " transforms", " creativity"]

Encoding: [5648, 1413, 15837, 29575, 28131]

Model Processing: [5648, 1413, 15837, 29575, 28131] → Neural Network
```

### 🏛️ Zip Code Analogy

**Encoding is like assigning zip codes:**

- Each location (token) gets a unique number (ID)
- Machines can process numbers much faster than names
- Consistent mapping: same token always gets same ID
- Enables efficient sorting, searching, and processing

### Types of Encoding

#### Positional Encoding

```text
Token: "AI"     Position: 2     Combined: [15837] + [position_vector_2]
Purpose: Helps model understand word order
```

#### Contextual Encoding

```text
"Bank" in "river bank" → [2934, context_modifier_1]
"Bank" in "money bank" → [2934, context_modifier_2]
Purpose: Same word, different meanings
```

### Encoding Impact on AI Performance

1. **Vocabulary Size**: Larger = more nuanced, but computationally expensive
2. **Unknown Handling**: How the system deals with never-seen-before tokens
3. **Compression Rate**: How efficiently text is converted to numbers
4. **Cross-lingual**: How well encoding works across languages

---

## 📊 4. Embeddings: Capturing Semantic Meaning

### What Are Embeddings?

**Embeddings are high-dimensional vectors (lists of numbers) that capture the semantic meaning and relationships between tokens.** They're the "meaning maps" that enable AI to understand context and similarity.

### Embedding Structure

```text
Token: "King"
Embedding: [0.12, -0.98, 0.45, 0.67, -0.23, 0.89, ...] (768 dimensions typical)

Token: "Queen"
Embedding: [0.15, -0.95, 0.41, 0.70, -0.19, 0.85, ...] (similar to King)

Token: "Banana"
Embedding: [-0.67, 0.23, -0.89, 0.12, 0.95, -0.34, ...] (very different)
```

### Semantic Relationships in Vector Space

```text
Mathematical Relationships:
King - Man + Woman ≈ Queen
Paris - France + Italy ≈ Rome
Swimming - Water + Snow ≈ Skiing

Distance Measurements:
cosine_similarity("King", "Queen") = 0.85 (very similar)
cosine_similarity("King", "Banana") = 0.12 (very different)
```

### 🗺️ Multi-Dimensional Map Analogy

**Embeddings are like a vast, multi-dimensional city map:**

- Each word has coordinates in meaning-space
- Similar concepts cluster in neighborhoods
- Distance = semantic similarity
- Directions capture relationships (King → Queen = Male → Female)

### Embedding Dimensions and Meaning

#### Low-Dimensional Example (Simplified for Understanding)

```text
Dimension 1: Royalty (King=0.9, Queen=0.9, Peasant=0.1)
Dimension 2: Gender (King=-0.8, Queen=0.8, Person=0.0)
Dimension 3: Power (King=0.7, Queen=0.7, Child=0.2)
```

#### Real-World High-Dimensional

```text
Typical embedding sizes:
- Word2Vec: 300 dimensions
- BERT: 768 dimensions
- GPT-3: 12,288 dimensions
- GPT-4: 16,000+ dimensions (estimated)
```

### Types of Embeddings

#### Token-Level Embeddings

```text
Input: "AI revolutionizes industry"
Output: 3 separate vectors for ["AI", "revolutionizes", "industry"]
```

#### Sentence-Level Embeddings

```text
Input: "AI revolutionizes industry"
Output: 1 vector representing entire sentence meaning
```

#### Document-Level Embeddings

```text
Input: Entire research paper
Output: 1 vector capturing document's core concepts
```

---

## 🎓 Part 2 Self-Assessment

### Understanding Check

1. **Encoding Logic**: If "cat" = 2543, what happens when the model sees "cats"?
2. **Embedding Similarity**: Which should be closer in vector space: "doctor" and "nurse" or "doctor" and "computer"?
3. **Dimensional Impact**: Why do larger embedding dimensions generally improve AI understanding?

### Practical Challenge

Given these simplified embeddings, calculate similarity:

```text
"Happy": [0.8, 0.6, 0.1]
"Joyful": [0.7, 0.5, 0.2]
"Sad": [-0.6, -0.4, 0.1]
```

**Hint**: Which vectors point in similar directions?

---

## 🔄 Coming Up in Part 3

In the final part, we'll explore:

- **Complete Processing Flow**: How all pieces work together
- **Real-World Applications**: Search, recommendations, RAG systems
- **Advanced Connections**: How these concepts enable modern AI features

**Integration Focus**: Seeing the big picture and practical applications!

---

*Continue to: [foundational-concepts-part3.md](./foundational-concepts-part3.md)*
*Previous: [foundational-concepts-part1.md](./foundational-concepts-part1.md)*
*Part of the [90-Day Generative AI Learning Path](../learning-path-90-days.md)*
