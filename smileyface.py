import pgzrun


WIDTH = 1000
HEIGHT = 1000

def draw():
    screen.draw.circle((500,450),300,"white")
    screen.draw.circle((400,350),50,"white")
    screen.draw.circle((600,350),50,"white")
    screen.draw.line((400,550),(600,550),"white")
    screen.draw.line((400,550),(300,500),"white")
    screen.draw.line((600,550),(700,500),"white")


pgzrun.go()