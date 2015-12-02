#coding: utf-8
import imdbpie
import requests
from imdbpie import Imdb
import os
import glob
import threading


imdb = Imdb()

def ryddopp():
    # Sletter alle filer som slutter på .jpg i mappen vår
    bilder = glob.glob("*.jpg")
    for bilde in bilder:
        os.remove(bilde)

def tittelsok(tittel):
    # Henter mer info om film fra imdb om vi gir den tittel.
    global imdb
    # Skriv om til å søke på variabel
    results = imdb.search_for_title(tittel)
    #For no, antar vi at første svar er riktig film.
    riktig_film = results[0]

    mer_info = imdb.get_title_by_id( riktig_film['imdb_id'] )
    return mer_info


def hent_bilde(url, filnavn):
    def bakgrunnsoppgave():
        # Egen funksjon for filhenting av cover-bilde fra imdb
        bildesvar = requests.get( url )
        if bildesvar.status_code == 200:
            with open(filnavn, "+wb") as f:
                for chunk in bildesvar:
                    f.write(chunk)

    # Lage en tråd som vil kjøre en funksjon ved start
    t = threading.Thread(target=bakgrunnsoppgave)
    # Få tråden til å avslutte om hovedprogrammet blir lukket.
    t.daemon = True
    # Starter faktisk tråden.
    t.start()

