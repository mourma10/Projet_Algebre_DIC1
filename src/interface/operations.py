# -*-coding:UTF-8 -*

import time
from Tkinter import Button
from tkMessageBox import showinfo, showerror

from .getroot import root_operation


def operation_produit(mat1, mat2, nb1, nb2, nb3, nb4):
    if nb2 != nb3:
        showerror("Erreur", "Produit Impossible")
        return -1
    else:
        (root_produit, canvas) = root_operation(nb1, "Produit de matrices")
        produit = [[0] * nb4 for _ in range(nb1)]
        prod = [[0] * nb4 for _ in range(nb1)]
        for i in range(nb1):
            for j in range(nb4):
                produit[i][j] = 0
                for k in range(nb2):
                    produit[i][j] += float(mat1[i][k].get()) * float(mat2[k][j].get())
                prod[i][j] = Button(root_produit, text=produit[i][j], relief="groove", width=1, height=1,
                                    font="/font/myfont 9 bold", bg="#eee")
                canvas.create_window((200 * nb1 - 100) / 2 - 10 + 45 * j, (100 * nb1 - 50) / 4 + 25 + 30 * i,
                                     window=prod[i][j])
        canvas.create_text((200 * nb1 - 100) / 2 - 60, ((100 * nb1 - 50) / 2 + 30 * nb1) / 2 + 10,
                           text="A * B =", font="/font/myfont 10 bold", fill="black")
        canvas.pack()


def operation_somme(mat1, mat2, nb1, nb2, nb3, nb4):
    if (nb1 != nb3) | (nb2 != nb4):
        showerror("Erreur", "Somme Impossible")
        return -1
    else:
        (root_somme, canvas) = root_operation(nb1, "Somme de matrices")
        somme = [[0] * nb2 for _ in range(nb1)]
        for i in range(nb1):
            for j in range(nb2):
                somme[i][j] = Button(root_somme, text=float(mat1[i][j].get()) + float(mat2[i][j].get()),
                                     width=1, height=1, relief="groove",
                                     font="/font/myfont 9 bold", bg="#eee")
                canvas.create_window((200 * nb1 - 100) / 2 - 10 + 45 * j, (100 * nb1 - 50) / 4 + 25 + 30 * i,
                                     window=somme[i][j])
            canvas.create_text((200 * nb1 - 100) / 2 - 60, ((100 * nb1 - 50) / 2 + 30 * nb1) / 2 + 10,
                               text="A + B =", font="/font/myfont 10 bold", fill="black")
        canvas.pack()


def operation_stockmorse(mat, n):
    (root_morse, canvas) = root_operation(n, "Stockage Morse de la matrice")
    k = 0
    for i in range(n):
        for j in range(n):
            if float(mat[i][j].get()) != 0.0:
                k += 1
    indiceligne = [0] * k
    indicecolonne = [0] * k
    elmtnonnul = [0] * k
    x = 0
    for i in range(n):
        for j in range(n):
            if float(mat[i][j].get()) != 0.0:
                indiceligne[x] = Button(root_morse, text=i, width=1, height=1, relief="groove",
                                        font="/font/myfont 9",
                                        bg="#eee")
                indicecolonne[x] = Button(root_morse, text=j, width=1, height=1, relief="groove",
                                          font="/font/myfont 9",
                                          bg="#eee")
                elmtnonnul[x] = Button(root_morse, text=mat[i][j].get(), width=1, height=1, relief="groove",
                                       font="/font/myfont 9",
                                       bg="#eee")
                canvas.create_window(100 + 40 * x, (100 * n - 50) / 2 - 25, window=indiceligne[x])
                canvas.create_window(100 + 40 * x, (100 * n - 50) / 2, window=indicecolonne[x])
                canvas.create_window(100 + 40 * x, (100 * n - 50) / 2 + 25, window=elmtnonnul[x])
                x += 1
    canvas.create_text(50, (100 * n - 50) / 2 - 20, text="indices i", font="/font/myfont 9 bold",
                       fill="black")
    canvas.create_text(50, (100 * n - 50) / 2, text="indices j", font="/font/myfont 9 bold", fill="black")
    canvas.create_text(50, (100 * n - 50) / 2 + 20, text="A[i][j]", font="/font/myfont 9 bold",
                       fill="black")
    canvas.pack()


