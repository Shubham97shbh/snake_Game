from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed("fast")
        self.refresh()
    def refresh(self):
        X = random.randint(-280, 280)
        Y = random.randint(-280, 280)
        self.goto(X, Y)