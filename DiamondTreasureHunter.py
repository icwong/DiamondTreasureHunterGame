
# "The Diamond Treasure Hunter"

import random

def ran_board(dim): #generate a random board
    mat = []
    for r in range(int(dim)):
        row = []
        for c in range(int(dim)):
            randinte = random.randint(0,maxdiam) #random number between 0 and maximum diamonds
            row.append(randinte)       
        mat.append(row)
    return mat
    
def hunterpath_row(row): # hunter travels along a row
    accum = 0
    checkflag = 0
    topflag = True
    i = 0
    print "positions visited: " 
    while topflag == True and i<len(board): #Validation check
        if board[row][i]%2 != 0: #checks each row position
            if board[row][i] == -1: #Check if -1 in the cell
                checkflag = 1
                topflag = False
                print [row],[i],'-1 found'
            else:
                accum = accum + board[row][i] #if the cell does not contain -1 accumulate diamonds
                board[row][i] = 0 
        if board[row][i]%2 == 0: #Collecting diamonds
            board[row][i] = board[row][i]/2
            accum = accum + board[row][i] #Total accumulated in the row diamonds
            print [row],[i]
        i = i + 1
    print 'points obtained in this trip: ',accum # 
    print
    print 'board after trip: '
    print
    displayboard() #displays the board
    return [accum,topflag,checkflag] 

def hunterpath_col(col): #hunter travels along a column
    accum = 0
    checkflag = 0
    topflag = True
    i = 0
    print "positions visited: "
    while topflag == True and i<len(board):  #Validation check
        if board[i][col]%2 != 0: #checks each column position
            if board[i][col] == -1: #check if -1 in the cell 
                checkflag = 1 
                topflag = False 
                print [i],[col],'-1 found'
            else:
                accum = accum + board[i][col] #Accumulate diamonds in the column
                board[i][col] = 0
        if board[i][col]%2 == 0:
            board[i][col] = board[i][col]/2 #Diamond in the cell is even / 2
            accum = accum + board[i][col]
            print [i],[col]
        i = i + 1
    print 'points obtained in this trip: ',accum
    print
    print 'board after trip: '
    print
    displayboard()
    return [accum,topflag,checkflag]
    
def hunterpath_main(): #hunter travels along the main diagonal
    accum = 0
    topflag = True
    checkflag = 0
    i = 0
    print "positions visited: "
    while topflag == True and i<len(board): #validation check
        if board[i][i]%2 != 0: #if cell is odd
            if board[i][i] == -1: #check for -1 
                checkflag = 1
                topflag = False
                print [i],[i],'-1 found'
            else:
                accum = accum + board[i][i] #accumulate diamond 
                board[i][i] = 0
        if board[i][i]%2 == 0: # if cell is even
            board[i][i] = board[i][i]/2 
            accum = accum + board[i][i]
            print [i],[i]
        i = i + 1
    print 'points obtained in this trip: ',accum
    print
    print 'board after trip: '
    print
    displayboard()
    return [accum,topflag,checkflag]

def hunterpath_second(): #hunter travels along the secondary diagonal
    p = len(board) -1
    accum = 0
    topflag = True
    checkflag = 0
    i = 0
    print "positions visited: "
    while topflag == True and i<len(board): #validation check
        if board[i][p]%2 != 0: #if cell is odd
            if board[i][p] == -1: #check for -1
                checkflag = 1
                topflag = False
                print [i],[p],'-1 found'
            else:
                accum = accum + board[i][p]
                board[i][p] = 0
                print [i],[p]
                
        elif board[i][p]%2 == 0: #if cell is even
            board[i][p] = board[i][p]/2 #cell / 2
            accum = accum + board[i][p]
            print [i],[p]
        p = p - 1
        i = i + 1
    print 'points obtained in this trip: ',accum
    print
    print 'board after trip: '
    print
    displayboard()
    return [accum,topflag,checkflag]

def hunterpath_rand(var): #hunter travels randomly
    i = 0
    accum = 0
    topflag = True
    checkflag = 0
    print "positions visited: "
    while topflag == True and i<var: #validation check
        randrow = random.randint(0,len(board)-1) #generate a random row number between 0 and len of the board
        randcol = random.randint(0,len(board)-1) #generate a random column number between 0 and len of the board 
        if board[randrow][randcol]%2 == 0: #check if cell is even
            board[randrow][randcol] = board[randrow][randcol]/2
            accum = accum + board[randrow][randcol]
            print [randrow],[randcol]
        elif board[randrow][randcol]%2 != 0: #check if cell is odd
            if board[randrow][randcol] == -1: #check for -1 in the cell 
                print [randrow],[randcol],'-1 found'
                checkflag = -1
                topflag = False
            else:
                accum = accum + board[randrow][randcol]
                board[randrow][randcol] = 0
                print [randrow],[randcol]
        i = i + 1
    print 'points obtained in this trip: ',accum
    print
    print 'board after trip: '
    print
    displayboard()
    return [accum,topflag,checkflag]
    

