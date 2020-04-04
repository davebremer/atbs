# output should look like this
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
#
# First char of each list is the string in line one
# second char of each list is the string on line two
#etc

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

row=0
col=0
while row < len(grid[0]): #number of rows is the length of any member of grid
    while col < len(grid): 
        # print(str(col) + " " + str(row))
        print(grid[col][row], end="")
        col += 1
    print()  #time for a newline
    col=0    # reset the column
    row += 1 #on to another row

