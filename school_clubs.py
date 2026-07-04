clubs = {
    "coding":{"Aayan", "Seán", "John", "Henry"},
    "music" :{"Michael", "Mícheal", "Micheal", "Aayan"},
    "football":{"Connor", "Chrono", "Conor", "Hadrian", "Michael"},
    "debating":{"Henry", "Harry", "Hadrian", "John"},
    "chess":{"Henry", "Harry", "Hadrian", "John"}
}

def display_clubs():
    print("\nAvailable Clubs:")
    for club in clubs:
        print("-", club.capitalize())

def display_students():
    club_name = input("Enter club anme: ").lower()

    if club_name in clubs:
        if len(clubs[club_name]) == 0:
            print("No students in this club")
        else:
            print(f"\nStudents in {club_name.capitalize()} Club:")
            for student in clubs[club_name]:
                print(student)
    else:
        print("club not found.")

def add_student():
    club_name = input("Enter club name:").lower()

    if club_name in clubs:
        student_name = input("enter student name to add: ").capitalize()
        
        if student_name in clubs[club_name]:
            print("student already exists in this club")
        
        else:
            clubs[club_name].add(student_name)
            print(student_name, "added to", club_name.capitalize(), "club successfully")
    else:
        print("club not found")

def remove_student():
    club_name = input("enter club name: ").lower()

    if club_name in clubs:
        student_name = input("enter student name to remove").capitalize()
        
        if student_name in clubs[club_name]:
            clubs[club_name].remove(student_name)
            print(student_name, "removed from", club_name.capitalize(), "club successfully")
        else:
            print("student not found in this club")
    else:
        print("club not found")

def check_student():
    club_name = input("enter club name: ").lower()

    if club_name in clubs:
        student_name = input("enter student name to check").capitalize()

        if student_name in clubs[club_name]:
            print(student_name, "is a member of", club_name.capitalize(), "club")
        else:
            print(student_name, "is not a member of", club_name.capitalize(), "club")
    else:
        print("club not found")

def common_students():
    club1 = input("enter first club name: ").lower()
    club2 = input("enter second club name: ").lower()

    if club1 in clubs and club2 in clubs:
        common = clubs[club1].intersection(clubs[club2])

        if len(common) == 0:
            print("no common students in both clubs")
        else:
            print(f"\nCommon studnets in {club1.capitalize()} and {club2.capitalize()} clubs.")
            for student in common:
                print(student)
    else:
        print("one or both club names are invalid")

def all_students_two_clubs():
    club1 = input("enter first club name: ").lower()
    club2 = input("enter second club name: ").lower()

    if club1 in clubs and club2 in clubs:
        all_students = clubs[club1].union(clubs[club2])

        print(f"\nAll students in {club1.capitalize()} and {club2.capitalize()} clubs:")
    
    else:
      print("one or both club names are invalid")

def only_in_first_club():
    club1 = input("enter first club name: ").lower()
    club2 = input("enter second club name: ").lower()

    if club1 in clubs and club2 in clubs:
        diff = clubs[club1].difference(clubs[club2])

        if len(diff) == 0:
            print(f"no students are exclusively in {club1.capitalize()} club")
        
        else:
            print(f"\nStudents only in {club1.capitalize()} Club:")
            for student in diff:
                print(student)
    else:
        print("one or both club names are invalid")    

def students_in_exactly_one():
    club1 = input("enter first club name: ").lower()
    club2 = input("enter second club name: ").lower()

    if club1 in clubs and club2 in clubs:
        result = clubs[club1].symmetric_difference(clubs[club2])

        if len(result) == 0:
            print("no such students found")
        else:
            print(f"\nStudents in exactly one of {club1.capitalize()} or {club2.capitalize()} clubs:")
            for student in result:
                print(student)
    else:
        print("one or both club names are invalid")    

def count_students():
    club_name = input("enter club name: ").lower()

    if club_name in clubs:
        print("total students in", club_name.capitalize(), "club =", len(clubs[club_name]))
    else:
        print("club not found")

def all_unique_students():
    unique_students = set()

    for club in clubs.values():
        unique_students = unique_students.union(club)
    
    print("\nAll unique students in all clubs:")
    for student in unique_students:
        print(student)
    
    print("total unique student =", len(unique_students))

def check_subset():
    club1 = input("enter first club name: ").lower()
    club2 = input("enter second club name: ").lower()

    if club1 in clubs and club2 in clubs:
        if clubs[club1].issubset(clubs[club2]):
            print(f"all students of {club1.capitalize()} club are present in {club2.capitalize()} club")
        
        else:
            print(f"{club1.capitalize()} club is not a subset of {club2.capitalize()} club")
    else:
        print("one or both club names are invalid")