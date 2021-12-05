from utils import getFilename, readFile

filename = 'day3.txt'
output = readFile(filename, '\n')

bitSums = [sum([int(num[i]) for num in output]) for i in range(len(output[0]))]
commonBits = [bitSum >= len(output) // 2 for bitSum in bitSums]

### PART 1 ###
gamma = sum([commonBits[-(i+1)] * 2**i for i in range(len(commonBits))])
epsilon = sum([(not commonBits[-(i+1)]) * 2**i for i in range(len(commonBits))])
print(gamma * epsilon)

### PART 2 ###
oxygenList = output[:]
i = 0
while len(oxygenList) > 1:
    commonBit = sum([int(o[i]) for o in oxygenList]) >= len(oxygenList) / 2
    oxygenList = list(filter(lambda x: int(x[i]) == int(commonBit), oxygenList))
    i += 1
oxygen = sum([int(oxygenList[0][-(i+1)]) * 2**i for i in range(len(oxygenList[0]))])

co2List = output[:]
i = 0
while len(co2List) > 1:
    commonBit = sum([int(c[i]) for c in co2List]) < len(co2List) / 2
    co2List = list(filter(lambda x: int(x[i]) == int(commonBit), co2List))
    i += 1
co2 = sum([int(co2List[0][-(i+1)]) * 2**i for i in range(len(co2List[0]))])

print(oxygen * co2)