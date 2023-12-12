from functools import reduce

from utils import read_file

#### PART 1 ####
strs = read_file('day1.txt')
step1 = list(map(lambda s: list(filter(lambda x: x.isdigit(), s)), strs))
step2 = reduce(lambda a,b: a + b, list(map(lambda s: int(s[0] + s[-1]), step1)), 0)
print(step2)

#### PART 2 ####
nums = {
  3: ['one', 'two', 'six'],
  4: ['four', 'five', 'nine'],
  5: ['three', 'seven', 'eight']
}
numConversion = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def findFirstNum(str, reverse=False):
  steps = range(len(str))
  if reverse:
    steps = range(len(str)-1, -1, -1)

  for i in steps:
    if str[i].isdigit():
      return str[i]
    else:
      for n in nums:
        if i + n <= len(str):
          for num in nums[n]:
            if str[i:i+n] == num:
              return numConversion[num]

strs = read_file('day1.txt')
step1 = reduce(lambda a,b: a + b, list(map(lambda s: int(findFirstNum(s) + findFirstNum(s, True)), strs)), 0)
print(step1)
