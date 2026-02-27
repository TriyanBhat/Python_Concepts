import random

number = random.randint(1, 10)

print("Guess the number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(" Correct! You guessed the number.")
        break
    elif guess < number:
        print("Low, Try again.")
    else:
        print("High, Try again.")
