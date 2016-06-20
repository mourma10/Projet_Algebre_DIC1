# -*-coding:UTF-8-*

try:
    from Tkinter import Tk, Canvas
except Tk:
    print("veuillez installer Tkinter : sudo apt-get install python-tk")
    exit()

from tkMessageBox import askyesno

from .affiche_saisie import *

(dimx_, dimy_) = (1024, 661)


def create_root():
    iam_root = Tk()
    iam_root.title("Projet Python DIC1")
    w_ = iam_root.winfo_screenwidth()
    h = iam_root.winfo_screenheight()
    x = w_ / 2 - dimx_ / 2
    y = h / 2 - dimy_ / 2
    iam_root.geometry("%dx%d+%d+%d" % ((dimx_, dimy_) + (x, y)))
    iam_root.resizable(width=False, height=False)
    return iam_root


root = create_root()


def creer_canvas(window):  # Création du canvas qui sera utilisé sur toutes les fenêtres
    canvas = Canvas(window, width=dimx_, height=dimy_, bg="#dee")
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


def root_navigation(fonction, canvas, back):
    bouton_effacer = Button(root, text="Effacer", relief="raised", font="/font/myfont 8 bold",
                            command=lambda: effacer(fonction),
                            bg="#eee", fg="black", activebackground="#dcc")
    bouton_prec = Button(root, text="Precedent", relief="raised", font="/font/myfont 8 bold", command=back,
                         bg="#eee", fg="black", activebackground="#dcc")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised", font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    bouton_effacer.pack()
    bouton_prec.pack()
    bouton_quitt.pack()
    canvas.create_window(dimx_ / 2 + 18, dimy_ - 20, window=bouton_effacer)
    canvas.create_window(60, dimy_ - 20, window=bouton_prec)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)


def root_menu():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 - 10, 20, text="   MENU", font="/font/myfont 20 bold", fill="#544")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised", font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    bouton_operation = Button(root, command=root_opmatrices_menu, text="Opérations Sur Les Matrices", relief="raised",
                              font="/font/myfont 10 bold", bg="#eee", fg="black", activebackground="#dcc")
    bouton_record = Button(root, command=root_bouton_enregistrement, text="  Enrégistreur Vocal Python  ",
                           relief="raised", font="/font/myfont 10 bold", bg="#eee", fg="black", activebackground="#dcc")
    bouton_syslin = Button(root, command=root_syslineaires_menu,
                           text="      Systémes Linéaires       ",
                           relief="raised", font="/font/myfont 10 bold", bg="#eee", fg="black", activebackground="#dcc")
    bouton_quitt.pack()
    canvas.create_window(dimx_ / 4 + 30, dimy_ / 4 - 12, window=bouton_operation)
    canvas.create_window(3 * (dimx_ / 4) + 10, dimy_ / 4 - 12, window=bouton_record)
    canvas.create_window(dimx_ / 4 + 30, dimy_ / 2 - 20, window=bouton_syslin)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas.pack()


def root_syslineaires_menu():
    root_clear()
    canvas = creer_canvas(root)
    bouton_prec = Button(root, text="Precedent", relief="raised", font="/font/myfont 8 bold", command=root_menu,
                         bg="#eee", fg="black", activebackground="#dcc")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised", font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    canvas.create_text(520, 20, text="  Veuillez choisir une méthode s'il vous plaît.", font="/font/myfont 18 bold",
                       fill="#544")
    bouton_gauss = Button(root, command=root_bouton_methodegauss,
                          text="Methode de GAUSS",
                          relief="raised", font="/font/myfont 9 bold", bg="#eee", fg="black", activebackground="#dcc")
    bouton_prec.pack()
    bouton_quitt.pack()
    canvas.create_window(dimx_ / 4 + 30, dimy_ / 4 - 10, window=bouton_gauss)
    canvas.create_window(dimx_ / 16 - 10, dimy_ - 20, window=bouton_prec)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas.pack()


