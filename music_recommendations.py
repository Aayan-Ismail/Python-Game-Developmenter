classical = {"If I am with you",
             "Gwyn lord of cinder",
             "luallaby of resembool",
             "in the pool",
             "knife to the throat"
}

rock = {"Aizo",
        "Special",
        "Kick Back",
        "Corruption"
}

dramatic = { "The Golden land",
            "Elesion",
            "Ansatsu Ikka no Yakata",
            "Let's just crash",
            "IRIS OUT"
}

while True:
    print("\n ------------------ song menu ------------------")
    print("1. see classical songs")
    print("2. see rock songs")
    print("3. see dramatic songs")
    print("4. search songs")
    print("5. show all songs")
    print("6. exit")

    choice = int(input("enter the choice (has to be a number): "))
    
    if choice == 1:
        print("classical songs")
        for games in classical:
            print(games)

    elif choice == 2:
        print("rock songs")
        for games in rock:
            print(games)

    elif choice == 3:
        print("dramatic songs")
        for games in dramatic:
            print(games)
    
    elif choice == 4:
        game_name = input("enter song name: ")

        found = False

        if game_name in classical:
            print(f"{game_name} is in the classical genre")
            found = True

        if game_name in rock:
            print(f"{game_name} is in the rock genre")
            found = True

        if game_name in dramatic:
            print(f"{game_name} is in the dramatic genre")
            found = True
        
        if not found:
            print("song not found in database")
    
    elif choice == 5:
        for games in classical:
            print(games)
        print("\n")

        for games in rock:
            print(games)
        print("\n")
        
        for games in dramatic:
            print(games)

    elif choice == 6:
        break

    else:
        print("invalid choice, please choose a number from 1 to 6")