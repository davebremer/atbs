# two parts: 
# the first part generates a list of 100 randomly selected 'heads' and 'tails' values,
# and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times

import random

def coinToss(): #return either "H" or "T"
    if random.randint(0, 1) == 0:
        return "H"
    else:
        return "T"

def commaCode(theList):
    op=""
    idx=0
    for i in theList:
        op=op + str(i)
        if idx < len(theList)-1:
            op+=", "
        idx+=1

    return(op)

def findStreak(theList, streakLength):
    return None

streakList = []
for bigloop in range(10000):
    sequence = []
    for i in range(100):
        sequence.append(coinToss())

    streakCount = 0
    # print(commaCode(sequence)+ "\n")
    for i in range((len(sequence)-6)):
        checkSeq = (sequence[i:i+6])
        if not ('H' in checkSeq and 'T' in checkSeq):
            streakCount += 1
            # print("Position " + str(i) + ": " + commaCode(checkSeq) + " " + str(streakCount))

    streakList.append(streakCount)

streaksum = 0
for i in range(len(streakList)):
    streaksum += streakList[i]

print('Chance of streak: ' + str.format('{0:.2f}',(streaksum / len(streakList))) + '%')