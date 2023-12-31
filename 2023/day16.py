import re
import sys
from utils import read_file

sys.setrecursionlimit(5000)

#### PART 1 ####
def beam(row, col, dir, layout, visited):
  if (row, col, dir) in visited:
    return ()
  
  visited.add((row, col, dir))
  op = layout[row][col]

  # go up
  if (op == '.' and dir == 'up') or \
     (op == '/' and dir == 'right') or \
     (op == '\\' and dir == 'left') or \
     (op == '|' and dir == 'up'):
    if row-1 >= 0:
      visited = visited.union(beam(row-1, col, 'up', layout, visited))

  # go down
  elif (op == '.' and dir == 'down') or \
       (op == '/' and dir == 'left') or \
       (op == '\\' and dir == 'right') or \
       (op == '|' and dir == 'down'):
    if row+1 < len(layout):
      visited = visited.union(beam(row+1, col, 'down', layout, visited))

  # go right
  elif (op == '.' and dir == 'right') or \
       (op == '/' and dir == 'up') or \
       (op == '\\' and dir == 'down') or \
       (op == '-' and dir == 'right'):
    if col+1 < len(layout[0]):
      visited = visited.union(beam(row, col+1, 'right', layout, visited))

  # go left
  elif (op == '.' and dir == 'left') or \
       (op == '/' and dir == 'down') or \
       (op == '\\' and dir == 'up') or \
       (op == '-' and dir == 'left'):
    if col-1 >= 0:
      visited = visited.union(beam(row, col-1, 'left', layout, visited))

  # go up and down
  elif op == '|' and (dir == 'left' or dir == 'right'):
    if row-1 >= 0:
      visited = visited.union(beam(row-1, col, 'up', layout, visited))
    if row+1 < len(layout):
      visited = visited.union(beam(row+1, col, 'down', layout, visited))

  # go left and right
  elif op == '-' and (dir == 'up' or dir == 'down'):
    if col+1 < len(layout[0]):
      visited = visited.union(beam(row, col+1, 'right', layout, visited))
    if col-1 >= 0:
      visited = visited.union(beam(row, col-1, 'left', layout, visited))

  return visited

def getNumVisited(visited):
  squares = set()
  for v in visited:
    squares.add((v[0], v[1]))
  return len(squares)

strs = read_file('day16.txt')
strs = list(map(lambda s: re.sub(r'\n', '', s), strs))
step1 = beam(0, 0, 'right', strs, set())
step2 = getNumVisited(step1)
print(step2)

#### PART 2 ####
def testAllStartPos(layout):
  maxSquares = 0

  # test top row (down)
  print('Testing top row')
  for col in range(len(layout[0])):
    maxSquares = max(maxSquares, getNumVisited(beam(0, col, 'down', layout, set())))

  # test bottom row (up)
  print('Testing bottom row')
  for col in range(len(layout[0])):
    maxSquares = max(maxSquares, getNumVisited(beam(len(layout)-1, col, 'up', layout, set())))

  # test left column (right)
  print('Testing left column')
  for row in range(len(layout)):
    maxSquares = max(maxSquares, getNumVisited(beam(row, 0, 'right', layout, set())))

  # test right column (left)
  print('Testing right column')
  for row in range(len(layout)):
    maxSquares = max(maxSquares, getNumVisited(beam(row, len(layout[0])-1, 'left', layout, set())))

  return maxSquares

strs = read_file('day16.txt')
strs = list(map(lambda s: re.sub(r'\n', '', s), strs))
step1 = testAllStartPos(strs)
print(step1)