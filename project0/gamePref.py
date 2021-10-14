games = ["Chess", "Waterpolo", "Splitgate"]
for game in games:
    print("I like to play ", game)
new_game = input("What game do you like to play")
games.append(new_game)
for game in games:
    print("We like to play ", game)