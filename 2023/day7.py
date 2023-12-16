from collections import Counter, defaultdict, OrderedDict
import re
from utils import read_file

def parseInput(s, handMappings):
  s = re.sub(r'\n', '', s)
  s = re.split('\s+', s)
  return list(map(lambda x: handMappings[x], list(s[0]))), int(s[1])

def groupHands(step1, part1=True):
  # hand type -> first card -> second card -> third card -> fourth card -> fifth card -> bet
  allHands = OrderedDict()
  allHands[5,] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))         # five of a kind
  allHands[4, 1] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))      # four of a kind
  allHands[3, 2] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))      # full house
  allHands[3, 1, 1] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))   # three of a kind
  allHands[2, 2, 1] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))        # two pair
  allHands[2, 1, 1, 1] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))     # one pair
  allHands[1, 1, 1, 1, 1] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict( lambda: defaultdict(int)))))  # high card

  for s in step1:
    counter = Counter(s[0])
    if part1:
      handType = tuple(sorted(list(counter.values()), reverse=True))
    else:
      handType = sorted(list(counter.values()), reverse=True)
      # Remove number of Js and add to first number to become strongest type
      numJs = counter[1]
      if numJs > 0 and handType != [5]:
        handType.remove(numJs)
        handType[0] += numJs
      handType = tuple(handType)
    allHands[handType][s[0][0]][s[0][1]][s[0][2]][s[0][3]][s[0][4]] = s[1]

  return allHands

def scoreHands(step2, numHands):
  rank = numHands
  winnings = 0
  for handType in step2:
    for card1 in sorted(step2[handType], reverse=True):
      for card2 in sorted(step2[handType][card1], reverse=True):
        for card3 in sorted(step2[handType][card1][card2], reverse=True):
          for card4 in sorted(step2[handType][card1][card2][card3], reverse=True):
            for card5 in sorted(step2[handType][card1][card2][card3][card4], reverse=True):
              # print(rank, winnings)
              winnings += rank * step2[handType][card1][card2][card3][card4][card5]
              rank -= 1

  return winnings

#### PART 1 ####
handMappings1 = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14,
}

strs = read_file('day7.txt')
step1 = list(map(lambda s: parseInput(s, handMappings1), strs))
step2 = groupHands(step1)
step3 = scoreHands(step2, len(step1))
print(step3)

#### PART 2 ####
handMappings2 = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 1,
  'Q': 12,
  'K': 13,
  'A': 14,
}

strs = read_file('day7.txt')
step1 = list(map(lambda s: parseInput(s, handMappings2), strs))
step2 = groupHands(step1, False)
step3 = scoreHands(step2, len(step1))
print(step3)