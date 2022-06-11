#Rock Paper Scissors App

print("Enter R for Rock")
print("Enter P for Paper")
print("Enter S for Scissors")

import random
run = True
def rps():
    global run
    options = ["R","P","S"]
    choice = random.randint(0, 2)
    computer = options[choice]
    player = input("Your choice: ")
    cpu = play = ""

    def result(play,cpu):
        return "Player("+play+") : CPU("+cpu+")"

    def statement(win,lose):
        return win+" beats "+lose

    check = player in options

    if check == False:
        print("Oops! invalid choice")
    elif player == computer:
        print("Tied")
    elif player == options[0]:
        play = "Rock"
        if computer == options[1]:
            cpu = "Paper"
            print(statement(cpu,play))
            print(result(play,cpu))
            run = False
        elif computer == options[2]:
            cpu = "Scissors"
            print(statement(play,cpu))
            print(result(play,cpu))
            run = False
    elif player == options[1]:
        play = "Paper"
        if computer == options[0]:
            cpu = "Rock"
            print(statement(play,cpu))
            print(result(play,cpu))
            run = False
        elif computer == options[2]:
            cpu = "Scissors"
            print(statement(cpu,play))
            print(result(play,cpu))
            run = False
    elif player == options[2]:
        play = "Scissors"
        if computer == options[0]:
            cpu = "Rock"
            print(statement(cpu,play))
            print(result(play,cpu))
            run = False
        elif computer == options[1]:
            cpu = "Paper"
            print(statement(play,cpu))
            print(result(play,cpu))
            run = False
while run:
    rps()