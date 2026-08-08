import pgzrun
import random

WIDTH = 500
HEIGHT = 750

ROWS = 6
COLS = 5
TILE_SIZE = 60
GAP = 8

BG = (18,18,19)
EMPTY = (58,58,60)
GREEN = (83,141,78)
YELLOW = (181,159,59)
GRAY = (120,124,126)
DARK_GRAY = (80,80,80)
WHITE = (255,255,255)
BUTTON = (70,130,180)

words = [
    # A
    "abode", "about", "above", "actor", "adult",
    # B
    "basic", "beach", "brain", "brave", "bread",
    # C
    "cable", "catch", "chair", "chaos", "clean",
    # D
    "dance", "delta", "demon", "depth", "draft",
    # E
    "eager", "early", "earth", "elbow", "entry",
    # F
    "faith", "flame", "flash", "focus", "frame",
    # G
    "ghost", "giant", "glass", "globe", "grace",
    # H
    "habit", "happy", "heart", "heavy", "house",
    # I
    "ideal", "image", "index", "inner", "input",
    # J
    "jaunt", "jazzy", "jelly", "jewel", "judge",
    # K
    "karma", "kayak", "knife", "knock", "koala",
    # L
    "label", "laser", "lemon", "light", "logic",
    # M
    "magic", "major", "match", "media", "music",
    # N
    "nerve", "night", "ninja", "noble", "ocean",
    # O
    "offer", "often", "olive", "order", "other",
    # P
    "paper", "party", "pause", "peace", "phone",
    # Q
    "quake", "queen", "query", "quest", "quick",
    # R
    "radar", "radio", "reach", "relax", "river",
    # S
    "scale", "scene", "scope", "share", "smart",
    # T
    "table", "taste", "tiger", "title", "train",
    # U
    "uncle", "under", "unify", "union", "urban",
    # V
    "vague", "valid", "value", "video", "voice",
    # W
    "water", "wheel", "where", "world", "write",
    # Y
    "yacht", "yearn", "yeast", "yield", "young"
]
game_state = "start"

def init_game():
    global grid,colors,current_row,current_col
    global secret_word, message, key_colors

    grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
    colors = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    current_row = 0
    current_col = 0
    secret_word = random.choice(words)
    message = ""
    key_colors = {}

init_game()

start_button = Rect((150,300), (200,60))
play_again_button = Rect((150,680),(200,50))

keyboard_layout = [list("QWERTYUIOP"),
                   list("ASDFGHJKL"),
                   ["ENTER"] + list("ZXCVNM") + ["BACK"]
]

key_rects = []

def create_keyboard():
    key_rects.clear()
    y_start = 500

    for row_index, row in enumerate(keyboard_layout):
        key_widths = []
        for key in row:
            if key in ["ENTER","BACK"]:
                key_widths.append(65)
            else:
                key_widths.append(40)
        total_width = sum(key_widths) + (len(row) - 1)*5
        x_start = (WIDTH - total_width)//2

        x = x_start
        for key, width in zip(row, key_widths):
            rect = Rect((x, y_start + row_index*55),(width,45))
            key_rects.append((rect,key))
            x += width + 5

create_keyboard()

def draw():
    screen.fill(BG)

    if game_state == "start":
        screen.draw.text("WORDLE", center=(WIDTH//2,200), fontsize = 60, color = WHITE)
        screen.draw.filled_rect(start_button,BUTTON)
        screen.draw.text("START", center=start_button.center, fontsize = 35, color = WHITE) 

    else:
        grid_width = COLS * TILE_SIZE + (COLS - 1) * GAP 
        x_start = (WIDTH - grid_width) // 2           
        for r in range(ROWS):
            for c in range(COLS):
                x = x_start + c * (TILE_SIZE + GAP)
                y = 80 + r * (TILE_SIZE + GAP)

                rect = Rect((x,y), (TILE_SIZE, TILE_SIZE))
                screen.draw.filled_rect(rect, colors[r][c])
                if grid[r][c]:
                    screen.draw.text(
                        grid[r][c],
                        center = rect.center,
                        fontsize = 35,
                        color = WHITE
                    )
            
        screen.draw.text("WORLDE", center = (WIDTH//2,30), fontsize = 50, color = WHITE)
        screen.draw.text(message, center = (WIDTH//2, 460), fontsize = 30, color = WHITE)

        for rect,key in key_rects:
            color = key_colors.get(key,GRAY)
            screen.draw.filled_rect(rect, color)
            screen.draw.text(key, center=rect.center, fontsize = 18, color = WHITE)
            
        if game_state == "gameover":
            screen.draw.filled_rect(play_again_button, BUTTON)
            screen.draw.text("PLAY AGAIN, center = play_again_button.center, fontsize = 25, color = WHITE")
            
            

def on_mouse_down(pos):
    global game_state
            
    if game_state == "start":
        if start_button.collidepoint(pos):
            init_game()
            game_state = "playing"
            
    elif game_state in ["playing", "gameover"]:
        for rect,key in key_rects:
            if rect.collidepoint(pos):
                handle_key(key)
                
        if game_state == "gameover":
            if play_again_button.collidepoint(pos):
                init_game()
                game_state = "playing"

def handle_key(key):
    global current_col, current_row

    if game_state != "playing":
        return
    
    if key == "ENTER":
        if current_col == COLS:
            check_word()
    
    elif key == "BACK":
        if current_col > 0:
            current_col -= 1
            grid[current_row][current_col] = ""
    
    else:
        if current_col < COLS:
            grid[current_row][current_col] = key
            current_col += 1

def update_key_color(letter,color):
    current = key_colors.get(letter)

    if current == GREEN:
        return
    if current == YELLOW and color == DARK_GRAY:
        return
    
    key_colors[letter] = color

def check_word():
    global current_row, current_col, game_state, message

    guess = "".join(grid[current_row])
    secret_list = list(secret_word)

    for i in range(COLS):
        if guess[i] == secret_word[i]:
            colors[current_row][i] = GREEN
            secret_list[i] = None
            update_key_color(guess[i], GREEN)
    
    for i in range(COLS):
        if colors[current_row][i] != GREEN:
            if guess[i] in secret_list:
                colors[current_row][i] = YELLOW
                secret_list[secret_list.index(guess[i])] = None
                update_key_color(guess[i]. DARK_GRAY)

    if guess == secret_word:
        message = "YOU WON!"
        game_state = "gameover"
        return

    current_row += 1
    current_col = 0

    if current_row == ROWS:
        message = f"WORD:{secret_word}"
        game_state = "gameover"

pgzrun.go()