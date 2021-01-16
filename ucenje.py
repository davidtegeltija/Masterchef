import bottle

@bottle.get("/")
def basic():
    return bottle.template("index.html")

@bottle.get("/index")
def index():
    return bottle.template("index.html")

@bottle.get("/recepti")
def recepti():
    return bottle.template("recepti.html")

@bottle.get("/vseckano")
def vseckano():
    return bottle.template("vseckano.html")

@bottle.get("/dodaj")
def dodaj():
    return bottle.template("dodaj.html")


#@bottle.post("/isci/<vneseno>")
#def isci(vneseno):
#    return bottle.template

#@bottle.get("/")
#def staticna_spletna(style):
#    pot = "C:/Users/David/Documents/Šola FAKS - 2.letnik/Spletna stran"
#    return bottle.static_file(index.html, root=pot)

#@bottle.post("/sestej/")
#def sestej():
#    a = int(bottle.request.forms["a"])
#    b = int(bottle.request.forms["b"])
#    return "{} + {} = {}".format(a, b, a + b)


bottle.run(debug=True, reloader=True)