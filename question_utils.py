from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma:2b", streaming=True)

def generate_logic_questions(text, num_qs=3):
    prompt = f"Generate {num_qs} logic-based or comprehension-based questions. Include answers and justifications:\n\n{text[:2000]}"
    result = llm.invoke(prompt)

    questions = []
    blocks = result.strip().split("\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 3:
            q = lines[0].replace("Q:", "").strip()
            a = lines[1].replace("A:", "").strip()
            j = lines[2].replace("Justification:", "").strip()
            questions.append({
                "question": q,
                "answer": a,
                "source": j
            })
    return questions
