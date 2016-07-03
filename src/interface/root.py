# -*-coding:UTF-8-*

from tkMessageBox import askyesno

from .affiche_saisie import *


def creer_canvas(window):  # Création du canvas qui sera utilisé sur toutes les fenêtres
    canvas = Canvas(window, width=dimx_, height=dimy_, bg="#cdd")
    return canvas


def effacer(fonction):
    root_clear()
    fonction()


def root_fermer():  # Prompt confirmation fermeture de la fenêtre
    if askyesno('Confirmer la fermeture', 'Êtes-vous sûr de vouloir quitter?'):
        root.quit()


def root_clear():  # Effacer la fenêtre
    for w in root.winfo_children():
        w.destroy()


def root_navigation(canvas, back):
    bouton_prec = Button(root, text="Precedent", relief="raised", font="/font/myfont 8 bold", command=back,
                         bg="#eee", fg="black", activebackground="#dcc")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised",
                          font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    canvas.create_window(60, dimy_ - 20, window=bouton_prec)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas.pack()


def root_menu():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 - 10, 20, text="   MENU", font="/font/myfont 20 bold", fill="#544")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised",
                          font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    bouton_operation = Button(root, command=root_opmatrices_menu, text="Opérations Sur Les Matrices",
                              relief="raised",
                              font="/font/myfont 15 bold", bg="#eee", fg="black", activebackground="#dcc")
    bouton_syslin = Button(root, command=root_syslineaires_menu,
                           text="      Systémes Linéaires       ",
                           relief="raised", font="/font/myfont 15 bold", bg="#eee", fg="black",
                           activebackground="#dcc")
    canvas.create_window(dimx_ / 4 + 30, dimy_ / 2 - 12, window=bouton_operation)
    canvas.create_window(dimx_ / 4 + 30 + 390, dimy_ / 2 - 12, window=bouton_syslin)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas.pack()


def root_syslineaires_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_1matrice(root, canvas, affiche_saisiesyslin)
    root_navigation(canvas, root_menu)
    canvas.pack()


def root_opmatrices_menu():  # Choix de l'opération à affectuer
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 - 10, 20, text="    Operations de bases sur les matrices",
                       font="/font/myfont 15 "
                            "bold", fill="#544")
    bouton_1matrice = Button(root, text="Operations sur une matrice", relief="raised",
                             font="/font/myfont 14 bold", command=root_op1matrices_menu,
                             bg="#eee", fg="black", activebackground="#dcc")
    bouton_2matrice = Button(root, text="Operations sur deux matrices", relief="raised",
                             font="/font/myfont 14 bold", command=root_op2matrices_menu,
                             bg="#eee", fg="black", activebackground="#dcc")
    canvas.create_window(dimx_ / 4 + 30, dimy_ / 2 - 12, window=bouton_1matrice)
    canvas.create_window(dimx_ / 4 + 30 + 390, dimy_ / 2 - 12, window=bouton_2matrice)
    root_navigation(canvas, root_menu)
    canvas.pack()


def root_op1matrices_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_1matrice(root, canvas, affiche_saisie_1matrice)
    root_navigation(canvas, root_opmatrices_menu)
    canvas.pack()


def root_op2matrices_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_2matrices(root, canvas)
    root_navigation(canvas, root_opmatrices_menu)
    canvas.pack()


def root_boutons_opmatricemenu1(affiche_saisie, texte):
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32, text=texte, font="/font/myfont 9 bold", fill="black")
    saisie_1matrice(root, canvas, affiche_saisie)


def root_boutons_opmatricemenu2(texte):
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 60, dimy_ / 32, text=texte, font="/font/myfont 9 bold", fill="black")
    saisie_2matrices(root, canvas)

# M.TALL 2015-2016
