import re
from utils import read_file

def parseInput(strs):
  patterns = []
  pattern = []
  for s in strs:
    if s == '\n':
      patterns.append(pattern)
      pattern = []
    else:
      pattern.append(re.sub('\n', '', s))
  patterns.append(pattern)

  return patterns

def getPatternVertical(pattern):
  return [''.join([pattern[row][col] for row in range(len(pattern))]) for col in range(len(pattern[0]))]

def checkForMatchHelper(pattern, i):
  halfSize = min(i+1, len(pattern)-(i+1))
  half1StartIndex = i - halfSize + 1
  half2EndIndex = i+1 + halfSize - 1
  return pattern[half1StartIndex:i] == pattern[i+2:half2EndIndex+1][::-1]


def checkForMatch(patternTuple):
  (pattern, patternVertical) = patternTuple

  for i in range(len(pattern)-1):
    if pattern[i] == pattern[i+1] and checkForMatchHelper(pattern, i):
      return (i+1) * 100
      
  for i in range(len(patternVertical)-1):
    if patternVertical[i] == patternVertical[i+1] and checkForMatchHelper(patternVertical, i):
      return i+1

#### PART 1 ####
strs = read_file('day13.txt')
step1_1 = parseInput(strs)
step1_2 = list(map(getPatternVertical, step1_1))
part1_step2 = list(map(checkForMatch, zip(step1_1, step1_2)))
step3 = sum(part1_step2)

#### PART 2 ####
def smudge(c):
  if c == '#': return '.'
  return '#'

def bruteForce(patternTuple):
  (pattern, patternVertical, part1Score) = patternTuple
  originalPattern = [p for p in pattern]
  originalPatternVertical = [p for p in patternVertical]

  for row in range(len(pattern)):
    for col in range(len(pattern[0])):
      pattern = [p for p in originalPattern]
      patternVertical = [p for p in originalPatternVertical]

      pattern[row] = list(pattern[row])
      pattern[row][col] = smudge(pattern[row][col])
      pattern[row] = ''.join(pattern[row])

      patternVertical[col] = list(patternVertical[col])
      patternVertical[col][row] = smudge(patternVertical[col][row])
      patternVertical[col] = ''.join(patternVertical[col])

      for i in range(len(pattern)-1):
        if (i+1) * 100 == part1Score:
          continue
        if pattern[i] == pattern[i+1] and checkForMatchHelper(pattern, i):
          return (i+1) * 100
          
      for i in range(len(patternVertical)-1):
        if i+1 == part1Score:
          continue
        if patternVertical[i] == patternVertical[i+1] and checkForMatchHelper(patternVertical, i):
          return i+1

part2_step2 = list(map(bruteForce, zip(step1_1, step1_2, part1_step2)))
print(sum(part2_step2))