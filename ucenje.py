import bottle

@bottle.get("/")
def pozdravi():
    return bottle.template("osnovna_stran.html")


@bottle.post("/sestej/")
def sestej():
    a = int(bottle.request.forms["a"])
    b = int(bottle.request.forms["b"])
    return "{} + {} = {}".format(a, b, a + b)


bottle.run(debug=True, reloader=True)