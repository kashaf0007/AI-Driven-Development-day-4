# ⭐ Project Overview

OpenAgents SDK for agent workflow

Streamlit for a simple PDF-upload UI

Python 3.11+

PyPDF for extracting text from PDFs

Gemini CLI for generating summaries and quizzes

Context7 MCP as the tool provider for structured outputs
---

# A. PDF Summerizer ✨

User uploads a PDF file through the interface.

PyPDF extracts all readable text from the PDF.

The agent processes the text and generates a clean, meaningful summary using Gemini.

The summary is displayed in any UI style the student prefers (card view, block view, container, etc.).

# B. Quiz Generator 📘

After the summary is created, the user clicks Create Quiz.

The agent re-reads the original PDF content (not the summary).

It generates quizzes such as:

MCQs

Mixed-style quizzes

# project structure

task4/
│
├── .gemini/
│   └── settings.json       # Gemini CLI configuration
│
├── gemini.md               # Main agent prompt for Gemini
├── main.py                 
├── pyproject.toml          
├── README.md               # Documentation
├── .env                    
└── uv.lock                

# How to Run

 ## Install dependencies
pip install -r requirements.txt
## Start the Streamlit app
streamlit run main.py
## Run the Gemini agent
gemini run gemini.md
