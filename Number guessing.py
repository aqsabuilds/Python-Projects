import random

number = int(input("Guess a number between 1 to 100: "))

computerNumber = random.randint(1, 100)

if number == computerNumber:
    print("You guessed the exact number")
elif number > computerNumber:
    print("Very high")
elif number < computerNumber:
    print("Very small")
