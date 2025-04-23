# from openai import OpenAI
# from config.settings import Settings

# api_key = Settings.OPENAI_API_KEY
# client = OpenAI(api_key = api_key)

# response = client.response.create(
#     model = "gpt-4.1",
#     input = "write one story about CR7"
# )

# print(response.output_text)


import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("api key", api_key)