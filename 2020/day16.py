import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar="\n")
# print(output)

def addToRange(allRanges, range):
    added = False
    for low in allRanges:
        high = allRanges[low]
        if low <= range[0] <= high:
            allRanges[low] = range[1]
        elif low <= range[1] <= high:
            allRanges[low] = -1
            allRanges[range[0]] = high
        else:
            continue
        added = True
        break

    if not added:
        allRanges[range[0]] = range[1]

    return allRanges


fields = dict()         # field -> list of lists for ranges
tickets = []
allRanges = dict()      # low -> high

ticket = False
for o in output:
    if o == '' or o == 'your ticket:' or o == 'nearby tickets:':
        ticket = True
    elif ticket:
        tickets.append([int(f) for f in o.split(',')])
    else:
        colonIndex = o.index(':')
        orIndex = o.rindex('or')
        field = o[:colonIndex]
        ranges = []
        ranges.append([int(r) for r in o[colonIndex+2:orIndex-1].split('-')])
        ranges.append([int(r) for r in o[orIndex+3:].split('-')])
        fields[field] = ranges

        # add combined ranges
        # if start/end within another range, extend range
        # otherwise add range to dict
        addToRange(allRanges, ranges[0])
        addToRange(allRanges, ranges[1])


### PART 1 ###

count = 0
for i in range(1, len(tickets)):
    for j in range(len(tickets[i])):
        valid = False
        for low in allRanges:
            if low <= tickets[i][j] <= allRanges[low]:
                valid = True
                break

        if not valid:
            count += tickets[i][j]

print(count)                            # 20060


### PART 2 ###

def removeFinalized(possibleFields, index, finalized):
    finalizedField = possibleFields[index][0]
    if len(possibleFields[index]) == 1 and finalizedField not in finalized:
        finalized.append(finalizedField)
        for p in range(len(possibleFields)):
            if p != index and finalizedField in possibleFields[p]:
                possibleFields[p].remove(finalizedField)
                possibleFields, finalized = removeFinalized(possibleFields, p, finalized)

    return possibleFields, finalized


i = 1
while i < len(tickets):
    for j in range(len(tickets[i])):
        valid = False
        for low in allRanges:
            if low <= tickets[i][j] <= allRanges[low]:
                valid = True
                break

        if not valid:
            break

    if not valid:
        tickets.pop(i)
    else:
        i += 1


# determine possible ranges for each field -- start with all dict keys and eliminate
# if one is set, then remove from all others
possibleFields = [list(fields.keys()) for i in range(len(tickets[0]))]
finalized = []

for i in range(1, len(tickets)):
    for j in range(len(tickets[0])):
        if len(possibleFields[j]) > 1:
            k = 0
            while k < len(possibleFields[j]):
                # check if tickets[i][j] in range of possibleFields[j][k]
                # if yes, keep
                # if no, remove
                fieldRanges = fields[possibleFields[j][k]]
                possible = False
                for r in fieldRanges:
                    if r[0] <= tickets[i][j] <= r[1]:
                        possible = True
                        break

                if not possible:
                    possibleFields[j].pop(k)
                else:
                    k += 1

            possibleFields, finalized = removeFinalized(possibleFields, j, finalized)
        
# print(possibleFields)

departureFields = []
for f in range(len(possibleFields)):
    if 'departure' in possibleFields[f][0]:
        departureFields.append(f)

result = 1
for d in departureFields:
    result *= tickets[0][d]

print(result)                               # 2843534243843