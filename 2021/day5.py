from utils import getFilename, readFile
from collections import Counter

filename = 'day5.txt'
output = readFile(filename, '')

output = [x for o in output for x in o.split(',')]
output = [output[i:i+5] for i in range(0, len(output)-4, 5)]

### PART 1 & 2 ###
visited = []
for x1, y1, _, x2, y2 in output:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1 == x2:
        yFrom = min(y1, y2)
        yTo = max(y1, y2)
        visited += [(x1, y) for y in range(yFrom, yTo+1)]
    elif y1 == y2:
        xFrom = min(x1, x2)
        xTo = max(x1, x2)
        visited += [(x, y1) for x in range(xFrom, xTo+1)]
    else:
        xChange = 1 if x1 < x2 else -1
        yChange = 1 if y1 < y2 else -1
        dist = abs(x1 - x2)
        visited += [(x1+i*xChange, y1+i*yChange) for i in range(dist+1)]
counter = Counter(visited)
count = sum([counter[c] > 1 for c in counter])

# print(counter)
print(count)