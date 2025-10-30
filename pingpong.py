from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.title("Ping Pong game")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width = 500, height = 300, bd = 2, highlightthickness = 3)
canvas.config(bg = "black")
canvas.pack()

root.update()
# x1, y1    x2, y2
canvas.create_line(275, 0, 275, 600, fill = "white")

leftpaddlescore = 0
rightpaddlescore = 0

score_font = ("Calibri", 30, "bold")
score_text = (canvas.create_text(275, 20, font = score_font, text = f"{leftpaddlescore}:{rightpaddlescore}", fill = "white"))
# Create circle at the center of the canvas
x = 150
y = 125
r = 175
s = 125
canvas.create_oval(x, y, r, s, fill = "white")

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.id = canvas.create_oval(10, 10, 30, 30, fill = color)
        self.canvas = canvas
        canvas.move(self.id, 250, 150)
        self.paddle1 = paddle1
        self.paddle2 = paddle2

# Randomizes ball’s start direction and speed for both X and Y axes.
        start = [-3, -2, -1, 1, 2, 3 ]
        random.shuffle(start)
        self.x = start[0]
        self.y = start[1]

        self.canvas_height = self.canvas.winfo_height() 
        self.canvas_width = self.canvas.winfo_width()   

        self.score1 = 0
        self.score2 = 0
    
    def draw(self):
        global leftpaddlescore, rightpaddlescore
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos [1] <= 0:      # The top of the ball touches the top of the  game screen which is 0
            self.y = 4
        elif pos [3] >= self.canvas_height:     # The bottom most of the ball touches the bottom of the game screen
            self.y = -4
        if self.hit_paddle1(pos):
            self.x = 4
        elif self.hit_paddle2(pos):
            self.x = -4
        elif pos [2] >= self.canvas_width:
            self.x = -self.x
            leftpaddlescore += 1
            canvas.itemconfigure(score_text, text = str(leftpaddlescore) + ":" + str(rightpaddlescore))
        if pos [0] <= 0:
            self.x = 4
            rightpaddlescore += 1
            canvas.itemconfigure(score_text, text = str(leftpaddlescore) + ":" + str(rightpaddlescore))
            
    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        
            
        return False

    def hit_paddle2(self, pos):
        paddle_pos2 = self.canvas.coords(self.paddle2.id)
        if pos[1] >= paddle_pos2[1] and pos[3] <= paddle_pos2[3]:
            if pos[2] >= paddle_pos2[0] and pos[0] <= paddle_pos2[2]:
                return True
            
        return False

class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 125, 20, 200, fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("w", self.move_up)
        self.canvas.bind_all("s", self.move_down)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0





    def move_up(self, event):
        self.y = -4
    
    def move_down(self, event):
        self.y = 4



class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(490, 125, 500, 200, fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0





    def move_up(self, event):
        self.y = -4
    
    def move_down(self, event):
        self.y = 4

paddle1 = Paddle1(canvas, "orange")
paddle2 = Paddle2(canvas, "teal")
ball = Ball(canvas, paddle1, paddle2, "yellow")




def gameloop():
    paddle1.draw()
    paddle2.draw()
    ball.draw()
    root.after(20, gameloop)

 
 
gameloop()
root.mainloop()

