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


def load_images_from_folder(user):    
    data = read_json()
    list_of_images = []
    for i in data:
        if type(data[i]) == list: # element in json is not picture but list of users
            continue
        if data[i]["image"] is not None:
            list_of_images.append(data[i])
    return list_of_images

"""def load_images_from_folder(folder):
        images = []
        with open(folder, "r") as slike:
        for filename in slike:
            img = matplotlib.image.imread(os.path.join(slike, filename))
            if img is not None:
                images.append(img) 
        return images """

def save_picture(slika):
    with io.BytesIO() as output:
        slika.save(output)
        contents = output.getvalue()
        return str(contents)
    

def resized_image(image_path):
    basewidth = 300
    img = Image.open(image_path)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(image_path)
