from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = raw_input("Rock, Paper, Scissors?" + "  ")
    if player == computer:
        print "Tie!" /n
    elif player == "Rock":
        if computer == "Paper":
            print"You lose!", computer, "covers", player, "\n"
        elif computer == "Scissors":
            print"You win!", player, "smashes", computer, "\n"
    elif player == "Paper":
        if computer == "Scissors":
            print "You lose!", computer, "cuts", player, "\n"
        elif computer == "Rock":
            print "You win!", player, "covers", computer, "\n"
    elif player == "Scissors":
        if computer == "Rock":
            print "You lose!", computer, "smashes", player, "\n"
        elif computer == "Paper":
            print "You win!", player, "cuts", computer, "\n"
    elif player == "quit":
        exit()
    else: print "Put a real value in boyo or girlo"

    player = False
    computer = t[randint(0,2)]
