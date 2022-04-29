import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('Clickerv1.py')
window.geometry('250x250')
window.counter = 0
def UpButton():
    window.counter += 1
    WindowCounterLabel['text'] = window.counter
    Color()

def Color():
    if window.counter < 0:
        window.configure(bg = 'green')
    elif window.counter > 0:
        window.configure(bg = 'red')
    else:
        window.configure(bg = 'gray')

def DownButton():
    window.counter -=1
    WindowCounterLabel['text'] = window.counter
    Color()

WindowUpButton = Button(window, text = 'Up', command = UpButton)
WindowUpButton.pack(fill = 'x',pady = 15)
WindowCounterLabel = Label(window, text = '0')
WindowCounterLabel.pack()
WindowDownButton = Button(window, text = 'Down', command = DownButton)
WindowDownButton.pack(fill = 'x',pady = 15)

window.mainloop()
