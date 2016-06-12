#!/usr/bin/python
# -*- coding:UTF-8 -*

from interface.root import *


def presentation():  # Ma Présentation
    root_clear()
    canvas_fen = creer_canvas(root)
    canvas_fen.create_text(dimx_ / 2 + 8, dimy_ / 2 + 5, text="Projet Python 2015-2016", font="/font/myfont 45 bold",
                           fill="#544")
    bouton_suiv = Button(root, text="Suivant", command=root_menu, relief="raised", font="/font/myfont 8 bold",
                         bg="#eee",
                         fg="black", activebackground="#dcc")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised", font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    canvas_fen.create_text(dimx_ / 2 + 8, 30, text="TALL Mamour", font="/font/myfont 30 bold", fill="#544")
    canvas_fen.create_text(dimx_ / 2 + 8, 110, text="DIC1 Info ESP Dakar", font="/font/myfont 30 bold", fill="#544")
    canvas_fen.create_window(dimx_ / 2 + 18, dimy_ - 20, window=bouton_suiv)
    canvas_fen.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas_fen.pack()


def __main__():
    print("test")
    presentation()
    root.mainloop()


if __name__ == "__main__":
    __main__()

# M.TALL 2015-2016
