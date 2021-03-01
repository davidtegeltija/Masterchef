import bottle
import os
import json
from PIL import Image

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
    return list_of_images

def imena():
    data = read_json()
    ime = []
    for oseba in data:
        kljuci = data[oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "owner":
                ime.append(data[oseba][lastnosti][0])
    return ime

def priimki():
    data = read_json()
    priimek = []
    for oseba in data:
        kljuci = data[oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "owner":
                priimek.append(data[oseba][lastnosti][1])
    return str(priimek)

def resized_image(slika):
    basewidth = 300
    img = Image.open(slika)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(slika)
