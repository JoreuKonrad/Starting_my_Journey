# importing required modules
import PyPDF2
  
# creating a pdf file object
pdfFileObj = open('C:/Users/joreu.konrad/Desktop/Repo/PB/Testes/LeitorPDF/Fichas Técnicas de Produto - Elizabeth Revestimentos.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
  
# printing number of pages in pdf file
print(len(pdfReader.pages))
  
# creating a page object
pageObj = pdfReader.pages[0]
  
# extracting text from page
print(pageObj.extract_text())
  
# closing the pdf file object
pdfFileObj.close()