from turtle import Turtle


class Center(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.width(8)
        self.goto(0, -300)
        self.move()

    def move(self):
        self.left(90)
        draw = True
        while draw:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            if self.ycor() == 300:
                draw = False
