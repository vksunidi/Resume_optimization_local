Resume Optimization Using Local Language Models for Job Matching

---

## 1. Abstract

This project presents a Python-based system for automated resume optimization using locally hosted large language models (LLMs). With the increasing adoption of AI in recruitment, tailoring resumes to specific job descriptions has become a crucial yet repetitive task. This project uses open-source tools such as **Ollama** to run models like **Mistral** locally, avoiding cloud dependencies like the OpenAI API. The system reads a resume in Markdown format, processes a job description, and generates an optimized resume highlighting relevant skills and experiences. The final output is rendered in PDF format using Pyppeteer. This approach is scalable, privacy-preserving, and cost-effective.

---

## 2. Introduction

In competitive job markets, generic resumes often fail to capture employer attention. Customizing resumes to match specific job descriptions significantly improves shortlisting chances. However, manually rewriting resumes is tedious and error-prone. This project aims to automate this process using local LLMs — providing a private, offline alternative to cloud-based services like OpenAI's GPT.

---

## 3. Objectives

- To design a system that dynamically tailors resumes to job descriptions.
- To implement this system using local LLMs (Ollama + Mistral).
- To generate Markdown-based resumes optimized for specific job roles.
- To convert the generated Markdown into a PDF for professional use.

---

## 4. Methodology

### 4.1 Tools and Technologies

- **Ollama**: Framework to run open-source LLMs like Mistral locally.
- **Python**: Core scripting language.
- **Markdown2**: Converts Markdown to HTML.
- **Pyppeteer**: Renders HTML into PDF using headless Chromium.
- **VS Code**: Development environment on macOS.

### 4.2 Process Flow

1. **Input Collection**: The user provides a `resume.md` and `job_description.txt`.
2. **Prompt Construction**: A custom prompt is created to guide the LLM in rewriting the resume.
3. **LLM Execution**: Python calls `ollama run mistral` with the prompt using subprocess.
4. **Output Parsing**: The model's output (optimized resume) is saved in `updated_resume.md`.
5. **Conversion**: Markdown is converted to HTML and then to PDF using Pyppeteer.

---

## 5. Results

The system successfully rewrote resumes to reflect job-specific skills and keywords. The final resume was well-structured and ready for submission. Tests across multiple job descriptions demonstrated adaptability and clarity in the generated content. Sample output files (`updated_resume.md`, `.html`, `.pdf`) were generated consistently.

---

## 6. Advantages

- **Privacy**: All processing happens locally.
- **Cost**: No reliance on paid APIs.
- **Flexibility**: Works for any resume format and job role.
- **Customizable**: Easily extensible to include cover letter generation.

---

## 7. Limitations

- Model quality depends on the capability of the local model (Mistral is good, but GPT-4 is stronger).
- Initial setup requires downloading large models.
- Pyppeteer can be heavy for simple use cases.

---

## 8. Future Work

- Add batch optimization (process multiple resumes at once).
- Use better fine-tuned models for resume rewriting.
- Create a simple web interface using Flask or Streamlit.
- Add keyword analytics to show resume-JD match score.

---

## 9. Conclusion

This project demonstrates the practical use of open-source LLMs in resume optimization, offering a privacy-friendly and cost-effective alternative to commercial AI services. With local model capabilities advancing rapidly, such tools can empower users to enhance their job search effectively.

---

## 10. References

- Ollama: https://ollama.com  
- Pyppeteer: https://github.com/pyppeteer/pyppeteer  
- Markdown2: https://github.com/trentm/python-markdown2  
- Mistral AI: https://mistral.ai    
