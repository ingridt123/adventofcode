import intcode

text = intcode.readFile("day11.txt")

width = 5
height = 5
grid = [[0 for col in range(width)] for row in range(height)]       # 0 is black, 1 is white

i = 0

directions = ["up", "left", "down", "right"]
curRow = 2
curCol = 2
curDir = directions[0]

paintedCells = []

for x in range(20):
    # print(curRow, curCol, height, width)
    inputNum = int(not grid[curRow][curCol] == 0)

    output, text, i = intcode.compute(text, inputNum, i)
    
    if output == "HALT":
        break

    grid[curRow][curCol] = output[0]
    if (curRow, curCol) not in paintedCells:
        paintedCells.append((curRow, curCol))
    
    if output[1] == 0:
        curDir = directions[(directions.index(curDir)+1) % len(directions)]
    else:
        newIndex = directions.index(curDir) - 1
        if newIndex < 0:
            newIndex = len(directions) - 1
        curDir = directions[newIndex]

    if curDir == directions[0]:
        if curRow == 0:
            height += 1
            grid.insert(0, [0 for col in range(width)])
            paintedCells = [(a+1,b) for (a,b) in paintedCells]
        else:
            curRow -= 1
    elif curDir == directions[1]:
        if curCol == 0:
            width += 1
            paintedCells = [(a,b+1) for (a,b) in paintedCells]
            for col in range(height):
                grid[col].insert(0, 0)
        else:
            curCol -= 1
    elif curDir == directions[2]:
        if curRow == height-1:
            height += 1
            grid.append([0 for col in range(width)])
        curRow += 1
    elif curDir == directions[3]:
        if curCol == width-1:
            width += 1
            for col in range(height):
                grid[col].append(0)
        curCol += 1

print(paintedCells)
print(len(paintedCells))