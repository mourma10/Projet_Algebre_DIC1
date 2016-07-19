# -*-coding:UTF-8-*

from Tkinter import Entry

from .getroot import root, dimx_
from .operations import *


def saisie_2matrices(window, canvas):
    canvas.create_text(400, 20, text="n1,m1", font="/font/myfont 10 bold", fill="black")
    canvas.create_text(400, 60, text="n2,m2", font="/font/myfont 10 bold", fill="black")
    ligne1 = Entry(window, relief="groove", width=3, bg="#eee")
    col1 = Entry(window, relief="groove", width=3, bg="#eee")
    ligne2 = Entry(window, relief="groove", width=3, bg="#eee")
    col2 = Entry(window, relief="groove", width=3, bg="#eee")
    ligne1.pack()
    ligne2.pack()
    col1.pack()
    col2.pack()
    bouton_ok = Button(window, text="Ok", relief="groove", font="/font/myfont 6 bold",
                       command=lambda: affiche_saisie_2matrices(window, canvas, ligne1.get(),
                                                                col1.get(), ligne2.get(), col2.get(),
                                                                bouton_ok), bg="#eee", fg="black",
                       activebackground="#dcc", width=2)
    canvas.create_window(445, 20, window=ligne1)
    canvas.create_window(485, 20, window=col1)
    canvas.create_window(445, 60, window=ligne2)
    canvas.create_window(485, 60, window=col2)
    canvas.create_window(540, 40, window=bouton_ok)
    canvas.pack()


def saisie_1matrice(window, canvas, saiz):
    canvas.create_text(400, 20, text="n ", font="/font/myfont 10 bold", fill="black")
    ligne = Entry(window, relief="groove", width=3, bg="#eee")
    ligne.pack()

    bouton_ok = Button(window, text="Ok", relief="groove", font="/font/myfont 6 bold",
                       command=lambda: saiz(window, canvas, ligne.get(), bouton_ok),
                       bg="#eee", fg="black", activebackground="#dcc", width=2)
    canvas.create_window(425, 20, window=ligne)
    canvas.create_window(480, 20, window=bouton_ok)
    canvas.pack()


