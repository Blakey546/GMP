from tkinter import *
from tkinter import filedialog
import simpleaudio as sa

tk = Tk()

class imageButton:
    def __init__(self, function, filePath):
        buttonTest = PhotoImage(file=filePath)
        button = Button(tk, image=buttonTest, command= lambda : function, borderwidth=0)
        button.pack(pady=30)
