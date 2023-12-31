import time
from turtle import *
from defender import Defender
from aliens import Aliens
from barricade import Barricade
from score import Scoreboard
import keyboard

#Create Screen
screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

space_defender = Defender()
alien_invaders = Aliens()
barricade_wall = Barricade()
scoreboard = Scoreboard()

alien_invaders.create_aliens()
barricade_wall.create_barricade()

#Defender movement, left and right
screen.listen()
screen.onkeypress(space_defender.move_left, "a")
screen.onkeypress(space_defender.move_right, "d")
screen.onkeypress(space_defender.fire_laserbeam, "space")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    #Auto cannon, auto fire laser
    space_defender.fire_laserbeam()

    #Movement to right of aliens
    alien_invaders.move_to_right()

    #Fire missiles/laser from aliens
    alien_invaders.create_alien_missile()
    alien_invaders.fire_alien_missle()

    # Laser reload/reset
    if space_defender.laser.ycor() > 380:
        space_defender.reload()
        print("Reload")

    # Aliens right wall collision
    # Aliens left wall collision
    for c3 in alien_invaders.alien_list_layer3:
        if c3.xcor() > 380:
            alien_invaders.x_move_main = -5
            alien_invaders.move_to_left()

        if c3.xcor() < -380:
            alien_invaders.x_move_main = 5
            alien_invaders.move_to_right()

    for c2 in alien_invaders.alien_list_layer2:
        if c2.xcor() > 380:
            alien_invaders.x_move_main = -5
            alien_invaders.move_to_left()

        if c2.xcor() < -380:
            alien_invaders.x_move_main = 5
            alien_invaders.move_to_right()

    for c1 in alien_invaders.alien_list_layer1:
        if c1.xcor() > 380:
            alien_invaders.x_move_main = -5
            alien_invaders.move_to_left()

        if c1.xcor() < -380:
            alien_invaders.x_move_main = 5
            alien_invaders.move_to_right()


    #Laser collision to aliens
    for alien1 in alien_invaders.alien_list_layer1:
        if space_defender.laser.distance(alien1) < 30 and space_defender.laser.ycor() >= 290:
            alien_invaders.alien_kill(alien1)
            space_defender.reload()
            scoreboard.add_point_update(1)
            print("hit")
            print(alien_invaders.alien_list_layer1)
            print(alien_invaders.hits)

    for alien2 in alien_invaders.alien_list_layer2:
        if space_defender.laser.distance(alien2) < 30 and space_defender.laser.ycor() >= 320:
            alien_invaders.alien_kill(alien2)
            space_defender.reload()
            scoreboard.add_point_update(1)
            print("hit")
            print(alien_invaders.alien_list_layer2)
            print(alien_invaders.hits)

    for alien3 in alien_invaders.alien_list_layer3:
        if space_defender.laser.distance(alien3) < 30 and space_defender.laser.ycor() >= 350:
            alien_invaders.alien_kill(alien3)
            space_defender.reload()
            scoreboard.add_point_update(1)
            print("hit")
            print(alien_invaders.alien_list_layer3)
            print(alien_invaders.hits)

    #Laser collision to alien missle
    for msl in alien_invaders.missile_list:
        if space_defender.laser.distance(msl) < 25:
            alien_invaders.missle_collide(msl)
            space_defender.reload()
            print("laser colide to alien missle")

    #Alien missile collision to spaceship
        if msl.distance(space_defender) < 10:
            space_defender.destroy_reset()
            print("destroyed ship")

    #Space laser collision to barricade
    for wl1 in barricade_wall.bar1:
        if space_defender.laser.distance(wl1) < 20:
            barricade_wall.destroy_barricade(wl1)
            print("destroy barricade")

        for msl_test in alien_invaders.missile_list:
            if msl_test.distance(wl1) < 20:
                barricade_wall.destroy_barricade(wl1)
                print("destroy barricade by alien")


    for wl2 in barricade_wall.bar2:
        if space_defender.laser.distance(wl2) < 20:
            barricade_wall.destroy_barricade(wl2)
            print("destroy barricade")

        for msl_test in alien_invaders.missile_list:
            if msl_test.distance(wl2) < 20:
                barricade_wall.destroy_barricade(wl2)
                print("destroy barricade by alien")

    #Gameover condition
    if alien_invaders.alien_list_layer3 == [] and alien_invaders.alien_list_layer2 == [] and alien_invaders.alien_list_layer1 == []:
        scoreboard.gameover()



#TODO: Laser beam, when space is pressed fires laser continuously, recheck loop - Almost done, new concept continuous laserbeam, ####MODIFY laser, setposition and goto, fire using space####
#TODO: Aliens - turtle,position,collision same as breakout game - Done
#TODO Firebeams from aliens(random firing order) - Done
#TODO: Barricades - Done
#TODO: Collisions(laser to missile, missile to ship, barricades to laser and missile) - Done
#TODO: For future updating, spaceship lives, manual firing, speed increment for aliens

































screen.exitonclick()
