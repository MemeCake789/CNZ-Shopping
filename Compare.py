import os
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_comparison(items):
    items_str = items
    with open('prompts/compare.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()

    user_message = f"Compare the following items: {items_str}"

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_message}
    ]

    tools = [{"type": "web_search_preview"}]
    
    response = client.responses.create(
        model="gpt-4o",
        input=messages,
        tools=tools,
        # max_output_tokens=10000
    )

    try:
        result = json.loads(response.output_text)
        return result
    except Exception as e:
        return {"error": f"Error parsing response: {str(e)}", "comparison": None}
