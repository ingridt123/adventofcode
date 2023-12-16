from functools import reduce
import math
import re
from utils import read_file

def parseDirections(s):
  s = re.sub('\n', '', s)
  return list(s)

def parseLR(strs, part1=True):
  leftMap = dict()
  rightMap = dict()
  startingNodes = []

  for s in strs:
    s = re.sub('\n', '', s)
    s = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', s)
    leftMap[s[1]] = s[2]
    rightMap[s[1]] = s[3]

    if not part1:
      endsWithA = re.match(r'\w\wA', s[1])
      if endsWithA:
        startingNodes.append(s[1])
  
  return leftMap, rightMap, startingNodes

def navigate(startNode, directions, leftMap, rightMap, checkEndNode):
  curNode = startNode
  index = 0
  steps = 0
  while checkEndNode(curNode):
    index %= len(directions)
    if directions[index] == 'L':
      curNode = leftMap[curNode]
    else:
      curNode = rightMap[curNode]
    index += 1
    steps += 1
  
  return steps

#### PART 1 ####
def checkEndNode1(node):
  return node != 'ZZZ'

strs = read_file('day8.txt')
step1_1 = parseDirections(strs[0])
step1_2, step1_3, _ = parseLR(strs[2:])
step2 = navigate('AAA', step1_1, step1_2, step1_3, checkEndNode1)
print(step2)

#### PART 2 ####
# brute force solution
def navigate2(directions, leftMap, rightMap, startingNodes):
  index = 0
  steps = 0
  while not all(list(map(lambda s: re.match(r'\w\wZ', s), startingNodes))):
    index %= len(directions)
    if directions[index] == 'L':
      startingNodes = list(map(lambda s: leftMap[s], startingNodes))
    else:
      startingNodes = list(map(lambda s: rightMap[s], startingNodes))
    index += 1
    steps += 1

  return steps

def checkEndNode2(node):
  return not re.match(r'\w\wZ', node)

strs = read_file('day8.txt')
step1_1 = parseDirections(strs[0])
step1_2, step1_3, step1_4 = parseLR(strs[2:], False)
# step2 = navigate2(step1_1, step1_2, step1_3, step1_4)
step2 = list(map(lambda s: navigate(s, step1_1, step1_2, step1_3, checkEndNode2), step1_4))
step3 = reduce(math.lcm, step2)
print(step3)