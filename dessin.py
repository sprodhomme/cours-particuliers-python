import tkinter as tk
import random
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "#000000")

choix=0

def fchoix():
    global choix
    choix = choix + 1

def fcouleur(choix):
    if choix%4 == 0:
        fill="green"
    elif choix%4 == 1:
        fill="red"
    elif choix%4 == 2:
        fill="blue"
    elif choix%4 == 3:
        fill="yellow"
    return fill

def tirage_point():
    x = random.randint(0,500)
    y = random.randint(0,500)
    
    return x,y

def fcercle():
    x,y = tirage_point()
    canvas.create_oval(x, y, x+100, y+100,fill=fcouleur(choix))

def fcarré():
    x,y = tirage_point()
    canvas.create_rectangle(x, y, x+100, y+100,fill=fcouleur(choix))

def fcroix():
    x,y = tirage_point()
    canvas.create_line(x,y,x+100,y+100, fill=fcouleur(choix), width=15)
    canvas.create_line(x,y+100,x+100,y, fill=fcouleur(choix), width=15)

couleur = tk.Button (root, text ="Choisir une couleur", bg="#ffffff", command=fchoix)
cercle = tk.Button (root, text ="Cercle", bg="#ffffff", command=fcercle)
carré = tk.Button (root, text ="Carré", bg="#ffffff", command=fcarré)
croix = tk.Button (root, text ="Croix", bg="#ffffff", command=fcroix)

couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1,)
carré.grid(column=0, row= 2,)
croix.grid(column=0, row=3,)

canvas.grid(column=1, row=1, rowspan=3)
root.mainloop()

