import os
from flask import Flask, request, render_template
import fitz  # PyMuPDF for PDF text extraction
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

# List of supported languages with their code
languages = {
    'es': 'Spanish',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'sa': 'Sanskrit',  # Sanskrit code is 'sa'
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'en': 'English',  # Ensure 'en' for English is available
}

# Ensure the upload folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', translated_text=None, languages=languages, error=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file part is included in the request
    if 'file' not in request.files:
        return render_template('index.html', translated_text=None, languages=languages, error="No file part")
    
    file = request.files['file']
    
    # If no file is selected
    if file.filename == '':
        return render_template('index.html', translated_text=None, languages=languages, error="No selected file")
    
    # Check if the file is a PDF
    if file and file.filename.endswith('.pdf'):
        # Save the file temporarily to extract text
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)  # Full path to the uploads directory
        try:
            file.save(file_path)
        except Exception as e:
            return render_template('index.html', translated_text=None, languages=languages, error=f"Error saving file: {str(e)}")
        
        # Extract text from PDF using PyMuPDF
        try:
            text = extract_text_from_pdf(file_path)
        except Exception as e:
            return render_template('index.html', translated_text=None, languages=languages, error=f"Error extracting text: {str(e)}")
        
        # Check if text extraction was successful
        if not text:
            return render_template('index.html', translated_text=None, languages=languages, error="Could not extract text from the PDF")
        
        # Get the selected language from the form (default to 'es' for Spanish)
        target_language = request.form.get('language', 'es') 
        
        try:
            # Translate the extracted text to the selected language using googletrans
            translated_text = translator.translate(text, dest=target_language)
        except Exception as e:
            # If the translation fails for Sanskrit (or any language), fallback to Hindi or English
            if target_language == 'sa':
                translated_text = translator.translate(text, dest='hi')  # Fallback to Hindi
                return render_template('index.html', translated_text=translated_text.text, languages=languages, error=f"Error during translation: {str(e)} (Fallback to Hindi)")
            return render_template('index.html', translated_text=None, languages=languages, error=f"Error during translation: {str(e)}")
        
        # Render the page with the translated text
        return render_template('index.html', translated_text=translated_text.text, languages=languages, error=None)
    
    # If the uploaded file is not a valid PDF
    return render_template('index.html', translated_text=None, languages=languages, error="Invalid file format")


def extract_text_from_pdf(file_path):
    """Extract text from a PDF using PyMuPDF."""
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Load a page
            text += page.get_text("text")  # Extract text
        return text
    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
