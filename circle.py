import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
def draw():
    r = randint(25,100)
    g = 0
    b = 255
    center = (250,250)
    radius = 60
    for i in range(18):
        screen.draw.circle(center, radius,  (r,g,b))
        radius += 10
        r += 10
        b -= 10



pgzrun.go()