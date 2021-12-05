from utils import getFilename, readFile

filename = 'day1.txt'
output = readFile(filename, int)

### PART 1 ###
print(sum([output[i-1] < output[i] for i in range(1, len(output))]))

### PART 2 ###
print(sum([sum(output[i-3:i]) < sum(output[i-2:i+1]) for i in range(3, len(output))]))