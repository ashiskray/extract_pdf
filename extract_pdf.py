import PyPDF2
with open(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\sample.pdf","rb") as file:  
    reader = PyPDF2.PdfReader(file)
    page =reader.pages[0]        # This is will open the 1st page only
    text = page.extract_text()
    print (text)
