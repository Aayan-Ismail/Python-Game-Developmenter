horror = {"Routine",
          "Dead Space",
          "Amensia: The Bunker",
          "Outlast",
          "Resident Evil 7"
}

fantasy = {"Dark souls 1",
           "Dark souls 3",
           "Elden Ring",
           "Bloodborne",
           "The Witcher 3: Wild Hunt"
}

action = { "Sekiro: Shadows Die Twice",
          "Devil May Cry 5",
          "Doom Eternal",
          "Halo Reach",
          "Halo 3"

}

while True:
    print("\n ------------------ game menu ------------------")
    print("1. see fantasy games")
    print("2. see action games")
    print("3. see horror games")
    print("4. search games")
    print("5. show all games")
    print("6. exit")

    choice = int(input("enter the choice (has to be a number): "))
    
    if choice == 1:
        print("fantasy games")
        for games in fantasy:
            print(games)

    elif choice == 2:
        print("action games")
        for games in action:
            print(games)

    elif choice == 3:
        print("horror games")
        for games in horror:
            print(games)
    
    elif choice == 4:
        game_name = input("enter game name: ")

        found = False

        if game_name in fantasy:
            print(f"{game_name} is in the fantasy genre")
            found = True

        if game_name in action:
            print(f"{game_name} is in the action genre")
            found = True

        if game_name in horror:
            print(f"{game_name} is in the horror genre")
            found = True
        
        if not found:
            print("anime not found in database")
    
    elif choice == 5:
        for games in fantasy:
            print(games)
        print("\n")

        for games in action:
            print(games)
        print("\n")
        
        for games in horror:
            print(games)

    elif choice == 6:
        break

    else:
        print("invalid choice, please choose a number from 1 to 6")