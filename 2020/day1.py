from utils import readFile

output = readFile("day1.txt", int)
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
print(nums1[0] * nums1[1])


### PART 2 ###

nums2 = findNum2(outputDict, finalTotal)
print(nums2[0] * nums2[1] * nums2[2])


# for o1 in output:
#     for o2 in output:
#         if 

#     if total - o in output:
#         print(o * (total - o))
#         break
