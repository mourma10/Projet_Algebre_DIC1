from Tkinter import Entry

from .operations import *


def saisie_2matrices(window, canvas, op):
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
    canvas.create_window(150, 20, window=ligne1)
    canvas.create_window(220, 20, window=col1)
    canvas.create_window(150, 60, window=ligne2)
    canvas.create_window(220, 60, window=col2)
    canvas.create_window(280, 40, window=bouton_ok)
    canvas.pack()


def saisie_1matrice(window, canvas, saiz):
    canvas.create_text(50, 20, text="Donner N", font="/font/myfont 10 bold", fill="black")
    ligne = Entry(window, relief="raised", width=3, bg="#eee")
    ligne.pack()

    bouton_ok = Button(window, text="Ok", relief="raised", font="/font/myfont 6 bold",
                       command=lambda: saiz(window, canvas, ligne.get(), bouton_ok), bg="#eee", fg="black",
                       activebackground="#dcc", width=3)
    canvas.create_window(150, 20, window=ligne)
    canvas.create_window(240, 20, window=bouton_ok)
    canvas.pack()


def affiche_saisie_1matrice(window, canvas, n, bouton, res):
    try:
        n = int(n)
        if n == 0:
            showerror("Erreur", "Veuillez saisir un entier strictement positif")
            return -1
        bouton.destroy()
        case = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                case[i][j] = Entry(window, width=3, relief="raised", font="/font/myfont 9", bg="#eee")
                canvas.create_window(70 + 35 * j, 100 + 35 * i, window=case[i][j])
        bouton_ok = Button(window, text="Ok", bg="#eee", font="/font/myfont 6 bold", fg="black",
                           activebackground="#dcc",
                           width=3,
                           relief="raised", command=lambda: res(window, canvas, case, n, bouton_ok))
        canvas.create_text(20, 100 + (35 * n / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_window(50 + 35 * n + 30, 100 + (35 * n / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir un entier positif!")
        return -1


def affiche_saisie_2matrices(window, canvas, a, b, c, d, bouton, res, typeop):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if (a, b, c, d) == (0, 0, 0, 0):
            showerror("Erreur", "Veuillez saisir des entiers strictement positifs")
            return -1
        sign = ' '
        if typeop == "somme":
            sign = '+'
            if (a != c) | (b != d):
                showerror("Erreur", "Somme Impossible")
                return -1
        if typeop == "produit":
            sign = '*'
            if b != c:
                showerror("Erreur", "Produit Impossible")
                return -1
        bouton.destroy()
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
        canvas.create_text(20, 100 + (30 * a / 2) - 20, text="A=", font="/font/myfont 13", fill="black")
        canvas.create_text(370, 100 + (30 * a / 2) - 20, text="B=", font="/font/myfont 13", fill="black")
        canvas.create_text((400 + 50 + 30 * b) / 2 - 10, 100 + (30 * b / 2) - 20, text=sign,
                           font="/font/myfont 20",
                           fill="black")
        canvas.create_window(400 + 50 + 30 * a, 100 + (30 * a / 2) - 20, window=bouton_ok)
    except ValueError:
        showerror("Erreur :-/", "Veuillez saisir des entiers positifs!")
        return -1


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


def affiche_saisiemorse(window, canvas, n, bouton):
    affiche_saisie_1matrice(window, canvas, n, bouton, operation_stockmorse)


def affiche_saisieinverse(window, canvas, n, bouton):
    affiche_saisie_1matrice(window, canvas, n, bouton, operation_inverse)


def affiche_saisiedet(window, canvas, n, bouton):
    affiche_saisie_1matrice(window, canvas, n, bouton, operation_determinant)


def affiche_saisietrans(window, canvas, n, bouton):
    affiche_saisie_1matrice(window, canvas, n, bouton, operation_transposee)


def affiche_saisiesomme(window, canvas, nb1, nb2, nb3, nb4, bouton):
    affiche_saisie_2matrices(window, canvas, nb1, nb2, nb3, nb4, bouton, operation_somme, "somme")


def affiche_saisieproduit(window, canvas, nb1, nb2, nb3, nb4, bouton):
    affiche_saisie_2matrices(window, canvas, nb1, nb2, nb3, nb4, bouton, operation_produit, "produit")

# M.TALL 2015-2016
