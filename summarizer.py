from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma:2b", streaming=True)

def summarize_doc(text):
    prompt = f"Summarize the following document in less than 150 words:\n{text[:2000]}"
    return llm.invoke(prompt)
