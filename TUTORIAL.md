# Prompt Engineering Tutorial: From Basic to Advanced

This project demonstrates different levels of prompt engineering techniques using OpenAI's GPT models. It's designed to help you understand and practice various prompt engineering approaches, from basic to advanced levels.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Project Structure](#project-structure)
5. [Understanding the Components](#understanding-the-components)
6. [Running the Examples](#running-the-examples)
7. [Understanding Different Prompt Types](#understanding-different-prompt-types)
8. [Troubleshooting](#troubleshooting)

## Project Overview

This project is divided into three main levels of prompt engineering:
- **Basic Prompts**: Simple, direct instructions
- **Intermediate Prompts**: More structured approaches with examples
- **Advanced Prompts**: Complex techniques with multiple perspectives

## Prerequisites

Before you start, make sure you have:
1. Python 3.8 or higher installed
2. An OpenAI API key (get it from [OpenAI's website](https://platform.openai.com/))
3. Basic understanding of Python programming

## Setup Instructions

### Step 1: Create Project Directory
```bash
# Create a new directory for the project
mkdir prompt_engineering_tutorial
cd prompt_engineering_tutorial
```

### Step 2: Set Up Virtual Environment
A virtual environment is like a separate container for your project's dependencies. It prevents conflicts between different projects' requirements.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
# Install the required packages
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in your project root directory:
```bash
# Create .env file
touch .env
```

Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

**Why do we need .env?**
- The `.env` file stores sensitive information (like API keys) separately from your code
- It prevents accidentally committing sensitive data to version control
- It makes it easy to use different configurations in different environments

## Project Structure

```
prompt_engineering_tutorial/
├── .env                    # Environment variables (API keys)
├── .gitignore             # Specifies which files Git should ignore
├── requirements.txt       # Project dependencies
├── setup.py              # Package configuration
├── config/               # Configuration files
│   └── settings.py       # Settings management
├── utils/                # Utility functions
│   └── prompt_engineer.py # Base prompt engineering class
├── basic/                # Basic prompt examples
│   └── simple_prompts.py
├── intermediate/         # Intermediate prompt examples
│   └── advanced_prompts.py
├── advanced/             # Advanced prompt examples
│   └── expert_prompts.py
└── examples/             # Example usage
    └── prompt_showcase.py
```

## Understanding the Components

### 1. Configuration (`config/settings.py`)
- Manages application settings using Pydantic
- Loads environment variables securely
- Defines default values for model parameters

### 2. Base Prompt Engineer (`utils/prompt_engineer.py`)
- Core class for interacting with OpenAI's API
- Handles API key management
- Provides basic response generation functionality

### 3. Prompt Levels

#### Basic Prompts (`basic/simple_prompts.py`)
- Clear Instruction Prompting
- Role-Based Prompting
- Step-by-Step Prompting

#### Intermediate Prompts (`intermediate/advanced_prompts.py`)
- Few-Shot Prompting
- Chain of Thought (CoT)
- Self-Consistency

#### Advanced Prompts (`advanced/expert_prompts.py`)
- Tree of Thoughts
- Reflection Prompting
- Meta-Prompting

## Running the Examples

1. Make sure your virtual environment is activated
2. Ensure your `.env` file is set up correctly
3. Run the example script:
```bash
python examples/prompt_showcase.py
```

## Understanding Different Prompt Types

### Basic Prompts
1. **Clear Instruction Prompting**
   - Direct, explicit instructions
   - No examples provided
   - Good for simple tasks

2. **Role-Based Prompting**
   - Assigns a specific role to the AI
   - Helps get specialized responses
   - Useful for expert-level answers

3. **Step-by-Step Prompting**
   - Breaks down complex tasks
   - Provides structured guidance
   - Good for learning processes

### Intermediate Prompts
1. **Few-Shot Prompting**
   - Provides examples before the question
   - Helps the model understand the format
   - Useful for consistent output

2. **Chain of Thought (CoT)**
   - Encourages step-by-step reasoning
   - Makes the thinking process visible
   - Good for complex problems

3. **Self-Consistency**
   - Generates multiple solutions
   - Compares different approaches
   - Helps find the best solution

### Advanced Prompts
1. **Tree of Thoughts**
   - Explores multiple perspectives
   - Considers different angles
   - Synthesizes best approach

2. **Reflection Prompting**
   - Critiques initial responses
   - Identifies improvements
   - Generates better solutions

3. **Meta-Prompting**
   - Uses contextual information
   - Considers multiple factors
   - Generates nuanced responses

## Troubleshooting

### Common Issues and Solutions

1. **ModuleNotFoundError**
   - Make sure virtual environment is activated
   - Check if all packages are installed
   - Verify Python path

2. **API Key Issues**
   - Check `.env` file format
   - Verify API key is correct
   - Ensure environment variables are loaded

3. **Import Errors**
   - Check project structure
   - Verify `__init__.py` files
   - Ensure correct Python path

4. **Response Generation Issues**
   - Check API rate limits
   - Verify model parameters
   - Ensure proper prompt formatting

### Getting Help
- Check the OpenAI documentation
- Review error messages carefully
- Try simpler prompts first
- Test with different parameters

## Best Practices

1. **Environment Setup**
   - Always use virtual environments
   - Keep sensitive data in `.env`
   - Document dependencies

2. **Code Organization**
   - Follow the project structure
   - Use clear naming conventions
   - Document your code

3. **Prompt Engineering**
   - Start with simple prompts
   - Test and iterate
   - Document successful patterns

4. **Version Control**
   - Use `.gitignore` properly
   - Commit frequently
   - Write clear commit messages

## Next Steps

1. Experiment with different prompt types
2. Try combining multiple techniques
3. Create your own prompt patterns
4. Document your findings

## Resources

- [OpenAI Documentation](https://platform.openai.com/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Environment Variables Best Practices](https://12factor.net/config) 