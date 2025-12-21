import random
while True:
    rando = random.randint(1,100)
    print ("Guess a number between 1 and 100. You have 10 tries!")
    for i in range (0, 10):
        player_guess = input(">")
        try:
            player_guess = int(player_guess)
        except:
            print("Please enter a number!")
            i = i-1
            continue
        if player_guess > rando:
            print("Too high!")
        elif player_guess < rando:
            print("Too low!")
        else:
            print("Correct!")
            break
        print(f"{9-i} Guesses remain")
    print("Do you want to play again? (y/n)")
    answer_pl = input(">")
    if answer_pl != "y":
        break


