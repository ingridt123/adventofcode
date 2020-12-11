import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str)

output = [list(o) for o in output]
originalOutput = output[:]


def getResult(output, printOutput=True):
    result = []
    for o in output:
        result.append("".join(o))
        if printOutput:
            print(result[-1])
    result = "".join(result)

    return result


### PART 1 ###

def adjOccupiedNum(output, row, col):
    check = []
    for i in range(max(row-1,0), min(row+2, len(output))):
        for j in range(max(col-1,0), min(col+2, len(output[0]))):
            if not i == row or not j == col:
                check.append((i, j))

    count = 0
    for r,c in check:
        if output[r][c] == '#':
            count += 1

    return count


change = True
while change:
    nextOutput = []
    change = False
    for row in range(len(output)):
        nextRow = []
        for col in range(len(output[0])):
            nextRow.append(output[row][col])
            if output[row][col] != '.':
                num = adjOccupiedNum(output, row, col)
                if output[row][col] == 'L' and num == 0:
                    nextRow[-1] = '#'
                    change = True
                elif output[row][col] == '#' and num >= 4:
                    nextRow[-1] = 'L'
                    change = True
        nextOutput.append(nextRow)
    output = nextOutput

result = getResult(output)
print(result.count('#'))            # 2310

### PART 2 ###

output = originalOutput[:]

def seeOccupiedNum(output, row, col):
    check = []
    for i in range(max(row-1,0), min(row+2, len(output))):
        for j in range(max(col-1,0), min(col+2, len(output[0]))):
            if not i == row or not j == col:
                check.append((i, j))

    count = 0
    for r,c in check:
        if output[r][c] == '#':
            count += 1
        elif output[r][c] == '.':
            rowDiff = r - row
            colDiff = c - col

            i = r + rowDiff
            j = c + colDiff
            while (0 <= i < len(output) and 0 <= j < len(output[0])):
                if output[i][j] == '#':
                    count += 1
                if not output[i][j] == '.':
                    break

                i += rowDiff
                j += colDiff

    return count


change = True
while change:
    nextOutput = []
    change = False
    for row in range(len(output)):
        nextRow = []
        for col in range(len(output[0])):
            nextRow.append(output[row][col])
            if output[row][col] != '.':
                num = seeOccupiedNum(output, row, col)
                if output[row][col] == 'L' and num == 0:
                    nextRow[-1] = '#'
                    change = True
                elif output[row][col] == '#' and num >= 5:
                    nextRow[-1] = 'L'
                    change = True
        nextOutput.append(nextRow)
    output = nextOutput


result = getResult(output)
print(result.count('#'))            # 2074