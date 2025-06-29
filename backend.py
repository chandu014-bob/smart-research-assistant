from PyPDF2 import PdfReader
from langchain_ollama import OllamaLLM
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
from question_utils import generate_logic_questions

llm = OllamaLLM(model="gemma:2b", streaming=True)

def process_document(file):
    metadata = {}
    try:
        if file.name.endswith(".pdf"):
            reader = PdfReader(file)
            if reader.is_encrypted:
                reader.decrypt("")
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            meta = reader.metadata
            metadata = {
                "Title": meta.title,
                "Author": meta.author,
                "Subject": meta.subject,
                "Pages": len(reader.pages)
            }
            return text, metadata

        elif file.name.endswith(".txt"):
            text = file.read().decode("utf-8")
            return text, {"File Type": "Plain Text", "Length": len(text)}

        else:
            return "Unsupported file type.", {}

    except Exception as e:
        return f"Error processing document: {e}", {}

def answer_query(text, query):
    try:
        docs = [Document(page_content=text)]
        chain = load_qa_chain(llm, chain_type="stuff")
        answer = chain.run(input_documents=docs, question=query)
        return answer, "Answer based on full document context."
    except Exception as e:
        return f"Error answering query: {e}", "No justification available."

def generate_challenges(text):
    return generate_logic_questions(text)
