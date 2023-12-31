import random
from turtle import Turtle

class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hits = 0
        self.ht()
        self.penup()
        self.alien_list_layer3 = []
        self.alien_list_layer2 = []
        self.alien_list_layer1 = []
        self.missile_list = []
        self.x_move_main = 5



    def create_aliens(self):
        x_pos3 = 0
        for a in range(8):
            x_pos3 += 50
            self.alien3 = Turtle(shape="turtle")
            self.alien3.setheading(270)
            self.alien3.hideturtle()
            self.alien3.speed(0)
            self.alien3.penup()
            self.alien3.color("red")
            self.alien3.setposition(-225 + x_pos3,350)
            self.alien3.showturtle()
            self.alien_list_layer3.append(self.alien3)



        x_pos2 = 0
        for a in range(8):
            x_pos2 += 50
            self.alien2 = Turtle(shape="turtle")
            self.alien2.setheading(270)
            self.alien2.hideturtle()
            self.alien2.speed(0)
            self.alien2.penup()
            self.alien2.color("red")
            self.alien2.setposition(-225 + x_pos2, 320)
            self.alien2.showturtle()
            self.alien_list_layer2.append(self.alien2)



        x_pos1 = 0
        for n in range(8):
            x_pos1 += 50
            self.alien1 = Turtle(shape="turtle")
            self.alien1.setheading(270)
            self.alien1.hideturtle()
            self.alien1.speed(0)
            self.alien1.penup()
            self.alien1.color("green")
            self.alien1.setposition(-225 + x_pos1, 290)
            self.alien1.showturtle()
            self.alien_list_layer1.append(self.alien1)



    def move_to_right(self):
        for self.a3 in self.alien_list_layer3:
            n_x = self.a3.xcor() + self.x_move_main
            self.a3.goto(n_x, self.a3.ycor())

        for self.a2 in self.alien_list_layer2:
            n_x = self.a2.xcor() + self.x_move_main
            self.a2.goto(n_x, self.a2.ycor())

        for self.a1 in self.alien_list_layer1:
            n_x = self.a1.xcor() + self.x_move_main
            self.a1.goto(n_x, self.a1.ycor())

    def move_to_left(self):
        for self.a3 in self.alien_list_layer3:
            n_x = self.a3.xcor() + self.x_move_main
            self.a3.goto(n_x, self.a3.ycor())

        for self.a2 in self.alien_list_layer2:
            n_x = self.a2.xcor() + self.x_move_main
            self.a2.goto(n_x, self.a2.ycor())

        for self.a1 in self.alien_list_layer1:
            n_x = self.a1.xcor() + self.x_move_main
            self.a1.goto(n_x, self.a1.ycor())

    def alien_kill(self,index):
        if index in self.alien_list_layer1:
            self.hits += 1
            index.ht()
            self.alien_list_layer1.remove(index)

        if index in self.alien_list_layer2:
            self.hits += 1
            index.ht()
            self.alien_list_layer2.remove(index)

        if index in self.alien_list_layer3:
            self.hits += 1
            index.ht()
            self.alien_list_layer3.remove(index)

    def create_alien_missile(self):
        f = random.randint(1, 25)
        # print(f)
        if f == 1:
            pos_list = [i.pos() for i in self.alien_list_layer1]
            pos_list2 = [i2.pos() for i2 in self.alien_list_layer2]
            pos_list3 = [i3.pos() for i3 in self.alien_list_layer3]
            all_aliens_pos = pos_list + pos_list2 + pos_list3
            try:
                fire_pos = random.choice(all_aliens_pos)
            except IndexError:
                print("Gameover")
            else:
                fire_pos = random.choice(all_aliens_pos)

                self.missile = Turtle()
                self.missile.shape("arrow")
                self.missile.setheading(270)

                self.missile.setposition(fire_pos)
                self.missile.penup()
                self.missile.fillcolor("red")
                self.missile.st()
                self.missile.y_move = 10
                self.missile_list.append(self.missile)

                print(self.missile_list)

    def get_position(self):
        pos_list = [i.pos() for i in self.alien_list_layer1]
        fire_pos = random.choice(pos_list)
        return fire_pos
        # print(pos_list)
        # print(random.choice(pos_list))

    def fire_alien_missle(self):
        for self.m1 in self.missile_list:
            n_y = self.m1.ycor() - self.m1.y_move
            self.m1.goto(self.m1.xcor(), n_y)

    def missle_collide(self,index):
        if index in self.missile_list:
            index.ht()
            self.missile_list.remove(index)

    def missile_barricade_collide(self,index):
        if index in self.missile_list:
            index.ht()
            self.missile_list.remove(index)

