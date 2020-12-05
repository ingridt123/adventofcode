from utils import readFile
import math

output = readFile("day5.txt", str)

def findRowCol(string, low, high):
    if len(string) == 0:
        return low

    if string[0] == 'F' or string[0] == 'L':
        return findRowCol(string[1:], low, math.floor((low+high)/2))
    elif string[0] == 'B' or string[0] == 'R':
        return findRowCol(string[1:], math.ceil((low+high)/2), high)

MAX_ROW = 2 ** 7 - 1
MAX_COL = 2 ** 3 - 1

maxSeatId = -1
allSeats = [x for x in range(MAX_ROW * 8 + MAX_COL)]
for o in output:
    row = findRowCol(o[:7], 0, 127)
    col = findRowCol(o[7:], 0, 7)

    seatId = row * 8 + col
    if seatId > maxSeatId:
        maxSeatId = seatId
    allSeats.remove(seatId)

print(maxSeatId)

for a in allSeats:
    if a-1 not in allSeats and a+1 not in allSeats:
        print(a)
        break