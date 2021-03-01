import bottle
import os
import json
from PIL import Image
import io

path_to_json = os.path.join(os.getcwd(),"./", "Datoteke", "data.json")
path_to_images = os.path.join(os.getcwd(),"..", "Datoteke")

def read_json():
    with open(path_to_json, "r", encoding="utf8") as json_file:
        data = json.load(json_file)
        return data

def write_json(data):
    with open(path_to_json, "w", encoding="utf8") as json_file:
        if data is not None:
            json.dump(data, json_file, indent=4)


def seznam_slik():    
    data = read_json()
    list_of_images = []
    for oseba in data:
        kljuci = data[oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "image":
                if data[oseba][lastnosti] is not None:
                    ime_slike = data[oseba][lastnosti].split("/")
                    list_of_images.append(ime_slike[1])
    print(list_of_images)
    return list_of_images

"""def load_images_from_folder(folder):
        images = []
        with open(folder, "r") as slike:
        for filename in slike:
            img = matplotlib.image.imread(os.path.join(slike, filename))
            if img is not None:
                images.append(img) 
        return images """

def ime_slike(slika):
    file_path = "Datoteke/{file}".format(file=slika.filename)
    imeni = file_path.split("/")
    return imeni[1]
    

def resized_image(image_path):
    basewidth = 300
    img = Image.open(image_path)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(image_path)
