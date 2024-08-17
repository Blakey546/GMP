from tkinter import Button, PhotoImage, filedialog
import simpleaudio as sa

class imageButton:
    def __init__(self):
        pass
    
    def makeButton(self, function, filePath, screen):
        self.image = PhotoImage(file=filePath)
        button = Button(screen, image=self.image, command=function, borderwidth=0)
        button.pack(pady=30)
        return button

