import copy
import re
from utils import read_file

def parseWorkflowRule(r):
  if re.match(r'^\w+$', r):
    return r
  
  ruleMatch = re.match(r'(\w+)([<|>])(\d+):(\w+)', r)
  # op = lambda a,b: a < b if ruleMatch[2] == '<' else lambda a,b: a > b
  return (ruleMatch[1], ruleMatch[2], int(ruleMatch[3]), ruleMatch[4])


def parseInput(s):
  workflowMatch = re.match(r'(\w+)\{([\w\d<>:,]+)\}', s)
  if workflowMatch:
    workflowName = workflowMatch[1]
    workflowRules = re.split(r',', workflowMatch[2])
    workflowRules = list(map(parseWorkflowRule, workflowRules))
    return 'W', workflowName, workflowRules
  
  partMatch = re.match(r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}', s)
  if partMatch:
    return 'P', (int(partMatch[1]), int(partMatch[2]), int(partMatch[3]), int(partMatch[4]))
  
  return '', None

def parseAllInput(strs):
  workflows = dict()
  parts = []
  for s in strs:
    match = parseInput(s)
    if match[0] == 'W':
      workflows[match[1]] = match[2]
    elif match[0] == 'P':
      parts.append({
        'x': match[1][0],
        'm': match[1][1],
        'a': match[1][2],
        's': match[1][3],
      })
  return workflows, parts

#### PART 1 ####
def runPart(p, workflows):
  workflowName = 'in'
  while (workflowName != 'R' and workflowName != 'A'):
    workflow = workflows[workflowName]
    for w in workflow:
      if type(w) == str:
        workflowName = w
        break
      elif (w[1] == '>' and p[w[0]] > w[2]) or (w[1] == '<' and p[w[0]] < w[2]):
        workflowName = w[3]
        break
  
  if workflowName == 'A':
    return p['x'] + p['m'] + p['a'] + p['s']
  return 0

strs = read_file('day19.txt')
step1_1, step1_2 = parseAllInput(strs)
step2 = list(map(lambda s: runPart(s, step1_1), step1_2))
print(sum(step2))

#### PART 2 ####
def addToCorrectPartList(result, part, acceptedParts, rejectedParts, inProgressParts):
  if result == 'A':
    acceptedParts.append(part)
  elif result == 'R':
    rejectedParts.append(part)
  else:
    inProgressParts.append([result, part])
  return acceptedParts, rejectedParts, inProgressParts

def findAllPartRanges(workflows):
  inProgressParts = [] # (next workflow, {'x':(x range), 'm':(m range), 'a':(a range), 's':(s range)})
  acceptedParts = []   # {'x':(x range), 'm':(m range), 'a':(a range), 's':(s range)}
  rejectedParts = []   # {'x':(x range), 'm':(m range), 'a':(a range), 's':(s range)}

  # start with 1-4000 for all, break up as run through workflow
  inProgressParts.append(['in', {'x': (1, 4000), 'm': (1, 4000), 'a':(1, 4000), 's':(1, 4000)}])

  # assume no infinite cycles // all parts eventually lead to A or R
  while len(inProgressParts) > 0:
    part = inProgressParts.pop()
    workflow = workflows[part[0]]
    for w in workflow:
      if type(w) == str:
        acceptedParts, rejectedParts, inProgressParts = addToCorrectPartList(w, part[1], acceptedParts, rejectedParts, inProgressParts)
      else:
        if w[1] == '>':
          if part[1][w[0]][1] <= w[2]:    # no overlap in range, can ignore
            continue
          elif part[1][w[0]][0] > w[2]:   # full range matches, can break out of for loop
            acceptedParts, rejectedParts, inProgressParts = addToCorrectPartList(w[3], part[1], acceptedParts, rejectedParts, inProgressParts)
            break
          else:
            # upper range goes to another workflow
            updatedRanges = copy.deepcopy(part[1])
            updatedRanges[w[0]] = (w[2]+1, part[1][w[0]][1])
            acceptedParts, rejectedParts, inProgressParts = addToCorrectPartList(w[3], updatedRanges, acceptedParts, rejectedParts, inProgressParts)
            # lower range continues with current workflow
            part[1][w[0]] = (part[1][w[0]][0], w[2])
        else:
          if part[1][w[0]][0] >= w[2]:    # no overlap in range, can ignore
            continue
          elif part[1][w[0]][1] < w[2]:   # full range matches, can break out of for loop
            acceptedParts, rejectedParts, inProgressParts = addToCorrectPartList(w[3], part[1], acceptedParts, rejectedParts, inProgressParts)
            break
          else:
            # lower range goes to another workflow
            updatedRanges = copy.deepcopy(part[1])
            updatedRanges[w[0]] = (part[1][w[0]][0], w[2]-1)
            acceptedParts, rejectedParts, inProgressParts = addToCorrectPartList(w[3], updatedRanges, acceptedParts, rejectedParts, inProgressParts)
            # upper range continues with current workflow
            part[1][w[0]] = (w[2], part[1][w[0]][1])
  return acceptedParts

def sumAcceptedCombinations(acceptedParts):
  num = 0
  for a in acceptedParts:
    num += (a['x'][1] - a['x'][0] + 1) * (a['m'][1] - a['m'][0] + 1) * (a['a'][1] - a['a'][0] + 1) * (a['s'][1] - a['s'][0] + 1)
  return num

strs = read_file('day19.txt')
step1_1, _ = parseAllInput(strs)
step2 = findAllPartRanges(step1_1)
step3 = sumAcceptedCombinations(step2)
print(step3)
