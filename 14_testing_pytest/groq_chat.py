MODEL = "llama-3.3-70b-versatile"


def ask_groq(question, client=None):
    if not question.strip():
        raise ValueError("question cannot be empty")
    if client is None:
        from groq import Groq

        client = Groq()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        max_tokens=1024,
    )
    return response.choices[0].message.content
