import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "#000000")

x = 100
y = 100

canvas.create_oval( x, y, x+300, y+300, fill="blue")
canvas.create_oval( x, y, x+250, y+250, fill="green")

canvas.grid()
root.mainloop()

# Lien : https://stackoverflow.com/questions/17985216/simpler-way-to-draw-a-circle-with-tkinter
