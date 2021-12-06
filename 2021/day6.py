from utils import getFilename, readFile
from collections import Counter
# import numpy as np

filename = 'day6.txt'
output = readFile(filename, '')

output = [int(o) for o in output[0].split(',')]

### PART 1 ###
output1 = output[:]
for i in range(80):
    numZeros = output1.count(0)
    output1 = list(map(lambda x: x - 1 if x > 0 else 6, output1))
    output1 += [8] * numZeros
print(len(output1))

### PART 2 ###
fish_counter = Counter(output)
for i in range(256):
    temp_counter = Counter()
    for fish in fish_counter:
        if fish == 0:
            temp_counter[6] += fish_counter[fish]
            temp_counter[8] += fish_counter[fish]
        else:
            temp_counter[fish-1] += fish_counter[fish]
    fish_counter = temp_counter
print(sum(fish_counter.values()))
