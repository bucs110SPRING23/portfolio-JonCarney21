import random

num = random.randrange(1, 11)

for _ in range(3)
    guess = int(input("guess a number between 1 and 10:"))


    if guess == num:
        print("you guessed it!")
    elif guess < num:
        print("to low!")
    
