import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('Clickerv4.py')
window.geometry('250x250')
window.counter = 0
LastClick = 'white'

def changeColour():
    global LastClick
    if window.counter < 0:
        window.configure(bg = "red")
    elif window.counter > 0:
        window.configure(bg = 'green')
    elif window.counter == 0:
        window.configure(bg="gray")
    
def UpButton():
    global LastClick
    window.counter += 1
    WindowCounterLabel['text'] = window.counter
    WindowCounterLabel.bind('<Double-Button-1>', CounterTimesThree)
    changeColour()
    LastClick = 'green'

def UpButtonPlus(event):
    window.counter += 1
    WindowCounterLabel['text'] = window.counter
    WindowCounterLabel.bind('<Double-Button-1>', CounterTimesThree)
    changeColour()

def DownButton():
    global LastClick
    window.counter -=1
    WindowCounterLabel['text'] = window.counter
    WindowCounterLabel.bind('<Double-Button-1>', CounterDividesByThree)
    changeColour()
    LastClick = 'red'

def DownButtonMin(event):
    window.counter -= 1
    WindowCounterLabel['text'] = window.counter
    WindowCounterLabel.bind('<Double-Button-1>', CounterDividesByThree)
    changeColour()

def Repeat(event):
    if LastClick == 'green':
        UpButton()
    elif LastClick == 'red':
        DownButton()

def enterButton(event):
    window.configure(bg = 'yellow')
    
def LeaveButton(event):
    window.configure(bg = LastClick)

def CounterTimesThree(event):
    window.counter *= 3
    WindowCounterLabel['text'] = window.counter
    changeColour()

def CounterDividesByThree(event):
    window.counter /= 3
    WindowCounterLabel['text'] = window.counter
    changeColour()

WindowUpButton = Button(window, text = 'Up', command = UpButton)
WindowUpButton.pack(fill = 'x',pady = 15)

window.bind('+',UpButtonPlus)
window.bind('-',DownButtonMin)
window.bind('<space>',Repeat)
    
WindowCounterLabel = Label(window, text = '0')
WindowCounterLabel.pack()

WindowCounterLabel.bind('<Enter>', enterButton)
WindowCounterLabel.bind('<Leave>', LeaveButton)

WindowDownButton = Button(window, text = 'Down', command = DownButton)
WindowDownButton.pack(fill = 'x',pady = 15)

window.mainloop()