def operation_inverse(mat, n):
    matid = [[0] * n for _ in range(n)]
    newmat = [[0] * (2 * n) for _ in range(n)]
    for i in range(n):  # Creation de la matrice identité
        for j in range(n):
            if i == j:
                matid[i][j] = 1.0
            else:
                matid[i][j] = 0.0

    for a in range(n):  # On cree la matrice n lignes 2n colonnes
        for b in range(2 * n):
            if b < n:
                newmat[a][b] = float(mat[a][b].get())
            else:
                newmat[a][b] = matid[a][b - n]

    inversible = 1
    k = 0

    while (inversible == 1) and (k < n):  # Methode de Gauss-Jordan
        if newmat[k][k] != 0:
            var = float(newmat[k][k])
            for colonne in range(2 * n):
                newmat[k][colonne] = float(newmat[k][colonne]) / var
            for i in range(n):
                if i != k:
                    var1 = float(newmat[i][k])
                    for colonnebis in range(2 * n):
                        newmat[i][colonnebis] = float(newmat[i][colonnebis]) - \
                                                (float(newmat[k][colonnebis]) * var1)
            k += 1
        else:
            inversible = 0
    if inversible == 1:  # Affichage de la matrice inverse
        (root_inverse, canvas) = root_operation(n, "Inverse de la matrice")
        inv = [[0] * (2 * n) for _ in range(n)]
        i = 0
        while i < n:
            j = n
            while j < 2 * n:
                inv[i][j] = Button(root_inverse, text=round(newmat[i][j], 2), relief="groove",
                                   width=1, height=1,
                                   font="/font/myfont 9 bold", bg="#eee")
                canvas.create_window((200 * n - 100) / 2 - 200 + 50 * j, (100 * n - 50) / 2 - 30 + 40 * i,
                                     window=inv[i][j])
                j += 1
            i += 1
        canvas.create_text((200 * n - 100) / 2 - 100, (100 * n - 50) / 2 + 10, text="Inv(A)= ",
                           font="/font/myfont 12", fill="black")
        canvas.pack()
    else:
        showinfo(":-/", "La matrice n'est pas inversible")


def permcol(mat, n, j, i):
    for k in range(n - 1, -1, -1):
        (mat[k][j], mat[k][i]) = (mat[k][i], mat[k][j])


def proddiag(mat, n):
    j = 0
    p = 1
    while j < n:
        p *= mat[j][j]
        j += 1
    return p


def operation_determinant(mat1, n1):
    (root_det, canvas) = root_operation(n1, "Determinant de la matrice")
    mat = [[0] * n1 for _ in range(n1)]
    for a in range(n1):
        for b in range(n1):
            mat[a][b] = float(mat1[a][b].get())
    sign = 1
    n = n1 - 1
    for i in range(n, 0, -1):
        for j in range(0, i):
            if mat[i][j + 1] != 0.0:
                q = mat[i][j] / mat[i][j + 1]
                if q != 0.0:
                    for k in range(n, -1, -1):
                        mat[k][j] -= q * mat[k][j + 1]
            else:
                permcol(mat, n1, j + 1, j)
                sign *= -1
    determinant = Button(root_det, text=round(sign * proddiag(mat, n1), 2), relief="groove", width=3,
                         height=1, font="/font/myfont 15 bold", bg="#eee")
    canvas.create_text((200 * n1 - 100) / 2 - 90, (100 * n1 - 50) / 2 - 20, text="det(M) = ",
                       font="/font/myfont 12 bold", fill="black")
    canvas.create_window((200 * n1 - 100) / 2, (100 * n1 - 50) / 2 - 20, window=determinant)
    canvas.pack()


def operation_transposee(mat1, n):
    (root_trans, canvas) = root_operation(n, "Transposee de la matrice")
    mat = [[0] * n for _ in range(n)]
    trans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(mat1[i][j].get())
    for a in range(n):
        for b in range(n):
            trans[a][b] = Button(root_trans, text=mat[b][a], relief="groove", width=1, height=1,
                                 font="/font/myfont 9 bold",
                                 bg="#eee")
            canvas.create_window((200 * n - 100) / 2 - 50 + 45 * b, (100 * n - 50) / 2 + 50 * a,
                                 window=trans[a][b])
    canvas.create_text((200 * n - 100) / 2 - 150, (100 * n - 50) / 2 + 50, text="t(A)= ", fill="black",
                       font="/font/myfont 12 bold")
    canvas.pack()


def operation_gauss(mat, vect, n):
    matrice = [[0] * n for _ in range(n)]
    vecteur = [0] * n
    solution = x = [0] * n
    for i in range(n):
        for j in range(n):
            matrice[i][j] = float(mat[i][j].get())
    for k in range(n):
        vecteur[k] = float(vect[k].get())
    t1 = time.time()
    for k in range(n):
        valmin = matrice[k][k]
        imin = k
        i = k + 1
        while i < n:
            if valmin != 0:
                if (abs(matrice[i][k]) < abs(valmin)) & (matrice[i][k] != 0):
                    valmin = matrice[i][k]
                    imin = i
            else:
                valmin = matrice[i][k]
                imin = i
            i += 1
        if valmin == 0:
            showinfo("Erreur", "Résolution Impossible")
            return -1
        else:
            for j in range(n):
                tampon = matrice[imin][j]
                matrice[imin][j] = matrice[k][j]
                matrice[k][j] = tampon
            tampon1 = vecteur[imin]
            vecteur[imin] = vecteur[k]
            vecteur[k] = tampon1
            i = k + 1
            while i < n:
                p = matrice[i][k] / matrice[k][k]
                for l in range(n):
                    matrice[i][l] -= p * matrice[k][l]
                vecteur[i] -= p * vecteur[k]
                i += 1
    if matrice[n - 1][n - 1] == 0:
        showinfo("Erreur", "Résolution Impossible")
    else:
        t2 = time.time() - t1
        (root_gauss, canvas) = root_operation(n, "Methode de GAUSS")
        t3 = time.time()
        x[n - 1] = vecteur[n - 1] / matrice[n - 1][n - 1]
        i = n - 2
        while i >= 0:
            som = 0.0
            j = n - 1
            while j >= 0:
                som += matrice[i][j] * x[j]
                j -= 1
            x[i] = (vecteur[i] - som) / matrice[i][i]
            i -= 1
        t4 = time.time() - t3
        t = t2 + t4
        for s in range(n):
            solution[s] = Button(root_gauss, text=round(x[s], 4), relief="groove", width=4, height=1,
                                 font="/font/myfont 9 bold",
                                 bg="#eee")
            canvas.create_window((200 * n - 100) / 2 + 10, (100 * n - 100) / 2 + 35 * s, window=solution[s])
        canvas.create_text((200 * n - 100) / 2 - 80, ((100 * n - 50) / 2 + 30 * n) / 2 + 30,
                           text="Solution=", font="/font/myfont 12 bold",
                           fill="black")
        canvas.create_text((200 * n - 100) / 2 + 150, ((100 * n - 50) / 2 + 30 * n) / 2 + 30,
                           text="Tps(ms)=" + str(round((t * 1000), 7)),
                           font="/font/myfont 10 bold", fill="black")
        canvas.pack()


