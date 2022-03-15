import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "#000000")

x = 150
y = 150

canvas.create_oval( x, y, x+100, y+100, fill="blue", width=15)

canvas.grid()
root.mainloop()
