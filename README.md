<h1>PDF Translator – Flask Application</h1>
A simple and elegant web application that extracts text from PDF files and translates it into multiple languages. Built using Flask, PyMuPDF, and googletrans.
🚀 Features
✅ Upload a PDF file
✅ Extract text automatically using PyMuPDF (fitz)
✅ Translate text into supported languages
✅ User-friendly responsive web interface
✅ Error handling for unsupported files and translation failures
✅ Automatic fallback translation for Sanskrit
📂 Project Structure
project_folder/
│ app.py
│ README.md
│
├── templates/
│    └── index.html
│
└── uploads/  (auto-created at runtime)
🛠 Requirements
Install necessary Python packages:
pip install flask pymupdf googletrans==4.0.0-rc1
▶️ How to Run
1. Ensure Python 3 is installed
Check version:
python3 --version
If python3 works but python does not, use python3 in all commands.
2. Install dependencies
pip3 install flask pymupdf googletrans==4.0.0-rc1
3. Run the Flask server
python3 app.py
You should see:
 * Running on http://127.0.0.1:5000/
4. Open in Browser
Go to:
http://127.0.0.1:5000/
🌍 Supported Languages
Code	Language
es	Spanish
fr	French
de	German
it	Italian
pt	Portuguese
en	English
hi	Hindi
bn	Bengali
sa	Sanskrit
⚠️ Sanskrit translation may fail depending on googletrans API.
✅ The app includes a fallback to Hindi.
🧠 How It Works
✔ PDF Text Extraction
The app uses PyMuPDF (fitz) to extract text from each page:
page.get_text("text")
✔ Translation
Uses googletrans to translate extracted text:
translated_text = translator.translate(text, dest=target_language)
⚠️ Known Issues
Some PDFs may contain scanned images – text extraction may fail (requires OCR).
googletrans API may fail intermittently.
Sanskrit translations may not always be reliable.
🧩 Future Improvements
🔹 Add OCR support (Tesseract)
🔹 Export translated text to PDF/Word
🔹 Add language detection
🔹 Improve UI formatting and layout
✨ Credits
Flask – Web Framework
PyMuPDF – PDF text extraction
googletrans – Translation API
