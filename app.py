from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        pdf_file = request.files['pdf_file']
        if pdf_file and pdf_file.filename.endswith('.pdf'):
            pdf_reader = PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        else:
            return 'Invalid PDF file. Please select a valid PDF file.'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)