def affiche_saisie_1matrice(window, canvas, n, bouton):
    try:
        n = int(n)
        if n == 0:
            showerror("Erreur", "Veuillez saisir un entier strictement positif")
            return -1
        bouton.destroy()
        case = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                case[i][j] = Entry(window, width=3, relief="groove", font="/font/myfont 9", bg="#eee")
                canvas.create_window(70 + 35 * j, 100 + 35 * i, window=case[i][j])
        bouton_ok = Button(window, text="Ok", bg="#eee", font="/font/myfont 6 bold", fg="black",
                           activebackground="#dcc",
                           width=2,
                           relief="groove", command=lambda: affiche_boutons_operations1matrice(canvas,
                                                                                               case, n,
                                                                                               bouton_ok))
        canvas.create_text(20, 100 + (35 * n / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_window(50 + 35 * n + 30, 100 + (35 * n / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")


def affiche_saisie_2matrices(window, canvas, a, b, c, d, bouton):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if (a, b, c, d) == (0, 0, 0, 0):
            showerror("Erreur", "Veuillez saisir des entiers strictement positifs")
            return -1
        bouton.destroy()
        case1 = [[0] * b for _ in range(a)]
        case2 = [[0] * d for _ in range(c)]
        for i in range(a):
            for j in range(b):
                case1[i][j] = Entry(window, width=3, relief="groove", font="/font/myfont 8", bg="#eee")
                canvas.create_window(70 + 30 * j, 100 + 30 * i, window=case1[i][j])
        for k in range(c):
            for l in range(d):
                case2[k][l] = Entry(window, width=3, relief="groove", font="/font/myfont 8", bg="#eee")
                canvas.create_window(dimx_ / 2 + 30 * l, 100 + 30 * k, window=case2[k][l])
        bouton_ok = Button(window, text="Ok", relief="groove",
                           command=lambda: affiche_boutons_operation2matrices(canvas, case1, case2, a,
                                                                              b, c, d, bouton_ok),
                           bg="#eee", fg="black", activebackground="#dcc",
                           font="/font/myfont 6 bold", width=2)
        canvas.create_text(20, 100 + (30 * a / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_text(370, 100 + (30 * a / 2) - 20, text="B=", font="/font/myfont 13", fill="black")
        canvas.create_window(400 + 50 + 30 * a, 100 + (30 * a / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir des entiers positifs!")


def affiche_saisiesyslin(window, canvas, n1, bouton):
    try:
        n = int(n1)
        bouton.destroy()
        case = [[0] * n for _ in range(n)]
        vecteur = [0] * n
        for i in range(n):
            for j in range(n):
                case[i][j] = Entry(window, width=3, relief="groove", font="/font/myfont 9", bg="#eee")
                canvas.create_window(70 + 35 * j, 100 + 35 * i, window=case[i][j])
        for i in range(n):
            vecteur[i] = Entry(window, width=3, relief="groove", font="/font/myfont 9", bg="#eee")
            canvas.create_window(200 + 35 * (n - 1), 100 + 35 * i, window=vecteur[i])
        bouton_ok = Button(window, text="Ok", bg="#eee", font="/font/myfont 6 bold", fg="black",
                           activebackground="#dcc",
                           width=3,
                           relief="groove",
                           command=lambda: affiche_bouton_operationssyslin(canvas, case, vecteur, n,
                                                                           bouton_ok))
        canvas.create_text(20, 100 + (35 * n / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_text(180 + 35 * (n - 1) - 20, 100 + (35 * n / 2) - 20, text="b=",
                           font="/font/myfont 13",
                           fill="black")
        canvas.create_window(250 + 35 * n + 30, 100 + (35 * n / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Error", "Veuillez saisir un entier positif!")


def affiche_bouton_operationssyslin(canvas, mat, vect, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat[a][b].get())
            float(vect[a].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des reels!")
    bouton.destroy()
    bouton_gauss = Button(root, command=lambda: operation_gauss(mat, vect, n),
                          text="Methode de GAUSS",
                          relief="groove", font="/font/myfont 15 bold", bg="#eee", fg="black",
                          activebackground="#dcc")
    bouton_lu = Button(root, command=lambda: operation_lu(mat, vect, n),
                       text="Factorisation LU",
                       relief="groove", font="/font/myfont 15 bold", bg="#eee", fg="black",
                       activebackground="#dcc")
    canvas.create_window(dimx_ / 4 + 100, 100 + 35 * n + 30, window=bouton_gauss)
    canvas.create_window(dimx_ / 4 + 400, 100 + 35 * n + 30, window=bouton_lu)


def affiche_boutons_operations1matrice(canvas, mat, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat[a][b].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    bouton.destroy()
    morse = Button(root, text="Stockage morse matrice", command=lambda: operation_stockmorse(mat, n),
                   relief="groove",
                   font="/font/myfont 11 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    inverser = Button(root, text="    Inverse d'une matrice",
                      command=lambda: operation_inverse(mat, n),
                      relief="groove",
                      font="/font/myfont 11 bold", bg="#eee", fg="black", activebackground="#dcc")
    determinant = Button(root, text="   Determinant matrice     ", command=lambda: operation_determinant(
        mat, n), relief="groove", font="/font/myfont 11 bold",
                         bg="#eee", fg="black", activebackground="#dcc")
    trans = Button(root, text="    Transposee matrice      ",
                   command=lambda: operation_transposee(mat, n), relief="groove",
                   font="/font/myfont 11 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    bouton_valeurpropre = Button(root, command="",
                                 text="Valeurs Propres matrice",
                                 relief="groove", font="/font/myfont 11 bold", bg="#eee", fg="black",
                                 activebackground="#dcc")
    canvas.create_window(dimx_ / 4 + 100, 100 + 35 * n + 30, window=morse)
    canvas.create_window(dimx_ / 4 + 100, 100 + 35 * n + 80, window=inverser)
    canvas.create_window(dimx_ / 4 + 350, 100 + 35 * n + 30, window=determinant)
    canvas.create_window(dimx_ / 4 + 350, 100 + 35 * n + 80, window=trans)
    canvas.create_window(dimx_ / 4 + 100, 100 + 35 * n + 130, window=bouton_valeurpropre)


def affiche_boutons_operation2matrices(canvas, mat1, mat2, a, b, c, d, bouton):
    try:
        for i in range(a):
            for j in range(b):
                float(mat1[i][j].get())
        for x in range(c):
            for y in range(d):
                float(mat2[x][y].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
    bouton.destroy()
    produit = Button(root, text="Produit", command=lambda: operation_produit(
        mat1, mat2, a, b, c, d), relief="groove",
                     font="/font/myfont 12 bold", bg="#eee", fg="black", activebackground="#dcc")
    somme = Button(root, text="Somme", command=lambda: operation_somme(mat1, mat2, a, b, c, d),
                   relief="groove", font="/font/myfont 12 bold",
                   bg="#eee", fg="black", activebackground="#dcc")
    canvas.create_window(dimx_ / 4 + 50, 250 + 35 * a, window=somme)
    canvas.create_window(dimx_ / 4 + 50 + 250, 250 + 35 * a, window=produit)

# M.TALL 2015-2016
