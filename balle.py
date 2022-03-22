import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt1 = 0


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
                                fill="blue", width=0)
    return [cercle, dx, dy]

def creer_carre():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    rectangle = canvas.create_rectangle((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="red")
    return [rectangle, dx, dy]

def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.move(carre[0], carre[1], carre[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle et le carré sur les bords du canevas"""
    global balle
    global carre
    global cpt1
    
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        carre[1] = -carre[1]
        cpt1 = cpt1 + 1
        print(cpt1)
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        carre[2] = -carre[2]
        cpt1 = cpt1 + 1
        print(cpt1)
    
    if cpt1 % 5 == 0:
        canvas.itemconfigure(carre[0], fill="blue")
        
    if cpt1 % 10 == 0:
        canvas.itemconfigure(carre[0], fill="black")

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle

carre = creer_carre()
balle = creer_balle()
# déplacement de la balle et du carré ensemble
mouvement()

# alternance balle / rectangle


# boucle principale
racine.mainloop()
