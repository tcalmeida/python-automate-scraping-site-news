from tkinter import *


class Grid:
    def __init__(self, lists, column=None):
        self.list = lists
        self.column = column

    def create_grid(self):
        for i in self.list:
            entry = Entry(relief=GROOVE, width=110)
            entry.grid(row=self.list.index(i), column=self.column, sticky=NSEW)
            entry.insert(self.list.index(i), i)
