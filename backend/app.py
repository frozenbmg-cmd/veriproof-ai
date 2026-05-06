from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from extractor import extract_text
from plagiarism import check_plagiarism

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.get("/")
def home():
    return {"message": "VeriProof AI Backend Running"}

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    originality_score, plagiarism_results = check_plagiarism(extracted_text)

    return {
        "originality_score": originality_score,
        "matches_found": len(plagiarism_results),
        "plagiarism_details": plagiarism_results
    }
