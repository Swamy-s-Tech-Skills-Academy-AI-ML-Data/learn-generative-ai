<!-- filename: day04-probability-basics.md -->
# Day 4: Mathematical Foundations I - Probability Basics (30 min)

## 📖 Reading Focus (10 minutes)

**Self-Contained Learning**: This guide contains all essential Day 4 concepts below.

- **Focus**: Probability distributions, sampling strategies, and mathematical foundations
- **Goal**: Understand probability's role in AI and different generation strategies

### Key Questions to Answer

1. Why is probability fundamental to generative AI?
2. How do probability distributions work in language models?
3. What does "next word prediction" really mean mathematically?
4. What are the different strategies for sampling from probability distributions?

### Essential Concepts

#### Probability in Language Modeling

- **Next Word Prediction**: Models assign probabilities to each possible next word
- **Distribution Shape**: Probability distributions can be sharp (confident) or flat (uncertain)
- **Temperature**: Controls randomness - low temperature = more predictable, high temperature = more creative

#### Sampling Strategies

Different methods to select outputs from probability distributions:

- **Greedy Sampling**: Always pick the highest probability word (deterministic)
- **Random Sampling**: Sample from the full probability distribution (most random)
- **Top-k Sampling**: Choose from top k most likely options (balanced)
- **Top-p (Nucleus) Sampling**: Choose from cumulative probability p (adaptive)

**When to Use Each:**

- Greedy: For factual, consistent outputs
- Random: For maximum creativity and variety
- Top-k: For controlled creativity with quality
- Top-p: For adaptive creativity that adjusts to context

## 🔬 Notebook Practice (15 minutes)

**Notebook**: [`day04-probability-basics.ipynb`](../../../notebooks/weekly/week01/day04-probability-basics.ipynb)

- **Probability Distribution Explorer**: Interactive visualization of uniform, normal, softmax, and attention distributions
- **AI Prediction Analysis**: See how AI models use softmax to convert raw scores into probabilities
- **Attention Weight Visualization**: Understand how AI "pays attention" to different parts of input
- **Real AI Examples**: Explore actual probability distributions used in classification and sequence modeling

### Hands-on Tasks

- [ ] Run the `explore_probability_distributions()` function to see comprehensive probability visualizations
- [ ] Analyze the softmax distribution showing AI model predictions for animal classification
- [ ] Study the attention weight distribution to understand sequence processing
- [ ] Compare uniform vs normal vs softmax distributions and their AI applications
- [ ] Execute the `explore_sampling_strategies()` function to see different text generation approaches
- [ ] Compare greedy vs random vs top-k vs top-p sampling methods
- [ ] Analyze how temperature affects prediction confidence and creativity
- [ ] Verify that probabilities sum to 1.0 in softmax and attention examples

## 🤔 Reflection & Planning (5 minutes)

### Daily Reflection Prompts

1. **Probability Understanding**: How does probability help AI generate text?
2. **Prediction Logic**: Why doesn't AI always pick the most likely word?
3. **Mathematical Intuition**: What probability concepts surprised you?

### Learning Journal Template

```text
Date: ___________
Probability Insight: ______________________________
Prediction Understanding: __________________________
Mathematical Connection: ___________________________
Tomorrow's Focus: __________________________________
```

## 🎯 Success Criteria

By the end of Day 4, you should be able to:

- [ ] Explain why probability is essential for text generation
- [ ] Describe how AI predicts the next word
- [ ] Calculate basic text probabilities
- [ ] Connect probability to generation quality

## 🔗 Quick Links

- **Previous Day**: [Day 3 - Key Components](day03-key-components.md)
- **Interactive Practice**: [Day 4 Interactive Notebook](../../../notebooks/weekly/week01/day04-probability-basics.ipynb)
- **Next Day**: [Day 5 - Loss Functions](day05-loss-functions.md)

---
*Part of [90-Day Generative AI Learning Path](../learning-path-90-days.md) - Week 1*
