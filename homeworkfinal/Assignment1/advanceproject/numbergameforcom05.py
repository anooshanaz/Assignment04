
import random

print("Think a number between 1 and 100")
input("Press Enter when you are ready")

low, high = 1 ,100
while True:
    guess = random.randint(low, high)
    feedback = input(f"is it {guess}? (H/L/C) ").upper()
    if feedback == "C":
        print("computer won!")
        break
    elif feedback == "H":
        high = guess - 1
    else:
        low = guess + 1

