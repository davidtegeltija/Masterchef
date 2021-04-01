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
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
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
            if lastnosti == "comments":
                seznam_za_osebo.append(data["recepti"][oseba][lastnosti])
        seznam_podatkov.append(seznam_za_osebo)
    return seznam_podatkov


def seznam_receptov():
    data = read_json()
    recepti = []
    for oseba in data["recepti"]:
        ime_recepta = data["recepti"][oseba]["title"]
        recepti.append(ime_recepta)
    return recepti


def seznam_slik():
    data = read_json()
    slike = []
    for oseba in data["recepti"]:
        slika = data["recepti"][oseba]["image"]
        if "$" in slika:
            ime_slike = slika.split("/")[1]
            ime_slike.split("$")
            slike.append(ime_slike.split("$")[0] + ime_slike.split("$")[2])
        else:
            slike.append(slika.split("/")[1])
    return slike
        

def glasuj_za(recept):
    data = read_json()
    for oseba in data["recepti"]:
        if data["recepti"][oseba]["title"] == recept:
            data["recepti"][oseba]["likes"] += 1
    write_json(data)


def glasuj_proti(recept):
    data = read_json()
    for oseba in data["recepti"]:
        if data["recepti"][oseba]["title"] == recept:
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


def vsec_mi_je_recept(recept, uporabnisko_ime):
    data = read_json()
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            moji_recepti = vseckani_naslovi_receptov(uporabnisko_ime)
            if recept in moji_recepti:
                pass
            else:   
                moji_recepti.append(str(recept))
                data["uporabniki"][uporabnik]["liked_recipe"] = moji_recepti
    write_json(data)


def ni_mi_vsec_recept(recept, uporabnisko_ime):
    data = read_json()
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            moji_recepti = nevseckani_naslovi_receptov(uporabnisko_ime)
            if recept in moji_recepti:
                pass
            else:   
                moji_recepti.append(str(recept))
                data["uporabniki"][uporabnik]["disliked_recipe"] = moji_recepti
    write_json(data)


def vseckani_naslovi_receptov(uporabnisko_ime):
    data = read_json()
    vseckani = []
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            if len(data["uporabniki"][uporabnik]["liked_recipe"]) != 0:
                for recept in data["uporabniki"][uporabnik]["liked_recipe"]:
                    vseckani.append(recept)
            else:
                return []
    return vseckani


def nevseckani_naslovi_receptov(uporabnisko_ime):
    data = read_json()
    vseckani = []
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            if len(data["uporabniki"][uporabnik]["disliked_recipe"]) != 0:
                for recept in data["uporabniki"][uporabnik]["disliked_recipe"]:
                    vseckani.append(recept)
            else:
                return []
    return vseckani


def vseckani_recepti(uporabnisko_ime):
    data = read_json()
    vseckani = []
    for uporabnik in data["uporabniki"]:
        if data["uporabniki"][uporabnik]["username"] == uporabnisko_ime:
            for naslov in vseckani_naslovi_receptov(uporabnisko_ime):
                for recept in seznam_podatkov():
                    if naslov == recept[1]:
                        vseckani.append(recept[:5])
    return vseckani


def moji_recepti(uporabnisko_ime):
    moji = []
    for recept in seznam_podatkov():
        if recept[0] == uporabnisko_ime:
            moji.append(recept)
    return moji


def odstrani_recept(recept, uporabnik):
    data = read_json()
    vseckani_naslovi = vseckani_naslovi_receptov(uporabnik)
    moji_recepti = vseckani_recepti(uporabnik)
    for recepti in moji_recepti:
        if recept == recepti[1]:
            moji_recepti.remove(recepti)
            vseckani_naslovi.remove(recepti[1])
            for oseba in data["uporabniki"]:
                if data["uporabniki"][oseba]["username"] == uporabnik:
                    data["uporabniki"][oseba]["liked_recipe"] = vseckani_naslovi
                write_json(data)  


