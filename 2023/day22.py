from collections import defaultdict
import re
from utils import read_file

class Block:
  def __init__(self, index, s):
    self.index = index

    match = re.match(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', s)
    s = list(map(int, [match[i] for i in range(1,7)]))
    self.coord1 = (min(s[0], s[3]), min(s[1], s[4]), min(s[2], s[5]))    # always the smaller index (only changes along one axis)
    self.coord2 = (max(s[0], s[3]), max(s[1], s[4]), max(s[2], s[5]))

    self.landingZ = -1
    self.supportingBlocks = set()
    
  def __repr__(self):
    return f'Block {self.index}: {self.coord1}~{self.coord2} | lands on {self.landingZ} and supported by {self.supportingBlocks}'


def parseInput(strs):
  blocks = []
  for i in range(len(strs)):
    blocks.append(Block(i, strs[i]))
  return blocks

def addBlockToCoverage(coverageZ, block):
  for x in range(block.coord1[0], block.coord2[0]+1):
    for y in range(block.coord1[1], block.coord2[1]+1):
      for z in range(block.coord1[2], block.coord2[2]+1):
        coverageZ[block.landingZ+(z-block.coord1[2])][(x,y)] = block.index
  return coverageZ

def blocksFall(blocks):
  # dictionary storing blocks by zCoord1 (z -> block)
  blocksZ = defaultdict(list)
  for b in blocks:
    blocksZ[b.coord1[2]].append(b)

  # dictionary storing coverage by z (zCoord -> (xCoord, yCoord) -> blockIndex)
  coverageZ = defaultdict(dict)
  for initialZ in sorted(blocksZ.keys()):
    # if originally at the bottom (min z), then must fall to z = 1
    if initialZ == min(blocksZ.keys()):
      for b in blocksZ[initialZ]:
        b.landingZ = 1
        coverageZ = addBlockToCoverage(coverageZ, b)
    # otherwise, look for highest z' where there is coverage with one or more cells for block, must fall to z = z'+1
    else: 
      for b in blocksZ[initialZ]:
        for lz in sorted(coverageZ.keys(), reverse=True):
          for x in range(b.coord1[0], b.coord2[0]+1):
            for y in range(b.coord1[1], b.coord2[1]+1):
              if (x,y) in coverageZ[lz].keys():
                b.supportingBlocks.add(coverageZ[lz][(x,y)])
          if len(b.supportingBlocks) > 0:
            b.landingZ = lz+1
            coverageZ = addBlockToCoverage(coverageZ, b)
            break
        if b.landingZ == -1:
          b.landingZ = 1
          coverageZ = addBlockToCoverage(coverageZ, b)
  return blocks

#### PART 1 ####
# if dependent block supported by one block only, then cannot be safely disintegrated, otherwise can
def blocksDisintegrate1(blocks):
  allBlocks = set()
  notSafe = set()
  for b in blocks:
    allBlocks.add(b.index)
    if len(b.supportingBlocks) == 1:
      notSafe.add(next(iter(b.supportingBlocks)))
  return allBlocks.difference(notSafe)

strs = read_file('day22.txt')
step1 = parseInput(strs)
step2 = blocksFall(step1)
step3 = blocksDisintegrate1(step2)
print(len(step3))

#### PART 2 ####
def blocksDisintegrate2(blocks):
  # dictionary storing blocks by landingZ (z -> block)
  blocksZ = defaultdict(list)
  for b in blocks:
    blocksZ[b.landingZ].append(b)

  disintegrateNum = 0
  for b in blocks:
    disintegrate = {b.index}
    for z in sorted(blocksZ.keys()):
      # can't disintegrate blocks at or below current block
      if z <= b.landingZ:
        continue
      for candidateBlock in blocksZ[z]:
        if candidateBlock.supportingBlocks <= disintegrate:
          disintegrate.add(candidateBlock.index)
    disintegrateNum += len(disintegrate) - 1
  
  return disintegrateNum


strs = read_file('day22.txt')
step1 = parseInput(strs)
step2 = blocksFall(step1)
step3 = blocksDisintegrate2(step2)
print(step3)