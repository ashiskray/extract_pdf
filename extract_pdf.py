# import PyPDF2

# # Open the PDF file in binary read mode
# with open(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\sample.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0]
#     text = page.extract_text()
#     print(text)

import PyPDF2
with open(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\sample.pdf","rb") as file:
    reader = PyPDF2.PdfReader(file)
    page =reader.pages[0]
    text = page.extract_text()
    print (text)
