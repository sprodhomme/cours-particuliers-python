import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "#000000")

x = 50
y = 50

canvas.create_oval( x, y, x+300, y+300, fill="blue")
canvas.create_oval( x, y, x+280, y+280, fill="green")
canvas.create_oval( x, y, x+260, y+260, fill="black")
canvas.create_oval( x, y, x+240, y+240, fill="yellow")
canvas.create_oval( x, y, x+220, y+220, fill="magenta")
canvas.create_oval( x, y, x+200, y+200, fill="red")
canvas.create_oval( x, y, x+180, y+180, fill="blue")
canvas.create_oval( x, y, x+160, y+160, fill="green")
canvas.create_oval( x, y, x+140, y+140, fill="black")
canvas.create_oval( x, y, x+120, y+120, fill="yellow")
canvas.create_oval( x, y, x+100, y+100, fill="magenta")
canvas.create_oval( x, y, x+80, y+80, fill="red")
canvas.create_oval( x, y, x+60, y+60, fill="blue")
canvas.create_oval( x, y, x+40, y+40, fill="green")
canvas.create_oval( x, y, x+20, y+20, fill="black")


canvas.grid()
root.mainloop()
