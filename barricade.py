from turtle import Turtle

class Barricade(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.bar1 = []
        self.bar2 = []

    def create_barricade(self):
        x_pos1 = 0
        for a in range(15):
            x_pos1 += 50
            self.wall1 = Turtle(shape="square")
            self.wall1.hideturtle()
            self.wall1.penup()
            self.wall1.color("white")
            self.wall1.setposition(-400 + x_pos1, -100)
            self.wall1.showturtle()
            self.bar1.append(self.wall1)

        x_pos2 = 0
        for a in range(15):
            x_pos2 += 50
            self.wall2 = Turtle(shape="square")
            self.wall2.hideturtle()
            self.wall2.penup()
            self.wall2.color("white")
            self.wall2.setposition(-400 + x_pos2, -150)
            self.wall2.showturtle()
            self.bar2.append(self.wall2)

    def destroy_barricade(self,index):
        if index in self.bar1:
            index.ht()
            self.bar1.remove(index)

        if index in self.bar2:
            index.ht()
            self.bar2.remove(index)

