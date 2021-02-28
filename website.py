import bottle
import os
import json
from model import *

@bottle.route("/data/<filename>")
def staticen_server(filename):
    return bottle.static_file(filename, root= os.path.join(os.getcwd(),'..', "data"))

@bottle.get("/")
def index():       
    return bottle.template("index.html")

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
    recept = bottle.request.forms.get("Recept")
    slika = bottle.request.files.get("Slika")


    data = read_json()
    index = len(data) + 1
    data[index] = {"owner" : [ime, priimek], "recipe" : recept, "image" : save_picture(slika)}
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


#@bottle.post("/sestej/")
#def sestej():
#    a = int(bottle.request.forms["a"])
#    b = int(bottle.request.forms["b"])
#    return "{} + {} = {}".format(a, b, a + b)

bottle.run(debug=True, reloader=True)