# imports
from tkinter import *

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
    button= Button(tk, image=buttonTest, command= lambda : print('test'), borderwidth=0)
    button.pack(pady=30)

    # tk mainloop
    tk.mainloop()


def addSong():
    print('test')


if __name__ == "__main__": # python boilerplate. hooray!
    main()