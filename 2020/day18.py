import sys
from utils import getFilename, readFile
import math

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar="\n")

output = [o.split() for o in output]

newOutput = []
for o in output:
    newO = []
    for c in o:
        while '(' in c:
            newO.append(c[0])
            c = c[1:]

        if ')' in c:
            newO.append(c[:c.index(')')])
        else:
            newO.append(c)
        
        while ')' in c:
            newO.append(c[-1])
            c = c[:-1]
    newOutput.append(newO)


def findMatchingParan(expr):
    paranCount = 1
    index = len(expr)-2
    while paranCount > 0:
        if expr[index] == ')':
            paranCount += 1
        elif expr[index] == '(':
            paranCount -= 1
        if paranCount == 0:
            return index
        index -= 1

    return math.inf
    

### PART 1 ###
# evaluate1 recursively from right to left
# if see a right paranthesis, find matching left paranthesis and evaluate1 smaller portion first

def evaluate1(expr):
    if len(expr) == 1:
        return int(expr[0])

    index = -2
    rightmostResult = -1
    if expr[-1] == ')':
        index = findMatchingParan(expr)
        rightmostResult = evaluate1(expr[index+1:-1])
        if index > 0:
            index -= 1
    else:
        rightmostResult = int(expr[-1])

    if index != 0:
        result = evaluate1(expr[:index])
        if expr[index] == '+':
            return result + rightmostResult
        else:
            return result * rightmostResult
    return rightmostResult


total = 0
for o in newOutput:
    total += evaluate1(o)
print(total)                    # 8929569623593


### PART 2 ###

