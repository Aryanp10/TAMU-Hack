# import tabula as tb
# import camelot
# import pandas as pd
# import numpy as np
import re
from PyPDF2 import PdfFileReader, PdfFileWriter

# Read all the text from a pdf file and save teh content on


def fileReader2(pagelist):
    pdfName = open("file.pdf", 'rb')
    try:
        pdfRead = PdfFileReader(pdfName)
        for i in range(pdfRead.getNumPages()):
            page = pdfRead.getPage(i)
            pagelist.append(page.extractText().replace('\n', ''))
            # page.extractText()
    except Exception as e:
        print("Error {}".format(e))

# Extract Important information ("Course info", "Meeting time", etc.)


# def extractInfo(pagelist):
#     print("Hello")


# def camReader():
#     tables = camelot.read_pdf("extraction/file2.pdf")
#     print(tables)


# def tabReader():
#     tb.io.read_pdf_with_template(
#         input_path="extraction/file2.pdf", stream=True)


# def tableReader():
#     pdfName = "extraction/file3.pdf"

#     try:

#         dfs = tb.read_pdf(pdfName, pages='all', multiple_tables=True)
#         print(dfs[0][0][0])
#     except Exception as e:
#         print("Error {}".format(e))


if __name__ == "__main__":
    pagelist = []
    fileReader2(pagelist)
    # print(pagelist[0])
    # counter = 0
    temp = str(pagelist)
    temp_split = temp.split()
    # [x.lower() for x in temp_split]

    # for i in range(len(temp_split)):
    #     if i == '\n':
    # temp_split.remove()

    # [temp_split.pop(i) for i, v in enumerate(temp_split) if v in ['\\n']] 
    temp_split.remove("['")
    # print (temp_split)
    course = ''
    location = ''
    time = ''
    faculty = ''
    counter = 0
    eva_gra = ''
    i = ''
    for i in temp_split:
        if i != 'TIME:':
            course += i
            course += ' '
            
        else:
            del temp_split[:temp_split.index('TIME:')]
            break

    for i in temp_split:
        if i != 'LOCATION:':
            time += i
            time += ' '
            # temp_split.pop(i)
        else:
            del temp_split[:temp_split.index('LOCATION:')]
            break
    
    for i in temp_split:
        if i != 'FACULTY:':
            location += i
            location += ' '
            # temp_split.pop(i)
        else:
            del temp_split[:temp_split.index('FACULTY:')]
            break            

    for i in temp_split:
        if i != 'OFFICE':
            faculty += i
            faculty += ' '
            # temp_split.pop(i)
        else:
            del temp_split[:temp_split.index('OFFICE')]
            break      

    for i in temp_split:
        if i != 'OFFICE':
            faculty += i
            faculty += ' '
            # temp_split.pop(i)
        else:
            del temp_split[:temp_split.index('OFFICE')]
            break  

    for i in temp_split:
        if i == 'VII.':
            del temp_split[:temp_split.index('VII.')]
            break
        else:
            pass
    del temp_split[0]
    for i in temp_split:
        if i != 'NOTE:':
            eva_gra += i
            eva_gra += ' '
            # temp_split.pop(i)
        else:
            break  
    
    # for i in temp_split:

    #     if i != 'TIME' and i != 'LOCATIION':
    #         course += i
    #         course += ' '
    #     elif i != 'LOCATION':
    #         location+= i
    #         location += ' '
    #     else:
    #         break
    
    print(course)
    print('\n')
    print(time)
    print('\n')
    print(location)    
    print('\n')
    print(faculty)
    print('\n')
    print(eva_gra)

    # print(location)


    # for i in range(2):

    #     print(temp_fix[i])
    
    # for index, i in enumerate(temp_split):
    #     # print (temp_split[0])
    #     if i == 'course':
    #         print (temp_split[index + 1])

        # for f in i:
        #     print(f)
        #     if f == 'COURSE':
        #         print("GOT IT!")
        #         exit()



    print('HERE')
        # print(i)
    #     for f in i:
    #         if f ==
    #         print(counter)
    #         counter = counter + 1
    # print(counter)
    # counter = counter + 1
