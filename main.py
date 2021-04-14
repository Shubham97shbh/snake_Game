import time
from turtle import Screen,Turtle
from score import Score
from food import Food
from snake import Snake
from tkinter import *

window = Tk()
snake = Snake()
food = Food()
screen = Screen()
score =Score()
tut = Turtle()

screen.bgcolor("red")
screen.title("Snake Game")
screen.screensize(canvwidth=500, canvheight=500)
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
def click_yes():
    game_on=True
    return game_on

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.speed("fast")
    score.update_text()
    if snake.b[0].distance(food)<15:
                    food.refresh()
                    score.count()
                    snake.update_pos()

    if snake.b[0].xcor()>330 or snake.b[0].xcor()<-330:
                                                    # lab = Label(text="Game Over\nstart again")
                                                    # lab.grid(row=2,column=2)
                                                    # my_button1 = Button(text="yes", command=click_yes)
                                                    # my_button2 = Button(text="no", command=click_n0)
                                                    # my_button1.grid(row=3, column=3)
                                                    # my_button2.grid(row=3, column=4)
                                                    snake.reset()
                                                    score.reset()

    if snake.b[0].ycor()>280 or snake.b[0].ycor()<-280:
                                                    snake.reset()
                                                    score.reset()


    # detecting collision
    for i in snake.b[1:]:
        if snake.b[0].distance(i)<10:
            # tut.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
            # game_on = False
            snake.reset()
            score.reset()

    tut.hideturtle()




window.mainloop()

