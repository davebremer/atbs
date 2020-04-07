# Write a function named printTable() that takes a list of lists of strings and 
# displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings.

# Example:
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
# Output:
#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose

def getColWidths(tableData):
    colWidths = [0]* len(tableData)   
    i=0
    for alist in tableData:
        for aword in alist:
            if len(aword) > colWidths[i]:
                colWidths[i] = len(aword)
        i+=1
    return(colWidths)

def rotateLists(tableData):
    #TODO probable error for empty list
    result = []
    for i in range(len(tableData[0])):
        theRow = []
        for j in range(len(tableData)):
            theRow.append(tableData[j][i])
        result.append(theRow)
    return(result)

def padTable(tableData,padList):
    result=[]
    for aList in tableData:
        for i in range(len(aList)):
            just=padList[i]
            aList[i] = aList[i].rjust(padList[i])
        result.append(aList)
    return(result)

def printTable(tableData):
    colWidths = getColWidths(tableData)
    rotatedTable = rotateLists(tableData)
    paddedTable = padTable(rotatedTable,colWidths)
    for theList in paddedTable:
        print(' '.join(theList))




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)