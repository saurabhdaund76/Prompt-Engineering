from utils.prompt_engineer import BasePromptEngineer

class SimplePromptEngineer(BasePromptEngineer):
    def __init__(self):
        super().__init__()

    def basic_prompt(self, topic: str) -> str:
        """
        Basic prompt with clear instructions
        """
        prompt = f"""
        Please explain the concept of {topic} in simple terms.
        Include:
        1. A clear definition
        2. A practical example
        3. Common use cases
        """
        return self.generate_response(prompt)

    def role_based_prompt(self, role: str, task: str) -> str:
        """
        Role-based prompting
        """
        system_message = f"You are an expert {role} with years of experience."
        prompt = f"""
        As a {role}, please help me with the following task:
        {task}
        """
        return self.generate_response(prompt, system_message)

    def step_by_step_prompt(self, problem: str) -> str:
        """
        Step-by-step prompting
        """
        prompt = f"""
        Let's solve this problem step by step:
        {problem}
        
        Please:
        1. Break down the problem into smaller parts
        2. Solve each part sequentially
        3. Combine the solutions
        4. Verify the final answer
        """
        return self.generate_response(prompt)

# Example usage
if __name__ == "__main__":
    engineer = SimplePromptEngineer()
    
    # Test basic prompt
    print("Basic Prompt Example:")
    print(engineer.basic_prompt("Prompt Engineering"))
    
    # Test role-based prompt
    print("\nRole-based Prompt Example:")
    print(engineer.role_based_prompt("Gen AI developer", "How to optimize the prompts?"))
    
    # Test step-by-step prompt
    print("\nStep-by-step Prompt Example:")
    print(engineer.step_by_step_prompt("How to implement a chat completion API?")) 