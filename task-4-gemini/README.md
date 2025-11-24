# Task day 4 🧑‍💻

## connect the Context7 MCP server to your Gemini CLI.✅

# 📚 PDF Summarizer & Quiz Generator Agent

This project is a **Study Notes Summarizer and Quiz Generator** built using **OpenAgents SDK**, **Streamlit**, **PyPDF**, **Gemini CLI**, and **Context7 MCP**. It allows students to upload PDFs, generate summaries, and create quizzes from the content.

---

## 🔧 Technologies Used

- **OpenAgents SDK** – For creating the agent workflow.
- **Streamlit** – User-friendly UI for PDF upload, summary display, and quiz generation.
- **PyPDF** – Extracts text from uploaded PDF files.
- **Gemini CLI** – AI model for text summarization and quiz generation.
- **Context7 MCP** – Provides structured outputs for the agent.

---

## 📝 Features

### A. PDF Summarizer 📁
1. User uploads a PDF file through the UI.
2. Text is extracted using PyPDF.
3. The agent generates a **clean and meaningful summary**.
4. The summary can be displayed in **different UI styles** (cards, blocks, containers, etc.).

### B. Quiz Generator 📁
1. After summarization, the user can click **Create Quiz**.
2. The agent reads the **original PDF content** (not the summary).
3. It generates quizzes, including:
   - Multiple Choice Questions (MCQs)
   - Correct answers for each question
   - Markdown-formatted output for easy readability

---

## ⚙️ How It Works

1. User uploads a PDF via the Streamlit sidebar.
2. The PDF content is extracted using PyPDF and stored in the session state.
3. Clicking **Generate Summary** calls the Gemini AI model to summarize the text.
4. Clicking **Create Quiz** generates a quiz based on the **original PDF text**.
5. Both summary and quiz are displayed in the Streamlit app.

---