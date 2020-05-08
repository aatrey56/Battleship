import random

print("We are playing battleship!") #introducing the player to the game
print()
print("You have seven guesses to win!") # how many guesses they have left
print()

def setupArray(): # method to set up an array which will be used later in the game
    arr = []
    for i in range(7):
        row = []
        for j in range(7):
            row.append('~')
        arr.append(row)
    return arr

def printArray(arr): # printing or displaying an array
    print(" \t1\t2\t3\t4\t5\t6\t7") # organized way of showing columns
    for x in range(7):
        line1 = str(x+1)+"\t"
        for x2 in range(7):
            line1 += (arr[x][x2]+"\t")
        print(line1)
            
def initBoard(): # creating both the display board and the one with the ship on it
    global shipSize
    global ship
    global board
    board=[]
    ship=[]
    shipSize=3
    ship = setupArray() # creating boards
    board = setupArray()
    orientation = random.randint(1,2) # randomly generating a value which will used to determine whether the ship is horizontal or vertical
    if (orientation==1): # these upcoming if statements adds ship either horizontally or vertically
        x = random.randint(0,6)
        y = random.randint(0,7-shipSize)
        for i in range(shipSize):
            ship[y].pop(x)
            ship[y].insert(x,"O")
            y+=1
    else:
        x = random.randint(0,7-shipSize)
        y = random.randint(0,6)
        for i in range(shipSize):
            ship[y].pop(x)
            ship[y].insert(x,"O")
            x+=1
      
def runBattleShip(): # where the game is actually made
    guesses=7
    correctGuesses=0
    initBoard()
    while(correctGuesses<shipSize and guesses>0): # makes sure game ends only when guesses are finished or the player has sunk the ship
        print()
        printArray(board)
        print()
        print("Guesses Left: "+str(guesses)) # prints guesses left
        row = (int)(input("Guess Row (1-7): "))
        col = (int)(input("Guess Column (1-7): "))
        while(row>7 or col>7):
            print("These coordinates are out of the boundaries. Please choose again.") # makes sure coordinates entered are in bounfd
            row = (int)(input("Guess Row (1-7): "))
            col = (int)(input("Guess Column (1-7): "))
        while(board[row-1][col-1] == "O" or board[row-1][col-1] == "X"): # makes sure of now repeats
            print("You have guessed this already. Please choose again.")
            row = (int)(input("Guess Row (1-7): "))
            col = (int)(input("Guess Column (1-7): "))
            while(row>7 or col>7):
                print("These coordinates are out of the boundaries. Please choose again.")
                row = (int)(input("Guess Row (1-7): "))
                col = (int)(input("Guess Column (1-7): "))
        if (ship[row-1][col-1]=="~"): # adds X if user doesn't doesnt guess correctly
            board[row-1].pop(col-1)
            board[row-1].insert(col-1,"X")
            guesses-=1
            print("You did not make any contact with the ship!")
        elif (ship[row-1][col-1]=="O"): #adds O if user guesses correctly
            board[row-1].pop(col-1)
            board[row-1].insert(col-1,"O")
            print("You have successfully hit the ship! ")
            guesses-=1
            correctGuesses+=1
        if (guesses>0 and correctGuesses==shipSize): # upcoming if statements determine winner
            printArray(board)
            print("You win!")
            guesses = -1
        elif(guesses==0):
            printArray(board)
            print("You lost!")

runBattleShip()

    
