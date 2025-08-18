from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

chat = ChatAnthropic(model='claude-3-5-sonnet-20241022')
response = chat.invoke("write 5 lines about Kabbadi")
print(response.content)
# print(response['usage_metadata'])
print(response.response_metadata)