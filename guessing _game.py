import random

secret_number = random.randint(1, 10)

guess = 0
while guess != secret_number:
    guess = float(input("Guess a number between 1 and 10:"))

    if guess < secret_number:
        print("Too low try again.")

    elif guess > secret_number:
        print("Too high try again.")

    else:
        print("congratulations you guessed the number!")