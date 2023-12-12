from functools import reduce

from utils import read_file

# getMaxCubes('Game 1: 2 red, 2 green; 1 red, 1 green, 2 blue; 3 blue, 3 red, 3 green; 1 blue, 3 green, 7 red; 5 red, 3 green, 1 blue')
# -> (1, ('3', '3', '7'))
def getMaxCubes(str):
  str = str.split('; ')
  str = str[0].split(': ') + str[1:]
  
  # key = game number
  key = int(str[0][5:]) # Format: 'Game #' <-- # starts from index 5

  # value = (max blue, max green, max red)
  step1 = list(map(lambda s: list(map(lambda x: x.split(' '), s.split(', '))), str[1:]))
  val = (getMaxPerColor(step1, 'blue'), getMaxPerColor(step1, 'green'), getMaxPerColor(step1, 'red'))

  return [key, val]

def getMaxPerColor(step1, color):
  step2 = list(map(lambda s: list(filter(lambda x: color in x[1], s)), step1))
  step3 = [int(x) for pairList in step2 for pair in pairList for x in pair if x.isdigit()]
  try:
    return max(step3)
  except ValueError:
    return 0


#### PART 1 ####
cubes = (14, 13, 12) # blue, green, red
strs = read_file('day2.txt')
step1 = list(map(lambda s: getMaxCubes(s), strs))
step2 = list(filter(lambda s: int(s[1][0]) <= cubes[0] and int(s[1][1]) <= cubes[1] and int(s[1][2]) <= cubes[2], step1))
step3 = reduce(lambda a,b: a+b[0], step2, 0)
print(step3)

#### PART 2 ####
strs = read_file('day2.txt')
step1 = list(map(lambda s: getMaxCubes(s), strs))
step2 = list(map(lambda s: reduce(lambda a,b: a*b, s[1], 1), step1))
step3 = reduce(lambda a,b: a+b, step2, 0)
print(step3)