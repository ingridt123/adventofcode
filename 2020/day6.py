from utils import readFile

output = readFile("day6.txt", str, sepChar="\n")

### PART 1 ###

def addCurrentGroup1(count, currentGroup):
    return count + len(currentGroup), set()


count1 = 0
currentGroup = set()
for o in output:
    if o == '':
        count1, currentGroup = addCurrentGroup1(count1, currentGroup)
    else:
        for q in o:
            currentGroup.add(q)

if len(currentGroup) != 0:
    count1, currentGroup = addCurrentGroup1(count1, currentGroup)

print(count1)


### PART 2 ###

def addCurrentGroup2(count, currentGroup, groupSize):
    for q in currentGroup:
        if currentGroup[q] == groupSize:
            count += 1

    return count, dict(), 0


count2 = 0
currentGroup = dict()
groupSize = 0
for o in output:
    if o == '':
        count2, currentGroup, groupSize = addCurrentGroup2(count2, currentGroup, groupSize)
    else:
        groupSize += 1
        for q in o:
            if q in currentGroup:
                currentGroup[q] += 1
            else:
                currentGroup[q] = 1

if currentGroup:
    count2, currentGroup, groupSize = addCurrentGroup2(count2, currentGroup, groupSize)

print(count2)