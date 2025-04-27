"""
OpenAI Integration Module

Handles communication with OpenAI's API to generate academic solutions.
Requires valid OpenAI API credentials in .env file.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_solution(task: str) -> str:
    """Generates academic solution for given task using OpenAI's GPT-4 model.
    
    Args:
        task: User-provided academic task/question/problem statement
        
    Returns:
        str: Formatted Markdown solution
        
    Raises:
        ValueError: If OpenAI API key is missing
        Exception: For general API communication errors
    
    Example:
        >>> generate_solution("Explain quantum computing")
        "# Quantum Computing\\n\\nQuantum computing is..."
    """
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORGANIZATION", ""),
        project=os.getenv("OPENAI_PROJECT", "")
    )
    
    if not client.api_key:
        raise ValueError("Missing API Key. Create a .env file with OPENAI_API_KEY=your_key")
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", 
                "content": "You are an expert academic assistant. Generate detailed answers in Markdown using # for main titles, ## for subtitles, - for lists, **bold** and *italic* text. Include complete explanations."
            },
            {"role": "user", "content": task}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    return response.choices[0].message.content