def displayboard(): #generates and displays the game board
    for row in range(len(board)):
        print '\t','col',row,'\t', #header for column
    print '\r'    
    for row in range(len(board)): #row 
        print '\r''row ',row,
        for col in range(len(board)):        
            print '\t',board[row][col],'\t',
        print '\r'
    print '\n'


def traveloptions(): #asks the hunter how he/she would like to travel
    travel = raw_input("How do you want " + name + " to travel?\nr - row\nc - col\nm - main diagonal\ns - secondary diagonal\nx - random            : ")
    travelvars = ['r','c','m','s','x'] #travel options (row, column, main diagonal, secondary diagonal, random)
    while travel not in travelvars: #validation check for travelvars
        print
        travel = raw_input ("Not a valid input.\nHow do you want " + name + " to travel?\nr - row\nc - col\nm - main diagonal\ns - secondary diagonal\nx - random: ")
    print
    topaccum = 0
    if (travel == "r"): #travel along a row
        row = raw_input("Number row(0 to " + str(size-1) + "):" )
        topflag = True
        while topflag == True:
            if not row.isdigit(): #validation check 
                row = raw_input("The value should only have digits, please re-enter: ")
            else:
                introw = int(row)
                if introw<=(size-1) and introw>=0: 
                    topflag = False
                else:
                    row = raw_input("That is not a valid input, please re-enter: ")
        listfunc = hunterpath_row(introw) #Use row traveloption 
        topaccum = topaccum + listfunc[0] 
        topflag = listfunc[1]
        checkflag = listfunc[2]
    elif (travel == "c"): #travel along a column
        col = raw_input("Number col(0 to " + str(size-1) + "):" )
        topflag = True
        while topflag == True:
            if not col.isdigit(): #validation check
                col = raw_input("The value should only have digits, please re-enter: ")
            else:
                intcol = int(col) #convert string column into integer column
                if intcol<=(size-1) and intcol>=0: #validation check
                    topflag = False
                else:
                    col = raw_input("That is not a valid input, please re-enter: ")
        listfunc = hunterpath_col(intcol) #use column function
        topaccum = topaccum + listfunc[0]
        topflag = listfunc[1]
        checkflag = listfunc[2]
    elif (travel == "m"): #travel along main diagonal
        listfunc = hunterpath_main() #use main diagonal function
        topaccum = topaccum + listfunc[0]
        topflag = listfunc[1]
        checkflag = listfunc[2]
    elif (travel == "s"): #travel along secondary diagonal
        listfunc = hunterpath_second() #use secondary diagonal function
        topaccum = topaccum + listfunc[0]
        topflag = listfunc[1]
        checkflag = listfunc[2]
    elif (travel == "x"): #travel randomly
        rand = raw_input("How many random cells shall " + name + " visit(Between row*col): ") #asks hunter how many cells to travel
        topflag = True
        while topflag == True:
            if not rand.isdigit(): #validation check for digits
                rand = raw_input("The value should only have digits, please re-enter: ")
            else:
                intrand = int(rand)
                if intrand<=(size*size): #validation check for square matrix
                    topflag = False
                else:
                    rand = raw_input("That is not a valid input, please re-enter: ")
        listfunc = hunterpath_rand(intrand) #use random travel function
        topaccum = topaccum + listfunc[0]
        topflag = listfunc[1]
        checkflag = listfunc[2]
    return [topaccum,topflag,checkflag]

def convert_2_to_10_values(binary): #converts to base 10 from binary generate statement
    add = 0
    dim = len(binary)
    values = ''
    for i in range(0,dim):
        stor = 0
        for p in range(0,dim):
            digit = binary[i][p]
            expon = dim -1 -p #
            add = add + digit*2**expon #convert base 10 to base 2
            stor = stor + digit*2**expon #stores convert base 10 to base 2 value
        values = values + str(stor) + ","
    return values

def convert_2_to_10(binary): #converts to base 10 from binary
    add = 0
    dim = len(binary)
    values = ''
    for i in range(0,dim):
        stor = 0
        for p in range(0,dim):
            digit = binary[i][p]
            expon = dim -1 -p
            add = add + digit*2**expon
            stor = stor + digit*2**expon
        values = values + str(stor)
    return add

####################################################
#                    TOP LEVEL                     #
####################################################

print ("Welcome to the 'Diamond Treasure Hunter' Game") #welcomes user
print

