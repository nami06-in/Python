from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # It is normally 20 x 20 pixel. Set it to 10 x 10 pixel
        self.color("red")
        self.speed("fastest")
        self.refresh()  # Create the first position of food on the screen

    def refresh(self):
        random_x = random.randint(-280, 280)  # Screen is 600 x 600, So x-axis is -300 to 300
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
