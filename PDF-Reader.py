import PyPDF2
import pyttsx3
path=open("Atomic Habits.pdf",'rb')
pdfReader=PyPDF2.PdfReader(path)
start=pdfReader.pages[]
text=start.extract_text()
speak=pyttsx3.init()
speak.say(text)
speak.runAndWait()
