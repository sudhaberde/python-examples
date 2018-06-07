print("Lets play rock paper scissors: \n rock \n paper \n scissors\n")

while True:

    game_dict = {'rock':1,'paper': 2, 'scissors': 3}

    input_1 = input("Player 1: Please enter your input here \n")

    input_2 = input("Player 2 : Please enter your input here \n")

    a = game_dict.get(input_1)

    b = game_dict.get(input_2)

    diff = a - b


    if diff in [ -1, 2]:
        print ("Player 1 wins")
        if input('Do you want to play another game, yes or no?\n') == 'yes':
            continue
        else:
            print("game done")
        break
    elif diff in [-2, 1]:
        print("Player 2 wins")
        if input('Do you want to play another game, yes or no?\n') == 'yes':
            continue
        else:
            print("game done")
    else:
        print ("Its a tie")
        if input('Do you want to play another game, yes or no?\n') == 'yes':
            continue
        else:
            print("game done")
