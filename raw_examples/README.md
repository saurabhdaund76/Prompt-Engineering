# Raw Prompt Engineering Examples

This directory contains simple, straightforward examples of different prompt engineering techniques. Each file demonstrates specific techniques without complex structures.

## Files

1. `1_basic_prompts.py`
   - Clear Instruction Prompting
   - Role-Based Prompting
   - Step-by-Step Prompting

2. `2_intermediate_prompts.py`
   - Few-Shot Prompting
   - Chain of Thought (CoT)
   - Self-Consistency

3. `3_advanced_prompts.py`
   - Tree of Thoughts
   - Reflection Prompting
   - Meta-Prompting

## How to Use

1. Make sure you have your OpenAI API key in the `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

2. Run any example file:
```bash
python 1_basic_prompts.py
python 2_intermediate_prompts.py
python 3_advanced_prompts.py
```

## What Each Technique Does

### Basic Prompts
- **Clear Instruction**: Simple, direct questions with specific formatting
- **Role-Based**: Assigns a specific role to the AI
- **Step-by-Step**: Breaks down complex tasks into smaller steps

### Intermediate Prompts
- **Few-Shot**: Provides examples before asking the question
- **Chain of Thought**: Shows step-by-step reasoning
- **Self-Consistency**: Solves problems in multiple ways

### Advanced Prompts
- **Tree of Thoughts**: Considers multiple perspectives
- **Reflection**: Critiques and improves responses
- **Meta-Prompting**: Uses context to generate better responses

## Tips
1. Start with basic prompts
2. Try modifying the examples
3. Experiment with different parameters
4. Combine techniques for better results 