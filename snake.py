from turtle import Turtle
from score import Score

tu = Turtle()
tu.color("white")
Move = 20


class Snake():
    def __init__(self):
        self.b = []
        self.create_snake()
        # whenever we call this funtion all the self part given here will be excecuted
        
    def update(self):
        tu.shape("circle")
        tu.shapesize(1, 1)
        tu.penup()
        self.b.append(tu.clone())
        tu.backward(20)

    def update_pos(self):
        tu.showturtle()
        self.update()
        tu.hideturtle()

    def create_snake(self):
        for i in range(0, 3):
                        self.update()
        tu.hideturtle()
        self.b[0].shape("turtle")


    def move(self):
        for i in range(len(self.b) - 1, 0, -1):
            X = self.b[i - 1].xcor()
            Y = self.b[i - 1].ycor()
            self.b[i].goto(X, Y)
        self.b[0].forward(Move)
        self.b[0].speed("fast")

    def reset(self):
        for i in self.b:
                   i.goto(1000, 1000)
        self.b.clear()
        tu.showturtle()
        self.create_snake()
        self.b[0].goto(0,0)

    def up(self):
        if self.b[0].heading() != 270:
            self.b[0].setheading(90)

    def down(self):
        if self.b[0].heading() != 90:
            self.b[0].setheading(270)

    def left(self):
        if self.b[0].heading() != 0:
            self.b[0].setheading(180)

    def right(self):
        if self.b[0].heading() != 180:
            self.b[0].setheading(0)