anothergame = True #flag to run the game 
play = raw_input ("Would you like to play? (y/n): ") #asks user if they would like to play
print
pointsoverall = 0
players = 0
maxhunter = ""
maxscore = 0
minhunter = ""
minlucky = 100000000000000
while anothergame == True: #validation check to start the game
    players = players + 1 #amount of players
    while play != 'y' and play != 'n' and anothergame == True: #validaiton check
        play = raw_input("Please provide a proper response (y/n): ")
    if play == "n": #end game
        print ("Goodbye!")
        break
    elif play == "y":
        print ("Let's play the game!\n(May the odds be ever in your favour)")
        print
        name = raw_input ("Name of treasure hunter: ") #ask user for name of hunter
        print
        rawsize = raw_input ("Size of board (between 3 and 6 inclusive): ") #ask user size of board desired
        sizeflag = True
        while sizeflag == True:
            if not rawsize.isdigit():
                rawsize = raw_input("The value should only have digits, please re-enter: ") #validate size of board
            else:
                size = int(rawsize)
                if size<=6 and size>2:
                    sizeflag = False
                else:
                    rawsize = raw_input("Please enter a valid value for size of board (between 3 and 6 inclusive): ")
        print
        creation = raw_input ("Creation of board? (r-random, u-user): ") #creation of board user or random generated
        print
        while creation != "u" and creation != "r": #validation check for creation of the board
            creation = raw_input("That is not a valid input, please re-enter: ") #validate creation of board
        if creation == "u": #user inputed list
            board = input ("Provide a list of lists, same number of rows and columns \nwith integer numbers between 0 and 10 inclusive \nand maybe one -1: ")
        elif creation == "r": #random list
            diam = raw_input ("Maximum number of diamonds in a cell (from 1 to 10): ") #max number of diamonds in cell
            diamflag = True
            while diamflag == True: #validation check
                if not diam.isdigit():
                    diam = raw_input("The value should only have digits, please re-enter: ")
                else:
                    maxdiam = int(diam)
                    if maxdiam<=10 and maxdiam>=1:
                        diamflag = False
                    else:
                        diam = raw_input("That is not a valid input, please re-enter: ")
            board = ran_board(size) 
            random_row = random.randint(0,len(board)-1)
            random_col = random.randint(0,len(board)-1)
            random_value = random.randint(1,10)
            if (random_value < 8): #ADDITIONAL: 80% chance of getting -1 in one of the cell
                board[random_row][random_col] = -1
            print (board) 
    print "Board is :"
    displayboard() #game board gets displayed
    
    points = 0

    listfunc = traveloptions() #calling upon values within the function
    points = points + listfunc[0] #accumulating points within a game
    pointsoverall = pointsoverall + points #accumulating points overall, finding max points
    topflag = listfunc[1]
    checkflag = listfunc[2]

    binary = []
    for row in range(len(board)):
        r = []
        for i in range(len(board)):
            if(int(board[row][i] % 2 == 0)): #create a binary board with 0 and 1
               r.append(0)
            else:
                r.append(1)
        binary.append(r)
    
    while topflag == True:
        travel_again = raw_input ("Do you want " + name + " to do another trip? (y/n): ") #ask user if he/she wants to play another game
        if (travel_again == "y"): #hunter wants to travel again
            print "Board is :"
            displayboard()
            listfunc = traveloptions()
            points = points + listfunc[0]
            pointsoverall = pointsoverall + points #points accumulated overall by hunter(s)
            topflag = listfunc[1]
            checkflag = listfunc[2]
            
        elif (travel_again == "n"): #hunter would not like to travel again
            print ("The treasure hunter " + name + " obtained " + str(points) + " points in his/her game")
            print
            print ("The values of each row in the board(as binary number) are: ")
            print (str(convert_2_to_10_values(binary)) + " and therefore the board lucky number is: " + str(convert_2_to_10(binary)))
            topflag = False

    if checkflag == 1 and topflag == False: #when hunter gets trapped in his game, comes upon a -1
        print ("The treasure hunter " + name + " became trapped\nand he/she can't travel again.")
        print ("The treasure hunter " + name + " obtained " + str(points) + " points in his/her game.")
        print
        print ("The values of each row in the board(as binary number) are: ")
        print (str(convert_2_to_10_values(binary)) + " and therefore the board lucky number is: " + str(convert_2_to_10(binary)))

    if points>=maxscore: #replacing maxscore if another value was found to be greater than or equal to
        maxscore = points #max score
        maxhunter = name #max score associated with the hunger
        if checkflag == 1: #check hunter if trapped or fine
            statusmax = 'trapped'
        else:
            statusmax = 'fine'
    if convert_2_to_10(binary) <= minlucky: #replacing minlucky if another value was lesser than or equal to
        minlucky = str(convert_2_to_10(binary))
        minhunter = name
        if checkflag == 1: 
            statusmin = 'trapped'
        else:
            statusmin = 'fine'
    print
    play_again = raw_input("Would you like to play again? (y/n): ") #starting game over
    while play_again != 'y' and play_again != 'n':
        play_again = raw_input("Please provide a proper response (y/n): ")
    if play_again == "y":
        anothergame = True
        print '\n'
        print '####################################################'
        print '#~*~~~~~*~~~~*~~~*~~Another Game~~*~~~*~~~~*~~~~~*~#'
        print '####################################################'
        print '\n'
    if play_again == "n":
        anothergame = False #This ends the game 
        print "Total hunters that played: ",players 
        print
        print "Total points of all hunters: ",pointsoverall
        print
        print "Maximum hunter points: \nThe hunter " + maxhunter + ", who is " + statusmax + "\ngot the maximum points: " + str(maxscore)
        print
        print "Minimum lucky number: \nThe board with the hunter " + minhunter + ", who is " + statusmin + "\ngot the minimum lucky number: " + str(minlucky)
        print "Bye!"
        














