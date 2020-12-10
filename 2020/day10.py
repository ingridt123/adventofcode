from utils import readFile

output = readFile("day10.txt", int)

output.sort()

### PART 1 ###

joltage = 0
ones = 0
threes = 0

for o in output:
    if o - joltage == 1:
        ones += 1
    elif o - joltage == 3:
        threes += 1
    joltage = o

threes += 1   # add device's built-in joltage adapter

print(ones * threes)


### PART 2 ###

start = 0
target = max(output) + 3

# check max next three -- if within 3 then can be next adapter
def findAllArrangements(index, joltage, target, output, memo):
    if joltage + 3 == target:
        return 1
    
    if joltage in memo:
        return memo[joltage]

    arrangements = 0
    for i in range(index+1, min(index+4, len(output))):
        if output[i] <= joltage + 3:
            arrangements += findAllArrangements(i, output[i], target, output, memo)
        else:
            break
    memo[joltage] = arrangements

    return arrangements

print(findAllArrangements(-1, start, target, output, dict()))
