import methods

# read input from txt file
input = methods.readFile("day2.txt")
input = [x.replace('\n', '') for x in input]

## PART 1 ##
# count number repeats of 2 and 3
two = 0
three = 0

# create dictionary of occurrences and find occurrences of 2 and 3
for string in input:
    letDict = {}
    for letter in string:
        if letter not in letDict:
            letDict[letter] = 1
        else:
            letDict[letter] += 1
    if 2 in letDict.values():
        two += 1
    if 3 in letDict.values():
        three += 1

print(two * three)


## PART 2 ##
for i in range(len(input)):
    for j in range(i+1, len(input)):
        count = 0
        for let in range(len(input[i])):
            if input[i][let] != input[j][let]:
                count += 1
        if count == 1:
            print(str(i) + " " + str(j))
            print(input[i] + " " + input[j])
