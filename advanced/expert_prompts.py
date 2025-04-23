from utils.prompt_engineer import BasePromptEngineer
from typing import List, Dict, Any
import json

class ExpertPromptEngineer(BasePromptEngineer):
    def __init__(self):
        super().__init__()

    def tree_of_thoughts(self, problem: str, depth: int = 3) -> str:
        """
        Tree of Thoughts prompting with multiple reasoning paths
        """
        prompt = f"""
        Let's explore this problem using a tree of thoughts approach:
        {problem}

        We'll explore {depth} different paths of reasoning:
        1. For each path, we'll:
           - Start with a different initial assumption
           - Follow logical consequences
           - Consider alternative perspectives
        2. We'll evaluate each path's:
           - Strengths
           - Weaknesses
           - Assumptions
        3. Finally, we'll synthesize the best elements from each path.
        """
        return self.generate_response(prompt)

    def reflection_prompt(self, initial_response: str, critique_points: List[str]) -> str:
        """
        Reflection prompting with self-critique
        """
        prompt = f"""
        Here's my initial response:
        {initial_response}

        Please critique this response considering:
        {', '.join(critique_points)}

        Then, provide an improved version that addresses these points.
        """
        return self.generate_response(prompt)

    def self_refinement_prompt(self, problem: str, iterations: int = 3) -> str:
        """
        Self-refinement prompting with multiple iterations
        """
        current_solution = self.generate_response(problem)
        
        for _ in range(iterations):
            refinement_prompt = f"""
            Current solution:
            {current_solution}

            Please:
            1. Identify potential improvements
            2. Suggest specific changes
            3. Provide a refined version
            """
            current_solution = self.generate_response(refinement_prompt)
        
        return current_solution

    def meta_prompt(self, problem: str, context: Dict[str, Any]) -> str:
        """
        Meta-prompting with contextual information
        """
        context_str = json.dumps(context, indent=2)
        prompt = f"""
        Context:
        {context_str}

        Problem:
        {problem}

        Please:
        1. Analyze the context and problem
        2. Identify relevant patterns and relationships
        3. Generate a solution that leverages the context
        4. Explain how the context influenced the solution
        """
        return self.generate_response(prompt)

# Example usage
if __name__ == "__main__":
    engineer = ExpertPromptEngineer()
    
    # Test Tree of Thoughts
    print("Tree of Thoughts Example:")
    print(engineer.tree_of_thoughts("How can we improve education using AI?"))
    
    # Test Reflection Prompt
    initial_response = "AI can help education by providing personalized learning experiences."
    critique_points = [
        "Consider implementation challenges",
        "Address ethical concerns",
        "Include specific examples"
    ]
    print("\nReflection Prompt Example:")
    print(engineer.reflection_prompt(initial_response, critique_points))
    
    # Test Self-refinement
    print("\nSelf-refinement Example:")
    print(engineer.self_refinement_prompt("Design a sustainable city transportation system"))
    
    # Test Meta-prompt
    context = {
        "user_expertise": "urban planning",
        "constraints": ["budget limited", "environmentally friendly"],
        "goals": ["reduce traffic", "improve accessibility"]
    }
    print("\nMeta-prompt Example:")
    print(engineer.meta_prompt("Design a bike-sharing system", context)) 