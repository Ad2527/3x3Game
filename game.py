import random
players = {'Player A': 0,'Player B':0}
def getboard(a, b):
    print("-----------------")
    # top row
    for i in range(7, 4, -1):
        if (i == a):
            print("A", end="\t")
        elif (i == b):
            print("B", end="\t")
        else:
            print(i, end="\t")
    print()

    # mid row
    if (a == 0):
        print("A", end="\t")
    elif (b == 0):
        print("B", end="\t")
    else:
        print("S", end="\t")

    if (a == 8):
        print("A", end="\t")
    elif (b == 8):
        print("B", end="\t")
    else:
        print("X", end="\t")

    if (a == 4):
        print("A", end="\t")
    elif (b == 4):
        print("B", end="\t")
    else:
        print("4", end="\t")

    print()

    # bottom
    for i in range(1, 4):
        if (i == a):
            print("A", end="\t")
        elif (i == b):
            print("B", end="\t")
        else:
            print(i, end="\t")
    print()
    print("-----------------")

def printWinner(player):
    print("THE Winner IS: ",player)

def playTurn(player,other):
    print("******************************************************")
    print("{}'s Turn".format(player))
    input("Press Enter key to roll a number from 1-3:")
    roll = roll = random.randint(1, 3)
    print("{} rolled ".format(player), roll)

    if (players[player] + roll == 8):
        players[player]  = players[player] + roll
        print("OUR WINNER IS: ".format(player))
        return True
    elif (players[other] == (players[player] + roll) and players[other] != 0):
        players[other] = 0
        players[player] = players[player] + roll
        print("OH NO!! {} has gone back to the safespace (0)".format(other))
        print("{} has moved to spot:".format(player), players[player])
        return False
    elif (players[player] + roll > 8):
        print("{} remains at spot: ".format(player), players[player])
        return False
    else:
        players[player] = players[player] + roll
        print("{} has moved to spot: ".format(player), players[player])
        return False

def Game():
    gamewon = False
    # playera = np.zeros(9)
    # safe spot 0, winning spot is 8
    turn = 0
    print("Both players start on space 0 and must race to reach 8 with rolls of 1-3 to win!!")
    input("Press Enter To START")
    print("******************** Game start: *********************")

    while (not gamewon):

    # safe spot at 0
    # if either reaches 8 they win
    # if they land on the same spot the first player goes back to 0
    # if they land 'above' 8 then their turn is skipped and dice =2/3
    # they land on a spot like normal
        if (turn % 2 == 0):
            player = 'Player A'
            other =  'Player B'
            gamewon = playTurn(player,other)
            ####
            getboard(players[player], players[other])
        else:
            player = 'Player B'
            other =  'Player A'
            gamewon = playTurn(player,other)
            ####
            getboard(players[other], players[player])

        turn = turn + 1
Game()



