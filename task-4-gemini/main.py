
import streamlit as st
import PyPDF2
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

st.set_page_config(layout="wide")

# ----------------------------
# Extract text from PDF
# ----------------------------
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        if page_text:
            text += page_text
    return text

# ----------------------------
# Generate Summary
# ----------------------------
def generate_summary(text):
    model = genai.GenerativeModel("gemini-2.0-flash")  # FIXED MODEL
    prompt = f"Summarize the following document:\n\n{text}\n\nSummary:"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return ""

# ----------------------------
# Generate Quiz with 3 Types
# ----------------------------
def generate_quiz(text, quiz_type="MCQ"):
    model = genai.GenerativeModel("gemini-2.0-flash")  # FIXED MODEL

    if quiz_type == "MCQ":
        instructions = """
        Generate a 5-question MCQ quiz. Each question must have:
        - 4 options
        - Correct answer clearly labeled
        """
    elif quiz_type == "True/False":
        instructions = """
        Generate a True/False quiz with 6 statements.
        Clearly mark each correct answer.
        """
    else:
        instructions = """
        Generate a short questions quiz with 5 questions.
        Provide answers in 2–3 lines.
        """

    prompt = f"""
    Based on this text, {instructions}

    Text:
    {text}

    {quiz_type} Quiz:
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating quiz: {e}")
        return ""

# ----------------------------
# Main Streamlit App
# ----------------------------
def main():
    st.title(" 📚 PDF Summarizer and Quiz Generator ✨")

    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.sidebar.success("📄 PDF uploaded successfully!")
        st.write("File uploaded:", uploaded_file.name)

        # Extract only once
        if "extracted_text" not in st.session_state:
            with st.spinner("Extracting text from PDF..."):
                text = extract_text_from_pdf(uploaded_file)
                st.session_state["extracted_text"] = text
            st.success("Text extraction complete!")

        # --------------------
        # Summary Button
        # --------------------
        if st.sidebar.button("📁 Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_summary(st.session_state["extracted_text"])
                st.session_state["summary"] = summary
            st.sidebar.success("Summary generated!")

        # --------------------
        # Quiz Type Selector
        # --------------------
        quiz_type = st.sidebar.selectbox(
            "Choose Quiz Type",
            ["MCQ", "True/False", "Short Questions"]
        )

        # --------------------
        # Quiz Button
        # --------------------
        if st.sidebar.button("📁 Create Quiz"):
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(st.session_state["extracted_text"], quiz_type)
                st.session_state["quiz"] = quiz
            st.sidebar.success("Quiz generated!")

        # --------------------
        # Show Summary
        # --------------------
        if "summary" in st.session_state:
            st.subheader("📘 Summary")
            st.markdown(st.session_state["summary"])

            st.download_button(
                "⬇ Download Summary",
                st.session_state["summary"],
                file_name="summary.txt",
                mime="text/plain"
            )

        # --------------------
        # Show Quiz
        # --------------------
        if "quiz" in st.session_state:
            st.subheader(f"📝 Generated Quiz ({quiz_type})")
            st.markdown(st.session_state["quiz"])

            st.download_button(
                "⬇ Download Quiz",
                st.session_state["quiz"],
                file_name="quiz.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
