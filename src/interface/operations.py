# -*-coding:UTF-8 -*

import pyaudio
import wave
from Tkinter import Button
from tkMessageBox import showerror, showinfo


def operation_produit(window, canvas, mat1, mat2, nb1, nb2, nb3, nb4, bouton):
    try:
        for a in range(nb1):
            for b in range(nb2):
                float(mat1[a][b].get())
        for x in range(nb3):
            for y in range(nb4):
                float(mat2[x][y].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    if nb2 == nb3:
        bouton.destroy()
        produit = prod = [[0] * nb4 for _ in range(nb1)]
        for i in range(nb1):
            for j in range(nb4):
                produit[i][j] = 0
                for k in range(nb2):
                    produit[i][j] += float(mat1[i][k].get()) * float(mat2[k][j].get())
                prod[i][j] = Button(window, text=produit[i][j], relief="raised", width=1, height=1,
                                    font="/font/myfont 9",
                                    bg="#eee")
                canvas.create_window(250 + 40 * j + 10, 350 + 40 * i, window=prod[i][j])
    canvas.create_text(200, 350 + (40 * nb1 / 2) - 20, text="A * B =", font="/font/myfont 13", fill="black")


def operation_somme(window, canvas, mat1, mat2, nb1, nb2, nb3, nb4, bouton):
    try:
        for a in range(nb1):
            for b in range(nb2):
                float(mat1[a][b].get())
        for x in range(nb3):
            for y in range(nb4):
                float(mat2[x][y].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    bouton.destroy()
    somme = [[0] * nb3 for _ in range(nb1)]
    for i in range(nb4):
        for j in range(nb2):
            somme[i][j] = Button(window, text=float(mat1[i][j].get()) + float(mat2[i][j].get()), width=1,
                                 height=1, relief="raised", font="/font/myfont 9", bg="#eee")
            canvas.create_window(250 + 40 * j + 10, 350 + 40 * i, window=somme[i][j])
    canvas.create_text(200, 350 + (40 * nb2 / 2) - 20, text="A + B =", font="/font/myfont 13", fill="black")


def operation_stockmorse(window, canvas, mat, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat[a][b].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1

    bouton.destroy()
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
                indiceligne[x] = Button(window, text=i, width=1, height=1, relief="raised",
                                        font="/font/myfont 9",
                                        bg="#eee")
                indicecolonne[x] = Button(window, text=j, width=1, height=1, relief="raised",
                                          font="/font/myfont 9",
                                          bg="#eee")
                elmtnonnul[x] = Button(window, text=mat[i][j].get(), width=1, height=1, relief="raised",
                                       font="/font/myfont 9",
                                       bg="#eee")
                canvas.create_window(230 + 40 * x, 360, window=indiceligne[x])
                canvas.create_window(230 + 40 * x, 390, window=indicecolonne[x])
                canvas.create_window(230 + 40 * x, 420, window=elmtnonnul[x])
                x += 1
    canvas.create_text(70, 360, text="Tableau des indices i", font="/font/myfont 9", fill="black")
    canvas.create_text(70, 390, text="Tableau des indices j", font="/font/myfont 9", fill="black")
    canvas.create_text(100, 420, text="Tableau des valeurs non nulles", font="/font/myfont 9", fill="black")


def operation_inverse(window, canvas, mat, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat[a][b].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1

    matid = [[0] * n for _ in range(n)]
    newmat = [[0] * (2 * n) for _ in range(n)]
    for i in range(n):  # Creation de la matrice identité
        for j in range(n):
            if i == j:
                matid[i][j] = 1
            else:
                matid[i][j] = 0

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
    bouton.destroy()
    if inversible == 1:  # Affichage de la matrice inverse
        inv = [[0] * (2 * n) for _ in range(n)]
        i = 0
        while i < n:
            j = n
            while j < 2 * n:
                inv[i][j] = Button(window, text=round(newmat[i][j], 2), relief="raised", width=1, height=1,
                                   font="/font/myfont 9 bold", bg="#eee")
                canvas.create_window(250 + 35 * j, 100 + 35 * i, window=inv[i][j])
                j += 1
            i += 1
        canvas.create_text(250 + 35 * n - 60, 100 + (35 * n / 2) - 20, text="Inv(A)= ", fill="black",
                           font="/font/myfont 13")
    else:
        showinfo("Oups! :-/", "La matrice n'est pas inversible")


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


def operation_determinant(window, canvas, mat1, n1, bouton):
    try:
        for a in range(n1):
            for b in range(n1):
                float(mat1[a][b].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    bouton.destroy()
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
    determinant = Button(window, text=round(sign * proddiag(mat, n1), 2), relief="raised", width=3, height=1,
                         font="/font/myfont 9 bold", bg="#eee")
    canvas.create_text(50, 360, text="det(M)=", font="/font/myfont 9 bold", fill="black")
    canvas.create_window(130, 360, window=determinant)


def operation_transposee(window, canvas, mat1, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat1[a][b].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    bouton.destroy()
    mat = [[0] * n for _ in range(n)]
    trans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(mat1[i][j].get())
    for a in range(n):
        for b in range(n):
            trans[a][b] = Button(window, text=mat[b][a], relief="raised", width=1, height=1,
                                 font="/font/myfont 9 bold",
                                 bg="#eee")
            canvas.create_window(400 + 35 * b, 100 + 35 * a, window=trans[a][b])
    canvas.create_text(335, 100 + (35 * n / 2) - 20, text="t(A)= ", fill="black", font="/font/myfont 13")


def operation_gauss(window, canvas, mat, vect, n, bouton):
    try:
        for a in range(n):
            for b in range(n):
                float(mat[a][b].get())
            float(vect[a].get())
    except ValueError:
        showerror("Erreur", "Veuillez saisir des réels!")
        return -1
    matrice = [[0] * n for _ in range(n)]
    vecteur = [0] * n
    solution = x = [0] * n
    for i in range(n):
        for j in range(n):
            matrice[i][j] = float(mat[i][j].get())
    for k in range(n):
        vecteur[k] = float(vect[k].get())
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
        bouton.destroy()
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
        for s in range(n):
            solution[s] = Button(window, text=round(x[s], 4), relief="raised", width=4, height=1,
                                 font="/font/myfont 9 bold",
                                 bg="#eee")
            canvas.create_window(150, 300 + 35 * s, window=solution[s])
        canvas.create_text(70, 300 + (35 * n / 2) - 20, text="Solution=", font="/font/myfont 12 bold",
                           fill="black")


def operation_record():
    chunk = 1024
    format_ = pyaudio.paInt32
    channels = 2
    rate = 44100
    record_seconds = 10
    wave_output_filename = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=format_,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format_))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# M.TALL 2015-2016
