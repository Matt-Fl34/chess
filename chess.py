import os

chessboard = {'A1' : 'wR', 'B1' : 'wH', 'C1' : 'wB', 'D1' : 'wQ', 'E1' : 'wK', 'F1' : 'wB', 'G1' : 'wH', 'H1' : 'wR',
              'A2' : 'wP', 'B2' : 'wP', 'C2' : 'wP', 'D2' : 'wP', 'E2' : 'wP', 'F2' : 'wP', 'G2' : 'wP', 'H2' : 'wP',
              'A3' : '  ', 'B3' : '  ', 'C3' : '  ', 'D3' : '  ', 'E3' : '  ', 'F3' : '  ', 'G3' : '  ', 'H3' : '  ',
              'A4' : '  ', 'B4' : '  ', 'C4' : '  ', 'D4' : '  ', 'E4' : '  ', 'F4' : '  ', 'G4' : '  ', 'H4' : '  ',
              'A5' : '  ', 'B5' : '  ', 'C5' : '  ', 'D5' : '  ', 'E5' : '  ', 'F5' : '  ', 'G5' : '  ', 'H5' : '  ',
              'A6' : '  ', 'B6' : '  ', 'C6' : '  ', 'D6' : '  ', 'E6' : '  ', 'F6' : '  ', 'G6' : '  ', 'H6' : '  ',
              'A7' : 'bP', 'B7' : 'bP', 'C7' : 'bP', 'D7' : 'bP', 'E7' : 'bP', 'F7' : 'bP', 'G7' : 'bP', 'H7' : 'bP',
              'A8' : 'bR', 'B8' : 'bH', 'C8' : 'bB', 'D8' : 'bQ', 'E8' : 'bK', 'F8' : 'bB', 'G8' : 'bH', 'H8' : 'bR',}

#dictionary that assigns numerical values to each column, used for doing mathematical calculations
column_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}

#list of keys in column_dict, would've made some calculations i'd done earlier a lot easier, but it's working so i'm not going to re-do them now
#This will help tremendously with collision detection for diagonal movement:
column_list = list(column_dict)


white_turn = True    #used to differenciate between white and black turns 

top_of_screen_msg1 = '' #used for storing messages to be printed at the beginning of a new game loop 
                        #just makes things neater 



