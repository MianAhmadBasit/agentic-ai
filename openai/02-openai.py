# pip install openai
# check requerment.txt for more details.
# pip install -r requirements.txt
# pip install python-dotenv

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file




client = OpenAI()   


response  = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello! How are you?"}
    ]
)

print(response.choices[0].message.content)
