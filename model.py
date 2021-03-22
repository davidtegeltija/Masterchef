import bottle
import os
import json
import re

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
    for oseba in data["recepti"]:
        seznam_za_osebo = []
        kljuci = data["recepti"][oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "owner":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti][0])
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti][1])
            if lastnosti == "title":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
            if lastnosti == "ingredients":  
                sestavine = data["recepti"][oseba][lastnosti].split("-")
                sestavine.pop(0)
                seznam_za_osebo.append(sestavine)
            if lastnosti == "procedure":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
            if lastnosti == "image":
                if "/" in data["recepti"][oseba][lastnosti]:
                    ime_slike = data["recepti"][oseba][lastnosti].split("/")
                    seznam_za_osebo.append(ime_slike[1])
                else:
                    seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
            if lastnosti == "likes":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
            if lastnosti == "dislikes":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])

        seznam_podatkov.append(seznam_za_osebo)
    return seznam_podatkov

def seznam_slik():
    data = read_json()
    slike = []
    for oseba in data["recepti"]:
        kljuci = data["recepti"][oseba].keys()
        for lastnosti in kljuci:
            if lastnosti == "image":
                if data["recepti"][oseba][lastnosti] is not None:
                    ime_slike = data["recepti"][oseba][lastnosti].split("/")
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
    for oseba in data["recepti"]:
        if data["recepti"][oseba]["image"].split("/")[1] == slika:
            data["recepti"][oseba]["likes"] += 1
    write_json(data)

def glasuj_proti(slika):
    data = read_json()
    for oseba in data["recepti"]:
        if data["recepti"][oseba]["image"].split("/")[1] == slika:
            data["recepti"][oseba]["dislikes"] += 1
    write_json(data)

def preveri_slovnico(beseda):
    if re.match("^[A-Za-z0-9_-]*$", beseda):
        return True
    return False

def prosto_uporabnisko_ime(ime, geslo):
    if not(preveri_slovnico(ime) and preveri_slovnico(geslo)):
        return False
    data = read_json()
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == ime:
            return False
    return True

def preveri_prijavo(ime, geslo):
    if preveri_slovnico(ime) and preveri_slovnico(geslo):
        data = read_json()
        for uporabnik in data["uporabniki"]:
            if data["uporabniki"][uporabnik]["username"] == ime and data["uporabniki"][uporabnik]["password"] == geslo:
                return True
    return False

def zahtevaj_prijavo():
    if bottle.request.get_cookie("uporabnik"):
        return True
    return False

def vsec_mi_je_slika(slika, uporabnisko_ime):
    data = read_json()
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            moje_slike = vseckane_slike(uporabnisko_ime)
            moje_slike.append(str(slika))
            data["uporabniki"][uporabnik]["liked_photos"] = moje_slike
    write_json(data)

def vseckane_slike(uporabnisko_ime):
    data = read_json()
    vseckane = []
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            if len(data["uporabniki"][uporabnik]["liked_photos"]) != 0:
                for slika in data["uporabniki"][uporabnik]["liked_photos"]:
                    vseckane.append(slika)
            else:
                return []
    return vseckane

def vseckani_recepti(uporabnisko_ime):
    data = read_json()
    vseckani = []
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            for slika in vseckane_slike(uporabnisko_ime):
                for recept in seznam_podatkov():
                    if slika == recept[5]:
                        vseckani.append(recept[:6])
    return vseckani