import methods
import collections

# read input from txt file
# input = methods.readFile("day7.txt")
input = methods.readFile("day7-test.txt")
input = [x.replace('\n', '') for x in input]

firstIndex = 5
secondIndex = 36
inSteps = [[x[firstIndex], x[secondIndex]] for x in input]

# dictionary of lists of steps that need to be finished before given step
stepCond = {}
for i in inSteps:
    if i[1] in stepCond:
        stepCond[i[1]].append(i[0])
        stepCond[i[1]].sort()
    else:
        stepCond[i[1]] = [i[0]]

    if i[0] not in stepCond:
        stepCond[i[0]] = []

## PART 1 ##
stepsList = []

# find first step
firstSteps = []
for i in sorted(stepCond):
    if stepCond[i] == []:
        firstSteps.append(i)
stepsList.append(firstSteps[0])
stepCond.pop(firstSteps[0])

# list of possible steps currently
firstSteps.pop(0)
curSteps = firstSteps
desiredLength = len(stepCond.keys()) + 1
while len(stepsList) < desiredLength:
    for i in sorted(stepCond):
        # if all necessary steps are completed
        if i not in curSteps and set(stepCond[i]).issubset(stepsList):
            curSteps.append(i)
    curSteps.sort()

    stepsList.append(curSteps[0])
    stepCond.pop(curSteps[0])
    curSteps.pop(0)

print(''.join(stepsList))


## PART 2 ##
# 2D array for workers x seconds
stepsArray = []
curSteps = firstSteps
workers = 5
counts = [0 for i in range(workers)]

stepsArray.append(['.' for i in range(workers)])
stepsArray[0][0] = 'C'
counts[0] = 60 + ord(stepsArray[0][0]) - 64
while len(stepsList) < desiredLength:
    stepsArray.append(['.' for i in range(workers)])

#-64


# # list of lists to determine order
# steps = []
# for i in inSteps:
#     for s in steps:
#         if i[0] == s[-1]:
#             s.append(i[1])
        
