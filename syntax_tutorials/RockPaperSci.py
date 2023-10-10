import sys
import random

print("")

playerChoice = input("Enter choice :\n1- Rock \n2-Paper \n3- Scissors\n\n")
playerInt = int(playerChoice)

if(playerInt < 1 or playerInt > 3):
    sys.exit("Invalid input : enter 1,2 or 3")

computerChoice = random.randint(1,3)

print(f"player choice {playerInt}" )
print(f"Computer choice {computerChoice}")

if playerInt == computerChoice :
    print("Draw")

elif ((playerInt == 1 and computerChoice == 3) or (playerInt == 2 and computerChoice == 1) or (playerInt == 3 and computerChoice == 2)):  
    print("You Win")

else :
    print("Computer Win")
