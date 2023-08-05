from tkinter import *
from Grid import Grid
from data_news import titles, links


def main():
    window = Tk()
    window.title('Latest News - Gamerant')

    grid_title = Grid(titles)
    grid_title.create_grid()

    grid_link = Grid(links, 1)
    grid_link.create_grid()

    window.mainloop()


if __name__ == '__main__':
    main()
