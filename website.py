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
        return bottle.template("index.tpl", podatki = podatki, uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("index.tpl", podatki = podatki, uporabnik = "Gost")

@bottle.post("/glasuj_za")
def Glasuj_za():
    if zahtevaj_prijavo():
        seznam = seznam_receptov()
        for recept in seznam:
            if bottle.request.POST.get("ja") == recept:
                glasuj_za(recept)
                vsec_mi_je_recept(recept, bottle.request.get_cookie("uporabnik"))
        return bottle.redirect("/")
    else:
        return bottle.template("neveljavna_prijava.tpl", sporocilo = "Za všečkanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")
                    

@bottle.post("/glasuj_proti")
def Glasuj_proti():
    if zahtevaj_prijavo():
        seznam = seznam_receptov()
        for recept in seznam:
            if bottle.request.POST.get("ne") == recept:
                glasuj_proti(recept)
                ni_mi_vsec_recept(recept, bottle.request.get_cookie("uporabnik"))
        return bottle.redirect("/")
    else:
        return bottle.template("neveljavna_prijava.tpl", sporocilo = "Za ne všečkanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")


@bottle.get("/vseckano")
def vseckano():
    if zahtevaj_prijavo():
        vseckani_naslovi = vseckani_naslovi_receptov(bottle.request.get_cookie("uporabnik"))
        moji_recepti = vseckani_recepti(bottle.request.get_cookie("uporabnik"))
        return bottle.template("vseckano.tpl", uporabnik = bottle.request.get_cookie("uporabnik"), vseckani_recepti = moji_recepti, vseckane_slike = vseckani_naslovi)
    return bottle.template("neveljavna_prijava.tpl", sporocilo = "Če želite videti recepte, ki ste jih všečkali se prijavite.", uporabnik = "Gost")

@bottle.post("/odstrani")
def odstrani():
    data = read_json()
    vseckani_naslovi = vseckani_naslovi_receptov(bottle.request.get_cookie("uporabnik"))
    moji_recepti = vseckani_recepti(bottle.request.get_cookie("uporabnik"))
    for recept in moji_recepti:
        if bottle.request.POST.get("odstrani") == recept[1]:
            moji_recepti.remove(recept)
            vseckani_naslovi.remove(recept[1])
            for oseba in data["uporabniki"]:
                if data["uporabniki"][oseba]["username"] == bottle.request.get_cookie("uporabnik"):
                    data["uporabniki"][oseba]["liked_recipe"] = vseckani_naslovi
                write_json(data)
    
    return bottle.template("vseckano.tpl", uporabnik = bottle.request.get_cookie("uporabnik"), vseckani_recepti = moji_recepti, vseckane_slike = vseckani_naslovi) 



@bottle.get("/dodaj")
def dodaj():
    if zahtevaj_prijavo():
        return bottle.template("dodaj.tpl", uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("neveljavna_prijava.tpl", sporocilo = "Za dodajanje receptov se morate prijaviti na spletno stran", uporabnik = "Gost")

@bottle.post("/dodaj_recept")
def dodaj_recept():
    ime = bottle.request.get_cookie("uporabnik")
    naslov = bottle.request.forms.get("Naslov")
    sestavine = bottle.request.forms.get("Sestavine")
    postopek = bottle.request.forms.get("Postopek")
    slika = bottle.request.files.get("Slika")

    data = read_json()
    index = len(data["recepti"]) + 1

    if slika is not None:
        name, ext = os.path.splitext(slika.filename)
        if ext not in (".png", ".jpg", ".jpeg"):
            return bottle.template("napacna_datoteka.tpl", uporabnik = bottle.request.get_cookie("uporabnik"))
        file_path = "Database/{file}".format(file=slika.filename) 
        slika.save(file_path)
        data["recepti"][f"recept_{index}"] = {"owner" : ime, "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : file_path, "likes" : 0, "dislikes" : 0}
        write_json(data)
    else:
        data["recepti"][f"recept_{index}"] = {"owner" : ime, "title" : naslov, "ingredients" : sestavine, "procedure" : postopek, "image" : "Database/noImage.png", "likes" : 0, "dislikes" : 0}
        write_json(data)
    return bottle.redirect("/")
        
@bottle.get("/vasi_recepti")
def vasi_recepti():
    recepti = moji_recepti(bottle.request.get_cookie("uporabnik"))
    return bottle.template("vasi_recepti.tpl", vasi_recepti = recepti, uporabnik = bottle.request.get_cookie("uporabnik"))

@bottle.get("/uredi/<recept>")
def uredi(recept):
    for celoten_recept in seznam_podatkov():
        if celoten_recept[1] == recept: 
            urejani_recept = celoten_recept
            bottle.response.set_cookie("recept", urejani_recept[1], path='/')
    return bottle.template("uredi.tpl", recept = urejani_recept, uporabnik = bottle.request.get_cookie("uporabnik"))

@bottle.post("/shrani")
def shrani():
    nove_sestavine = bottle.request.forms.get("Nove_sestavine")
    nov_postopek = bottle.request.forms.get("Nov_postopek")
    nova_slika = bottle.request.files.get("Nova_slika")
    data = read_json()
    for recept in data["recepti"]:
        if data["recepti"][recept]["title"] == bottle.request.get_cookie("recept"):
            if nove_sestavine is not None:
                data["recepti"][recept]["ingredients"] = nove_sestavine
            if nov_postopek is not None:
                data["recepti"][recept]["procedure"] = nov_postopek
            if nova_slika is not None:
                name, ext = os.path.splitext(nova_slika.filename)
                if ext not in (".png", ".jpg", ".jpeg"):
                    return bottle.template("napacna_datoteka.tpl", uporabnik = bottle.request.get_cookie("uporabnik"))
                file_path = "Database/{file}".format(file=nova_slika.filename) 
                nova_slika.save(file_path)
                data["recepti"][recept]["image"] = file_path
    write_json(data)
    return bottle.redirect("/vasi_recepti")


@bottle.get("/prijava")
def prijava():
    return bottle.template("prijava.tpl", uporabnik = "Gost")

@bottle.get("/odjava")
def odjava():
    bottle.response.delete_cookie("uporabnik")
    return bottle.redirect("/")

@bottle.get("/nov_profil")
def nov_profil():
    if zahtevaj_prijavo():
        return bottle.template("registracija.tpl", uporabnik = bottle.request.get_cookie("uporabnik"))
    return bottle.template("registracija.tpl", uporabnik = "Gost")

@bottle.post("/logiraj_me")
def logiraj_me():
    data = read_json()
    index = len(data["uporabniki"]) + 1

    if bottle.request.forms.get("Uporabnisko_ime") and bottle.request.forms.get("Geslo"):
        uporabnisko_ime = bottle.request.forms.get("Uporabnisko_ime")
        geslo = bottle.request.forms.get("Geslo")
        if preveri_prijavo(uporabnisko_ime, geslo):
            bottle.response.set_cookie("uporabnik", uporabnisko_ime, path='/')
            return bottle.redirect('/')
        else:
            return bottle.template("neveljavna_prijava.tpl", sporocilo = "Vaše uporabniško ime ali geslo je napačno", uporabnik = "Gost")
    
    if bottle.request.forms.get("Novo_uporabnisko_ime") and bottle.request.forms.get("Novo_geslo"):  
        nov_uporabnik = bottle.request.forms.get("Novo_uporabnisko_ime")
        novo_geslo = bottle.request.forms.get("Novo_geslo")
        print(nov_uporabnik)
        print(novo_geslo)
        if prosto_uporabnisko_ime(nov_uporabnik, novo_geslo):
            bottle.response.set_cookie("uporabnik", nov_uporabnik, path='/')
            data["uporabniki"][f"person_{index}"] = {"username" : nov_uporabnik, "password" : novo_geslo, "liked_recipe" : [], "disliked_recipe" : []}
            write_json(data)
            return bottle.redirect('/')
        else:
            return bottle.template("neveljavna_prijava.tpl", sporocilo = "Uporabniško ime je že zasedeno")
    else:
        return bottle.template("neveljavna_prijava.tpl", sporocilo = "Uporabniško ime in geslo nemoreta biti prazna", uporabnik = "Gost")

@bottle.get("/spremenite_geslo")
def sprememba_gesla():
    return bottle.template("sprememba_gesla.tpl", uporabnik = bottle.request.get_cookie("uporabnik"))

@bottle.post("/spremenite_geslo")
def sprememba_gesla():
    staro_geslo = bottle.request.forms.get("Staro_geslo")
    novo_geslo = bottle.request.forms.get("Novo_geslo")
    ime = bottle.request.get_cookie("uporabnik")
    if preveri_prijavo(ime, staro_geslo):
        data = read_json()
        for uporabnik in data["uporabniki"]:
            if data["uporabniki"][uporabnik]["password"] == staro_geslo:
                data["uporabniki"][uporabnik]["password"] = novo_geslo
        write_json(data)
        return bottle.redirect("/")
    else:
        return bottle.template("neveljavna_prijava.tpl", sporocilo = "Staro geslo ni pravilno", uporabnik = bottle.request.get_cookie("uporabnik"))


#bottle.request.query se uporablja za GET poizvedbe
#bottle.request.forms pa se uporablja za POST poizvedbe



bottle.run(debug=True, reloader=True)