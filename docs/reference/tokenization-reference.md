# Tokenization Reference Guide

Quick-access reference for tokenization patterns, best practices, and troubleshooting in AI applications.

## 🎯 Quick Reference Tables

### Common Tokenization Patterns

| Text Type | Example | Typical Efficiency | Notes |
|-----------|---------|-------------------|-------|
| Simple English | "Hello world" | 3-4 chars/token | Optimal efficiency |
| Technical Terms | "backpropagation" | 2-3 chars/token | Often splits meaningfully |
| Mixed Languages | "Hello 你好" | 1-3 chars/token | Varies by language |
| Numbers/Symbols | "$123.45" | 1-2 chars/token | Punctuation creates boundaries |
| Code | `def function():` | 2-4 chars/token | Keywords often single tokens |

### Encoding Schemes Quick Reference

| Encoding | Used By | Vocabulary Size | Best For |
|----------|---------|----------------|----------|
| cl100k_base | GPT-4, GPT-3.5 | ~100k tokens | General text processing |
| p50k_base | GPT-3 | ~50k tokens | Legacy compatibility |
| r50k_base | Early GPT models | ~50k tokens | Simple applications |

## 🔧 Practical Applications

### Token Counting Best Practices

**For Prompt Engineering**:

```python
# Educational pattern for efficient prompts
def optimize_prompt_tokens(prompt: str) -> str:
    """
    Educational function showing token optimization strategies.
    Focus on preserving meaning while reducing token count.
    """
    
    # Strategy 1: Remove redundant words
    # Before: "Please provide me with a detailed explanation"
    # After:  "Explain in detail"
    
    # Strategy 2: Use shorter synonyms
    # Before: "comprehensive analysis"
    # After:  "thorough review"
    
    # Strategy 3: Combine related concepts
    # Before: "fast and quick and speedy"
    # After:  "rapid"
    
    return optimized_prompt
```

**For API Cost Estimation**:

```python
# Original educational implementation
def estimate_api_cost(text: str, cost_per_1k_tokens: float) -> float:
    """
    Calculate approximate API costs based on token count.
    
    Educational note: Always include both input and output tokens
    in cost calculations for realistic estimates.
    """
    import tiktoken
    
    encoding = tiktoken.get_encoding("cl100k_base")
    token_count = len(encoding.encode(text))
    
    # Add estimated response tokens (often 20-50% of input)
    estimated_response_tokens = token_count * 0.3
    total_tokens = token_count + estimated_response_tokens
    
    cost = (total_tokens / 1000) * cost_per_1k_tokens
    return cost
```

### Context Window Management

**Strategy**: Hierarchical Information Prioritization

```text
Context Window Budget (4000 tokens):
├── System Prompt (200 tokens) - Essential, never truncate
├── Recent Context (1500 tokens) - High priority
├── Historical Context (2000 tokens) - Truncate from oldest
└── Response Buffer (300 tokens) - Reserve for output
```

## 🚨 Troubleshooting Guide

### Common Tokenization Issues

**Issue**: Unexpected high token count

**Diagnosis Steps**:

1. Check for special characters or formatting
2. Analyze text complexity and technical terminology
3. Compare with simpler text for baseline
4. Examine individual token mappings

**Solution Strategies**:

- Simplify language without losing meaning
- Replace technical terms with common equivalents where appropriate
- Remove unnecessary formatting and punctuation
- Break complex sentences into simpler ones

**Issue**: Inconsistent tokenization across similar texts

**Diagnosis**: Context dependency in tokenization

**Investigation**:

```python
# Educational debugging approach
def debug_tokenization_differences(text1: str, text2: str):
    """
    Compare tokenization of similar texts to identify differences.
    Educational tool for understanding tokenization sensitivity.
    """
    import tiktoken
    
    encoding = tiktoken.get_encoding("cl100k_base")
    
    tokens1 = encoding.encode(text1)
    tokens2 = encoding.encode(text2)
    
    print(f"Text 1 tokens: {len(tokens1)}")
    print(f"Text 2 tokens: {len(tokens2)}")
    
    # Find differences
    decoded1 = [encoding.decode([t]) for t in tokens1]
    decoded2 = [encoding.decode([t]) for t in tokens2]
    
    print("Token breakdown comparison:")
    for i, (t1, t2) in enumerate(zip(decoded1, decoded2)):
        if t1 != t2:
            print(f"Position {i}: '{t1}' vs '{t2}'")
```

## 🌍 Multilingual Considerations

### Language Efficiency Rankings

Based on typical training data representation:

1. **High Efficiency (3-4 chars/token)**:
   - English
   - Spanish
   - French
   - German

