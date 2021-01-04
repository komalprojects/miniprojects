import pyttsx3 as totext
import PyPDF2 as pdf
import slate3k as slate

book = open('E:/whatsapp/story.pdf', 'rb')
pdfReader = pdf.PdfFileReader(open('E:/whatsapp/story.pdf', 'rb'))
print(pdfReader)
pages = pdfReader.numPages
print(pages)
speaker = totext.init()
with open('E:/whatsapp/story.pdf', 'rb') as f :
    extracted_text = slate.PDF(f)
# print(extracted_text)
speaker.say(extracted_text)
speaker.runAndWait()
for num in range(3, pages):
    # page = pdfReader.getPage(num)
    text = pdfReader.getPage(num).extractText()
    # print(text.encode('utf-8'))

    # a = text.extractText()
    # print(text)
#     speaker.say(text)
#     speaker.runAndWait()