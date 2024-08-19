# imports
from tkinter import *
from tkinter import filedialog
from ui.ui_elements import *
from tinytag import TinyTag
from PIL import Image as pilImage

import simpleaudio as sa
import pygame.mixer
import ctypes
import io

def main():
    # tk screen stuff
    tk = Tk()
    tk.geometry("640x480")
    tk.resizable(0, 0)
    tk.title('WMP')

    # tk menu stuff
    menu = Menu(tk)
    tk.config(menu=menu)
    filemenu = Menu(menu, tearoff=False)
    editmenu = Menu(menu, tearoff=False)

    # pygame 
    pygame.mixer.init()
    
    # file menu
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Add Song', command= lambda : addSong(tk))
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=tk.quit)

    # edit menu
    menu.add_cascade(label='Edit', menu=editmenu)
    editmenu.add_command(label='Exit', command=tk.quit)

    file_path = filedialog.askopenfilename()

    #buttonTest = PhotoImage(file='assets/rewind.png')
    #button= Button(tk, image=buttonTest, command= lambda : print('test'), borderwidth=0)
    #button.pack(pady=30)

    buttonTest = imageButton()
    buttonTest.makeButton(lambda: print('gulp'), file_path, tk)

    # tk mainloop
    tk.mainloop()


def addSong(screen):
    # ask for file
    fileMenu = Toplevel(screen)
    file_path = filedialog.askopenfilename()
    # make a button i don't need this but i'm keeping it for debug
    #buttonTest2 = imageButton()
    #buttonTest2.makeButton(lambda: fileMenu.quit(), file_path, fileMenu)
    #file_path = filedialog.askopenfilename()
    
    # get song metadata (image)
    tag = TinyTag.get(file_path, image=True)
    image_data = tag.get_image()

    # make + save image
    pi = pilImage.open(io.BytesIO(image_data))
    pi.save('temp/tempCover.png')
    
    albumCover = Image()
    albumCover.makeImageWithPath('temp/tempCover.png', fileMenu)

    fileMenu.mainloop()
    # !!! DELETE TEMP COVER !!!
    fileMenu.destroy()

    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except:
        ctypes.windll.user32.MessageBoxW(0, u"Please text a valid audio file!", u"", 16)
        print('uh oh')
    


if __name__ == "__main__": # python boilerplate. hooray!
    main()