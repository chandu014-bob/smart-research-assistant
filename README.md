
# Offline GenAI Document Assistant

This is a fully offline GenAI-powered assistant that:

✅ Accepts PDF/TXT document uploads  
✅ Generates auto-summary (≤150 words)  
✅ Answers questions with comprehension and inference  
✅ Generates logic-based challenges  
✅ Justifies every answer with document references  
✅ Works 100% offline using Ollama + Gemma 2B  

## Technologies Used
- Python 3.10+
- Streamlit
- LangChain
- Ollama
- Gemma 2B model (local LLM)

## How to Run

### 1. Start the model server
```bash
ollama run gemma:2b
```

Leave this terminal open.

### 2. In VS Code or terminal:
```bash
cd smart-assistant-offline
python -m venv venv
venv\Scripts\activate        # For Windows
pip install -r requirements.txt
streamlit run app.py
```

Then open your browser at:  
http://localhost:8501

---

## Folder Structure

- app.py – Main Streamlit app UI
- backend.py – Handles PDF/text processing and Q&A
- summarizer.py – Summary generation
- question_utils.py – Challenge question generator
- requirements.txt – Required Python packages

---

## Notes

- All models run locally using Ollama
- Tested with gemma:2b on CPU (fast on laptop)
