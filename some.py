import random
from math import dist
from tkinter import *
import time
root = Tk()
root.geometry("600x400")
myCanvas = Canvas(root, width=600, height=400)
myCanvas.pack(pady=10)


def create_circle(x, y, r, canvasName: Canvas):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="#000000", outline="#FFFFFF")


def go():
    position = []
    distance = []
    myCanvas.delete("all")
    for _ in range(10):
        x = random.uniform(10, 590)
        y = random.uniform(10, 390)
        create_circle(x, y, 3, myCanvas)
        position.append([x, y])
    for i in position:
        distance.extend([dist(i, n)] for n in position)
        print(distance)
    print("============================")
    root.after(50, go)


go()
root.mainloop()
