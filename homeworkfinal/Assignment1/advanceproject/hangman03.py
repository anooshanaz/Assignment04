
import random

words = ["python","javascript","programming,colour"]
words = random.choice(words)
guess = ""
turns = 6

while turns > 0:
    failed = 0
    for char in words:
        if char in guess:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\n You won!")
        break

    guesses= input("\n Guess a letter? ").lower()
    guess += guesses
    if guess not in words:
        turns -= 1
        print(f"Wrong {turns}. turns left!!")
else:
    print(f"You lost! The word was {words}")