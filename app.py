import streamlit as st
from summarizer import summarize_notes

st.title("AI Notes Summarizer")

notes = st.text_area("Paste your notes here")

if st.button("Summarize"):

    summary = summarize_notes(notes)

    st.subheader("Summary")

    st.write(summary)