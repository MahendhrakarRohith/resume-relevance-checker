# app.py
import streamlit as st
from scripts.extract_resume import extract_pdf, extract_docx
from scripts.similarity import compute_similarity

st.set_page_config(page_title="Automated Resume Relevance Checker", layout="wide")
st.title("📝 Automated Resume Relevance Checker")

st.markdown("""
Upload a **job description** and a **resume** to get a relevance score.
""")

# Input Job Description
job_desc = st.text_area("Enter Job Description")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

# Check Relevance Button
if st.button("Check Relevance"):
    if not job_desc.strip():
        st.warning("Please enter a job description.")
    elif not resume_file:
        st.warning("Please upload a resume file.")
    else:
        try:
            # Extract text from resume
            if resume_file.type == "application/pdf":
                resume_text = extract_pdf(resume_file)
            elif resume_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                      "application/msword"]:
                resume_text = extract_docx(resume_file)
            else:
                st.error("Unsupported file type.")
                resume_text = None

            if resume_text:
                if not resume_text.strip():
                    st.warning("Could not extract text from the resume. Try another file.")
                else:
                    # Compute similarity score
                    score = compute_similarity(job_desc, resume_text)
                    st.success(f"Relevance Score: {score:.2f}")

                    # Optional: Preview first 1000 characters of resume
                    st.subheader("Resume Preview:")
                    st.text(resume_text[:1000] + "..." if len(resume_text) > 1000 else resume_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a job description and upload a resume to check relevance.")
