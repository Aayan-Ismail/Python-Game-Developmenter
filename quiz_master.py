import pgzrun 

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

score = 0
time_left = 20
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message

    screen.clear()
    screen.fill(color="black")

    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"navy blue")
    screen.draw.filled_rect(timer_box,"navy blue")
    screen.draw.filled_rect(skip_box,"dark green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"dark orange")

    marquee_message = "WELCOME TO QUIZ MASTER......"
    marquee_message += f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message,marquee_box, color= "white")

    screen.draw.textbox(
        str(time_left),
        timer_box,
        color="white",
        shadow =(0.5,0.5),
        scolor = "dim grey"
    )

    screen.draw.textbox("Skip",skip_box, color = "black", angle=-90)

    screen.draw.textbox(
        question[0].strip(),
        question_box,
        color="white",
        shadow=(0.5,0.5),
        scolor="dim grey"
    )

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color = "black")
        index += 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count, questions

    with open(question_file_name, "r") as q_file:
        for q in q_file:
            questions.append(q)
            question_count += 1

def read_next_question():
    global question_index

    if question_index < len(questions):
        q = questions[question_index]
        question_index += 1
        return q.split(",")

    else:
        game_over()
        return ["Game Over","-","-","-","-","5"]

def on_mouse_down(pos):
    index = 1

    for box in answer_boxes:
        if box.collidepoint(pos):
            try:
                correct_option = int(question[5].strip())
            except:
                correct_option = 0
        if index == correct_option:
            correct_answer()
        else:
            wrong_answer()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score
    score += 1
    next_question()

def wrong_answer():
    next_question()

def next_question():
    global question, time_left

    if question_index < question_count:
        question = read_next_question()
        time_left = 20
    
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over

    message = f"Game Over!\nScore:{score}/{question_count}"
    question = [message,"-","-","-","-","5"]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left

    if question_index < question_count and not is_game_over:
        question = read_next_question()
        time_left = 20
    else:
        game_over()

def update_time_left():
    global time_left

    if time_left > 0 and not is_game_over:
        time_left -= 1
    else:
        next_question()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)

pgzrun.go()

