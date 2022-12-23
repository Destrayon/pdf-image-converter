import os
from pdf2image import convert_from_path

directory = os.getcwd()



def program():

    pdf_name = ""

    for entry in os.scandir():
        if entry.name.endswith('.pdf'):
            pdf_name = entry.path
            break

    if pdf_name == "":
        return

    images = convert_from_path(pdf_name, poppler_path = directory + "/poppler-22.12.0/Library/bin")

    isExist = os.path.exists(directory + "/output/")

    if not isExist:
        os.mkdir(directory + "/output/")
        
    counter = 1
    for page in images:
        page.save(directory + "/output/" + str(counter) + ".png", 'PNG')
        counter += 1

program()