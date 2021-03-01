import bottle
import os
import json
from model import *

@bottle.route("/static/<filename>")
def staticen_server(filename):
    return bottle.static_file(filename, root= "./Datoteke")

@bottle.get("/")
def index(): 
    slike = seznam_slik() 
    Ime = imena()
    Priimek = priimki()
    return bottle.template("index.html", seznam_slik = slike, ime = Ime, priimek = Priimek)

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
        name, ext = os.path.splitext(slika.filename)
        if ext not in (".png", ".jpg", ".jpeg"):
            return bottle.template("error.html")
        file_path = "Datoteke/{file}".format(file=slika.filename)
        slika.save(file_path)
        data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "recipe" : recept, "image" : file_path}
        write_json(data)
    else:
        data[f"person_{index}"] = {"owner" : [ime, priimek], "title" : naslov,  "recipe" : recept, "image" : None}
        write_json(data)
    return bottle.redirect("/")



#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe






"""@post('/update')
def update():
    # Form data
    title = request.forms.get("title")
    body = request.forms.get("body")
    image = request.forms.get("image")
    author = request.forms.get("author")
    
    # Image upload
    file = request.files.get("file")
    if file:
        extension = file.filename.split(".")[-1]
        if extension not in ('png', 'jpg', 'jpeg'):
            return {"result" : 0, "message": "File Format Error"}
        save_path = "my/save/path"
        file.save(save_path)"""

#@bottle.post("/isci/<vneseno>")
#def isci(vneseno):
#    return bottle.template
# obrazec za iskanje ima GET poizvedbo


bottle.run(debug=True, reloader=True)