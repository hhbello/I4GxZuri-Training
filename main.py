import random

print("\n")
print("<<<<<<<< Rock, Paper & Scissors: A Zuri Training Python Task >>>>>>>>")
print("\n")

while True:
    choices = ["R", "P", "S"]

    # CPU and Player possible options
    CPUchoice = random.choice(choices).upper()
    Playerchoice = input("R, P, or S: ").upper()

    # Loop for invalid option
    while Playerchoice not in choices:
        print("Invalid option! Try again.")
        Playerchoice = input("R, P, or S: ").upper()

    # Tie condition
    while Playerchoice == CPUchoice:
        print(f"Player ({Playerchoice}) : CPU ({CPUchoice}) ")
        print("Tie! Select new option")
        Playerchoice = input("R, P, or S: ").upper()

    # Conditions to determine winner
    if Playerchoice == "R":
        if CPUchoice == "P":
            print("Player (Rock) : CPU (Paper)")
            print("Paper covered Rock")
            print("CPU Won!")

        if CPUchoice == "S":
            print("Player (Rock) : CPU (Scissors)")
            print("Rock smashed Scissors")
            print("Player Won!")

    elif Playerchoice == "P":
        if CPUchoice == "S":
            print("Player (Paper) : CPU (Scissors)")
            print("Scissors cut Paper")
            print("CPU Won!")
        if CPUchoice == "R":
            print("Player (Paper) : CPU (Rock)")
            print("Paper covered Rock")
            print("Player Won!")

    elif Playerchoice == "S":
        if CPUchoice == "R":
            print("Player (Scissors) : CPU (Rock)")
            print("Rock smashed Scissors")
            print("CPU Won!")
        if CPUchoice == "P":
            print("Player (Scissors) : CPU (Paper)")
            print("Scissors cut paper")
            print("Player Won!")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Goodbye!")

