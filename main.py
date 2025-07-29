import subprocess
import markdown
import pdfkit
import asyncio
from pyppeteer import launch

with open ("resume.md","r") as f:
    md_resume = f.read()

with open ("job_description.txt","r") as f:
    job_description = f.read()



prompt = f"""
I have a resume formatted in Markdown and a job description. Please adapt my resume to better align with the job requirements.

### Resume (Markdown):
{md_resume}

### Job Description:
{job_description}

Please modify the resume to:
- Use keywords from the job description.
- Emphasize relevant skills.
- Maintain professionalism.
Return the updated resume in Markdown format.
"""

def query_ollama(prompt):
    result = subprocess.run(["ollama", "run", "mistral"], input=prompt.encode(), stdout=subprocess.PIPE)
    return result.stdout.decode()

response = query_ollama(prompt)


with open("updated_resume.md","w") as f:
    f.write(response)

updated_html= markdown.markdown(response)

with open ("updated_html.html","w") as f:
    f.write(updated_html)

async def html_to_pdf(input_html: str, output_pdf: str):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    with open(input_html, "r") as f:
        content = f.read()
    await page.setContent(content)
    await page.pdf({'path': output_pdf, 'format': 'A4'})
    await browser.close()

# Convert HTML to PDF
asyncio.get_event_loop().run_until_complete(html_to_pdf("updated_html.html", "updated_resume.pdf"))




#pdfkit.from_file("updated_html.html","updated_resume.pdf")

print(" Resume is successfully saved in pdf which aligns with the given job description ")




