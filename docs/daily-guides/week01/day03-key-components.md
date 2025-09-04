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

**Notebook**: [`day03-key-components.ipynb`](../../../notebooks/weekly/week01/day03-key-components.ipynb)

- **System Architecture Explorer**: Interactive analysis of AI system components and their relationships
- **Complexity vs Importance Matrix**: Visualize component significance with scatter plot analysis
- **Data Flow Visualization**: Track how information moves through the AI system pipeline
- **Component Interaction Heatmap**: Understand how different parts of the system communicate
- **Performance Monitoring**: See real-time system performance metrics over time

### Hands-on Tasks

- [ ] Run the `explore_system_architecture()` function to see comprehensive component analysis
- [ ] Study the complexity vs importance scatter plot to understand component priorities
- [ ] Analyze the data flow chart showing information transformation stages
- [ ] Examine the interaction heatmap to see component relationships
- [ ] Review performance metrics showing processing time and memory usage patterns

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
- **Interactive Practice**: [Day 3 Interactive Notebook](../../../notebooks/weekly/week01/day03-key-components.ipynb)
- **Next Day**: [Day 4 - Probability Basics](day04-probability-basics.md)

---
*Part of [90-Day Generative AI Learning Path](../learning-path-90-days.md) - Week 1*
