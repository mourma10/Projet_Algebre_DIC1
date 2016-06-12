from Tkinter import Entry

from .operations import *


def saisie_2matrices(window, canvas, op):  # Saisie nombre de lignes et de colonnes de deux matrices  (Prototype)
    canvas.create_text(60, 20, text="Donner N1,C1", font="/font/myfont 10 bold", fill="black")
    canvas.create_text(60, 60, text="Donner N2,C2", font="/font/myfont 10 bold", fill="black")
    ligne1 = Entry(window, relief="raised", width=3, bg="#eee")
    col1 = Entry(window, relief="raised", width=3, bg="#eee")
    ligne2 = Entry(window, relief="raised", width=3, bg="#eee")
    col2 = Entry(window, relief="raised", width=3, bg="#eee")
    ligne1.pack()
    ligne2.pack()
    col1.pack()
    col2.pack()
    bouton_ok = Button(window, text="Ok", relief="raised", font="/font/myfont 6 bold",
                       command=lambda: op(window, canvas, ligne1.get(), col1.get(), ligne2.get(),
                                          col2.get(), bouton_ok), bg="#eee", fg="black",
                       activebackground="#dcc", width=3)
    bouton_ok.pack()
    canvas.create_window(150, 20, window=ligne1)
    canvas.create_window(220, 20, window=col1)
    canvas.create_window(150, 60, window=ligne2)
    canvas.create_window(220, 60, window=col2)
    canvas.create_window(280, 40, window=bouton_ok)
    canvas.pack()


def saisie_1matrice(window, canvas, saiz):  # Saisie nbre de lignes et de colonnes d'une matrice (Prototype)
    canvas.create_text(50, 20, text="Donner N", font="/font/myfont 10 bold", fill="black")
    ligne = Entry(window, relief="raised", width=3, bg="#eee")
    ligne.pack()

    bouton_ok = Button(window, text="Ok", relief="raised", font="/font/myfont 6 bold",
                       command=lambda: saiz(window, canvas, ligne.get(), bouton_ok), bg="#eee", fg="black",
                       activebackground="#dcc", width=3)
    bouton_ok.pack()
    canvas.create_window(150, 20, window=ligne)
    canvas.create_window(240, 20, window=bouton_ok)
    canvas.pack()


