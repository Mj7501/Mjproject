import random

def play_game():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != number:
        if guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        guess = int(input("Guess a number between 1 and 10: "))
    print("Congratulations, you guessed the number!")

play_game()
