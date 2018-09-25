import turtle
import math
import random
import os
import sys
import time
import threading
import winsound


# TODO: enemy explosion animate without halting rest of program
# TODO: levels cleanup
# TODO: bullet speed
# TODO: enemy shoot
# TODO: hold down move

def mainfullloop(mylevel,myscore):

    # set up screen
    wn = turtle.Screen()
    wn.setup( width = 600, height = 600, startx = 100, starty = 0)
    wn.bgcolor("black")
    wn.title("Space Invaders")
    wn.bgpic("space_invaders_background.gif")

    # register the shapes
    turtle.register_shape("invader.gif")
    turtle.register_shape("ship.gif")
    turtle.register_shape("explosion1o4.gif")
    turtle.register_shape("explosion2o4.gif")
    turtle.register_shape("explosion3o4.gif")
    turtle.register_shape("explosion4o4.gif")
    turtle.register_shape("bullet.gif")
    turtle.register_shape("enemybullet.gif")
    turtle.register_shape("shipx32.gif")
    turtle.register_shape("bulletspace.gif")
    turtle.register_shape("enemygif.gif")
    turtle.register_shape("mothership.gif")
    turtle.register_shape("defense.gif")

    # draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
    	border_pen.fd(600)
    	border_pen.lt(90)
    border_pen.hideturtle()

    # set the score to 0
    try:
        score = myscore
    except ValueError:
        score = 0


    # draw the score
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290,280)
    scorestring = "Score: " + str(score) + "  Level: " + str(mylevel) + ""
    score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    # draw the score
    center_pen = turtle.Turtle()
    center_pen.speed(0)
    center_pen.hideturtle()

    # create player Turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("shipx32.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    playerspeed = 18

    global killcount
    global brokenout
    brokenout = False
    killcount = 0

    # choose number of enemies
    # number_of_enemies = level * 10
    if mylevel == 1:
        number_of_enemies = 1
    else:
        number_of_enemies = mylevel * 10

    # create an empty list of enemies
    enemies = []

    global totalenemies
    totalenemies = number_of_enemies

    for i in range(number_of_enemies):
        # create the enemy
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("red")
        enemy.shape("enemygif.gif")
        enemy.penup()
        enemy.speed(0)
        enemy.shapesize(stretch_wid=1.5,stretch_len=1.5)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)

    enemyspeed = 2

    # create player  bullet
    bullet = turtle.Turtle()
    bullet.color("white")
    bullet.shape("bulletspace.gif")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    # create player  bullet
    enemybullet = turtle.Turtle()
    enemybullet.color("white")
    enemybullet.shape("bulletspace.gif")
    enemybullet.penup()
    enemybullet.speed(0)
    enemybullet.setheading(90)
    enemybullet.shapesize(0.5, 0.5)
    enemybullet.hideturtle()

    enemybullet2 = turtle.Turtle()
    enemybullet3 = turtle.Turtle()
    enemybullet4 = turtle.Turtle()
    enemybullet5 = turtle.Turtle()
    enemybullet6 = turtle.Turtle()


    # create player  bullet
    defense1 = turtle.Turtle()
    defense1.color("orange")
    defense1.shape("defense.gif")
    defense1.penup()
    defense1.speed(0)
    defense1.setheading(90)
    # defense1.shapesize(5, 0.5)
    defense1.hideturtle()
    enemy.shapesize(stretch_wid=2.5,stretch_len=2.5)
    x = random.randint(-200,200)
    defense1.setposition(x,-200)
    defense1.showturtle()

    # create player  bullet
    defense2 = turtle.Turtle()
    defense2.color("orange")
    defense2.shape("defense.gif")
    defense2.penup()
    defense2.speed(0)
    defense2.setheading(90)
    # defense1.shapesize(5, 0.5)
    defense2.hideturtle()
    enemy.shapesize(stretch_wid=2.5,stretch_len=2.5)
    x = random.randint(-200,200)
    defense2.setposition(x,-150)
    defense2.showturtle()

    # create player  bullet
    defense3 = turtle.Turtle()
    defense3.color("orange")
    defense3.shape("defense.gif")
    defense3.penup()
    defense3.speed(0)
    defense3.setheading(90)
    # defense1.shapesize(5, 0.5)
    defense3.hideturtle()
    enemy.shapesize(stretch_wid=2.5,stretch_len=2.5)
    x = random.randint(-200,-100)
    defense3.setposition(x,0)
    defense3.showturtle()

    # create player  bullet
    defense4 = turtle.Turtle()
    defense4.color("orange")
    defense4.shape("defense.gif")
    defense4.penup()
    defense4.speed(0)
    defense4.setheading(90)
    # defense1.shapesize(5, 0.5)
    defense4.hideturtle()
    enemy.shapesize(stretch_wid=2.5,stretch_len=2.5)
    x = player.xcor()
    defense4.setposition(x,-200)
    defense4.showturtle()

    global bulletspeed
    global enemybulletspeed
    enemybulletspeed = 30
    bulletspeed = 80

    # define bullet state
    # ready - ready to fire
    # fire - bullet is firing
    global bulletstate
    global enemybulletstate
    global enemybulletstate2
    global enemybulletstate3
    global enemybulletstate4
    global enemybulletstate5
    global enemybulletstate6
    bulletstate = "ready"
    enemybulletstate = "ready"
    enemybulletstate2 = "ready"
    enemybulletstate3 = "ready"
    enemybulletstate4 = "ready"
    enemybulletstate5 = "ready"
    enemybulletstate6 = "ready"


    # move player left and right
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)

    def move_up():
        y = player.ycor()
        y += playerspeed * 0.55
        # if y < 5:
        #     y= 5
        player.sety(y)

    def move_down():
        y = player.ycor()
        y -= playerspeed * 0.55
        # if y > 50:
        #     y= 50
        player.sety(y)

    def move_NE():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)
        y = player.ycor()
        y += playerspeed * 0.55
        # if y < 5:
        #     y= 5
        player.sety(y)

    def move_NW():
        y = player.ycor()
        y += playerspeed * 0.55
        # if y < 5:
        #     y= 5
        player.sety(y)
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)

    def move_SW():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)
        y = player.ycor()
        y -= playerspeed * 0.55
        # if y > 50:
        #     y= 50
        player.sety(y)

    def move_SE():
        y = player.ycor()
        y -= playerspeed * 0.55
        # if y > 50:
        #     y= 50
        player.sety(y)
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)


    def fire_bullet():
        # declare bulletstate as a global if it needs changed
        global bulletstate
        if bulletstate == "ready":
            winsound.PlaySound("laser", winsound.SND_ASYNC)
            bulletstate = "fire"
            # move bullet to just above player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x,y)
            bullet.showturtle()


    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 30:
            return True
        else:
            return False

    def isCollision2(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 30:
            return True
        else:
            return False

    def isCollision3(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 70:
            return True
        else:
            return False

    def playerExplode():
        player.shape("explosion1o4.gif")
        time.sleep(0.1)
        player.shape("explosion2o4.gif")
        time.sleep(0.1)
        player.shape("explosion3o4.gif")
        time.sleep(0.1)
        player.shape("explosion4o4.gif")
        enemy.penup()

    def resetEnemy(enemy):
        # reset enemy
        enemy.shape("invader.gif")
        enemy.penup()
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)

    def escape():
        exit(0)



    # create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_up, "Up")
    turtle.onkey(move_down, "Down")
    turtle.onkey(escape, "Escape")
    turtle.onkey(fire_bullet, "space")




    # main game loop
    while True:

        if enemybulletstate == "fire":
            #print("already firing!")
            None
        if enemybulletstate == "ready" or enemybulletstate == "fire" :
            #print("not firing right now")
            for z in enemies:
                enemyrand = random.randint(0,10)
                if enemyrand >= 1 and enemyrand <= 100:

                    #print("firing now!")
                    # enemybulletstate = "fire"
                    ##winsound.PlaySound("laser", winsound.SND_ASYNC)
                    for enemy in enemies:
                        for j in range(random.randint(0,totalenemies)):
                            x = enemy.xcor()
                            y = enemy.ycor() - 10

                    enemyrand2 = random.randint(1,len(enemies))
                    if enemyrand2 == 1:
                        if enemybulletstate == "ready":
                            enemybulletstate = "fire"
                            enemybullet.setposition(x,y)
                            enemybullet.showturtle()
                        else:
                            None
                    elif enemyrand2 == 2:
                        if enemybulletstate2 == "ready":
                            enemybulletstate2 = "fire"
                            enemybullet2 = enemybullet.clone()
                            enemybullet2.setposition(x,y)
                            enemybullet2.showturtle()
                        else:
                            None
                    elif enemyrand2 == 3:
                        if enemybulletstate3 == "ready":
                            enemybulletstate3 = "fire"
                            enemybullet3 = enemybullet.clone()
                            enemybullet3.setposition(x,y)
                            enemybullet3.showturtle()
                        else:
                            None
                    elif enemyrand2 == 4:
                        if enemybulletstate4 == "ready":
                            enemybulletstate4 = "fire"
                            enemybullet4 = enemybullet.clone()
                            enemybullet4.setposition(x,y)
                            enemybullet4.showturtle()
                        else:
                            None
                    elif enemyrand2 == 5:
                        if enemybulletstate5 == "ready":
                            enemybulletstate5 = "fire"
                            enemybullet5 = enemybullet.clone()
                            enemybullet5.setposition(x,y)
                            enemybullet5.showturtle()
                        else:
                            None
                    elif enemyrand2 == 6:
                        if enemybulletstate6 == "ready":
                            enemybulletstate6 = "fire"
                            enemybullet6 = enemybullet.clone()
                            enemybullet6.setposition(x,y)
                            enemybullet6.showturtle()
                        else:
                            None
                    else:
                        None
                    #print("enemy shoot = yes")
                    break
                else:
                    #print("no shooter")
                    None







        if bulletstate == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = bullet.ycor()
            y = y + bulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            bullet.sety(y)


        if enemybulletstate == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet.sety(y)
        if enemybulletstate2 == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet2.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet2.sety(y)
        if enemybulletstate3 == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet3.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet3.sety(y)
        if enemybulletstate4 == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet4.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet4.sety(y)
        if enemybulletstate5 == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet5.sety(y)
        if enemybulletstate6 == "fire":
            #print("bullet 1 is firing")
            # bullet.showturtle()
            # bullet2state = "ready"
            y = enemybullet6.ycor()
            y = y - enemybulletspeed
            #print("bullet1speed: " + str(bulletspeed))
            #print("y: " + y)
            enemybullet6.sety(y)


        for enemy in enemies:
            # move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            # #Move the enemy
    		# x = enemy.xcor()
    		# x += enemyspeed
    		# enemy.setx(x)

            if enemy.xcor() > 280 and enemy.xcor() < 666666:
                print("down1 out")
                #Move all enemies down
                for e in enemies:
                    print("down1 in")
                    y = e.ycor()
                    x = e.xcor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1
                print("kinda in fall")
                for z in range(4):
                    print("infall")
                    y -=40
                    x -=random.randint(0,5)
                    enemy.sety(y)
                    enemy.setx(x)
            if enemy.xcor() < -280 and enemy.xcor() > -444444:
                print("down2 out")
                #Move all enemies down
                for e in enemies:
                    print("down2 in")
                    y = e.ycor()
                    x = e.xcor()
                    y -= 40
                    e.sety(y)
                print("kinda in fall")
                for z in range(4):
                    print("infall")
                    y -=40
                    x -=random.randint(-5,0)
                    enemy.sety(y)
                    enemy.setx(x)
                #Change enemy direction
                enemyspeed *= -1

            # check for collision between bullet and enemy
            if isCollision(bullet, enemy):
                #print("bullet1")
                print(*enemies,sep=', ')
                winsound.PlaySound("explosion", winsound.SND_ASYNC)
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)

                # kill enemy
                killcount = killcount + 1
                enemy.shapesize(stretch_wid=-100,stretch_len=-100)
                enemy.clear()
                enemy.hideturtle()

                enemy.setx(7777777)


                # update score
                score += 10
                scorestring = "Score: " + str(score) + "  Level: " + str(mylevel) + ""
                score_pen.clear()
                score_pen.hideturtle()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                if killcount == totalenemies:
                     print("You Win!")
                     print("total enemies: " + str(totalenemies))
                     time.sleep(3)
                     # FIXME: eliminate useless code from here
                     print("turtles: " + str(wn.turtles()))
                     wn._delete(all)
                     print("turtles: " + str(wn.turtles()))
                     wn.clearscreen
                     print("turtles: " + str(wn.turtles()))
                     mylevel = mylevel + 1
                     enemies.clear()
                     score_pen.clear()
                     score_pen.hideturtle()
                     mainfullloop(mylevel,score)


            if isCollision2(player, enemy) or isCollision2(enemybullet, player) or isCollision2(enemybullet2, player) or isCollision2(enemybullet3, player) or isCollision2(enemybullet4, player) or isCollision2(enemybullet5, player) or isCollision2(enemybullet6, player):
                playerExplode()
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break

            if isCollision2(defense1, enemybullet) or isCollision2(defense2, enemybullet) or isCollision2(defense3, enemybullet) or isCollision2(defense4, enemybullet):
                enemybullet.hideturtle()
                enemybulletstate = "ready"
                enemybullet.setposition(0,-400)

            if isCollision2(defense1, enemybullet2) or isCollision2(defense2, enemybullet2) or isCollision2(defense3, enemybullet2) or isCollision2(defense4, enemybullet2):
                enemybullet2.hideturtle()
                enemybulletstate = "ready"
                enemybullet2.setposition(0,-400)

            if isCollision2(defense1, enemybullet3) or isCollision2(defense2, enemybullet3) or isCollision2(defense3, enemybullet3) or isCollision2(defense4, enemybullet3):
                enemybullet3.hideturtle()
                enemybulletstate = "ready"
                enemybullet3.setposition(0,-400)

            if isCollision2(defense1, enemybullet4) or isCollision2(defense2, enemybullet4) or isCollision2(defense3, enemybullet4) or isCollision2(defense4, enemybullet4):
                enemybullet4.hideturtle()
                enemybulletstate = "ready"
                enemybullet4.setposition(0,-400)

            if isCollision2(defense1, enemybullet5) or isCollision2(defense2, enemybullet5) or isCollision2(defense3, enemybullet5) or isCollision2(defense4, enemybullet5):
                enemybullet5.hideturtle()
                enemybulletstate = "ready"
                enemybullet5.setposition(0,-400)

            if isCollision2(defense1, enemybullet6) or isCollision2(defense2, enemybullet6) or isCollision2(defense3, enemybullet6) or isCollision2(defense4, enemybullet6):
                enemybullet6.hideturtle()
                enemybulletstate = "ready"
                enemybullet6.setposition(0,-400)

            if isCollision3(defense1, bullet) or isCollision2(defense2, bullet) or isCollision2(defense3, bullet) or isCollision2(defense4, bullet):
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)

            # if isCollision3(defense1, player) or isCollision2(defense2, player) or isCollision2(defense3, player) or isCollision2(defense4, player):
            #     bullet.hideturtle()
            #     bulletstate = "ready"
            #     bullet.setposition(0,-400)



        # check to see if the bullet has gone to the top
        if bullet.ycor() > 280:
            #bullet.hideturtle()
            bulletstate = "ready"
            #bullet.reset()
            bullet.setposition(0,-400)
        if enemybullet.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate = "ready"
            #bullet.reset()
            enemybullet.setposition(0,-400)
        if enemybullet2.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate2 = "ready"
            #bullet.reset()
            enemybullet2.setposition(0,-400)
        if enemybullet3.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate3= "ready"
            #bullet.reset()
            enemybullet3.setposition(0,-400)
        if enemybullet4.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate = "ready"
            #bullet.reset()
            enemybullet4.setposition(0,-400)
        if enemybullet5.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate4 = "ready"
            #bullet.reset()
            enemybullet5.setposition(0,-400)
        if enemybullet6.ycor() < -300:

            #bullet.hideturtle()
            enemybulletstate5 = "ready"
            #bullet.reset()
            enemybullet6.setposition(0,-400)





    wn.mainloop()


mainfullloop(1,0)
