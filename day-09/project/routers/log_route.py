from fastapi import HTTPException
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile
from services.log_analyzer import analyze_logs
import os

router = APIRouter()

@router.get("/upload", response_class=HTMLResponse) 
async def upload_form(): 
    return """ <!DOCTYPE html>
    <html> 
    <head> <title>Upload a File</title> 
    </head> 
    <body> <h2>Upload a File</h2> 
    <form action="/files/" method="post" enctype="multipart/form-data"> 
    <input type="file" name="file">
    <button type="submit">Upload</button> 
    </form> 
    </body> 
    </html> """

@router.post("/files/")
async def create_file(file: UploadFile):
    if not file.filename.endswith(".log"):
            print("Invalid file type")
            raise HTTPException(status_code=400, detail="Only .log files are allowed")
    try:                         
        lines = []
        for line in file.file:
            lines.append(line.decode("utf-8").strip())
        result = analyze_logs(lines)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return result