import streamlit as st
from summarizer import summarize_notes

st.title("AI Notes Summarizer")

notes = st.text_area("Paste your notes here")

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