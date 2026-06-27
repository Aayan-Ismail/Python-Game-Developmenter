quiz_questions = ("what is the best anime: ", "what is the tallest mountain on earth: ", "what celestial object has the most density: ", "what is transience: ", "what is avarice: ", "what does vainglorious folly mean: ",  "who is chrono: ", "is the OSA a battleship or supercarrier: ")
question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8 = quiz_questions

quiz_answers = ("personal opinion","mt everest", "black hole", "the idea you are subject to nature", "extreme greed for wealth", "overly boastful foolishness", "someone whose unbounded by physical form who took the usurper's offer to research for as long as he wanted", "battleship")
answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8 = quiz_answers

print("Welcome to the quiz!")

answer1 = input(question_1)
if answer1 == answer_1:
    print("that is correct")
else:
    print("incorrect. it is", answer_1)

answer2 = input(question_2)
if answer2 == answer_2:
    print("that is correct")
else:
    print("incorrect. it is", answer_2)

answer3 = input(question_3)
if answer3 == answer_3:
    print("that is correct")
else:
    print("incorrect. it is", answer_3)

answer4 = input(question_4)
if answer4 == answer_4:
    print("that is correct")
else:
    print("incorrect. it is", answer_4)

answer5 = input(question_5)
if answer5 == answer_5:
    print("that is correct")
else:
    print("incorrect. it is", answer_5)

answer6 = input(question_6)
if answer6 == answer_6:
    print("that is correct")
else:
    print("incorrect. it is", answer_6)

answer7 = input(question_7)
if answer7 == answer_7:
    print("that is correct")
else:
    print("incorrect. it is", answer_7)

answer8 = input(question_8)
if answer8 == answer_8:
    print("that is correct")
else:
    print("incorrect. it is", answer_8)