def domaca_stran(uporabnik):
    data = read_json()
    skupni_seznam_osebe = []
    for oseba in data["uporabniki"]:
        if data["uporabniki"][oseba]["username"] == uporabnik:
            vsec_mi_je = data["uporabniki"][oseba]["liked_recipe"]
            ni_mi_vsec = data["uporabniki"][oseba]["disliked_recipe"] 
            skupni_seznam_osebe.append(vsec_mi_je)
            skupni_seznam_osebe.append(ni_mi_vsec)
    return skupni_seznam_osebe


def komentiraj(recept, komentar):
    data = read_json()
    for recept_osebe in data["recepti"]:
        if data["recepti"][recept_osebe]["title"] == recept:
            data["recepti"][recept_osebe]["comments"].append(komentar)
    write_json(data)


def dodaj_recept(ime, naslov, sestavine, postopek, slika):
    data = read_json()
    ostevilcenje = len(data["recepti"]) + 1

    if slika is not None:
        if slika.filename not in seznam_slik():
            file_path = "Database/{file}".format(file=slika.filename) 
            slika.save(file_path)
            data["recepti"][f"recept_{ostevilcenje}"] = {"owner" : ime, 
                                                        "title" : naslov, 
                                                        "ingredients" : sestavine, 
                                                        "procedure" : postopek, 
                                                        "image" : file_path, 
                                                        "likes" : 0, 
                                                        "dislikes" : 0, 
                                                        "comments" : []}
        else:
            print(seznam_slik())
            print(slika.filename)
            ostevilcenje_slik = seznam_slik().count(slika.filename) + 1
            novo_ime = slika.filename.split(".")
            slika.filename = str(novo_ime[0] + f"${ostevilcenje_slik}$" + "." + novo_ime[1])
            print(slika.filename)
            file_path = "Database/{file}".format(file=slika.filename) 
            slika.save(file_path)  
            data["recepti"][f"recept_{ostevilcenje}"] = {"owner" : ime, 
                                                        "title" : naslov, 
                                                        "ingredients" : sestavine, 
                                                        "procedure" : postopek, 
                                                        "image" : file_path, 
                                                        "likes" : 0, 
                                                        "dislikes" : 0, 
                                                        "comments" : []}                         
        write_json(data)
    else:
        data["recepti"][f"recept_{ostevilcenje}"] = {"owner" : ime, 
                                                    "title" : naslov, 
                                                    "ingredients" : sestavine, 
                                                    "procedure" : postopek, 
                                                    "image" : "Database/noImage.png", 
                                                    "likes" : 0, 
                                                    "dislikes" : 0, 
                                                    "comments" : []}
        write_json(data)


def uredi(recept):
    data = read_json()
    for recept_osebe in data["recepti"]:
        if data["recepti"][recept_osebe]["title"] == recept:
            sestavine = data["recepti"][recept_osebe]["ingredients"]
    return sestavine


def shrani(Recept, nove_sestavine, nov_postopek, nova_slika):
    data = read_json()
    for recept in data["recepti"]:
        if data["recepti"][recept]["title"] == Recept:
            if nove_sestavine is not None:
                data["recepti"][recept]["ingredients"] = nove_sestavine
            if nov_postopek is not None:
                data["recepti"][recept]["procedure"] = nov_postopek
            if nova_slika is not None:
                if nova_slika.filename not in seznam_slik():
                    file_path = "Database/{file}".format(file=nova_slika.filename) 
                    nova_slika.save(file_path)
                    data["recepti"][recept]["image"] = file_path
                else:
                    ostevilcenje = seznam_slik().count(nova_slika.filename) + 1
                    novo_ime = nova_slika.filename.split(".")
                    nova_slika.filename = str(novo_ime[0] + f"${ostevilcenje}$" + "." + novo_ime[1])
                    file_path = "Database/{file}".format(file=nova_slika.filename) 
                    nova_slika.save(file_path)
                    data["recepti"][recept]["image"] = file_path
    write_json(data)