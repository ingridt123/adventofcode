import sys
from utils import getFilename, readFile
import functools
import operator

filename = getFilename(sys.argv)
output = readFile(filename, str)

# iterate over each -- index+3 (mod length)
# add to count if tree (#)

counts = [0, 0, 0, 0, 0]
indices = [0, 0, 0, 0, 0]
add = [1, 3, 5, 7, 1]
for o in range(len(output)):
    for i in range(len(indices)):
        if i != len(indices)-1 or o % 2 == 0:
            if output[o][indices[i]] == '#':
                counts[i] += 1
            indices[i] = (indices[i] + add[i]) % len(output[o])

print(counts[1])                                        # 176
print(functools.reduce(operator.mul, counts, 1))        # 5872458240
