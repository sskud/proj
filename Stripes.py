from random import randint

board = []

for x in range(3):
    board.append([" "] * 7)
    
for x in range(2,5):
    board[0][x] = "|"
for x in range(1,6):
    board[1][x] = "|"
for x in range(0,7):
    board[2][x] = "|"
    
def print_board(board):
    for row in board:
        print " ".join(row)
        
print "Let's play Stripes!"
print "Here are the rules: you fail, if you cross out the last stripe. You can once cross out one or some stripes only between crosses or in a clear row."
print_board(board)



def random_row(board):           #Computer choose a row
    r = randint(0, 2)
    flag = 0
    for i in range(7):
        if board[r][i]=="|":
            flag += 1
    if flag == 0:
        while flag == 0:
            r = randint(0, 2)
            for i in range(7):
                if board[r][i]=="|":
                    flag += 1
    return r

def random_stripe(board,row):   #Computer choose a stripe
    if row == 0:
        s = randint(2,4)
        if board[row][s]=="x":
            while board[row][s]=="x":
                s = randint(2,4)
        return s
    elif row == 1:
        s = randint(1,5)
        if board[row][s]=="x":
            while board[row][s]=="x":
                s = randint(1,5)
        return s
    elif row == 2:
        s = randint(0,6)
        if board[row][s]=="x":
            while board[row][s]=="x":
                s = randint(0,6)
        return s

def random_len(board,row,stripe):   #Computer choose the quantity of stripes
    if row == 0:
        for i in range(stripe, len(board[row])):
            if board[row][i]=="x" or board[row][i]==" ":
                break
        return randint(1, i - stripe)
    elif row == 1:
        for i in range(stripe, len(board[row])):
            if board[row][i]=="x" or board[row][i]==" ":
                break
        return randint(1, i - stripe)
    elif row == 2:
        for i in range(stripe, len(board[row])):
            if board[row][i]=="x" or board[row][i]==" ":
                break
        return randint(1, i - stripe)
        
        
        
for z in range(16):             #Common loop for the game
    flag = 0
    for x in range(3):         #Check for the end of the game
        for i in range(7):
            if board[x][i] == "|":
                flag += 1
    if flag == 1:
        print "You failed!!!"
        break
        
    '''Human's step'''
    c_row = int(raw_input("Input number of a row. Count from up to down. There must be at least one stripe in the row.")) - 1
    flag = 0
    for i in range(7):
        if board[c_row][i]=="|":
            flag += 1
    if flag == 0:
        print "You have done a forbidden step. You failed."
        break
    if c_row==0:
        c_stripe = int(raw_input("Input number of stripe. Count from left to right though all of the stripes and crosses.")) +1
    elif c_row==1:
        c_stripe = int(raw_input("Input number of stripe. Count from left to right though all of the stripes and crosses.")) 
    elif  c_row==2:
        c_stripe = int(raw_input("Input number of stripe. Count from left to right though all of the stripes and crosses.")) -1
    if board[c_row][c_stripe] == "x" or board[c_row][c_stripe] == " ":
        print "You have done a forbidden step. You failed."
        break
    
    c_s_len = int(raw_input("Input the quantity of stripes, you want to cross out."))
    flag = 0
    for i in range(c_stripe, c_stripe + c_s_len):
        if board[c_row][i] == "x" or board[c_row][i] == " ":
            flag = 1
    if flag == 1:
        print "You have done a forbidden step. You failed."
        break
    
    for x in range(c_stripe, c_stripe + c_s_len):
        board[c_row][x] = "x"
    print_board(board)
    
    
    flag = 0
    for x in range(3):         #Check for the end of the game
        for i in range(7):
            if board[x][i] == "|":
                flag += 1
    if flag == 0:
        print "You fail!!!"
        break
    
    
    flag = 0
    for x in range(3):         #Check for the end of the game
        for i in range(7):
            if board[x][i] == "|":
                flag += 1
    if flag == 1:
        print "You win!!!"
        break
    
    '''Computer's step '''
    row = random_row(board)
    print row+1
    stripe = random_stripe(board,row)
    print stripe+1
    s_len = random_len(board,row,stripe)
    print s_len+1
    
    for x in range(stripe, stripe + s_len):
        board[row][x] = "x"
    print_board(board)
    
    flag = 0
    for x in range(3):         #Check for the end of the game
        for i in range(7):
            if board[x][i] == "|":
                flag += 1
    if flag == 0:
        print "You win!!!"
        break
    
    
    
    
    
