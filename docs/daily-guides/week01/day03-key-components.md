# Day 3: Key Components & Architecture (30 min)

## 📖 Core Concepts (10 minutes)

### Key Components of Generative AI Systems

#### 1. **Tokenizer** (Text Processor)

- **Role**: Converts text into numbers AI can process
- **Example**: "Hello world" → [15496, 995] (token IDs)
- **Quality Impact**: Better tokenization = better understanding

#### 2. **Neural Network** (The Brain)

- **Architecture**: Transformer blocks with attention mechanisms
- **Parameters**: Billions of learned weights
- **Function**: Processes tokens and predicts next elements

#### 3. **Sampling Strategy** (Output Controller)

- **Greedy**: Always pick most likely next word (predictable)
- **Random**: Sample from probability distribution (creative)
- **Temperature**: Controls randomness vs consistency

### System Architecture Flow

```text
Input Text → Tokenizer → Neural Network → Sampling → Output Text
  "Hello"  →  [15496]  →  Probabilities →  Selection →  "world"
```

### Quality Levers You Can Control

1. **Temperature**: Higher = more creative, Lower = more predictable
2. **Max Tokens**: How long the output should be
3. **Top-k/Top-p**: Limit word choices for better quality
4. **System Prompts**: Guide the AI's behavior and style

### Key Questions to Answer

1. What are the main components of a generative AI system?
2. How do these components work together?
3. What quality levers can you control?

## 🔬 Notebook Practice (15 minutes)

**Notebook**: [`week01-comprehensive-practice.ipynb`](../../../notebooks/weekly/week01/week01-comprehensive-practice.ipynb)

- **Section**: "Day 3: System Architecture"
- **Activities**:
  - Explore component relationships
  - Interact with quality controls
  - Study architecture diagrams

### Hands-on Tasks

- [ ] List 2 quality levers you can control
- [ ] Study architecture diagrams in the notebook
- [ ] Test different quality settings
- [ ] Map components to real-world systems

## 🤔 Reflection & Planning (5 minutes)

### Daily Reflection Prompts

1. **Architecture**: Which component seems most important for your use case?
2. **Quality Control**: How would you prioritize speed vs quality?
3. **System Design**: What would your ideal GenAI system look like?

### Learning Journal Template

```text
Date: ___________
Key Component: _________________________________
Quality Insight: _______________________________
Architecture Thought: __________________________
Tomorrow's Focus: ______________________________
```

## 🎯 Success Criteria

By the end of Day 3, you should be able to:

- [ ] Name the key components of GenAI systems
- [ ] Explain how components interact
- [ ] Identify 3 quality control levers
- [ ] Design a basic system architecture

## 🔗 Quick Links

- **Previous Day**: [Day 2 - How GenAI Works](day02-genai-overview.md)
- **Main Concept**: [Generative AI Fundamentals](../archived/concepts/generative-ai-fundamentals.md)
- **Interactive Practice**: [Week 1 Notebook](../../notebooks/weekly/week01/genai-exploration.ipynb)
- **Next Day**: [Day 4 - Probability Basics](day04-probability-basics.md)

---
*Part of [90-Day Generative AI Learning Path](../learning-path-90-days.md) - Week 1*
