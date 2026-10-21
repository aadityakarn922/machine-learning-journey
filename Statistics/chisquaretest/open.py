import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:3001/v1"),
    api_key=os.environ["OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL", "auto:smart"),
    messages=[
        {
            "role": "user",
            "content": "Explain Python functions with a simple example.",
        }
    ],
)

print(resp.choices[0].message.content)
print("Routed via:", resp.headers.get("x-routed-via"))
