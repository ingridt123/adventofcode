from functools import reduce
import string
from utils import read_file

def isSymbol(c):
  return c != '.' and c in string.punctuation

def isStar(c):
  return c == '*'

def isDigit(c):
  return c.isdigit()

def getSymbolIndices(s, f):
  indices = set()
  for index, x in enumerate(s):
    if f(x):
      indices.add(index)
  return indices

# numCoords: row -> {[num, colStart, colEnd]}
def getNumIndices(s):
  indices = []
  firstIndex = None
  for index, x in enumerate(s):
    if firstIndex == None and x.isdigit():
      firstIndex = index
    elif firstIndex != None and not x.isdigit():
      indices.append((int(s[firstIndex:index]), firstIndex, index-1))
      firstIndex = None
  return indices

# numCoords: row -> {col -> num} for all cols of given num
def getNumIndices2(s):
  indices = dict()
  firstIndex = None
  for index, x in enumerate(s):
    if firstIndex == None and x.isdigit():
      firstIndex = index
    elif firstIndex != None and not x.isdigit():
      num = int(s[firstIndex:index])
      for i in range(firstIndex, index):
        indices[i] = num
      firstIndex = None
  return indices

def hasAdjacentSymbol(numCoordX, numCoords, step1_1):
  x = numCoordX
  (_, y1, y2) = numCoords
  
  # check left/right
  if x in step1_1 and y1-1 in step1_1[x] or y2+1 in step1_1[x]:
    return True
  
  # check above/below (incl diagonal)
  for i in range(y1-1, y2+2):
    if x-1 in step1_1 and i in step1_1[x-1]:
      return True
    if x+1 in step1_1 and i in step1_1[x+1]:
      return True
    
  return False

def findTwoAdjacentNums(starCoordX, starCoordY, step1_2, step1_3):
  x = starCoordX
  y = starCoordY
  nums = []

  # check left/right
  if x in step1_2 and y-1 in step1_2[x]:
    nums.append((x,y-1))

  if x in step1_2 and y+1 in step1_2[x]:
    nums.append((x,y+1))
  
  # check above/below (incl diagonal)
  # inital mistake: counting 3+ digit numbers directly above/below * as 2 numbers
  firstIndex = [True, True]
  for i in range(y-1, y+2):
    if x-1 in step1_2 and i in step1_2[x-1]:
      if firstIndex[0]:
        nums.append((x-1,i))
        firstIndex[0] = False
    else:
      firstIndex[0] = True
    if x+1 in step1_2 and i in step1_2[x+1]:
      if firstIndex[1]:
        nums.append((x+1,i))
        firstIndex[1] = False
    else:
      firstIndex[1] = True

  if len(nums) == 2:
    # print(starCoordX, starCoordY)
    return step1_3[nums[0][0]][nums[0][1]] * step1_3[nums[1][0]][nums[1][1]]
  return 0

#### PART 1 ####
strs = read_file('day3.txt')
# more efficient if comb for both at the same time
step1_1 = dict(enumerate(map(lambda s: getSymbolIndices(s, isSymbol), strs)))  # symbolCoords: row -> {cols}
step1_2 = dict(enumerate(map(lambda s: getNumIndices(s), strs)))  # numCoords: row -> {[num, colStart, colEnd]}
step2 = list(map(lambda k: list(filter(lambda v: hasAdjacentSymbol(k, v, step1_1), step1_2[k])), step1_2))
step3 = reduce(lambda x,y: x+y, list(map(lambda s: reduce(lambda a,b: a+b[0], s, 0), step2)), 0)
print(step3)

#### PART 2 ####
strs = read_file('day3.txt')
step1_1 = dict(enumerate(map(lambda s: getSymbolIndices(s, isStar), strs)))   # starCoords: row -> {cols}
step1_2 = dict(enumerate(map(lambda s: getSymbolIndices(s, isDigit), strs)))  # digitCoords: row -> {cols}
step1_3 = dict(enumerate(map(lambda s: getNumIndices2(s), strs)))  # numCoords: row -> {col -> num} for all cols of given num
step2 = list(map(lambda k: list(map(lambda v: findTwoAdjacentNums(k, v, step1_2, step1_3), sorted(step1_1[k]))), step1_1))
step3 = reduce(lambda x,y: x+y, list(map(lambda s: reduce(lambda a,b: a+b, s, 0), step2)), 0)
print(step3)

# step3 = list(filter(lambda s: len(s) > 0 and s != [], step2))
# print(step3)
# step4 = list(map(lambda s: list(map(lambda x: list(map(lambda a: step1_3[a[0]][a[1]], x)), s)), step3))
# step5 = list(map(lambda s: list(map(lambda x: reduce(lambda a,b: a*b, x) if len(x) > 0 else 0, s)) , step4))
# step6 = reduce(lambda x,y: x+y, list(map(lambda s: reduce(lambda a,b: a+b, s, 0), step5)), 0)
# print(step6)