from tkinter import messagebox
import tkinter
import random
from random import randint
import time
import threading
window = tkinter.Tk()
window.title('Simple FPS Trainer V1')
window.geometry('350x350')
window.configure(bg='#FFD5D5')
RandomLocatie = []
punten = 0
Tijd = 20


def Timer():
    global Tijd
    Tijd = 20
    Begin()
    for x in range(0, 20):
        time.sleep(1)
        Tijd = Tijd - 1
        TijdLabel.config(text=Tijd)
        if Tijd == 0:
            OpnieuwOfStoppen()


def OpnieuwOfStoppen():
    global punten
    OpnieuwOfNiet = messagebox.askquestion(
        "Einde", "Je tijd is op!\nJe hebt "+str(punten)+" punten behaald!\n\nOpnieuw spelen?")
    if OpnieuwOfNiet == "yes":
        punten = 0
        AantalPuntenLabel.config(text=0)
        GlobalEvent.destroy()
        TijdLabel.config(text=20)
        Timer()
    else:
        window.destroy()


def Opnieuw():
    BeginButton = tkinter.Button(
        window, command=threading.Thread(target=Timer).start)


def RandomPlaatsGenerator():
    for i in range(0, 2):
        RandomNummerOnder280 = randint(50, 280)
        RandomLocatie.append(RandomNummerOnder280)


def PlaatsMuisOfKey():
    global GlobalEvent
    global LaatsteBind
    RandomEvent = randint(1, 8)
    RandomPlaatsGenerator()
    if RandomEvent == 1:
        label = tkinter.Label(window, borderwidth=1, relief='solid')
        label.configure(text='W')
        label.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = label
        LaatsteBind = 'w'
        window.bind(LaatsteBind, ToetsenbordEvent)
    elif RandomEvent == 2:
        label = tkinter.Label(window, borderwidth=1, relief='solid')
        label.configure(text='A')
        label.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = label
        LaatsteBind = 'a'
        window.bind(LaatsteBind, ToetsenbordEvent)
    elif RandomEvent == 3:
        label = tkinter.Label(window, borderwidth=1, relief='solid')
        label.configure(text='S')
        label.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = label
        LaatsteBind = 's'
        window.bind(LaatsteBind, ToetsenbordEvent)
    elif RandomEvent == 4:
        label = tkinter.Label(window, borderwidth=1, relief='solid')
        label.configure(text='D')
        label.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = label
        LaatsteBind = 'd'
        window.bind(LaatsteBind, ToetsenbordEvent)
    elif RandomEvent == 5:
        label = tkinter.Label(window, borderwidth=1, relief='solid')
        label.configure(text='Spatie')
        label.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = label
        LaatsteBind = '<space>'
        window.bind(LaatsteBind, ToetsenbordEvent)
    elif RandomEvent == 6:
        button = tkinter.Button(window, borderwidth=1, relief='solid')
        button.configure(text='1 Click')
        button.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = button
        LaatsteBind = '<Button>'
        button.bind(LaatsteBind, MuisEvent)
    elif RandomEvent == 7:
        button = tkinter.Button(window, borderwidth=1, relief='solid')
        button.configure(text='2 Clicks')
        button.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = button
        LaatsteBind = '<Double-Button>'
        button.bind(LaatsteBind, MuisEvent)
    elif RandomEvent == 8:
        button = tkinter.Button(window, borderwidth=1, relief='solid')
        button.configure(text='3 Clicks')
        button.place(x=RandomLocatie[0], y=RandomLocatie[1])
        GlobalEvent = button
        LaatsteBind = '<Triple-Button>'
        button.bind(LaatsteBind, MuisEvent)


def VoegPuntenToe(PuntenToevoegen: int):
    global punten
    punten += PuntenToevoegen
    AantalPuntenLabel.config(text=punten)
    RandomLocatie.clear()
    PlaatsMuisOfKey()


def ToetsenbordEvent(event):
    window.unbind(LaatsteBind)
    GlobalEvent.destroy()
    VoegPuntenToe(1)


def MuisEvent(event):
    window.unbind(LaatsteBind)
    GlobalEvent.destroy()
    VoegPuntenToe(2)


def Begin():
    BeginButton.destroy()
    PlaatsMuisOfKey()


BeginButton = tkinter.Button(
    window, command=threading.Thread(target=Timer).start)
BeginButton.configure(text="Begin!", bg='#EFDECD')
BeginButton.pack(anchor='center', pady='50')


TijdLabel = tkinter.Label(window, borderwidth=1, relief='solid')
TijdLabel.configure(text='Tijd: ' + str(Tijd), bg="#A7D8DE")
TijdLabel.place(relx=1.0, rely=0.0, anchor='ne', width=75, height=25)


AantalPuntenLabel = tkinter.Label(window, borderwidth=1, relief='solid')
AantalPuntenLabel.configure(text='Punten: ' + str(punten), bg='#A7D8DE')
AantalPuntenLabel.place(anchor='nw', width=75, height=25)


FPSTrainerLabel = tkinter.Label(window, borderwidth=1, relief='solid', font=50)
FPSTrainerLabel.configure(text='FPS Trainer', fg='white', bg='#787878')
FPSTrainerLabel.pack(anchor='center', pady='10')


window.mainloop()
