import bottle
import os
import matplotlib


@bottle.get("/")
def index():       
    return bottle.template("index.html")

def load_images_from_folder(folder):
        images = []
        for filename in os.listdir(folder):
            img = matplotlib.image.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img) 
        return images 
   

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
    return "{} + {} = {}".format(ime, priimek, recept)

#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe

@bottle.get("/static/<filename>")
def staticen_server(filename):
    return bottle.static_file(filename, root="./slike")

"""@bottle.post("/dodamo_sliko")
def dodamo_sliko():
    if file.filename == "":

        return bottle.redirect("index.html")
        datoteke = dodaj.request.files["slike"]
        return bottle.template("dodaj.html")"""



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

if __name__ == "__main__":
    bottle.run(debug=True, reloader=True)