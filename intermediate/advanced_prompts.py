from utils.prompt_engineer import BasePromptEngineer
from typing import List, Dict

class AdvancedPromptEngineer(BasePromptEngineer):
    def __init__(self):
        super().__init__()

    def few_shot_prompt(self, examples: List[Dict[str, str]], query: str) -> str:
        """
        Few-shot prompting with examples
        """
        prompt = "Here are some examples:\n\n"
        for example in examples:
            prompt += f"Input: {example['input']}\n"
            prompt += f"Output: {example['output']}\n\n"
        
        prompt += f"Now, please solve this similar problem:\n{query}"
        return self.generate_response(prompt)

    def chain_of_thought(self, problem: str) -> str:
        """
        Chain of thought prompting
        """
        prompt = f"""
        Let's think about this problem carefully:
        {problem}

        First, let's understand what we're trying to solve.
        Then, let's break it down into logical steps.
        For each step, we'll explain our reasoning.
        Finally, we'll combine our thoughts to reach a conclusion.
        """
        return self.generate_response(prompt)

    def self_consistency_prompt(self, problem: str, num_samples: int = 3) -> str:
        """
        Self-consistency prompting with multiple reasoning paths
        """
        prompt = f"""
        Let's solve this problem in {num_samples} different ways:
        {problem}

        For each approach:
        1. Explain the reasoning
        2. Show the solution
        3. Discuss pros and cons

        Finally, let's compare all approaches and choose the best one.
        """
        return self.generate_response(prompt)

# Example usage
if __name__ == "__main__":
    engineer = AdvancedPromptEngineer()
    
    # Test few-shot prompting
    examples = [
        {
            "input": "Convert 100°C to Fahrenheit",
            "output": "To convert Celsius to Fahrenheit: (100°C × 9/5) + 32 = 212°F"
        },
        {
            "input": "Convert 0°C to Fahrenheit",
            "output": "To convert Celsius to Fahrenheit: (0°C × 9/5) + 32 = 32°F"
        }
    ]
    print("Few-shot Prompt Example:")
    print(engineer.few_shot_prompt(examples, "Convert 25°C to Fahrenheit"))
    
    # Test chain of thought
    print("\nChain of Thought Example:")
    print(engineer.chain_of_thought("Why is the sky blue?"))
    
    # Test self-consistency
    print("\nSelf-consistency Example:")
    print(engineer.self_consistency_prompt("What's the best way to sort a list of numbers?")) 