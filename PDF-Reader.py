import PyPDF2
import pyttsx3
path=open("book.pdf",'rb')
pdfReader=PyPDF2.PdfReader(path)
start=pdfReader.pages[100]
text=start.extract_text()
speak=pyttsx3.init()
speak.say(text)
speak.runAndWait()