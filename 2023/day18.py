from collections import defaultdict
import re
from utils import read_file

def digEdge(plan):
  trenchEdge = defaultdict(set)   # all vertices on edge
  trenchEdge[0] = {0}
  trenchEdgeList = []             # corner vertices
  coord = (0, 0)
  for p in plan:
    trenchEdgeList.append(coord)
    (dir, num) = p
    if dir == 'U':
      for row in range(coord[0]-1, coord[0]-num-1, -1):
        trenchEdge[row].add(coord[1])
      coord = (coord[0]-num, coord[1])
    elif dir == 'D':
      for row in range(coord[0]+1, coord[0]+num+1):
        trenchEdge[row].add(coord[1])
      coord = (coord[0]+num, coord[1])
    elif dir == 'L':
      for col in range(coord[1]-1, coord[1]-num-1, -1):
        trenchEdge[coord[0]].add(col)
      coord = (coord[0], coord[1]-num)
    elif dir == 'R':
      for col in range(coord[1]+1, coord[1]+num+1):
        trenchEdge[coord[0]].add(col)
      coord = (coord[0], coord[1]+num)
  return trenchEdge, trenchEdgeList

def calculateArea(trenchEdge, trenchEdgeList):
  area = 0

  # use shoelace algorithm (suggested by chatgpt) to get area
  for i in range(len(trenchEdgeList)):
    row1, col1 = trenchEdgeList[i]
    row2, col2 = trenchEdgeList[(i+1) % len(trenchEdgeList)]
    area += (row1 * col2) - (row2 * col1)

  area = abs(area) / 2.0

  # get number of vertices on edge of polygon
  numEdge = 0
  for row in trenchEdge:
    numEdge += len(trenchEdge[row])

  # then use pick's theorem to get number of points interior to polygon (A = i + b/2 - 1)
  numInterior = area - numEdge / 2 + 1

  return int(numInterior + numEdge)

# for visualization
def drawTrench(trenchEdge):
  minRow = min(trenchEdge.keys())
  maxRow = max(trenchEdge.keys())

  minCol = float('inf')
  maxCol = float('-inf')
  for row in trenchEdge:
    minCol = min(minCol, min(trenchEdge[row]))
    maxCol = max(maxCol, max(trenchEdge[row]))

  for row in range(minRow, maxRow+1):
    printRow = ['.'] * (maxCol - minCol + 1)
    for col in trenchEdge[row]:
      printRow[col-minCol] = '#'
    print(''.join(printRow))



#### PART 1 ####
def parseInput1(s):
  match = re.match(r'([UDLR]) (\d+) \(\#[0123456789abcdef]+\)', s)
  return match[1], int(match[2])

strs = read_file('day18.txt')
step1 = list(map(parseInput1, strs))
step2_1, step2_2 = digEdge(step1)
step3 = calculateArea(step2_1, step2_2)
print(step3)
# drawTrench(step2_1)

#### PART 2 ####
def parseInput2(s):
  match = re.match(r'[UDLR] \d+ \(\#([0123456789abcdef]+)\)', s)
  dist = int(match[1][:-1], 16)
  dir = match[1][-1]
  if dir == '0':
    return 'R', dist
  elif dir == '1':
    return 'D', dist
  elif dir == '2':
    return 'L', dist
  return 'U', dist

strs = read_file('day18.txt')
step1 = list(map(parseInput2, strs))
step2_1, step2_2 = digEdge(step1)
step3 = calculateArea(step2_1, step2_2)
print(step3)