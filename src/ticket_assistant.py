import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
        model= "gemini-3-flash-preview",
        temperature = 1.0,
        google_api_key=api_key,
)


@tool
def write_email(to:str, subject:str, body:str) -> str: 
    """Draft and send an email"""
    return f"Email sent {to} with {subject} and content {body}"

model = llm.bind_tools([write_email])

result = model.invoke("Draft a response to my manager about the bug found in streaming applicaton")

print(result)