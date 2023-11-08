from random import randint
from tkinter import Button, Frame, Label, Tk


def oppdater_farge():
    global RGB
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    RGB = f"#{R:02x}{G:02x}{B:02x}"
    farge_label.config(bg=RGB)
    svar.config(text="#")


RGB = "#000000"
window = Tk()
knapperamme = Frame(window)
knapperamme.grid(row=0, column=0)

svarknapp = Button(knapperamme, text="få svaret", command=lambda: svar.config(text=RGB))
nyknapp = Button(knapperamme, text="ny farge", command=oppdater_farge)
svarknapp.grid(row=0, column=0)
nyknapp.grid(row=0, column=2)

svar = Label(knapperamme, width=10, text="#")
svar.grid(row=0, column=1)

farge_label = Label(window, height=10, width=40, bg="#000000")
farge_label.grid(row=1)
oppdater_farge()
window.mainloop()
