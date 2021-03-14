import bottle
import os
import json
from model import *

@bottle.route("/static/<filename>")
def staticen_server(filename):
    return bottle.static_file(filename, root= "./Database")


@bottle.get("/")
def index(): 
    podatki = seznam_podatkov() 
    return bottle.template("index.html", podatki = podatki)

@bottle.get("/vseckano")
def vseckano():
    return bottle.template("vseckano.html")

@bottle.get("/dodaj")
def dodaj():
    return bottle.template("dodaj.html")

@bottle.get("/prijava")
def vseckano():
    return bottle.template("prijava.html")

@bottle.post("/logiraj_me")
def moj_profil():
    uporabnisko_ime = bottle.request.forms.get("Uporabnisko_ime")
    geslo = bottle.request.forms.get("Geslo") 
    return bottle.template("dodaj.html")

@bottle.get("/nov_profil")
def nov_profil():
    return bottle.template("registracija.html")

@bottle.post("/dodaj_recept")
def dodaj_recept():
    ime = bottle.request.forms.get("Ime")
    priimek = bottle.request.forms.get("Priimek")    
    naslov = bottle.request.forms.get("Naslov")
    sestavine = bottle.request.forms.get("Sestavine")
    postopek = bottle.request.forms.get("Postopek")
    slika = bottle.request.files.get("Slika")

    data = read_json()
    index = len(data) + 1

    if veljaven_recept(ime, priimek, sestavine, postopek):
        if slika is not None:
            name, ext = os.path.splitext(slika.filename)
            if ext not in (".png", ".jpg", ".jpeg"):
                return bottle.template("napacna_datoteka.html")
            file_path = "Database/{file}".format(file=slika.filename) 
            slika.save(file_path)
            data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : file_path, "likes" : 0, "dislikes" : 0}
            write_json(data)
        else:
            data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : "Database/noImage.png", "likes" : 0, "dislikes" : 0}
            write_json(data)
        return bottle.redirect("/")
    return bottle.template("ni_veljaven_recept.html")

@bottle.post("/glasuj_za")
def Glasuj_za():
    seznam = seznam_slik()
    for slika in seznam:
        if bottle.request.POST.get("ja") == slika:
            glasuj_za(slika)
    return bottle.redirect("/")
                    

@bottle.post("/glasuj_proti")
def Glasuj_proti():
    seznam = seznam_slik()
    for slika in seznam:
        if bottle.request.POST.get("ne") == slika:
            glasuj_proti(slika)
    return bottle.redirect("/")

#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe




#@bottle.post("/isci/<vneseno>")
#def isci(vneseno):
#    return bottle.template
# obrazec za iskanje ima GET poizvedbo


bottle.run(debug=True, reloader=True)