def affiche_saisie_1matrice(window, canvas, n, res):  # Affichage pour la saisie des elements de la matrice(Prototype)
    case = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            case[i][j] = Entry(window, width=3, relief="raised", font="/font/myfont 9", bg="#eee")
            canvas.create_window(70 + 35 * j, 100 + 35 * i, window=case[i][j])
    bouton_ok = Button(window, text="Ok", bg="#eee", font="/font/myfont 6 bold", fg="black", activebackground="#dcc",
                       width=3,
                       relief="raised", command=lambda: res(window, canvas, case, n, bouton_ok))
    bouton_ok.pack()
    canvas.create_text(20, 100 + (35 * n / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
    canvas.create_window(50 + 35 * n + 30, 100 + (35 * n / 2) - 20, window=bouton_ok)


def affiche_saisie_2matrices(window, canvas, a, b, c, d,
                             res):  # Affichage pour la saisie(case par case) de deux matrices (Prototype)
    case1 = [[0] * b for _ in range(a)]
    case2 = [[0] * d for _ in range(c)]
    for i in range(a):
        for j in range(b):
            case1[i][j] = Entry(window, width=3, relief="raised", font="/font/myfont 8", bg="#eee")
            canvas.create_window(70 + 30 * j, 100 + 30 * i, window=case1[i][j])
    for k in range(c):
        for l in range(d):
            case2[k][l] = Entry(window, width=3, relief="raised", font="/font/myfont 8", bg="#eee")
            canvas.create_window(420 + 30 * l, 100 + 30 * k, window=case2[k][l])
    bouton_ok = Button(window, text="Ok", relief="raised",
                       command=lambda: res(window, canvas, case1, case2, a, b, c, d, bouton_ok),
                       bg="#eee", fg="black", activebackground="#dcc", font="/font/myfont 6 bold", width=3)
    bouton_ok.pack()
    canvas.create_text(20, 100 + (30 * a / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
    canvas.create_text(370, 100 + (30 * a / 2) - 20, text="B=", font="/font/myfont 13", fill="black")
    canvas.create_window(400 + 50 + 30 * a, 100 + (30 * a / 2) - 20, window=bouton_ok)


def affiche_saisiegauss(window, canvas, n1, bouton):
    try:
        n = int(n1)
        bouton.destroy()
        case = [[0] * n for _ in range(n)]
        vecteur = [0] * n
        for i in range(n):
            for j in range(n):
                case[i][j] = Entry(window, width=3, relief="raised", font="/font/myfont 9", bg="#eee")
                canvas.create_window(70 + 35 * j, 100 + 35 * i, window=case[i][j])
        for i in range(n):
            vecteur[i] = Entry(window, width=3, relief="raised", font="/font/myfont 9", bg="#eee")
            canvas.create_window(200 + 35 * (n - 1), 100 + 35 * i, window=vecteur[i])
        bouton_ok = Button(window, text="Ok", bg="#eee", font="/font/myfont 6 bold", fg="black",
                           activebackground="#dcc",
                           width=3,
                           relief="raised",
                           command=lambda: operation_gauss(window, canvas, case, vecteur, n, bouton_ok))
        canvas.create_text(20, 100 + (35 * n / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_text(180 + 35 * (n - 1) - 20, 100 + (35 * n / 2) - 20, text="b=", font="/font/myfont 13",
                           fill="black")
        canvas.create_window(250 + 35 * n + 30, 100 + (35 * n / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Error", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisiemorse(window, canvas, n1,
                        bouton):  # On instancie affiche_saisie pour le stockage morse:ici res=stock_morse
    try:
        n = int(n1)
        bouton.destroy()
        affiche_saisie_1matrice(window, canvas, n, operation_stockmorse)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisieinverse(window, canvas, n1, bouton):  # On instancie affiche_saisie pour l'inverse:ici res=inverse
    try:
        n = int(n1)
        bouton.destroy()
        affiche_saisie_1matrice(window, canvas, n, operation_inverse)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisiedet(window, canvas, n1, bouton):
    try:
        n = int(n1)
        bouton.destroy()
        affiche_saisie_1matrice(window, canvas, n, operation_determinant)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisietrans(window, canvas, n1, bouton):
    try:
        n = int(n1)
        bouton.destroy()
        affiche_saisie_1matrice(window, canvas, n, operation_transposee)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisiesomme(window, canvas, nb1, nb2, nb3,
                        nb4, bouton):  # On instancie la fonction todo_op pour la somme:ici res=affiche_somme
    try:
        n1 = int(nb1)
        n2 = int(nb2)
        n3 = int(nb3)
        n4 = int(nb4)
        if (n1 != n3) | (n2 != n4):
            showinfo("Erreur", "Somme Impossible")
        else:
            bouton.destroy()
            affiche_saisie_2matrices(window, canvas, n1, n2, n3, n4, operation_somme)
            canvas.create_text((400 + 50 + 30 * n2) / 2 - 10, 100 + (30 * n2 / 2) - 20, text="+",
                               font="/font/myfont 20",
                               fill="black")
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir des entiers positifs!")
        return -1


def affiche_saisieproduit(window, canvas, nb1, nb2, nb3,
                          nb4, bouton):  # On instancie la fonction todo_op pour le produit:ici res=affiche_produit
    try:
        n1 = int(nb1)
        n2 = int(nb2)
        n3 = int(nb3)
        n4 = int(nb4)
        if n2 != n3:
            showinfo("Erreur", "Produit Impossible")
            return -1
        else:
            bouton.destroy()
            affiche_saisie_2matrices(window, canvas, n1, n2, n3, n4, operation_produit)
            canvas.create_text((400 + 50 + 30 * n2) / 2 - 10, 100 + (30 * n2 / 2) - 20, text="*",
                               font="/font/myfont 20",
                               fill="black")
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir des entiers positifs!")
        return -1

# M.TALL 2015-2016
