# This file was moved from tests/BaseLLMs/FirstLLMDemo.py
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

# ...existing code...

llm = OpenAI(model='gpt-3.5-turbo-instruct')
llm_response = llm.invoke("What is the capital of Germany?")
print(llm_response)
