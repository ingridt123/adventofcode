import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str)

output = [int(o) for o in output[0].split(',')]


def takeTurn(numDict, currentTurn, prevNum):
    nextNum = 0

    if prevNum in numDict:
        lastTurn = numDict[prevNum]
        numDict[prevNum] = currentTurn-1
        nextNum = (currentTurn - 1) - lastTurn

    numDict[prevNum] = currentTurn-1
    return nextNum


### PART 1 ###

LAST_TURN1 = 2020

numDict = {}      # num -> last turn spoken
prevNum = output[-1]

for turn in range(len(output)-1):
    numDict[output[turn]] = turn

for turn in range(len(output), LAST_TURN1):
    prevNum = takeTurn(numDict, turn, prevNum)

print(prevNum)                  # 981


### PART 2 ###

LAST_TURN2 = 30000000

numDict = {}      # num -> last turn spoken
prevNum = output[-1]

for turn in range(len(output)-1):
    numDict[output[turn]] = turn

for turn in range(len(output), LAST_TURN2):
    prevNum = takeTurn(numDict, turn, prevNum)

print(prevNum)                  # 164878