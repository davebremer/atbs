# Write a function named isValidChessBoard() that takes a dictionary argument and returns 
# True or False depending on if the board is valid.
#
# DONE: A valid board will have exactly one black king and exactly one white king. 
#
# DONE Each player can only have at most 16 pieces, 
# DONE at most 8 pawns, 
# DONE and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
# 
# DONE The piece names begin with either a 'w' or 'b' to represent white or black, 
# DONE followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
# This function should detect when a bug has resulted in an improper chess board.

def validateSquares(squares):
    validSquares = True
    for s in squares:
        if ( not s[0].isnumeric() or 
            int(s[0]) not in range(1,9) or 
            s[1] < 'a' or 
            s[1] > 'h'
        ):
           #print(s + ' not valid')
             
            validSquares = False
    return(validSquares)

def validatePieces(pieces):
    validPieces = True
    for p in pieces:
        if p[0] not in ['w','b']:
            validPieces = False
            #print(p + ' not valid piece - ' + p[0] + ' not b or w')
        if p[1:] not in ['pawn','knight','bishop','rook','queen','king']:
            validPieces = False
            # print(p[1:] + ' is not valid')
        
    return(validPieces)

def isValidChessBoard(board):
    validated = True
    thePieces = list(board.values())
    theSquares = list(board.keys())

    if not validateSquares(theSquares) :
        validated = False
    
    if not validatePieces(thePieces):
        validated = False

    whiteCount = 0
    blackCount = 0

    for i in thePieces:
        if i.startswith('w'):
            whiteCount += 1
        elif i.startswith('b'):
            blackCount += 1
        else: validated = False
    
    # print('Whites: ' + str(whiteCount))
    # print('Blacks: ' + str(blackCount))
    
    if whiteCount > 16 or blackCount > 16:
        validated = False

    if (thePieces.count('bking') != 1 or
        thePieces.count('bpawn') > 8 or
        thePieces.count('bknight') > 2 or
        thePieces.count('bbishop') > 2 or
        thePieces.count('brook') > 2 or
        thePieces.count('bqueen') > 1 or
        thePieces.count('wking') != 1 or
        thePieces.count('wpawn') > 8 or
        thePieces.count('wknight') > 2 or
        thePieces.count('wbishop') > 2 or
        thePieces.count('wrook') > 2 or
        thePieces.count('wqueen') > 1 
        ):
        validated = False

    return(validated)

print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "wqueen", "3e": "wking"}))  # false two white queens
print(isValidChessBoard({"1a": "bpawn", "2a": "wking"}))  # False: no bking
print(isValidChessBoard({"1a": "wking", "2a": "wking", "3c": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(isValidChessBoard({"1a": "bking", "9z": "wking"}))  # False: 9z is an invalid position
print(isValidChessBoard({"1a": "bking", "aa": "wking"}))  # False: 9z is an invalid position
print(isValidChessBoard({"1h": "bking", "6c": "queen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # false queen not on b or w
