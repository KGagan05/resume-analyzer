from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from analyzer import analyze_resume

app = FastAPI()
templates = Jinja2Templates(directory="templates")

job_description = """
We are looking for a Python developer with experience in Machine Learning,
Deep Learning, NLP, SQL, and building AI models.
"""


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):

    print("🔥 Analyze clicked")

    content = await file.read()
    resume_text = content.decode("utf-8", errors="ignore")

    score, skills, missing = analyze_resume(resume_text, job_description)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "score": score,
        "skills": skills,
        "missing": missing
    })