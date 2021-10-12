def crowd_test(roomList):
    if len(roomList) > 3:
        print("The room is crowded")
    else:
        print("the room is not crowded")

party =['Samantha', 'Bernard', 'Gukesh', 'Mike']
crowd_test(party)
party.remove('Bernard')
crowd_test(party)


