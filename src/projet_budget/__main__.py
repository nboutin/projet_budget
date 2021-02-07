'''
Created on Feb 7, 2021

@author: nbout
'''

from tkinter import *
from tkinter import ttk

_VERSION = '0.1.0'


class BudgetProjet:

    def __init__(self, parent):

        parent.title('Budget Projet ' + _VERSION)
        self.__set_windows_geometry(parent)

        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def __set_windows_geometry(self, parent):
        w = 300  # width for the Tk parent
        h = 200  # height for the Tk parent

        # get screen width and height
        ws = parent.winfo_screenwidth()  # width of the screen
        hs = parent.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk parent window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen and where it is placed
        parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    root = Tk()
    BudgetProjet(root)
    root.mainloop()
