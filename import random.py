import random
while True:
    rando = random.randint(1,100)
    print ("Guess a number between 1 and 100. You have 10 tries!")
    attempts = 10
    while attempts>0:
        player_guess = input(">")
        try:
            player_guess = int(player_guess)
        except ValueError:
            print("Please enter a number!")
            continue
        attempts -= 1
        if player_guess > rando:
            print("Too high!")
        elif player_guess < rando:
            print("Too low!")
        else:
            print("Correct!")
            break
        print(f"{attempts} Guesses remain")
    else:
        print("You are out of guesses!")
    print("Do you want to play again? (y/n)")
    answer_pl = input(">")
    if answer_pl != "y":
        break


