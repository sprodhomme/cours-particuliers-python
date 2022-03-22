import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
rebond_compte = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    global rebond_compte
    rectangle = canvas.create_rectangle(50, 50, 50, 50, fill="blue")
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
    if rebond_compte % 5 == 0:
        canvas.itemconfigure(balle[0], fill="yellow")
        
    if rebond_compte % 10 == 0:
        canvas.itemconfigure(balle[0], fill="blue")


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
