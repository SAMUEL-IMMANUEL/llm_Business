# llm_helper.py

import ollama

def generate_ollama_response(prompt):
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']
