user_marks = {}

for i in range(2):
    subject = input("enter the subject name ")
    marks = int(input("enter marks for subject "))
    user_marks[subject] = marks
    #print(user_marks)

total_marks = sum(user_marks.values())
average_marks = total_marks/len(user_marks)
highest_mark = max(user_marks.values())

print("Your total marks are" ,total_marks , "out of" , len(user_marks) * 100)
print("Average mark is" , average_marks)
print("the highest mark is" , highest_mark)