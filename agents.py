import os
import requests
from fpdf import FPDF
import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama
from dotenv import load_dotenv


# ------------------ OMDb API ------------------
OMDB_API_KEY = "81c5dbe2"  

def fetch_movie_data(title: str):
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "apikey": OMDB_API_KEY,
        "plot": "full"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


# ================== PDF GENERATOR ==================
def generate_pdf(text: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_name = "movie_report.pdf"
    pdf.output(file_name)
    return file_name


# ================== AGENT ==================
analysis_agent = Agent(
    name="Movie Analysis Agent",
    model=Ollama(model="llama3.1"),
    description="Analyzes movie data and answers user questions.",
    instructions=[
        "Use only the provided movie data",
        "Answer user questions strictly related to the movie",
        "Generate a clear, factual paragraph summary"
    ],
    markdown=True
)