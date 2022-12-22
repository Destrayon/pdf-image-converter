import os
from PIL import Image

directory = os.getcwd()

def program():

    list_image_paths = []
    list_images = []
    for entry in os.scandir():
        if entry.name.endswith('.png'):
            list_image_paths.append(entry.path)

    for item in list_image_paths:
        image = Image.open(item).convert('RGB')
        list_images.append(image)

    list_images[0].save(directory + "/output/output.pdf", save_all=True, append_images=list_images[1:])

program()