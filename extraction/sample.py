from PyPDF2 import PdfFileReader, PdfFileWriter

def fileReader():
    file_path = "extraction/file.pdf"
    pdfFileObj = open(file_path)
    pdfReader = PdfFileReader(pdfFileObj)

    print(pdfReader)

if __name__ == "__main__":
    fileReader()
    print("Hello")
