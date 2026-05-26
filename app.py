import streamlit as st
from summarizer import summarize_notes
from pypdf import PdfReader

st.title("AI Notes Summarizer")

notes = st.text_area("Paste your notes here")

uploaded_file = st.file_uploader(
    "Upload a TXT or PDF file",
    type=["txt", "pdf"]
)

if uploaded_file is not None:

    if uploaded_file.type == "text/plain":

        notes = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(uploaded_file)

        notes = ""

        for page in pdf_reader.pages:

            notes += page.extract_text()

    st.text_area("Uploaded Notes", notes, height=200)

summary_type = st.selectbox(
    "Choose Summary Type",
    [
        "Bullet Points",
        "Short Summary",
        "Detailed Summary",
        "Beginner Friendly"
    ]
)

if st.button("Summarize"):

    if notes.strip() == "":

        st.warning("Please enter some notes.")

    else:

        try:

            with st.spinner("Generating Summary..."):

                summary = summarize_notes(notes, summary_type)

            st.subheader("Summary")

            st.write(summary)

        except Exception:

            st.error(
                "Gemini API is currently overloaded or unavailable. Please try again in a few moments."
            )