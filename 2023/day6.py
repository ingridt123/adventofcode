from functools import reduce
import math
import re
from utils import read_file

def parseInput(strs, part2=False):
  times = re.sub(r'Time:\s+', '', strs[0])
  times = re.sub(r'\n', '', times)
  times = list(map(int, re.split(r'\s+', times)))

  distances = re.sub(r'Distance:\s+', '', strs[1])
  distances = re.sub(r'\n', '', distances)
  distances = list(map(int, re.split(r'\s+', distances)))

  if part2:
    times = reduce(lambda a,b: str(a) + str(b), times)
    distances = reduce(lambda a,b: str(a) + str(b), distances)
    return int(times), int(distances)
  else:
    return list(zip(times, distances))

#### PART 1 ####
def solveQuadratic(totalTime, recordDist):
  # 0 = t1^2 - t'*t1 + d'

  # t1 = (t' +- sqrt(t'^2 - 4d')) / 2
  upperT = (totalTime + math.sqrt(totalTime ** 2 - 4 * recordDist)) / 2
  lowerT = (totalTime - math.sqrt(totalTime ** 2 - 4 * recordDist)) / 2

  # times between upperT and lowerT (exclusive) are where d > d' (since multiplied by -1)
  upperTInt = math.floor(upperT)
  lowerTInt = math.ceil(lowerT)
  if upperT == upperTInt: upperTInt -= 1
  if lowerT == lowerTInt: lowerTInt += 1
  return upperTInt - lowerTInt + 1

# t' = total time, t1 = hold time, d' = goal distance
# d = t1 * (t' - t1) = t1*t' - t1^2  <-- find where intercepts d = d'
# solve for d' = t1*t' - t1^2 => 0 = t1^2 - t'*t1 + d'
strs = read_file('day6.txt')
step1 = parseInput(strs)
step2 = reduce(lambda a,b: a*b, list(map(lambda s: solveQuadratic(s[0], s[1]), step1)), 1)
print(step2)

#### PART 2 ####
strs = read_file('day6.txt')
step1 = parseInput(strs, True)
step2 = solveQuadratic(step1[0], step1[1])
print(step2)