games = ["Chess", "Waterpolo", "Splitgate"]
new_game = ''
while new_game != 'quit':
    for game in games:
        print("I like to play ", game)
    new_game = input("What game do you like to play")
    if new_game != 'quit':
        games.append(new_game)
    for game in games:
        print("We like to play ", game)