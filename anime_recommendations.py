fantasy = {"witch hat atelier",
           "delicious in dungeon",
           "frieren",
           "hunter x hunter"
           }

action = {"lord of the mysteries",
           "gachiakuta",
           "full metal alchemist",
           "jujustu kaisen,",
           "blue lock",
           "chainsaw man",
           "gurren lagann",
           "tokyo ghoul"
           }

psychological = {"death note",
                "monster",
                 "86",
                 "violet evergarden",
                 "vinland saga",
                 "code geass"
                 }

while True:
    print("\n ------------------ actually good anime menu ------------------")
    print("1. see fantasy anime")
    print("2. see action anime")
    print("3. see psychological anime")
    print("4. search anime")
    print("5. show all anime")
    print("6. exit")

    choice = int(input("enter the choice (has to be a number): "))
    
    if choice == 1:
        print("fantasy animes")
        for anime in fantasy:
            print(anime)

    elif choice == 2:
        print("action animes")
        for anime in action:
            print(anime)

    elif choice == 3:
        print("psycholgoical animes")
        for anime in psychological:
            print(anime)
    
    elif choice == 4:
        anime_name = input("enter anime name: ")

        found = False

        if anime_name in fantasy:
            print(f"{anime_name} is in the fantasy genre")
            found = True

        if anime_name in action:
            print(f"{anime_name} is in the action genre")
            found = True

        if anime_name in psychological:
            print(f"{anime_name} is in the psychological genre")
            found = True
        
        if not found:
            print("anime not found in database")
    
    elif choice == 5:
        for anime in fantasy:
            print(anime)
        print("\n")

        for anime in action:
            print(anime)
        print("\n")
        
        for anime in psychological:
            print(anime)

    elif choice == 6:
        break

    else:
        print("invalid choice, please choose a number from 1 to 6")