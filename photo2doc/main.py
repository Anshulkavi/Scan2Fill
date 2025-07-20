# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# import os
# from fastapi import UploadFile, File
# from fastapi.responses import JSONResponse
# from PIL import Image
# import pytesseract
# import io

# app = FastAPI()

# # Set custom tesseract path
# pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract\tesseract.exe"

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Mount the static directory (VERY IMPORTANT)
# app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "app", "static")), name="static")

# # Point templates to correct directory
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "app", "templates"))

# @app.get("/")
# async def read_form(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     contents = await file.read()

#     try:
#         # Load image from bytes
#         image = Image.open(io.BytesIO(contents))

#         # Run OCR using pytesseract
#         text = pytesseract.image_to_string(image)

#         return {"filename": file.filename, "extracted_text": text}

#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import os
from pdf2image import convert_from_bytes

app = FastAPI()

# Set tesseract and poppler paths
pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract\tesseract.exe"
POPPLER_PATH = r"E:\Poppler\poppler-24.08.0\Library\bin"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "app", "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "app", "templates"))

@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename.lower()

    try:
        if filename.endswith(".pdf"):
            images = convert_from_bytes(contents, poppler_path=POPPLER_PATH)
            text = ""
            for img in images:
                text += pytesseract.image_to_string(img)
        else:
            image = Image.open(io.BytesIO(contents))
            text = pytesseract.image_to_string(image)

        return {"filename": file.filename, "extracted_text": text}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
