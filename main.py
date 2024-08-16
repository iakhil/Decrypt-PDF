import PyPDF2

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

# Example usage
input_pdf = 'aadhar.pdf'     # Path to your encrypted PDF
output_pdf = 'Akhil_Aadhar.pdf'    # Path where the decrypted PDF will be saved
password = 'AKHI1999'      # The password for the encrypted PDF

remove_pdf_password(input_pdf, output_pdf, password)
