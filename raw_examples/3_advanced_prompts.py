import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tree_of_thoughts():
    """
    Example of tree of thoughts prompting
    """
    prompt = """
    Let's explore this problem from different angles:
    
    Problem: How can we improve education using AI?
    
    Consider:
    1. Technical perspective (implementation, tools, infrastructure)
    2. Business perspective (cost, ROI, scalability)
    3. User perspective (students, teachers, administrators)
    4. Ethical perspective (privacy, bias, accessibility)
    
    Then synthesize the best approach considering all perspectives.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def reflection_prompt():
    """
    Example of reflection prompting
    """
    initial_response = """
    AI can help education by providing personalized learning experiences. 
    It can adapt to each student's learning style and pace, making education more effective.
    """
    
    prompt = f"""
    Here's my initial response:
    {initial_response}
    
    Please critique this considering:
    1. Implementation challenges
    2. Ethical concerns
    3. Practical limitations
    4. Potential benefits
    
    Then provide an improved version that addresses these points.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def meta_prompt():
    """
    Example of meta-prompting
    """
    context = {
        "user_expertise": "intermediate",
        "constraints": ["budget limited", "time constrained"],
        "goals": ["improve learning", "reduce teacher workload"]
    }
    
    prompt = f"""
    Context:
    - User expertise: {context['user_expertise']}
    - Constraints: {', '.join(context['constraints'])}
    - Goals: {', '.join(context['goals'])}
    
    Problem:
    Design an AI-powered educational tool
    
    Please:
    1. Analyze the context and problem
    2. Identify relevant patterns and relationships
    3. Generate a solution that leverages the context
    4. Explain how the context influenced the solution
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print("=== Advanced Prompt Examples ===")
    
    print("\n1. Tree of Thoughts:")
    print(tree_of_thoughts())
    
    print("\n2. Reflection Prompt:")
    print(reflection_prompt())
    
    print("\n3. Meta-Prompt:")
    print(meta_prompt()) 