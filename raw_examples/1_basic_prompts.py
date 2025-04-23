import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clear_instruction_prompt():
    """
    Example of clear instruction prompting
    """
    prompt = """
    Please explain the concept of machine learning in simple terms.
    Include:
    1. A clear definition
    2. A practical example
    3. Common use cases
    Format your response in markdown with proper headings.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def role_based_prompt():
    """
    Example of role-based prompting
    """
    prompt = """
    You are a senior software architect with 15 years of experience.
    Please review this code and suggest improvements for scalability:
    
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def step_by_step_prompt():
    """
    Example of step-by-step prompting
    """
    prompt = """
    Let's solve this problem step by step:
    
    Problem: Calculate the factorial of a number
    
    1. First, understand what factorial means
    2. Then, write the mathematical formula
    3. Next, implement the code
    4. Finally, test with example numbers
    
    Please provide the solution following these steps.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print("=== Basic Prompt Examples ===")
    
    print("\n1. Clear Instruction Prompt:")
    print(clear_instruction_prompt())
    
    print("\n2. Role-Based Prompt:")
    print(role_based_prompt())
    
    print("\n3. Step-by-Step Prompt:")
    print(step_by_step_prompt()) 