def disp_board(board):
    print('    A    B    C    D    E    F    G    H')
    print('  |----|----|----|----|----|----|----|----|')
    print('8 |', board['A8'], '|', board['B8'], '|', board['C8'], '|', board['D8'], '|', board['E8'], '|', board['F8'], '|', board['G8'], '|', board['H8'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('7 |', board['A7'], '|', board['B7'], '|', board['C7'], '|', board['D7'], '|', board['E7'], '|', board['F7'], '|', board['G7'], '|', board['H7'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('6 |', board['A6'], '|', board['B6'], '|', board['C6'], '|', board['D6'], '|', board['E6'], '|', board['F6'], '|', board['G6'], '|', board['H6'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('5 |', board['A5'], '|', board['B5'], '|', board['C5'], '|', board['D5'], '|', board['E5'], '|', board['F5'], '|', board['G5'], '|', board['H5'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('4 |', board['A4'], '|', board['B4'], '|', board['C4'], '|', board['D4'], '|', board['E4'], '|', board['F4'], '|', board['G4'], '|', board['H4'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('3 |', board['A3'], '|', board['B3'], '|', board['C3'], '|', board['D3'], '|', board['E3'], '|', board['F3'], '|', board['G3'], '|', board['H3'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('2 |', board['A2'], '|', board['B2'], '|', board['C2'], '|', board['D2'], '|', board['E2'], '|', board['F2'], '|', board['G2'], '|', board['H2'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('1 |', board['A1'], '|', board['B1'], '|', board['C1'], '|', board['D1'], '|', board['E1'], '|', board['F1'], '|', board['G1'], '|', board['H1'], '|',  )
    print('  |----|----|----|----|----|----|----|----|')
    print('    A    B    C    D    E    F    G    H')

def pawn_move(position):
    #initialising variables:
    global white_turn
    first_move = False
    attack = False
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')#getting the square the player wishes to move to
        pl_move = pl_move.upper()#So that the user can enter lowercase letters without causing errors
        
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
        
        try: 
           
            #Writing the movement code for white pawns:
            if chessboard[position][0] == 'w':     
                
                if chessboard[pl_move][0] == 'w': #code that doesn't allow player to move pawn onto their own colour
                    print('Not a Valid Move. Try Again')
                    continue
                
                if  position[1] == '2':#Checking if pawn in starting position, and if it is, setting
                    first_move = True  #first_move to True, which means it's allowed to move two spaces this turn
                
                if chessboard[pl_move][0] == 'b' and int(pl_move[1]) - int(position[1]) == 1:#Checking if pawn is trying to take another piece, calculating that the move is one row up and setting attack to True if that is.
                    attack = True                                                            #This allows the pawn to move diagonally for this move
                
                #code for if it's the pawn's first move:
                if first_move == True and attack == False:
                   if collision_detect(pl_move, position) == False:#checking for collision
                       if (int(pl_move[1]) - int(position[1]) <= 2 ) and pl_move[0] == position[0]:#If the diffirence between the position of the pawn and the intended move is 2 or less and the pawn stays
                            chessboard[pl_move] = chessboard[position]                              #in the same column it's a valid move
                            chessboard[position] = '  '
                            first_move = False
                            if white_turn == True:
                                white_turn = False #the white_turn variable needs to be changed here bacause a valid move was made
                            else:                  #which means that it's the other persons turn now
                                white_turn = True   
                            break
                       else:
                            print('Not a Valid Move. Try Again')
                
                #code for if it's not the pawn's first move:        
                if first_move == False and attack == False:
                    if (int(pl_move[1]) - int(position[1]) == 1) and pl_move[0] == position[0]:#If first move is False then the pawn is only allowed
                        chessboard[pl_move] = chessboard[position]                             #to move one space in the same column
                        chessboard[position] = '  '
                        if white_turn == True:
                            white_turn = False #the white_turn variable needs to be changed here bacause a valid move was made
                        else:                  #which means that it's the other persons turn now
                            white_turn = True   
                        break
                    else:
                        print('Not a Valid Move. Try Again')
                    
                #code for if the pawn tries to take another piece:
                if attack == True:
                    if abs(column_dict[position[0]] - column_dict[pl_move[0]]) == 1:#Using numerical values in column_dict to detirmine that the move is
                        chessboard[pl_move] = chessboard[position]                  #one column away to either side. that's why abs() is important, the correct answer
                        chessboard[position] = '  '                                 #could be either 1 or -1(the fact that the move is one row up is determined when the attack variable gets set to True)
                        attack = False
                        if white_turn == True:
                            white_turn = False #the white_turn variable needs to be changed here because a valid move wa made
                        else:                  #which means that it's the other persons turn now
                            white_turn = True   
                        break
                    else:
                        print('Not a Valid Move. Try Again')
                        attack = False
            
            
            #Writing the movement code for black pawns:
            if chessboard[position][0] == 'b': 
                
                if chessboard[pl_move][0] == 'b': #code that doesn't allow player to move pawn onto their own colour
                    print('Not a Valid Move. Try Again')
                    continue
                
                if  position[1] == '7':#Checking if pawn in starting position, and if it is, setting
                    first_move = True  #first_move to True, which means it's allowed to move two spaces this turn
                
                if chessboard[pl_move][0] == 'w' and abs(int(pl_move[1]) - int(position[1])) == 1:#Checking if pawn is trying to take another piece, calculating that the move is one row up(or down) and setting attack to True if that is.
                    attack = True                                                                 #This allows the pawn to move diagonally for this move
                
                #code for if it's the pawn's first move:
                if first_move == True and attack == False:
                   if collision_detect(pl_move, position) == False:#checking for collision
                       if abs(int(pl_move[1]) - int(position[1])) <= 2  and pl_move[0] == position[0]:#If the diffirence between the position of the pawn and the intended move is 2 or less and the pawn stays
                            chessboard[pl_move] = chessboard[position]                                #in the same column it's a valid move
                            chessboard[position] = '  '
                            first_move = False
                            if white_turn == True:
                                white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                            else:                  #which means that it's the other persons turn now
                                white_turn = True   
                            break
                       else:
                            print('Not a Valid Move. Try Again')
                
                #code for if it's not the pawn's first move:        
                if first_move == False and attack == False:
                    if (abs(int(pl_move[1]) - int(position[1])) == 1) and pl_move[0] == position[0]:#If first move is False then the pawn is only allowed
                        chessboard[pl_move] = chessboard[position]                                  #to move one space in the same column
                        chessboard[position] = '  '                                          
                        if white_turn == True:
                            white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                        else:                  #which means that it's the other persons turn now
                            white_turn = True   
                        break
                    else:
                        print('Not a Valid Move. Try Again')
                    
                #code for if the pawn tries to take another piece:
                if attack == True:
                    if abs(column_dict[position[0]] - column_dict[pl_move[0]]) == 1:#Using numerical values in column_dict to detirmine that the move is
                        chessboard[pl_move] = chessboard[position]                  #one column away to either side. that's why abs() is important, the correct answer
                        chessboard[position] = '  '                                 #could be either 1 or -1(the fact that the move is one row up is determined when the attack variable gets set to True)
                        attack = False
                        if white_turn == True:
                            white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                        else:                  #which means that it's the other persons turn now
                             white_turn = True   
                        break
                    else:
                        print('Not a Valid Move. Try Again')
                        attack = False
       
        except KeyError:
            pass
        
def king_move(position):
    
    global white_turn
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')
        pl_move = pl_move.upper()#So that the user can enter lowercase letters without causing errors
        
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play 
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
        
        try:    
            if chessboard[pl_move][0] == chessboard[position][0]: #code that doesn't allow player to move king onto their own colour
                print('Not a Valid Move. Try Again')
                continue
        
            #This here fixes the 'super king' bug:     it's messy but it works
            if abs(column_dict[pl_move[0]] - column_dict[position[0]]) > 1 or abs(int(pl_move[1]) - int(position[-1])) >1:
                print('Not a Valid Move. Try Again.')
                continue
            
            
            #checking that the intended move is one block in any direction, which would make it a valid move:    
            if abs(int(pl_move[1]) - int(position[-1])) == 1 or abs(column_dict[pl_move[0]] - column_dict[position[0]]) == 1:
                chessboard[pl_move] = chessboard[position]
                chessboard[position] = '  '
                if white_turn == True:
                    white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                else:                  #which means that it's the other persons turn now
                    white_turn = True   
                break
            else:
                print('Not a Valid Move. Try Again.')
        
        except KeyError:
            pass
            
def rook_move(position):
    
    global white_turn
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')
        pl_move = pl_move.upper()#So that the user can enter lowercase letters without causing errors  
            
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play    
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
            
        try:
            if chessboard[pl_move][0] == chessboard[position][0]: #code that doesn't allow player to move rook onto their own colour
                print('Not a Valid Move. Try Again')
                continue
            
            if collision_detect(pl_move, position) == False:
                if pl_move[0] == position[0] or pl_move[1] == position[1]:#checking that move is in same column or same row
                    chessboard[pl_move] = chessboard[position]
                    chessboard[position] = '  '
                    if white_turn == True:
                        white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                    else:                  #which means that it's the other persons turn now
                        white_turn = True   
                    break
                else:
                    print('Not a Valid Move. Try Again')
        
        except KeyError:
            pass
                   
            
def knight_move(position):
    
    global white_turn
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')
        pl_move = pl_move.upper()#So that the user can enter lowercase letters without causing errors 
            
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
        
        
        if chessboard[pl_move][0] == chessboard[position][0]: #code that doesn't allow player to move knight onto their own colour
            print('Not a Valid Move. Try Again')
            continue
        
        try:
        #checking moves available to knight:
            if abs(int(pl_move[1]) - int(position[1])) == 1 and abs(column_dict[pl_move[0]] - column_dict[position[0]]) == 2:#moving two spaces to the side then one space up/down
                chessboard[pl_move] = chessboard[position]
                chessboard[position] = '  '
                if white_turn == True:
                    white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                else:                  #which means that it's the other persons turn now
                    white_turn = True   
                break
            elif abs(int(pl_move[1]) - int(position[1])) == 2 and abs(column_dict[pl_move[0]] - column_dict[position[0]]) == 1:#moving one space to the side then two spaces up/down
                chessboard[pl_move] = chessboard[position]
                chessboard[position] = '  '
                if white_turn == True:
                    white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                else:                  #which means that it's the other persons turn now
                    white_turn = True   
                break
            else:
                print('Not a Valid Move. Try Again')
        
        except KeyError:
            pass

def bishop_move(position):
    
    global white_turn
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')
        pl_move = pl_move.upper()#So that the user can enter lower case letters without causing errors
        
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play   
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
        
        try:    
            if chessboard[pl_move][0] == chessboard[position][0]: #code that doesn't allow player to move bishop onto their own colour
                print('Not a Valid Move. Try Again')
                continue
            
            if collision_detect(pl_move, position) == False:
                if abs(int(pl_move[1]) - int(position[1])) == abs(column_dict[pl_move[0]] - column_dict[position[0]]):#checking that the move is diagonal
                    chessboard[pl_move] = chessboard[position]
                    chessboard[position] = '  '
                    if white_turn == True:
                        white_turn = False #the white_turn variable needs to be changed here becase a valid move was made
                    else:                  #which means that it's the other persons turn now
                        white_turn = True   
                    break
                else:
                    print('Not a Valid Move. Try Again')
       
        except KeyError:
           pass
        
def queen_move(position):
    
    global white_turn
    
    while True:
        print('Which Square Would You Like To Move To? (Enter "e" To Exit And Choose Another Piece)')
        pl_move = input('>')
        pl_move = pl_move.upper()#So that the user can enter lower case letters without causing errors
        
        if pl_move.lower() == 'e': #Way for player to exit loop and choose another piece to play   
            break
        
        if pl_move not in chessboard.keys():#Validating that player move is a valid chessboard space
            print('Not a Valid Move. Try Again.')
        
        try:    
            if chessboard[pl_move][0] == chessboard[position][0]: #code that doesn't allow player to move queen onto their own colour
                print('Not a Valid Move. Try Again')
                continue
            
            if collision_detect(pl_move, position) == False:
                #checking if move is horizontal
                if pl_move[1] == position[1]:
                    chessboard[pl_move] = chessboard[position]
                    chessboard[position] = '  '
                    if white_turn == True:
                        white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                    else:                  #which means that it's the other persons turn now
                        white_turn = True   
                    break
                #checking if move is vertical
                elif pl_move[0] == position[0]:
                    chessboard[pl_move] = chessboard[position]
                    chessboard[position] = '  '
                    if white_turn == True:
                        white_turn = False #the white_turn variable needs to be changed here because a valid move was made
                    else:                  #which means that it's the other persons turn now
                        white_turn = True   
                    break
                #checking if move is diagonal
                elif abs(int(pl_move[1]) - int(position[1])) == abs(column_dict[pl_move[0]] - column_dict[position[0]]):
                    chessboard[pl_move] = chessboard[position]
                    chessboard[position] = '  '
                    if white_turn == True:
                        white_turn = False #the white_turn variable needs to be changed because a valid move was made
                    else:                  #which means that it's the other persons turn now
                        white_turn = True   
                    break
                else:
                    print('Not a Valid Move. Try Again')
        
        except KeyError:
            pass
            
#Function to detect any collision in the move
def collision_detect(move, position):
    #Checking collision if the move is in the same column:
    if move[0] == position[0]:
        if int(move[1]) - int(position[1]) > 0:#if the diffirence between these values is positive that means we're moving up the column
            counter = 1                        #negative means moving down, obviously
        else:                  #initialising counters for both moving up and moving down the column
            counter = -1
        #find difference between position and move, and iterate that many times .abs() impportant for moving down the column or else this statement would return a negative value        
        for i in range(abs(int(move[1]) - int(position[1])) - 1):#the -1 at the end is because the last block might be the player taking an apponent piece. so, not collision
            if chessboard[(position[0] + str(int(position[1]) + counter))] != '  ':#incrementing block to be checked by 1 (or -1) for each iteration.if block is not empty return True
                print('Not a Valid Move. Try Again')
                return True#if block is not empty return True
            
            if counter > 0:
                counter += 1   #incrementing counters for moving up(positive) and down(negative) the column
            else:
                counter -= 1
            
        return False#once all blocks have been checked return False
    
    #checking collision if move is in the same row:
    if move[1] == position[1]:
        if column_dict[move[0]] - column_dict[position[0]] > 0:#if the diffirence between these values is positive that means we're moving right in the row
            counter = 1                                        #negative means moving left, obviously
        else:             #initialising counters for moving right(positive) and left(negative)
            counter = -1
        #find difference between position and move and iterate that many times .abs() impportant for moving down the column or else this statement would return a negative value    
        for i in range(abs(column_dict[move[0]] - column_dict[position[0]]) - 1):#the -1 at the end is because the last block might be the player taking an apponent piece. so, not collision
            #this whole statement was a fkn headache. just know that I had to make column_dict a list so i could slice into the keys using the numerical values of that dictionary            
            if chessboard[list(column_dict)[column_dict[position[0]] + counter - 1] + position[1]] != '  ':#the counter - 1 is neccesary because arrays start at 0
                print('Not a Valid Move. Try Again')
                return True
            
            if counter > 0:
                counter += 1
            else:
                counter -= 1
    
    #collision detection for diagonal movement:
    if abs(int(move[1]) - int(position[1])) == abs(column_dict[move[0]] - column_dict[position[0]]):
       
       #moving diagonally up to the right
        if int(move[1]) - int(position[1]) > 0 and column_dict[move[0]] - column_dict[position[0]] > 0:
            row_counter = 1     #since it's diagonal movement, we need to set up counters for horizontal as well as vertical movement
            column_counter = 1
            
            for i in range(int(move[1]) - int(position[1]) - 1) :           #this -1  V  beacause i'm slicing into a list (starts at 0)
                if chessboard[column_list[column_dict[position[0]] + column_counter - 1] + str(int(position[1]) + row_counter)] != '  ':
                    print('Not a Valid Move. Try Again.')
                    return True
                column_counter += 1
                row_counter += 1
                
        #moving diagonally up to the left
        if int(move[1]) - int(position[1]) > 0 and column_dict[move[0]] - column_dict[position[0]] <  0:
            row_counter = 1     
            column_counter = -1
            
            for i in range(int(move[1]) - int(position[1]) - 1) :           #this -1  V  beacause i'm slicing into a list (starts at 0)
                if chessboard[column_list[column_dict[position[0]] + column_counter - 1] + str(int(position[1]) + row_counter)] != '  ':
                    print('Not a Valid Move. Try Again.')
                    return True
                column_counter -= 1
                row_counter += 1
                
        #moving diagonally down to the left
        if int(move[1]) - int(position[1]) < 0 and column_dict[move[0]] - column_dict[position[0]] < 0:
            row_counter = -1     
            column_counter = -1
            
            for i in range(abs(int(move[1]) - int(position[1])) - 1) :      #this -1  V  beacause i'm slicing into a list (starts at 0)
                if chessboard[column_list[column_dict[position[0]] + column_counter - 1] + str(int(position[1]) + row_counter)] != '  ':
                    print('Not a Valid Move. Try Again.')
                    return True
                column_counter -= 1
                row_counter -= 1
                
        #moving diagonally down to the right
        if int(move[1]) - int(position[1]) < 0 and column_dict[move[0]] - column_dict[position[0]] > 0:
            row_counter = -1    
            column_counter = 1
            
            for i in range(abs(int(move[1]) - int(position[1])) - 1) :      #this -1  V  beacause i'm slicing into a list (starts at 0)
                if chessboard[column_list[column_dict[position[0]] + column_counter - 1] + str(int(position[1]) + row_counter)] != '  ':
                    print('Not a Valid Move. Try Again.')
                    return True
                column_counter += 1
                row_counter -= 1        
                
    return False        
            
                
#Main game loop:
while True:
    
    os.system('cls')
    disp_board(chessboard)
    
    print(top_of_screen_msg1)
    top_of_screen_msg1 = ''
    
    if white_turn == True:#the white_turn variable starts out as True and changes each time a valid move is performed
        print('White Turn')
        print("Choose a Piece To Play By Selecting Its Square.")
        
    else:
        print('Black Turn')
        print("Choose a Piece To Play By Selecting Its Square.")    
        
    piece = input('>')
    piece = piece.upper()
    
    try:
        
        if piece not in chessboard.keys() or chessboard[piece] == '  ':#making sure selected square is on the board and is not empty
            top_of_screen_msg1 = 'No Piece Selected \n'
            continue
        
        if white_turn == True and chessboard[piece][0] != 'w':  #ensuring the user chose the right colour for who's turn it is
            top_of_screen_msg1 = 'Wrong Colour \n'
            continue
        
        if white_turn == False and chessboard[piece][0] != 'b':
            top_of_screen_msg1 = 'Wrong Colour \n'
            continue
    
    
        if chessboard[piece][1] == 'P':
            pawn_move(piece)
        if chessboard[piece][1] == 'K':
            king_move(piece)
        if chessboard[piece][1] == 'R':
            rook_move(piece)
        if chessboard[piece][1] == 'H':
            knight_move(piece)
        if chessboard[piece][1] == 'B':
            bishop_move(piece)
        if chessboard[piece][1] == 'Q':
            queen_move(piece)
    
    except KeyError:
        top_of_screen_msg1 = 'Incorrect Input \n'
            

