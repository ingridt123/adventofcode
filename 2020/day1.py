import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, int)

outputDict = {}
for o in output:
    outputDict[o] = []

finalTotal = 2020

def findNum1(arrDict, total):
    for a in list(arrDict.keys()):
        if total-a in arrDict:
            return (a, total-a)
    return ()

def findNum2(arrDict, total):
    for a in list(arrDict.keys()):
        result = findNum1(arrDict, total-a)
        if result != ():
            return (a, result[0], result[1])

### PART 1 ###

nums1 = findNum1(outputDict, finalTotal)
print(nums1[0] * nums1[1])                      # 1005459


### PART 2 ###

nums2 = findNum2(outputDict, finalTotal)
print(nums2[0] * nums2[1] * nums2[2])           # 92643264