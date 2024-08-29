import ollama

def ask_llama(question):
    stream = ollama.chat(
        model='llama3.1',
        messages=[{'role': 'user', 'content': question}],
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    # Ejemplo de uso
    pregunta = "por favor solo dame el valor en formato moneda del 3 porcierto de 1499000"
    ask_llama(pregunta)