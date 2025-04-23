import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def few_shot_prompt():
    """
    Example of few-shot prompting
    """
    prompt = """
    Here are some examples of converting temperatures:
    
    Example 1:
    Input: "Convert 100°C to Fahrenheit"
    Output: "To convert Celsius to Fahrenheit: (100°C × 9/5) + 32 = 212°F"
    
    Example 2:
    Input: "Convert 0°C to Fahrenheit"
    Output: "To convert Celsius to Fahrenheit: (0°C × 9/5) + 32 = 32°F"
    
    Now convert 25°C to Fahrenheit.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def chain_of_thought():
    """
    Example of chain of thought prompting
    """
    prompt = """
    Let's solve this math problem step by step:
    
    Problem: If a train travels 300 miles in 5 hours, what is its average speed?
    
    Let's think about this:
    1. What information do we have?
    2. What formula do we need?
    3. How do we apply the formula?
    4. What is the final answer?
    
    Please show your reasoning for each step.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def self_consistency():
    """
    Example of self-consistency prompting
    """
    prompt = """
    Let's solve this problem in three different ways:
    
    Problem: Find the sum of all even numbers from 1 to 10
    
    Approach 1: List all even numbers and add them
    Approach 2: Use a mathematical formula
    Approach 3: Use a loop in programming
    
    Please solve using all three approaches and compare the results.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print("=== Intermediate Prompt Examples ===")
    
    print("\n1. Few-Shot Prompt:")
    print(few_shot_prompt())
    
    print("\n2. Chain of Thought:")
    print(chain_of_thought())
    
    print("\n3. Self-Consistency:")
    print(self_consistency()) 