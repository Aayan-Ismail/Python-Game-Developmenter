import pgzrun
from random import randint
TITLE = "EASY GAME"
WIDTH = 500
HEIGHT = 500
message = ""
score = 0
game_over = False
evil_character_who_i_hate = Actor('pixelatedtamsy.png')
def draw():
    screen.clear()
    screen.fill((128,0,0))
    if game_over:
        screen.draw.text(
            "game OVER, how did you mess up on such an easy game man please lock in next time",
            center = (WIDTH//2, HEIGHT//2),
            fontsize = 60,
            color = "white"
            
        )
        screen.draw.text(
            f"final score: {score}",
            center = (WIDTH//2, HEIGHT//2 + 50),
            fontsize = 40,
            color = "white"
        )
    else:
        evil_character_who_i_hate.draw()
        screen.draw.text(
            message,
            center = (400,20),
            fontsize = 30,
            color = "black"
        )
        screen.draw.text(
            f"score: {score}",
            topleft = (10,10),
            fontsize = 30,
            color = "black"

        )
def place_actor():
    evil_character_who_i_hate.x = randint(50,WIDTH - 50)
    evil_character_who_i_hate.y = randint(50,HEIGHT - 50)

def end_game():
    quit()

def on_mouse_down(pos):
    global message, score, game_over
    if game_over:
        return
    if evil_character_who_i_hate.collidepoint(pos):
        