games = {
   "cricket" : "A bat and bat game",
   "football" : "a game played using a ball and feet",
   "chess" : "a game played by using pieces",
    }

print("--------Game Dictionary Menu--------")
print("1. get game descripition")
print("2. add a new game")
print("3. change game descripition")
print("4. delete a game")

choice = input("enter your choice (1-4) ")


if choice == "1":
    game = input("enter game name ").strip().lower()
    if game in games:
        print("descripition ", games[games])
    else:
        print("no game found")

elif choice == "2":
    new_game = input("enter new game name ").strip().lower()
    game_descripition = input("enter game descripition ")
    games[new_game] = game_descripition
    print("game has been added successfully")

print("n\ updated games list")
print(games)