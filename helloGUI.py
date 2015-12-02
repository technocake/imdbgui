#coding: utf-8
import requests
import webbrowser
from tkinter import *
import imdbmodul
import os


root = Tk()

w = Label(root, text="Hello, world eofjefoj!")
x = Label(root, text="Hadet, world eofjefoj!")

def panic():
    # Les tittel fra filmtittel textboksen
    tittel = filmtittel.get()

    #Sjekker at vi har skrevet en faktisk tittel.
    if tittel == "" or tittel is None:
        return

    # Vi har en tittle, la oss hente bilde!
    film = imdbmodul.tittelsok(tittel)
    bildefilnavn = "%s.jpg"%tittel
    # Hent og skriv til fil bildet vårt.
    imdbmodul.hent_bilde(film.cover_url, bildefilnavn)



knapp = Button(root,  text="DONT HIT THIS BUTTON",
                bg="red", command=panic)

filmtittel = Entry(root)

filmtittel.pack()
knapp.pack()
w.pack()
x.pack()

root.mainloop()