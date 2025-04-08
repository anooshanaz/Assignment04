import random

print("Welcome to the game. This is a number guessing game.\nYou have 5 attempts to guess a number between 50 and 100. Let's start the game!")

# Generate a random number between 50 and 100
number_to_guess = random.randrange(50, 100)

# Initialize the guess counter and chances
guess_counter = 0
chances = 5

# Start the game loop
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess:
        print(f"Congratulations! The number is {number_to_guess}, and you guessed it right in {guess_counter} attempt(s)! 🎉")
        break
    elif my_guess > number_to_guess:
        print("Your guess is too high. Try again! ⬇️")
    elif my_guess < number_to_guess:
        print("Your guess is too low. Try again! ⬆️")

# If the player runs out of attempts
if guess_counter >= chances and my_guess != number_to_guess:
    print(f"Sorry! The number was {number_to_guess}. Better luck next time! 💪")




