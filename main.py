# imports
from tkinter import *
from tkinter import filedialog
import simpleaudio as sa
import pygame.mixer
import ctypes

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
    filemenu.add_command(label='Add Song', command= lambda : addSong())
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=tk.quit)

    # edit menu
    menu.add_cascade(label='Edit', menu=editmenu)
    editmenu.add_command(label='Exit', command=tk.quit)

    # image button
    buttonTest = PhotoImage(file='assets/rewind.png')
    button = Button(tk, image=buttonTest, command= lambda : print('test'), borderwidth=0)
    button.pack(pady=30)

    # tk mainloop
    tk.mainloop()


def addSong():
    file_path = filedialog.askopenfilename()
    print(file_path)
    
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except:
        ctypes.windll.user32.MessageBoxW(0, u"Please text a valid audio file!", u"", 16)
        print('uh oh')


if __name__ == "__main__": # python boilerplate. hooray!
    main()