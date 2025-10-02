from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

chat = ChatOpenAI(model="gpt-4")

chat_history = []

while True:
    # Get user input from the console
    input_user = input("user query: ")
    if input_user.strip().lower() == "exit":
        print("Exiting chat.")
        break
    chat_history.append(input_user)
    response = chat.invoke(chat_history)
    chat_history.append(response.content)
    print("AI: " + response.content)

# Print the chat history
print("\n======Chat History=====:")
for x in chat_history:
    print("\n"+x)