import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from tools import write_email

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
        model= "gemini-3-flash-preview",
        temperature = 1.0,
        google_api_key=api_key,
)



model = llm.bind_tools([write_email])

result = model.invoke("Draft a response to my manager about the bug found in streaming applicaton")

print(result)