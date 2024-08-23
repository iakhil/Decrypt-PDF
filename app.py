import PyPDF2
from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])

def upload_file():
    file = request.files['file']
    password = request.files['password']

    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    file_path = remove_pdf_password(file_path, f"decrypted_{filename}", password)

    return send_file(file_path, as_attachment=True)

def remove_pdf_password(input_pdf, output_pdf, password):
    # Open the encrypted PDF
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Decrypt the PDF with the password
        if reader.is_encrypted:
            reader.decrypt(password)
        
        # Create a PdfWriter object to save the decrypted PDF
        writer = PyPDF2.PdfWriter()
        
        # Add all pages to the writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        
        # Write the decrypted content to a new PDF
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    curr_path = os.getcwd()
    return curr_path + "output_pdf.pdf"

if __name__ == '__main__':
    app.run(debug=True)