from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # or llama3-70b
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    max_tokens=20,
)

response = llm.invoke("Hello, how are you?")
print(response.content)