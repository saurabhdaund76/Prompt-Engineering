from openai import OpenAI
from typing import List, Dict, Any
from config.settings import settings

class BasePromptEngineer:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME
        self.temperature = settings.TEMPERATURE
        self.max_tokens = settings.MAX_TOKENS

    def generate_response(self, prompt: str, system_message: str = None) -> str:
        """
        Generate a response using the OpenAI API
        """
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return None

    def analyze_response(self, response: str) -> Dict[str, Any]:
        """
        Analyze the response for various metrics
        """
        return {
            "length": len(response),
            "word_count": len(response.split()),
            "has_code": "```" in response,
            "has_list": any(char in response for char in ["-", "*", "1."])
        } 