2. **Medium Efficiency (2-3 chars/token)**:
   - Italian
   - Portuguese
   - Dutch

3. **Lower Efficiency (1-2 chars/token)**:
   - Chinese
   - Japanese
   - Arabic
   - Korean

### Cross-Language Optimization Strategies

**For Multilingual Applications**:

- Use English for system prompts when possible
- Consider language-specific tokenizers for specialized applications
- Budget extra tokens for non-Latin script languages
- Test tokenization efficiency during development

## 🎯 Performance Optimization

### Token-Efficient Writing Patterns

**Replace verbose patterns**:

```text
Verbose → Efficient
"in order to" → "to"
"due to the fact that" → "because"
"a large number of" → "many"
"it is important to note that" → "note that"
"please be aware that" → "note:"
```

**Optimize technical descriptions**:

```text
Technical → Streamlined
"implement a function that calculates" → "function to calculate"
"create a comprehensive analysis of" → "analyze"
"provide a detailed explanation of" → "explain"
```

### Context Window Strategies

**Priority-Based Truncation**:

1. **Never truncate**: System prompts, critical instructions
2. **Truncate carefully**: Examples, background context
3. **Truncate first**: Repeated information, verbose explanations

**Sliding Window Approach**:

```python
# Educational implementation
def manage_conversation_context(messages: list, max_tokens: int) -> list:
    """
    Maintain conversation context within token limits.
    Educational approach to context window management.
    """
    
    # Always preserve system message and recent messages
    system_msg = messages[0] if messages[0]['role'] == 'system' else None
    recent_messages = messages[-5:]  # Keep last 5 exchanges
    
    # Calculate tokens and truncate if needed
    # [Implementation would include token counting logic]
    
    return optimized_messages
```

## 📊 Measurement and Analytics

### Token Analysis Metrics

**Efficiency Metrics**:

- Characters per token ratio
- Vocabulary coverage percentage
- Compression ratio vs plain text
- Cost per semantic unit

**Quality Indicators**:

- Consistent tokenization across similar contexts
- Meaningful subword boundaries
- Preservation of semantic relationships
- Minimal unknown token frequency

### Monitoring Tokenization in Production

**Key Metrics to Track**:

```python
# Educational monitoring framework
class TokenizationMonitor:
    """
    Educational class for tracking tokenization metrics
    in production AI applications.
    """
    
    def track_efficiency(self, text: str, tokens: int):
        """Record efficiency metrics for analysis."""
        efficiency = len(text) / tokens
        # Log for analysis and optimization
        
    def detect_anomalies(self, expected_tokens: int, actual_tokens: int):
        """Identify unusual tokenization patterns."""
        variance = abs(expected_tokens - actual_tokens) / expected_tokens
        if variance > 0.3:  # 30% variance threshold
            # Flag for investigation
            pass
```

## 🚀 Advanced Techniques

### Custom Tokenization Strategies

**Domain-Specific Optimization**:

- Legal documents: Preserve clause structure
- Medical texts: Maintain terminology integrity
- Code: Respect syntactic boundaries
- Creative writing: Balance efficiency with style preservation

**Preprocessing for Better Tokenization**:

```python
# Educational preprocessing pipeline
def optimize_text_for_tokenization(text: str) -> str:
    """
    Educational function showing text preprocessing strategies
    that improve tokenization efficiency while preserving meaning.
    """
    
    # Strategy 1: Normalize whitespace
    text = ' '.join(text.split())
    
    # Strategy 2: Standardize punctuation
    text = text.replace(' .', '.').replace(' ,', ',')
    
    # Strategy 3: Remove redundant formatting
    # (Implementation depends on specific use case)
    
    return text
```

## 💡 Best Practices Summary

### Development Guidelines

1. **Always measure**: Count tokens before deploying prompts
2. **Test variations**: Compare different phrasings for efficiency
3. **Monitor production**: Track tokenization metrics in live applications
4. **Plan for growth**: Design systems that can handle tokenization changes

### Cost Management

1. **Estimate conservatively**: Include buffer for response tokens
2. **Optimize prompts**: Regular review and refinement of templates
3. **Cache results**: Avoid re-tokenizing identical inputs
4. **Monitor usage**: Set alerts for unexpected token consumption

### Quality Assurance

1. **Validate semantics**: Ensure optimization doesn't change meaning
2. **Test edge cases**: Verify behavior with unusual inputs
3. **Cross-language testing**: Validate multilingual applications thoroughly
4. **User experience**: Balance efficiency with readability

---

*This reference guide provides practical, actionable information for applying tokenization knowledge in real-world AI development scenarios. All examples follow our zero-copy methodology with original implementations designed for educational clarity.*
