import random

while True:
    print("<<<<<<<< Rock, Paper & Scissors: A Zuri Training Python Task >>>>>>>>")
    print("\n")

    playerName = input("Enter player name: ")
    print("\n")

    playerChoice = input("Enter rock, paper or scissors: ")

    # Player's choice.
    if playerChoice not in ("rock", "paper", "scissors"):
        print("Invalid Selection! Please enter Rock, Paper or Scissors...")

    # Computer's Choice.
    computerChoice = random.choice(["rock", "paper", "scissors"])
    if computerChoice == "rock":
        print(f"Computer chose {computerChoice}.")
    if computerChoice == "paper":
        print(f"Computer chose {computerChoice}.")
    if computerChoice == "scissors":
        print(f"Computer chose {computerChoice}.")

    # Tie Condition
    if playerChoice == computerChoice:
        print(f"Tie! {playerName}, and CPU made the same selection...")

    # Conditions to determine winner.
    if playerChoice == "rock" and computerChoice == "paper":
        print("Paper covers Rock")
        print("CPU WINS!!!")
    if playerChoice == "paper" and computerChoice == "rock":
        print("Paper covers Rock")
        print(f"{playerName} WINS!!!")

    if playerChoice == "scissors" and computerChoice == "rock":
        print("Rock smashes Scissors")
        print("CPU WINS!!!")
    if playerChoice == "rock" and computerChoice == "scissors":
        print("Rock smashes Scissors")
        print(f"{playerName} WINS!!!")

    if playerChoice == "paper" and computerChoice == "scissors":
        print("Scissors cut Paper")
        print("CPU WINS!!!")
    if playerChoice == "scissors" and computerChoice == "paper":
        print("Scissors cut Paper")
        print(f"{playerName} WINS!!!")

    exit = input("\nWould you like to play again? Y/N: ")
    if exit == "N":

        break