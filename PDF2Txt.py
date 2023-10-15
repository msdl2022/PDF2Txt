import PyPDF2

# Open the PDF file in read-binary mode
with open('input.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Create a text file for output
    with open('output.txt', 'w') as text_file:
        
        # Iterate through each page in the PDF
        for page_num in range(pdf_reader.numPages):
            
            # Extract text from the current page
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            
            # Write the extracted text to the text file
            text_file.write(page_text)

# Close the files
pdf_file.close()
text_file.close()
