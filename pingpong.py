from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.title("Ping Pong game")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width = 600, height = 300, bd = 2, highlightthickness = 3)
canvas.config(bg = "black")
canvas.pack()

car = canvas.create_text(300, 20, fill = "white", font = ("bold", 40), text = ":")
root.update()
# x1, y1    x2, y2
canvas.create_line(300, 0, 300, 600, fill = "white", opacity = 0.5)























root.mainloop()

