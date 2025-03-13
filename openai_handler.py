from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_solution(task):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORGANIZATION", ""),  # Parámetro opcional
        project=os.getenv("OPENAI_PROJECT", "")  # Parámetro opcional
    )
    
    if not client.api_key:
        raise ValueError("Falta la API Key. Crea un archivo .env con OPENAI_API_KEY=tu_clave")
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", 
                "content": "Eres un asistente académico experto. Genera respuestas detalladas en Markdown usando # para títulos principales, ## para subtítulos, - para listas, **negritas** y *cursivas*. Incluye explicaciones completas."
            },
            {"role": "user", "content": task}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    return response.choices[0].message.content  # Acceso correcto al contenido