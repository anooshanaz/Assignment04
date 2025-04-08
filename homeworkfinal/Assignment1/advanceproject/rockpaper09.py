#this game classic rock,paper,scissor game play by user against computer
import random 

choices = ["rock","paper","scissor"]
user_input = str(input("Enter your choices (rock,paper,scissor):"))

computer_choice = random.choice(choices)
print(f"Computer choice {computer_choice}")

if user_input == computer_choice:
    print("It's tie!")
elif (user_input == "rock") and (computer_choice == "paper"):
    print("You win 🏆!") 
elif (user_input == "paper") and (computer_choice == "scissor"):
    print("You win!🏆")
elif (user_input == "scissor") and (computer_choice == "rock"):
    print("You win 🏆!")
else:
    print("Computer win! 🏆")

