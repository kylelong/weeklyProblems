import random

answer = random.randint(1,100)

guess = int(input("Guess the number! \n"))
attempts = 1
while guess != answer:
    if guess > answer:
        guess = int(input("lower \n"))
        attempts += 1
    else:
        guess = int(input("higher \n"))
        attempts += 1
msg = f"Correct! You won in {attempts} guesses!"
print(msg)
