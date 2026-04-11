import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

sattelites = []
lines = []

next_sattelite = 0

start_time = 0
end_time = 0
total_time = 0

number_of_sattelites = 8

def create_sattelites():
    global start_time
    for count in range(0,number_of_sattelites):
        sattelite = Actor("satellite")
        sattelite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        sattelites.append(sattelite)
    start_time = time()

def draw():
    global total_time
    screen.blit("background", (0,0))
    number = 1
    for sattelite in sattelites:
        sattelite.draw()
        screen.draw.text(
            str(number),
            center = (sattelite.x, sattelite.y +50),
            fontsize = 35,
            color = "yellow",
            owidth = 1.5,
            ocolor = "black"
        )
        number = number + 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_sattelite < number_of_sattelites:
        total_time = time() - start_time

    screen.draw.text(
        str(round(total_time, 1)),
        (10,10),
        fontsize = 40,
        color = "cyan",
        owidth = 1.5,
        ocolor = "black"
    )

def update():
    pass

def on_mouse_down(pos):
    global next_sattelite, lines 
    if next_sattelite < number_of_sattelites:
        if sattelites[next_sattelite].collidepoint(pos):
            if next_sattelite:
                lines.append((
                    sattelites[next_sattelite - 1].pos,
                    sattelites[next_sattelite].pos
                ))
            next_sattelite = next_sattelite + 1
    else:
        lines = []
        next_sattelite = 0
        create_sattelites()

create_sattelites()
pgzrun.go()