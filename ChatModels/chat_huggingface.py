from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_API_KEY=os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(
    api_key=HUGGINGFACE_API_KEY
)

# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {"role": "user", "content": "Explain what RAG is"}
#     ]
# )

# print(response.choices[0].message.content)