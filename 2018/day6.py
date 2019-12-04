import methods
import sys

# read input from txt file
input = methods.readFile("day6.txt")
input = [x.replace('\n', '').split(', ') for x in input]
input = [[int(x[0]), int(x[1])] for x in input]

xCoords = [i[0] for i in input]
yCoords = [i[1] for i in input]

# create map of dimensions x+1 * y+1
coord = [["." for col in range(max(xCoords)+1)] for row in range(max(yCoords)+1)]

# fill in points from input
count = 0
for x in input:
    coord[x[1]][x[0]] = count
    count += 1

# calculate closest point for each point in coord
for col in range(len(coord)):
    for row in range(len(coord[col])):
        if coord[col][row] == '.':
            minDist = sys.maxsize
            minPoint = -1
            for x in input:
                dist = abs(col - x[0]) + abs(row - x[1])
                if minDist == dist:
                    minPoint = '.'
                    break
                elif minDist > dist:
                    minDist = dist
                    minPoint = input.index(x)
            coord[col][row] = minPoint

checkCoord = []
for x in coord:
    checkCoord += x
checkCoord = [x for x in checkCoord if x != '.']

# find max and check that it doesn't have an edge
found = False
while not found:
    maxPoint = max(checkCoord, key=checkCoord.count)
    found = True
    for col in range(len(coord)):
        for row in range(len(coord[col])):
            if coord[col][row] == maxPoint:
                if col == 0 or col == max(xCoords) or row == 0 or row == max(yCoords):
                    print(maxPoint)
                    found = False
                    checkCoord = [x for x in checkCoord if x != maxPoint]
                    break
        if found == False:
            break
    
print(checkCoord.count(maxPoint))