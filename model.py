import bottle
import os
import json
from PIL import Image

path_to_json = os.path.join(os.getcwd(),"./", "Database", "data.json")

def read_json():
    with open(path_to_json, "r", encoding="utf8") as json_file:
        data = json.load(json_file)
        return data

def write_json(data):
    with open(path_to_json, "w", encoding="utf8") as json_file:
        if data is not None:
            json.dump(data, json_file, indent=4)


def seznam_podatkov():    
    data = read_json()
    seznam_podatkov = []
    for oseba in data:
        seznam_za_osebo = []
        kljuci = data[oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "owner":
                seznam_za_osebo.append(data[oseba][lastnosti][0])
                seznam_za_osebo.append(data[oseba][lastnosti][1])
            if lastnosti == "title":
                seznam_za_osebo.append(data[oseba][lastnosti])
            if lastnosti == "ingredients":  
                sestavine = data[oseba][lastnosti].split("-")
                sestavine.pop(0)
                seznam_za_osebo.append(sestavine)
            if lastnosti == "procedure":
                seznam_za_osebo.append(data[oseba][lastnosti])
            if lastnosti == "image":
                if "/" in data[oseba][lastnosti]:
                    ime_slike = data[oseba][lastnosti].split("/")
                    seznam_za_osebo.append(ime_slike[1])
                else:
                    seznam_za_osebo.append(data[oseba][lastnosti])
            if lastnosti == "likes":
                seznam_za_osebo.append(data[oseba][lastnosti])
            if lastnosti == "dislikes":
                seznam_za_osebo.append(data[oseba][lastnosti])

        seznam_podatkov.append(seznam_za_osebo)
    return seznam_podatkov

def seznam_slik():
    data = read_json()
    slike = []
    for oseba in data:
        kljuci = data[oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "image":
                if data[oseba][lastnosti] is not None:
                    ime_slike = data[oseba][lastnosti].split("/")
                    slike.append(ime_slike[1])  
    return slike

def veljaven_recept(ime, priimek, sestavine, postopek):
    if len(ime) or len(priimek) != 0:
        if len(sestavine) != 0:
            if len(postopek) != 0:
                return True
    return False
        
def glasuj_za(slika):
    data = read_json()
    for oseba in data:
        if data[oseba]["image"].split("/")[1] == slika:
            data[oseba]["likes"] += 1
    write_json(data)

def glasuj_proti(slika):
    data = read_json()
    for oseba in data:
        if data[oseba]["image"].split("/")[1] == slika:
            data[oseba]["dislikes"] += 1
    write_json(data)

def resized_image(slika):
    basewidth = 300
    img = Image.open(slika)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(slika)
