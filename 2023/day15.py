from collections import defaultdict
import re
from utils import read_file

def hash(s):
  result = 0
  for c in s:
    result += ord(c)
    result *= 17
    result %= 256
  return result

#### PART 1 ####
strs = read_file('day15.txt')
strs = strs[0].split(',')
step1 = list(map(hash, strs))
print(sum(step1))

#### PART 2 ####
def hashmap(strs):
  boxes = defaultdict(list)
  for s in strs:
    match = re.match(r'(\w+)([-|=])(\d*)', s)
    label = match[1]
    op = match[2]
    length = match[3]

    boxNum = hash(label)

    if op == '-':
      foundIndex = None
      for i in range(len(boxes[boxNum])):
        if boxes[boxNum][i][0] == label:
          foundIndex = i
          break
      if foundIndex != None:
        boxes[boxNum].pop(foundIndex)

    else:
      found = False
      for i in range(len(boxes[boxNum])):
        if boxes[boxNum][i][0] == label:
          boxes[boxNum][i] = (label, length)
          found = True
          break
      if not found:
        boxes[boxNum].append((label, length))
  return boxes

def computeFocusingPower(boxes):
  fp = 0
  for boxNum in boxes:
    for i in range(len(boxes[boxNum])):
      fp += ((boxNum+1) * (i+1) * int(boxes[boxNum][i][1]))
  return fp

strs = read_file('day15.txt')
strs = strs[0].split(',')
step1 = hashmap(strs)
step2 = computeFocusingPower(step1)
print(step2)