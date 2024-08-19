from tkinter import Button, PhotoImage, Label
import simpleaudio as sa

class imageButton:
    def __init__(self):
        pass

    def makeButton(self, function, filePath, screen):
        self.image = PhotoImage(file=filePath)
        button = Button(screen, image=self.image, command=function, borderwidth=0)
        button.pack(pady=30)
        return button

class Image:
    def __init__(self):
        pass
    
    def makeImageWithPath(self, filePath, screen):
        self.image = PhotoImage(file=filePath)
        image_label = Label(screen, image=self.image)
        image_label.pack(pady=30)
        return image_label