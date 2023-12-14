from functools import reduce
import re
from utils import read_file

mappings = {
  'seed': 'soil',
  'soil': 'fertilizer',
  'fertilizer': 'water',
  'water': 'light',
  'light': 'temperature',
  'temperature': 'humidity',
  'humidity': 'location',
}

def parseInput(strs):
  seeds = strs[0]
  seeds = re.sub(r'seeds:\s+', '', seeds)
  seeds = re.sub(r'\n', '', seeds)
  seeds = re.split('\s+', seeds)
  seeds = list(map(lambda s: int(s), seeds))
  
  # source -> {(start range, end range) -> +/- change}
  maps = dict()
  currentSource = ''
  i = 2
  while i < len(strs):
    if strs[i] != '\n':
      titleMatch = re.match(r'(\w+)-to-(\w+) map:', strs[i])
      if titleMatch:
        currentSource = titleMatch.group(1)
        maps[currentSource] = dict()
      else:
        rangeMatch = re.match(r'(\d+)\s+(\d+)\s+(\d+)', strs[i])
        destStart = int(rangeMatch.group(1))
        srcStart = int(rangeMatch.group(2))
        rangeLen = int(rangeMatch.group(3))
        maps[currentSource][(srcStart, srcStart + rangeLen - 1)] = destStart - srcStart
    i += 1

  return seeds, maps

def convert(srcNum, srcType, maps):
  destType = mappings[srcType]
  for key in maps[srcType].keys():
    (srcStart, srcEnd) = key
    if srcNum >= srcStart and srcNum <= srcEnd:
      return srcNum + maps[srcType][key], destType
  return srcNum, destType

def getLocation(seedNum, maps):
  num = seedNum
  type = 'seed'
  while type != 'location':
    num, type = convert(num, type, maps)
    # print(num, type)
  return num

#### PART 1 ####
strs = read_file('day5.txt')
seeds, maps = parseInput(strs)
step1 = reduce(lambda a,b: a if a < b else b, list(map(lambda s: getLocation(s, maps), seeds)))
print(step1)

#### PART 2 ####
def getSeedRanges(seeds):
  seedRanges = []
  for i in range(0, len(seeds), 2):
    seedRanges.append((seeds[i], seeds[i] + seeds[i+1] - 1, 'seed'))
  return seedRanges

def getMinLocationForRange(seedRange, maps):
  minLoc = None
  for seedNum in range(seedRange[0], seedRange[1]+1):
    loc = getLocation(seedNum, maps)
    if minLoc == None or loc < minLoc:
      minLoc = loc
  print(minLoc)
  return minLoc

def getMinLocationForRange2(ranges, maps):
  minLoc = None

  while len(ranges) > 0:
    # print(ranges)
    (srcStart, srcEnd, type) = ranges.pop()

    if type == 'location':
      minLoc = min(srcStart, minLoc) if minLoc != None else srcStart
      continue

    rangeComplete = False
    for key in sorted(maps[type]):
      (srcMapStart, srcMapEnd) = key
      diff = maps[type][key]

      # outside of range
      if srcEnd < srcMapStart or srcStart > srcMapEnd:
        continue

      # overlapping range
      if srcStart < srcMapStart:
        ranges.add((srcStart, srcMapStart-1, type)) # outside part
        srcStart = srcMapStart

      if srcEnd > srcMapEnd:
        ranges.add((srcMapEnd+1, srcEnd, type)) # outside part
        srcEnd = srcMapEnd

      # now must be within range
      ranges.add((srcStart + diff, srcEnd + diff, mappings[type]))
      rangeComplete = True

    if not rangeComplete:
      ranges.add((srcStart, srcEnd, mappings[type]))

  return minLoc
    
# (brute force)
# strs = read_file('day5.txt')
# seeds, maps = parseInput(strs)
# seedRanges = getSeedRanges(seeds)
# step1 = reduce(lambda a,b: a if a < b else b, list(map(lambda s: getMinLocationForRange(s, maps), seedRanges)))
# print(step1)

strs = read_file('day5.txt')
seeds, maps = parseInput(strs)
seedRanges = getSeedRanges(seeds)
step1 = getMinLocationForRange2(set(seedRanges), maps)
print(step1)