import streamlit as st
from backend import process_document, answer_query, generate_challenges
from summarizer import summarize_doc

st.set_page_config(page_title="GenAI Document Assistant", layout="wide")
st.title("📄 GenAI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    st.success("✅ Document uploaded successfully.")
    doc_text, doc_meta = process_document(uploaded_file)

    st.subheader("📋 Document Info")
    st.json(doc_meta)

    summary = summarize_doc(doc_text)
    st.subheader("🧠 Auto Summary (≤150 words)")
    st.write(summary)

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        query = st.text_input("Ask a question that requires understanding or inference")
        if query:
            answer, source = answer_query(doc_text, query)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"📖 _Justification:_ {source}")

    elif mode == "Challenge Me":
        if st.button("Generate Logic-Based Questions"):
            questions = generate_challenges(doc_text)
            for idx, q in enumerate(questions):
                user_ans = st.text_input(f"Q{idx+1}: {q['question']}", key=idx)
                if user_ans:
                    st.markdown(f"✅ **Your Answer:** {user_ans}")
                    st.markdown(f"💡 **Correct Answer:** {q['answer']}")
                    st.markdown(f"📖 _Justification:_ {q['source']}")
