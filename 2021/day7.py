from utils import getFilename, readFile
from collections import Counter

filename = 'day7.txt'
output = readFile(filename, 'int')

output = [int(o) for o in output[0].split(',')]

### PART 1 ###
output.sort()
startIndex = 0
endIndex = 0
minDist = float('inf')
minPos = 0
for x in range(min(output), max(output)+1):
    if x == max(output):
        endIndex = len(output)-1
    else:
        while output[endIndex] <= x:
            endIndex += 1
    lessThan = output[:startIndex]
    greaterThan = output[endIndex:]
    dist = x * len(lessThan) - sum(lessThan) + sum(greaterThan) - x * len(greaterThan)
    if dist < minDist:
        minDist = dist
        minPos = x
    startIndex = endIndex
print(minDist, minPos)

### PART 2 ###
output_counter = Counter(output)
minDist = float('inf')
minPos = 0
for x in range(min(output), max(output)+1):
    dist = 0
    for c in output_counter:
        diff = abs(c - x)
        dist += diff / 2 * (1 + diff) * output_counter[c]
    if dist < minDist:
        minDist = dist
        minPos = x
print(int(minDist), minPos)