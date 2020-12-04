from utils import readFile

output = readFile("day2.txt", str, sepChar="\n")
splitOutput = []
for o in output:
    index1 = o.index("-")
    index2 = o.index(" ")
    index3 = o.index(":")
    splitOutput.append((int(o[:index1]), int(o[index1+1:index2]), o[index2+1:index3], o[index3+2:]))

### PART 1/2 ###

validCount1 = 0
validCount2 = 0
for s in splitOutput:
    ranges = (s[0], s[1])
    letter = s[2]
    password = s[3]

    count = password.count(letter)
    if count >= ranges[0] and count <= ranges[1]:
        validCount1 += 1

    check1 = password[ranges[0]-1] == letter
    check2 = password[ranges[1]-1] == letter
    if (check1 and not check2) or (not check1 and check2):
        validCount2 += 1

print(validCount1)
print(validCount2)

