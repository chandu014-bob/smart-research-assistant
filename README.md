
# Smart Research Assistant (Offline GenAI App)

This project is an intelligent, offline document assistant powered by local LLMs using [Ollama](https://ollama.com). It allows users to upload long documents (PDF or TXT), automatically generates summaries, answers comprehension-level questions, and even creates logic-based quizzes — all without requiring an internet connection or OpenAI API.

---

## Features

✅ Upload PDF or TXT files  
✅ Extract and display metadata (title, pages, author)  
✅ Summarize the document in ≤150 words  
✅ Ask your own questions — get answers with explanations  
✅ Generate logic-based quiz questions from the document  
✅ Justifies every answer using content from the document  
✅ Fully offline and fast (Gemma 2B via Ollama)  

---

## Built With

- Python 3.10+
- Streamlit
- LangChain
- PyPDF2
- Ollama (Local LLM runtime)
- Gemma 2B model (lightweight, fast on CPU)

---

## Project Structure

```
smart-research-assistant/
├── app.py                # Main Streamlit interface
├── backend.py            # Handles PDF/TXT parsing and logic
├── summarizer.py         # Document summarization logic
├── question_utils.py     # Logic question generator using LLM
├── requirements.txt      # Dependencies
└── README.md             # You're reading it!
```

---

## ⚙️ How to Run Locally

### Step 1: Install Python and Ollama

- Install Python: https://www.python.org/downloads/
- Install Ollama: https://ollama.com/download

---

### Step 2: Clone the Repo & Set Up Virtual Environment

```bash
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

---

### Step 3: Run Ollama in Separate Terminal

```bash
ollama run gemma:2b
```

This loads the LLM locally and should remain running.

---

### Step 4: Launch the App

```bash
streamlit run app.py
```

Your browser will open at:  
http://localhost:8501

---



## Example Use Cases

- Summarizing long research papers or legal documents
- Building comprehension-based MCQ quizzes
- Offline AI assistant for students and researchers

