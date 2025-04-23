from utils.prompt_engineer import BasePromptEngineer
from typing import List, Dict, Any
import json

class PromptShowcase(BasePromptEngineer):
    def __init__(self):
        super().__init__()
        # Test API connection
        try:
            test_response = self.generate_response("Hello, please respond with 'API is working' if you can read this.")
            print("API Test Response:", test_response)
            if "API is working" in test_response:
                print("✅ API Key is working correctly!")
            else:
                print("❌ API Key test failed")
        except Exception as e:
            print(f"❌ API Error: {str(e)}")

    def demonstrate_basic_prompts(self):
        """Showcase basic prompt engineering techniques"""
        print("\n=== Basic Prompt Examples ===")
        
        # 1. Clear Instruction Prompt
        print("\n1. Clear Instruction Prompt:")
        prompt = """
        Please explain the concept of recursion in programming.
        Include:
        1. A clear definition
        2. A simple example in Python
        3. Common use cases
        Format your response in markdown.
        """
        response = self.generate_response(prompt)
        print(response)

        # 2. Role-Based Prompt
        print("\n2. Role-Based Prompt:")
        system_message = "You are an expert Python developer with 10 years of experience."
        prompt = "Write a function to find the longest common subsequence between two strings."
        response = self.generate_response(prompt, system_message)
        print(response)

        # 3. Step-by-Step Prompt
        print("\n3. Step-by-Step Prompt:")
        prompt = """
        Let's solve this problem step by step:
        How to implement a binary search algorithm?

        Please:
        1. Explain the algorithm
        2. Write the code
        3. Show an example
        4. Discuss time complexity
        """
        response = self.generate_response(prompt)
        print(response)

    def demonstrate_intermediate_prompts(self):
        """Showcase intermediate prompt engineering techniques"""
        print("\n=== Intermediate Prompt Examples ===")
        
        # 1. Few-Shot Prompt
        print("\n1. Few-Shot Prompt:")
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
        prompt = "Here are some examples:\n\n"
        for example in examples:
            prompt += f"Input: {example['input']}\n"
            prompt += f"Output: {example['output']}\n\n"
        prompt += "Now convert 25°C to Fahrenheit."
        response = self.generate_response(prompt)
        print(response)

        # 2. Chain of Thought
        print("\n2. Chain of Thought Prompt:")
        prompt = """
        Let's think about this problem carefully:
        Why is the sky blue?

        Please:
        1. Explain the scientific principle
        2. Describe the process
        3. Provide a simple analogy
        4. Address common misconceptions
        """
        response = self.generate_response(prompt)
        print(response)

        # 3. Self-Consistency
        print("\n3. Self-Consistency Prompt:")
        prompt = """
        Let's solve this problem in three different ways:
        How to optimize a website's loading speed?

        For each approach:
        1. Front-end optimization
        2. Back-end optimization
        3. Infrastructure optimization

        Then compare and choose the best approach.
        """
        response = self.generate_response(prompt)
        print(response)

    def demonstrate_advanced_prompts(self):
        """Showcase advanced prompt engineering techniques"""
        print("\n=== Advanced Prompt Examples ===")
        
        # 1. Tree of Thoughts
        print("\n1. Tree of Thoughts Prompt:")
        prompt = """
        Let's explore this problem from different angles:
        How can we improve education using AI?

        Consider:
        1. Technical perspective
        2. Educational perspective
        3. Ethical perspective
        4. Implementation perspective

        Then synthesize the best approach.
        """
        response = self.generate_response(prompt)
        print(response)

        # 2. Reflection Prompt
        print("\n2. Reflection Prompt:")
        initial_response = "AI can help education by providing personalized learning experiences."
        prompt = f"""
        Here's my initial response:
        {initial_response}

        Please critique this considering:
        1. Implementation challenges
        2. Ethical concerns
        3. Practical limitations
        4. Potential benefits

        Then provide an improved version.
        """
        response = self.generate_response(prompt)
        print(response)

        # 3. Self-Refinement
        print("\n3. Self-Refinement Prompt:")
        current_solution = "We can use machine learning to predict student performance."
        prompt = f"""
        Current solution:
        {current_solution}

        Please:
        1. Identify potential improvements
        2. Suggest specific changes
        3. Provide a refined version
        4. Explain the improvements
        """
        response = self.generate_response(prompt)
        print(response)

        # 4. Meta-Prompt
        print("\n4. Meta-Prompt:")
        context = {
            "user_expertise": "intermediate",
            "constraints": ["budget limited", "time constrained"],
            "goals": ["improve learning", "reduce teacher workload"]
        }
        prompt = f"""
        Context:
        {json.dumps(context, indent=2)}

        Problem: Design an AI-powered educational tool

        Please analyze and provide a solution that considers all aspects.
        """
        response = self.generate_response(prompt)
        print(response)

if __name__ == "__main__":
    showcase = PromptShowcase()
    
    # Demonstrate all prompt types
    showcase.demonstrate_basic_prompts()
    showcase.demonstrate_intermediate_prompts()
    showcase.demonstrate_advanced_prompts() 