import random, sys

# Ascii art variables: Rock, Paper, Scissor 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Variables

# List with Options for Computer to choose from.
choiceList = ['R','P','S']

# Stores User's Score.
userScore = 0

# Stores Computer's Score.
computerScore = 0

# Prompts the User with Instruction and Stores the Given Input for Game.
userInput = input("\n\nType 'Exit' to quit the program or 'Play' to play the game.")

# Main Game Loop
while True:
    computerChoice = random.choice(choiceList)
    if userScore == 5 or computerScore == 5:
        break
    elif userInput.lower() == 'exit':
        sys.exit()
    else:
        userInput = input("\nPress (R) for Rock, (P) for Paper and (S) for Scissor: ").upper()
        # The following bkock of code shows what you are choosing.
        if userInput.upper() == 'R':
            print(f"\nYou Choose: Rock\n{rock}")
        elif userInput.upper() == 'P':
            print(f"\nYou Choose: Paper\n{paper}")
        elif userInput.upper() == 'S':
            print(f"\nYou Choose: Scissors\n{scissors}")

        # The following Block of code shows what the computer is choosing.
        if userInput.upper() != 'R' and userInput.upper() != 'P' and userInput.upper() != 'S':
            print("Wrong input! You can only choose from (R) Rock, (P) Paper or (S) Scissors.")
            userScore += 0
            computerScore += 0
            continue
        else:
            if computerChoice == 'R':
                print(f"Computer Choose: Rock\n{rock}")
            elif computerChoice == 'P':
                print(f"Computer Input: Paper\n{paper}")
            else:
                print(f"Computer Input: Scissors\n{scissors}")

        # Score Adding Logic
        if userInput == computerChoice.upper():
            print(f"No Score! Opponent too choose {userInput}!")
        elif userInput == 'R' and computerChoice == 'S':
            userScore += 1
        elif userInput == 'P' and computerChoice == 'R':
            userScore += 1
        elif userInput == 'S' and computerChoice == 'P':
            userScore += 1
        else:
            computerScore += 1
print("\n\nSCORE BOARD:")
if userScore == computerScore:
    print(f"\n\nDraw match!\nUser Score: {userScore}\nComputer Score: {computerScore}")
elif userScore > computerScore:
    print(f"You Won!\Your Score: {userScore}\nComputer Score: {computerScore}")
else:
    print(f"You Lose!\Your Score: {userScore}\nComputer Score: {computerScore}")
