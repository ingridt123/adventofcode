from collections import defaultdict
from itertools import combinations
import re
from utils import read_file

def parseInput(strs, adjustment=1):
  # save coords in dict (col -> row), so that can just update cols after parsing input
  galaxyCoords = defaultdict(list)
  rowAdjustment = 0

  for row in range(len(strs)):
    strs[row] = re.sub('\n', '', strs[row])
    galaxies = [col for col, c in enumerate(strs[row]) if c == '#']
    if len(galaxies) == 0:
      rowAdjustment += adjustment
    else:
      for g in galaxies:
        galaxyCoords[g].append(row + rowAdjustment)

  galaxyCoords_withColAdjustment = defaultdict(list)
  colAdjustment = 0
  for col in range(len(strs[0])):
    s = [strs[row][col] for row in range(len(strs))]
    galaxies = [row for row, c in enumerate(s) if c == '#']
    if len(galaxies) == 0:
      colAdjustment += adjustment
    else:
      galaxyCoords_withColAdjustment[col + colAdjustment] = galaxyCoords[col]

  return galaxyCoords_withColAdjustment

def listPairs(step1):
  galaxyPairs = []
  for col in step1:
    for row in step1[col]:
      galaxyPairs.append((row, col))
  return galaxyPairs

def calculateDist(coord1, coord2):
  return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def getAllDist(step2):
  galaxyDists = dict()
  for coord1, coord2 in combinations(step2, 2):
    if coord1 != coord2 and (coord1, coord2) not in galaxyDists and (coord2, coord1) not in galaxyDists:
      galaxyDists[(coord1, coord2)] = calculateDist(coord1, coord2)
  return galaxyDists

#### PART 1 ####
strs = read_file('day11.txt')
step1 = parseInput(strs)
step2 = listPairs(step1)
step3 = sum(getAllDist(step2).values())
print(step3)

#### PART 2 ####
strs = read_file('day11.txt')
step1 = parseInput(strs, 999999)
step2 = listPairs(step1)
step3 = sum(getAllDist(step2).values())
print(step3)
