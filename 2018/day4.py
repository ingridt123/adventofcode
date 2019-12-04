import methods
from functools import reduce

# read input from txt file
input = methods.readFile("day4.txt")
input = [x.replace('\n', '') for x in input]

# create dictionary with date/time: description
# count for each guard using 2d array

# 0 = month, 1 = day, 2 = hour, 3 = min, 5 = id or w/f
sortedInput = []
# sort by time
for i in input:
    month = i.index("-")+1
    day = i[month:].index("-")+1
    hour = i.index(" ")+1
    minute = i.index(":")+1
    item = i[hour:].index(" ")+1
    temp = [int(i[month:month+2]), int(i[month:][day:day+2]), int(i[hour:hour+2]), int(i[minute:minute+2])]
    if temp[2] == 23:
        temp[1] += 1
        temp.insert(2, temp[3]-40)
    else:
        temp.insert(2, temp[3]+19)
    if i[hour:][item] == "G":
        numStart = i.index("#")+1
        numEnd = i[numStart:].index(" ") + numStart
        temp.append(i[numStart:numEnd])
    else:
        temp.append(i[hour:][item])
    sortedInput.append(temp)

sortedInput.sort()

# create dictionary with key = guard id, value = list of times (count times when asleep)
times = {}
curGuard = -1
fallsAsleep = -1
for i in sortedInput:
    if i[5].isdigit():
        curGuard = int(i[5])
        if curGuard not in times:
            times[curGuard] = [0 for x in range (80)]
    elif i[5] == 'f':
        fallAsleep = i[2]
    elif i[5] == 'w':
        # loop from fallsAsleep time to wakeUp time --> add 1 to index at times[curGuard]
        for index in range(fallAsleep, i[2]):
            times[curGuard][index] += 1

# get sum of max list
sums = []
for i in times:
    sums.append(reduce((lambda x,y: x+y), times[i]))

# get max guard --> minute that guard slept most
maxGuard = list(times.keys())[0]
maxTimes = times[maxGuard]
maxTime = maxTimes.index(max(maxTimes))
if maxTime < 20:
    maxTime += 40
else:
    maxTime -= 19

print(maxGuard * maxTime)