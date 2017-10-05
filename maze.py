import turtle
import math
from time import *
import pygame

pygame.mixer.init()
pygame.mixer.music.load("./Music/SoundTest.wav")
pygame.mixer.music.play(-1)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Zombie head adventure")
wn.setup(700,700)
wn.tracer(0)
wn.bgpic("./image/giphy.gif")

class  Pen(turtle.Turtle):
        def  __init__(self):
                turtle.Turtle.__init__(self)
                v=self.getscreen()
                v.register_shape("./image/block.gif")
                self.shape("./image/block.gif")
                self.color("white")
                self.penup()
                self.speed(0)

class Player(turtle.Turtle):
        def __init__(self):
                turtle.Turtle.__init__(self)
                v=self.getscreen()
                v.register_shape("./image/zombie.gif")
                self.shape("./image/zombie.gif")
                self.color("blue")
                self.penup()
                self.speed(0)
                self.gold = 0

        def go_up(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24

                if (move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x, move_to_y)

        def go_down(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24

                if (move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x, move_to_y)

        def go_left(self):
                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()

                if (move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x, move_to_y)

        def go_right(self):
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()

                if (move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x, move_to_y)

        def is_collision(self, other):
                a = self.xcor()-other.xcor()
                b = self.ycor()-other.ycor()
                distance = math.sqrt((a**2)+(b**2))

                if distance < 5:
                        return True
                else:
                        return False

class Treasure(turtle.Turtle):
        def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                v=self.getscreen()
                v.register_shape("./image/treasure.gif")
                self.shape("./image/treasure.gif")
                self.color("gold")
                self.penup()
                self.speed(0)
                self.gold = 100
                self.goto(x,y)

        def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

class Enemy(turtle.Turtle):
        def __init__(self,x,y):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("purple")
                self.penup()
                self.speed(0)
                self.gold = 25
                self.goto(x, y)
                self.direction= random.choice(["up","down","left","right"])

        def move(self):
                if self.direction =="up":
                        dx = 0
                        dy= 24
                elif self.direction =="down":
                        dx = 0
                        dy = -24
                elif self.direction =="right":
                        dx = -24
                        dy = 0
                elif self.direction == "left":
                        dx= 24
                        dy= 0
                else:
                        dx = 0
                        dy = 0

                move_to_x = self.xcor() + dx
                move_to_y = self.ycor() +dy

                if(move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x,move_to_y)
                else:
                        self.direction = random.choice()["up","down","left","right"]

                turtle.ontimer(self.move, t=random.randint (100,300))

        def destroy(self):
                self.goto(2000,2000)
                self.hideturtle()

level = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX   TXXX     X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX             TX",
"XX T XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

treasures = []

level.append(level_1)

def setup_maze(level):
        for y in range(len(level)):
                for x in range(len(level[y])):
                        character = level[y][x]
                        screen_x = -288 + (x *24)
                        screen_y = 288 - (y * 24)

                        if character =="X":
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                walls.append((screen_x, screen_y))
                        elif character=="P":
                                player.goto(screen_x, screen_y)
                        elif character =="T":
                                treasures.append(Treasure(screen_x,screen_y))

def Starttime():
        treasure.destroy()
        treasures.remove(treasure)
        wn.update()

        pygame.mixer.music.load("./Music/Gameover.wav")
        pygame.mixer.music.play(4)


        start_timer = time()

        struct = localtime(start_timer)

        print("\nRespawn in 20 seconds",strftime("%X",struct))

        i = 20        
        while i> -1:
                print(i)
                i-=1
                sleep(1)
                wn.update()
        end_timer = time()

        pygame.mixer.music.load("./Music/SoundTest.wav")
        pygame.mixer.music.play()

        

pen= Pen()
player = Player()

walls = []

setup_maze(level[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

while True:
        for treasure in treasures:
                if player.is_collision(treasure):
                        player.gold += treasure.gold
                        if player.gold == 100:
                                print("haha it's a fake gold,into laggy mode muahhahahahah,dont worry it'll end after count down")
                                Starttime()
                        else:
                                print("Player Gold:{}".format(player.gold))
                                treasure.destroy()
                                treasures.remove(treasure)
                                wn.update()

                wn.update()
