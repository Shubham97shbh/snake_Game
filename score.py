from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count=0
        self.max_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.update_text()

    def count(self):
        self.score_count += 1

    def reset(self):
           if self.max_score<self.score_count:
                               self.max_score = self.score_count
                               with open("../../score_record.txt", mode="a") as file:
                                   file.write(f"{self.max_score}\n")
           self.score_count = 0


    def update_text(self):
        self.clear()
        with open("../../score_record.txt", mode="r") as file:
                                              a = file.readlines()
                                              self.max_score = int(a.pop(len(a)-1))
        self.write(f"Score= {self.score_count} Highest Score= {self.max_score}", align="center", font=("Arial", 13, "bold"))
    
    