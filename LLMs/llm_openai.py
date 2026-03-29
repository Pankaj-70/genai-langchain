from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()
# print(OPENAI_API_KEY)

llm=OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke('How are you dude?')
print(result)