from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

chat = ChatOpenAI(model="gpt-4")
response = chat.invoke("write 5 lines about Kabbadi")
print(response.content)
# print(response['usage_metadata'])
print(response.response_metadata)