from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def summarize_notes(notes, summary_type):
    if summary_type == "Bullet Points":

        prompt = f"""
        Summarize these notes into simple bullet points:

        {notes}
        """

    elif summary_type == "Short Summary":

        prompt = f"""
        Summarize these notes in a short paragraph using simple language:

        {notes}
        """

    elif summary_type == "Detailed Summary":

        prompt = f"""
        Provide a detailed summary of these notes with all important concepts:

        {notes}
        """

    elif summary_type == "Beginner Friendly":

        prompt = f"""
        Explain these notes in very simple beginner-friendly language:

        {notes}
        """
        
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
