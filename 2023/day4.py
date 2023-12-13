import re
from functools import reduce
from utils import read_file

def getNumHits(s):
  # Parse input
  s = re.sub(r'\n$', '', s)
  s = re.sub(r'^Card\s+\d+:\s+', '', s)
  s = re.split(r'\s+\|\s+', s)
  
  winningNums = set(re.split(r'\s+', s[0]))
  cardNums = set(re.split(r'\s+', s[1]))
  return len(winningNums & cardNums)

#### PART 1 ####
def score1(s):
  numHits = getNumHits(s)
  if numHits == 0: return 0
  elif numHits == 1: return 1
  return 2 ** (numHits-1)

strs = read_file('day4.txt')
step1 = reduce(lambda a,b: a+b, list(map(lambda s: score1(s), strs)), 0)
print(step1)


#### PART  2 ####
strs = read_file('day4.txt')
step1 = list(map(lambda s: getNumHits(s), strs))

i = 0
numCards = [1 for _ in range(len(step1))]
while i < len(step1):
  num = step1[i]
  for x in range(i+1, min(i+num+1, len(step1))):
    numCards[x] += numCards[i]
  i += 1

print(sum(numCards))