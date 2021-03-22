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
    if zahtevaj_prijavo():
        return bottle.template("index.html", podatki = podatki, uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("index.html", podatki = podatki, uporabnik = "Gost")

@bottle.post("/glasuj_za")
def Glasuj_za():
    if zahtevaj_prijavo():
        seznam = seznam_slik()
        for slika in seznam:
            if bottle.request.POST.get("ja") == slika:
                glasuj_za(slika)
                vsec_mi_je_slika(slika, bottle.request.get_cookie("uporabnik"))
        return bottle.redirect("/")
    else:
        return bottle.template("neveljavna_prijava.html", sporocilo = "Za všečkanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")
                    

@bottle.post("/glasuj_proti")
def Glasuj_proti():
    if zahtevaj_prijavo():
        seznam = seznam_slik()
        for slika in seznam:
            if bottle.request.POST.get("ne") == slika:
                glasuj_proti(slika)
        return bottle.redirect("/")
    else:
        return bottle.template("neveljavna_prijava.html", sporocilo = "Za ne všečkanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")


@bottle.get("/vseckano")
def vseckano():
    if zahtevaj_prijavo():
        vseckane_fotografije = vseckane_slike(bottle.request.get_cookie("uporabnik"))
        moji_recepti = vseckani_recepti(bottle.request.get_cookie("uporabnik"))
        return bottle.template("vseckano.html", uporabnik = bottle.request.get_cookie("uporabnik"), vseckani_recepti = moji_recepti, vseckane_slike = vseckane_fotografije)
    return bottle.template("neveljavna_prijava.html", sporocilo = "Če želite videti recepte, ki ste jih všečkali se prijavite.", uporabnik = "Gost")

@bottle.get("/dodaj")
def dodaj():
    if zahtevaj_prijavo():
        return bottle.template("dodaj.html", uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("dodaj.html", uporabnik = "Gost")

@bottle.post("/dodaj_recept")
def dodaj_recept():
    if zahtevaj_prijavo():
        ime = bottle.request.forms.get("Ime")
        priimek = bottle.request.forms.get("Priimek")    
        naslov = bottle.request.forms.get("Naslov")
        sestavine = bottle.request.forms.get("Sestavine")
        postopek = bottle.request.forms.get("Postopek")
        slika = bottle.request.files.get("Slika")

        data = read_json()
        index = len(data["recepti"]) + 1

        if veljaven_recept(ime, priimek, sestavine, postopek):
            if slika is not None:
                name, ext = os.path.splitext(slika.filename)
                if ext not in (".png", ".jpg", ".jpeg"):
                    return bottle.template("napacna_datoteka.html", uporabnik = bottle.request.get_cookie("uporabnik"))
                file_path = "Database/{file}".format(file=slika.filename) 
                slika.save(file_path)
                data["recepti"][f"recept_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : file_path, "likes" : 0, "dislikes" : 0}
                write_json(data)
            else:
                data["recepti"][f"recept_{index}"] = {"owner" : [ime, priimek], "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : "Database/noImage.png", "likes" : 0, "dislikes" : 0}
                write_json(data)
            return bottle.redirect("/")
        return bottle.template("ni_veljaven_recept.html", uporabnik = bottle.request.get_cookie("uporabnik"))
    else:
        return bottle.template("neveljavna_prijava.html", sporocilo = "Za dodajanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")



@bottle.get("/prijava")
def prijava():
    if zahtevaj_prijavo():
        return bottle.template("prijava.html", uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("prijava.html", uporabnik = "Gost")

@bottle.get("/odjava")
def odjava():
    bottle.response.delete_cookie("uporabnik")
    return bottle.redirect("/")

@bottle.get("/nov_profil")
def nov_profil():
    if zahtevaj_prijavo():
        return bottle.template("registracija.html", uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("registracija.html", uporabnik = "Gost")

@bottle.post("/logiraj_me")
def logiraj_me():
    data = read_json()
    index = len(data["uporabniki"]) + 1

    if bottle.request.forms.get("Uporabnisko_ime") and bottle.request.forms.get("Geslo"):
        uporabnisko_ime = bottle.request.forms.get("Uporabnisko_ime")
        geslo = bottle.request.forms.get("Geslo")
        if preveri_prijavo(uporabnisko_ime, geslo):
            bottle.response.set_cookie("uporabnik", uporabnisko_ime)
            return bottle.redirect('/')
        else:
            return bottle.template("neveljavna_prijava.html", sporocilo = "Vaše uporabniško ime ali geslo je napačno", uporabnik = "Gost")
    
    if bottle.request.forms.get("Novo_uporabnisko_ime") and bottle.request.forms.get("Novo_geslo"):  
        nov_uporabnik = bottle.request.forms.get("Novo_uporabnisko_ime")
        novo_geslo = bottle.request.forms.get("Novo_geslo")
        if prosto_uporabnisko_ime(nov_uporabnik, novo_geslo):
            bottle.response.set_cookie("uporabnik", nov_uporabnik)
            data["uporabniki"][f"person_{index}"] = {"username" : nov_uporabnik, "password" : novo_geslo, "liked_photos" : []}
            write_json(data)
            return bottle.redirect('/')
        else:
            return bottle.template("neveljavna_prijava.html", sporocilo = "Uporabniško ime je že zasedeno")
    else:
        return bottle.template("neveljavna_prijava.html", sporocilo = "Uporabniško ime in geslo nemoreta biti prazna", uporabnik = "Gost")



#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe



bottle.run(debug=True, reloader=True)