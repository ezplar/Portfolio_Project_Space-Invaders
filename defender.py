from turtle import Turtle

LEFT = 180
RIGHT = 0

class Defender(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("arrow")
        self.ht()
        self.goto((0, -300))
        self.penup()
        self.color("white")
        self.st()
        # self.ship_main()
        # self.laser_beam()
        # self.ss = self.spaceship[0]
        # self.ln = self.spaceship[1]
        # print(self.spaceship)
        # self.laser = Turtle()
        # self.laser.setheading(90)
        # self.laser.goto((0, -300))
        # self.laser.penup()
        # self.laser.fillcolor("red")
        # self.laser.st()
        # self.ship_main()
        self.laser_beam()



    def move_left(self):
        n_x = self.xcor() - 20
        self.goto(n_x,self.ycor())
        self.laser.goto(n_x,self.ycor())

    def move_right(self):
        n_x = self.xcor() + 20
        self.goto(n_x,self.ycor())
        self.laser.goto(n_x, self.ycor())

    # def ship_main(self):
    #     self.ship = Turtle()
    #     self.ship.setheading(90)
    #     self.ship.shape("arrow")
    #     self.ship.ht()
    #     self.ship.goto((0, -300))
    #     self.ship.penup()
    #     self.ship.color("white")
    #     self.ship.st()
    #     self.spaceship.append(self.ship)

    def laser_beam(self):
        self.laser = Turtle()
        self.laser.setheading(90)
        self.laser.setposition((0, -300))
        self.laser.penup()
        self.laser.fillcolor("red")
        self.laser.st()
        self.laser.y_move = 20

        # n_y = laser.ycor() + laser.y_move
        # laser.goto(self.xcor(), n_y)

    def fire_laserbeam(self):
        n_y = self.laser.ycor() + self.laser.y_move
        self.laser.goto(self.laser.xcor(), n_y)

    def reload(self):
        self.laser.goto(self.xcor(), self.ycor())

    def destroy_reset(self):
        self.goto((0, -300))
        self.reload()






