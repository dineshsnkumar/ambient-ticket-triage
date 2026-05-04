from langchain.tools import tool


@tool
def write_email(to:str, subject:str, body:str) -> str: 
    """Draft and send an email"""
    return f"Email sent {to} with {subject} and content {body}"