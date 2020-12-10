import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, int)

PREAMBLE_LENGTH = 25

# check if two of previous preambleLength integers sum to output[i]
def sumPrev(output, i, preambleLength):
    sum = output[i]
    numsDict = dict()
    for k in range(i-preambleLength, i):
        numsDict[output[k]] = sum - output[k]
    
    for n in numsDict:
        if numsDict[n] in numsDict:
            return True
    
    return False

# check if group of two or more contiguous numbers sum to target
def sumNext(output, i, target):
    nums = []
    while sum(nums) < target:
        nums.append(output[i])
        i += 1

    if sum(nums) == target and len(nums) > 1:
        return nums
    else:
        return []


### PART 1 ###

num = -1
for i in range(PREAMBLE_LENGTH, len(output)):
    if not sumPrev(output, i, PREAMBLE_LENGTH):
        num = output[i]
        break
print(num)                                          # 258585477

### PART 2 ###

result = []
for i in range(len(output)):
    result = sumNext(output, i, num)
    if result != []:
        break
min = min(result)
max = max(result)
print('%d + %d = %d' % (min, max, min+max))         # 36981213