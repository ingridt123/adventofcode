import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar="\n")

result = []
for o in output:
    if 'mask' in o:
        result.append([int(x) if x != 'X' else x for x in o[o.index('=')+2:]])
    elif 'mem' in o:
        result.append([int(o[o.index('[')+1:o.index(']')]), int(o[o.index('=')+2:])])

MASK_LEN = len(result[0])

def convertToBinary(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal % 2)
        decimal //= 2
    binary += ([0] * (MASK_LEN - len(binary)))
    binary.reverse()
    
    return binary


def convertToDecimal(binary):
    decimal = 0
    binary.reverse()
    for i in range(len(binary)):
        decimal += (binary[i] * (2 ** i))

    return decimal


### PART 1 ###

def applyMask1(mask, binary):
    for i in range(len(mask)):
        if mask[i] != 'X':
            binary[i] = mask[i]

    return binary


memoryDict = dict()
currentMask = []
for r in result:
    if len(r) > 2:
        currentMask = r
    else:
        binary = convertToBinary(r[1])
        binary = applyMask1(currentMask, binary)
        decimal = convertToDecimal(binary)
        memoryDict[r[0]] = decimal

print(sum(list(memoryDict.values())))                   # 11501064782628


### PART 2 ###

def applyMask2(mask, binary):
    maskIndices = []
    for i in range(len(mask)):
        if mask[i] != 0:
            binary[i] = mask[i]
        if mask[i] == 'X':
            maskIndices.append(i)

    return binary, maskIndices


memoryDict = dict()
currentMask = []
for r in result:
    if len(r) > 2:
        currentMask = r
    else:
        binary = convertToBinary(r[0])
        binary, maskIndices = applyMask2(currentMask, binary)
        firstIndex = MASK_LEN - len(maskIndices)

        for val in range(2 ** len(maskIndices)):
            binaryTemp = convertToBinary(val)
            for i in range(len(maskIndices)):
                binary[maskIndices[i]] = binaryTemp[firstIndex+i]
            memoryDict[convertToDecimal(binary[:])] = r[1]

print(sum(list(memoryDict.values())))                   # 5142195937660