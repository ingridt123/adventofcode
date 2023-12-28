from functools import reduce
import re
from utils import read_file

def parseInput(s):
  s = re.sub(r'\n', '', s)
  s = re.split(r'\s+', s)
  s = list(map(int, s))
  return s

def bruteForce(s, part1=True):
  nums = [s]
  while any(nums[-1]):
    newNums = []
    for i in range(len(nums[-1])-1):
      newNums.append(nums[-1][i+1]-nums[-1][i])
    nums.append(newNums)
  
  if part1:
    nums[-1].append(0)
    for i in range(len(nums)-2, -1, -1):
      nums[i].append(nums[i][-1] + nums[i+1][-1])
    return nums[0][-1]
  else:
    nums[-1].insert(0, 0)
    for i in range(len(nums)-2, -1, -1):
      nums[i].insert(0, nums[i][0] - nums[i+1][0])
    return nums[0][0]

#### PART 1 ####
strs = read_file('day9.txt')
step1 = list(map(parseInput, strs))
step2 = reduce(lambda a,b: a+b, list(map(bruteForce, step1)))
print(step2)

#### PART 2 ####
strs = read_file('day9.txt')
step1 = list(map(parseInput, strs))
step2 = reduce(lambda a,b: a+b, list(map(lambda s: bruteForce(s, False), step1)))
print(step2)