def root_opmatrices_menu():  # Choix de l'opération à affectuer
    root_clear()
    canvas = creer_canvas(root)
    bouton_prec = Button(root, text="Precedent", relief="raised", font="/font/myfont 8 bold", command=root_menu,
                         bg="#eee", fg="black", activebackground="#dcc")
    bouton_quitt = Button(root, text="Quitter", command=root_fermer, relief="raised", font="/font/myfont 8 bold",
                          bg="#eee",
                          fg="black", activebackground="#dcc")
    canvas.create_text(dimx_ / 2 + 10, 20, text="  Veuillez choisir une opération s\'il vous plaît.",
                       font="/font/myfont 18 bold",
                       fill="#544")
    morse = Button(root, text="Stockage morse matrice", command=root_bouton_morse, relief="raised",
                   font="/font/myfont 9 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    produit = Button(root, text="Produit de deux matrices", command=root_bouton_produitmatrice, relief="raised",
                     font="/font/myfont 9 bold", bg="#eee", fg="black", activebackground="#dcc")
    somme = Button(root, text="Somme de deux matrices", command=root_bouton_sommematrice, relief="raised",
                   font="/font/myfont 9 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    inverser = Button(root, text="    Inverse d'une matrice", command=root_bouton_inverse, relief="raised",
                      font="/font/myfont 9 bold", bg="#eee", fg="black", activebackground="#dcc")
    determinant = Button(root, text="   Determinant matrice     ", command=root_bouton_determinant, relief="raised",
                         font="/font/myfont 9 bold",
                         bg="#eee", fg="black", activebackground="#dcc")
    trans = Button(root, text="   Transposee matrice     ", command=root_bouton_transposee, relief="raised",
                   font="/font/myfont 9 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    bouton_valeurpropre = Button(root, command="",
                                 text="Valeurs Propres matrice",
                                 relief="raised", font="/font/myfont 9 bold", bg="#eee", fg="black",
                                 activebackground="#dcc")
    bouton_prec.pack()
    bouton_quitt.pack()
    canvas.create_window(dimx_ / 3 - 40, dimy_ / 3 - 15, window=morse)
    canvas.create_window(dimx_ / 3 - 40, 11 * (dimy_ / 24) - 15, window=inverser)
    canvas.create_window(7 * (dimx_ / 10) - 15, dimy_ / 2 + 35, window=determinant)
    canvas.create_window(dimx_ / 3 - 40, dimy_ / 2 + 35, window=trans)
    canvas.create_window(dimx_ / 3 - 40, dimy_ / 2 + 115, window=bouton_valeurpropre)
    canvas.create_window(7 * (dimx_ / 10) - 15, dimy_ / 3 - 15, window=somme)
    canvas.create_window(7 * (dimx_ / 10) - 15, 11 * (dimy_ / 24) - 15, window=produit)
    canvas.create_window(dimx_ / 16 - 10, dimy_ - 20, window=bouton_prec)
    canvas.create_window(dimx_ - 40, dimy_ - 20, window=bouton_quitt)
    canvas.pack()


def root_bouton_methodegauss():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32, text="Resolution Systemes Lineaires", font="/font/myfont 9 bold",
                       fill="black")
    saisie_1matrice(root, canvas, affiche_saisiegauss)
    root_navigation(root_bouton_methodegauss, canvas, root_syslineaires_menu)


def root_bouton_morse():  # (On instancie la fonction saisie_1mat pour le stockage morse:ici saiz=affiche_saisiemorse
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32, text="Stockage morse d'une matrice", font="/font/myfont 9 bold",
                       fill="black")
    saisie_1matrice(root, canvas, affiche_saisiemorse)
    root_navigation(root_bouton_morse, canvas, root_opmatrices_menu)


def root_bouton_inverse():  # On instancie la fonction saisie_1mat pour l'inverse:ici saiz=affiche_saisieinverse
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 10, dimy_ / 32, text="Inverse d'une matrice", font="/font/myfont 9 bold",
                       fill="black")
    saisie_1matrice(root, canvas, affiche_saisieinverse)
    root_navigation(root_bouton_inverse, canvas, root_opmatrices_menu)


def root_bouton_determinant():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32, text="Determinant d'une matrice", font="/font/myfont 9 bold",
                       fill="black")
    saisie_1matrice(root, canvas, affiche_saisiedet)
    root_navigation(root_bouton_determinant, canvas, root_opmatrices_menu)


def root_bouton_transposee():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32, text="Transposee d'une matrice", font="/font/myfont 9 bold",
                       fill="black")
    saisie_1matrice(root, canvas, affiche_saisietrans)
    root_navigation(root_bouton_transposee, canvas, root_opmatrices_menu)


def root_bouton_sommematrice():  # On instancie la fonction saisie_mat pour la somme:ici op=op_somme
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 60, dimy_ / 32, text="Somme de deux matrices", font="/font/myfont 9 bold",
                       fill="black")
    saisie_2matrices(root, canvas, affiche_saisiesomme)
    root_navigation(root_bouton_sommematrice, canvas, root_opmatrices_menu)


def root_bouton_produitmatrice():  # On instancie la fonction saisie_mat pour le produit:ici op=op_produit
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 60, dimy_ / 32, text="Produit de deux matrices", font="/font/myfont 9 bold",
                       fill="black")
    saisie_2matrices(root, canvas, affiche_saisieproduit)
    root_navigation(root_bouton_produitmatrice, canvas, root_opmatrices_menu)


def root_bouton_enregistrement():
    root_clear()
    canvas = creer_canvas(root)
    entry = Button(root, text="", width=25, height=1, relief="raised", bg="white")
    button = Button(root, text="Record", width=4, command=lambda: operation_record, font="/font/myfont 8 bold",
                    relief="raised", bg="white")
    root_navigation(root_bouton_enregistrement, canvas, root_menu)
    canvas.create_window(dimx_ / 2 + 70, dimy_ / 2 - 25, window=entry)
    canvas.create_window(dimx_ / 2 - 80, dimy_ / 2 - 25, window=button)
    canvas.pack()

# M.TALL 2015-2016
