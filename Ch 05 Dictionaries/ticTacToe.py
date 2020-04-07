# todo:
 # done 1) check if value already set - turn stays the same
 # done 2) force case
 # done 3) if typo (ie key doesn't match) repeat turn
 # done 4) check for win - see https://stackoverfLOW.com/questions/37376516/python-check-if-multiple-variables-have-the-same-value
 # done 5) check if all 9 suqares complete. If no win then draw

theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
            'LOW-L': ' ', 'LOW-M': ' ', 'LOW-R': ' '}

def printBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
    print('-+-+-')
    print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
    print('-+-+-')
    print(board['LOW-L'] + '|' + board['LOW-M'] + '|' + board['LOW-R'])

def won(board):    
    if (((board['TOP-L'] == board['TOP-M'] == board['TOP-R']) and board['TOP-L'] != " ") or
        ((board['MID-L'] == board['MID-M'] == board['MID-R'])  and board['MID-L'] != " ") or
        ((board['LOW-L'] == board['LOW-M'] == board['LOW-R'])  and board['LOW-L'] != " ") or
        ((board['TOP-L'] == board['MID-M'] == board['LOW-R'])  and board['TOP-L'] != " ") or
        ((board['TOP-R'] == board['MID-M'] == board['LOW-L']) and board['TOP-R'] != " ") or
        ((board['TOP-L'] == board['MID-L'] == board['LOW-L']) and board['TOP-L'] != " ") or
        ((board['TOP-M'] == board['MID-M'] == board['LOW-M']) and board['TOP-M'] != " ") or
        ((board['TOP-R'] == board['MID-R'] == board['LOW-R']) and board['TOP-R'] != " ")
    ):
        return(True)
    else:
        return(False)

def finished(board):
    return not(' ' in board.values())


turn = 'X'
playerWon = False
while not playerWon and not finished(theBoard):
    used = True
    while used:
        printBoard(theBoard)
        print('\nTurn for ' + turn + '. Move on which space?')
        print('row: TOP, MID, LOW')
        print('col: L, M, R')
        move = input().upper()
        try:
            if theBoard[move] == " ":
                theBoard[move] = turn
                used = False
            else:
                print('\n' + move + ' already has the value ' + theBoard[move])
                print('Try again\n')
        except:
            print('\nUnsure what ' + move + ' meant\nTry again\n')
    
    if won(theBoard):
        printBoard(theBoard)
        print('\n\n'+ turn + ' WINS!!!!!!!!')
        playerWon = True
    
    if turn == 'X':
            turn = 'O'
    else:
        turn = 'X'
        
if not playerWon:
    print('\n\nNo one wins - its a draw')

printBoard(theBoard)