def creematcar(n):
    return [[0.0 for _ in range(n)] for _ in range(n)]


def creerliste(n):
    return [0.0 for _ in range(n)]


def eliminationlu(k, mat):
    n = len(mat)
    i = k + 1
    while i < n:
        r = mat[i][k] / mat[k][k]
        j = k
        while j < n:
            mat[i][j] -= r * mat[k][j]
            j += 1
        i += 1
    return mat


def descente(mat, b):
    n = len(mat)
    y = creerliste(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= mat[i][j] * y[j]
    return y


def remonte(mat, b):
    n = len(mat)
    x = creerliste(n)
    x[n - 1] = b[n - 1] / mat[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]
    return x


def factlu(mat1):
    n = len(mat1)
    mat = mat1
    k = 0
    arret = 0
    l = creematcar(n)
    while k != n and arret != 1:
        l[k][k] = 1
        if mat[k][k] != 0:
            for i in range(k + 1, n):
                l[i][k] = mat[i][k] / mat[k][k]
            mat = eliminationlu(k, mat)
            k += 1
        else:
            arret = 1
    if (arret == 0) and (mat[n - 1][n - 1] != 0):
        return l, mat
    else:
        showerror("Erreur", "Resolution impossible")
        return -1


def operation_lu(mat, vect, n):
    (root_lu, canvas) = root_operation(3 * n / 2, "Factosiation LU")
    mat1 = [[0] * n for _ in range(n)]
    b = [0] * n
    solution = [0] * n
    matrice_l = [[0] * n for _ in range(n)]
    matrice_u = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat1[i][j] = float(mat[i][j].get())
        b[i] = float(vect[i].get())
    t1 = time.time()
    l, u = factlu(mat1)
    if l != 0:
        y = descente(l, b)
        x = remonte(mat1, y)
        t2 = time.time()
        t = t2 - t1
        for s in range(len(x)):
            solution[s] = Button(root_lu, text=round(x[s], 4), relief="groove", width=4, height=1,
                                 font="/font/myfont 9 bold", bg="#eee")
            canvas.create_window((300 * n - 100) / 2 - 40, 20 + 35 * s, window=solution[s])
        canvas.create_text((300 * n - 100) / 2 - 120, 20 + (35 * n / 2) - 20, text="Solution=",
                           font="/font/myfont 10 bold", fill="black")
        canvas.create_text((300 * n - 100) / 2 + 100, 20 + (35 * n / 2) - 20,
                           text="Tps(ms)=" + str(round((t * 1000), 7)),
                           font="/font/myfont 10 bold", fill="black")
        for i in range(n):
            for j in range(n):
                matrice_l[i][j] = Button(root_lu, text=round(l[i][j], 4), relief="groove", width=4, height=1,
                                         font="/font/myfont 9 bold", bg="#eee")
                matrice_u[i][j] = Button(root_lu, text=round(u[i][j], 4), relief="groove", width=4,
                                         height=1, font="/font/myfont 9 bold", bg="#eee")
                canvas.create_window(90 + 60 * j + 10, 150 * n - 245 + 50 * i, window=matrice_l[i][j])
                canvas.create_text(40, 150 * n - 245 + (50 * n / 2) - 20, text="L = ",
                                   font="/font/myfont 12 bold", fill="black")
                canvas.create_window((300 * n - 100) / 2 + 50 + 60 * j + 10, 150 * n - 245 + 50 * i,
                                     window=matrice_u[i][j])
                canvas.create_text((300 * n - 100) / 2, 150 * n - 245 + (50 * n / 2) - 20, text="U = ",
                                   font="/font/myfont 12 bold", fill="black")
        canvas.pack()
        return x, l, t * 1000000
    else:
        showerror("Erreur", "Resolution impossible")
        return -1

# M.TALL 2015-2016
