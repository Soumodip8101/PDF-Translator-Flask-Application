<h1>PDF Translator – Flask Application</h1>
A simple and elegant web application that extracts text from PDF files and translates it into multiple languages. Built using Flask, PyMuPDF, and googletrans.
🚀<h2>Features</h2> 
✅ Upload a PDF file<br>
✅ Extract text automatically using PyMuPDF (fitz)<br>
✅ Translate text into supported languages<br>
✅ User-friendly responsive web interface<br>
✅ Error handling for unsupported files and translation failures<br>
✅ Automatic fallback translation for Sanskrit<br>
📂 <h3>Project Structure</h3>
project_folder/
│ app.py
│ README.md
│
├── templates/
│    └── index.html
│
└── uploads/  (auto-created at runtime)
🛠 <h4>Requirements</h4>
Install necessary Python packages:
pip install flask pymupdf googletrans==4.0.0-rc1
▶️<h5>How to Run</h5> 
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
es	Spanish<br>
fr	French<br>
de	German<br>
it	Italian<br>
pt	Portuguese<br>
en	English<br>
hi	Hindi<br>
bn	Bengali<br>
sa	Sanskrit<br>
⚠️ Sanskrit translation may fail depending on googletrans API.<br>
✅ The app includes a fallback to Hindi.<br>
🧠 How It Works<br>
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
Flask – Web Framework<br>
PyMuPDF – PDF text extraction<br>
googletrans – Translation API<br>
