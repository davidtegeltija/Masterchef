import bottle
import os
import json
from model import *

@bottle.route("/static/<filename>")
def staticen_server(filename):
    return bottle.static_file(filename, root= "./Datoteke")

@bottle.get("/")
def index(): 
    podatki = seznam_podatkov()
    for oseba in podatki:
        if "." in oseba[4]: #imamo pravo sliko
            slika = True
        else:
            slika = False
        return bottle.template("index.html", podatki = podatki, slika = slika)

@bottle.get("/vseckano")
def vseckano():
    return bottle.template("vseckano.html")

@bottle.get("/dodaj")
def dodaj():
    return bottle.template("dodaj.html")

@bottle.post("/dodaj_recept")
def dodaj_recept():
    ime = bottle.request.forms.get("Ime")
    priimek = bottle.request.forms.get("Priimek")    
    naslov = bottle.request.forms.get("Naslov")
    recept = bottle.request.forms.get("Recept")
    slika = bottle.request.files.get("Slika")

    data = read_json()
    index = len(data) + 1

    if slika is not None:
        ext = slika.filename.split(".")[-1]
        if ext not in (".png", ".jpg", ".jpeg"):
            return bottle.template("error.html")
        file_path = "Datoteke/{file}".format(file=slika.filename) 
        slika.save(file_path)
        data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "recipe" : recept, "image" : file_path}
        write_json(data)
    else:
        data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov,  "recipe" : recept, "image" : "Nobena slika ni bila naložena"}
        write_json(data)
    return bottle.redirect("/")



#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe




#@bottle.post("/isci/<vneseno>")
#def isci(vneseno):
#    return bottle.template
# obrazec za iskanje ima GET poizvedbo


bottle.run(debug=True, reloader=True)