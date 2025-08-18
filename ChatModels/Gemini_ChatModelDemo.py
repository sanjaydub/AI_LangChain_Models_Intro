from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
response = chat.invoke("write 3 lines about cricket")
print(response)
print("================================")
print(response.response_metadata)