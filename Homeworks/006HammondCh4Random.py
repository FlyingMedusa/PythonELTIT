import random

letters = "abcdefghijklmnopqrstuvwxyz"
letter = letters[random.randint(0,25)]

while True:
    guess = input("Type a lower-case letter: ")
    if guess not in letters:
        print("That's not a lower-case letter.")
        continue
    if guess == letter:
        print("That's right!")
        break
    if guess > letter:
        print("It's earlier in the alphabet.")
    else:
        print("It's later in the alphabet.")