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
    filemenu = Menu(menu)
    
    # file menu
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=tk.quit)

    # file menu
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=tk.quit)

    #
    restore_button = Button(tk, text="Minimize", command=tk.withdraw())
    restore_button.pack()

    # tk mainloop
    tk.mainloop()



if __name__ == "__main__": # python boilerplate. hooray!
    main()