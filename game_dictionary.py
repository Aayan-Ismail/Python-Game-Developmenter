games = {
   "cricket" : "A bat and bat game",
   "football" : "a game played using a ball and feet",
   "chess" : "a game played by using pieces",
    }

while True:
    print("--------Game Dictionary Menu--------")
    print("1. get game descripition")
    print("2. add a new game")
    print("3. change game descripition")
    print("4. delete a game")

    choice = input("enter your choice (1-4) ")

    if choice == "1":
        game = input("enter game name ").lower()
        if game in games:
            print("descripition", games[game])
        else:
            print("no game found")

    elif choice == "2":
        new_game = input("enter new game name ").lower()
        game_descripition = input("enter game descripition ")
        games[new_game] = game_descripition
        print("game has been added successfully")

    elif choice == "3":
        game = input("enter game name to change descripition: ").lower()
        if game in games:
            new_descripition = input("enter new descripition: ")
            games[game] = new_descripition
            print("descripition has been updated successfully")
        else:
            print("no game found")

    elif choice == "4":
        game = input("enter game name to delete: ").lower()
        if game in games:
            del games[game]
            print("game has been deleted successfully")
        else:
            print("no game found")

    else:
        print("invalid input")


    print("n\ updated games list")
    print(games)