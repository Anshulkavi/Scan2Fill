# 📄 Scan2Fill – Auto-Fill Forms from Images

**Scan2Fill** is a powerful tool that lets users upload photos of printed or handwritten forms (e.g. government forms, college forms) and automatically extracts key information using **OCR (Optical Character Recognition)** to pre-fill digital form templates.

> Built with **FastAPI** and **vanilla HTML/CSS/JS**, this project aims to simplify manual data entry from physical forms.

---

## 🚀 Features (MVP – Initial Stage)

- 📤 Upload scanned images or PDFs of forms  
- 🧠 Backend powered by **FastAPI**  
- 🧾 Frontend with clean **HTML + CSS**  
- ⚙️ Project-ready folder structure with static files and templates  
- 🛠️ Setup for integrating **OCR & field detection** (Tesseract or Google Vision API)  

---

## 🗂️ Project Structure

<pre> Scan2Fill/ 
    └── photo2doc/
    ├── main.py # FastAPI entry point 
    └── app/ 
        ├── templates/  
        │   └── index.html # Main upload page
        └── static/ 
            ├── style.css # Styling 
            └── script.js # Client-side JS (to be added)
</pre>

---

## ⚙️ Tech Stack

- 🐍 **FastAPI** – for backend API and templating  
- 🎨 **HTML/CSS/JS** – for frontend  
- 🔍 (Upcoming) **OCR Integration** – Tesseract or Google Vision  
- 🗃️ (Planned) **MongoDB/PostgreSQL** – for storing user-submitted data  

---

## 🧪 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/Scan2Fill.git
cd Scan2Fill/photo2doc

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install fastapi uvicorn jinja2

# 4. Run the server
uvicorn main:app --reload

# Visit
http://127.0.0.1:8000/
```
📌 To-Do (Upcoming Features)
🧠 OCR Text Extraction

🧩 Auto Mapping of Fields (like Name, DOB, etc.)

📝 Fillable Form Preview

🧾 Export to PDF

🧑‍💻 User Accounts & Saved History

☁️ Deployment on Render/Heroku

🤝 Contributions
Open to ideas, feedback, and collaboration.
Let’s make form filling painless 💡

📜 License
MIT License

