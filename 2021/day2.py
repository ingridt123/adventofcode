from utils import getFilename, readFile

filename = 'day2.txt'
output = readFile(filename, '')

output = [(output[i], int(output[i+1])) for i in range(len(output)) if i % 2 == 0]

### PART 1 ###
horPos = 0
depth = 0
for dir, dist in output:
    if dir == 'forward': horPos += dist
    elif dir == 'up':    depth -= dist
    elif dir == 'down':  depth += dist
print(horPos * depth)

### PART 2 ###
aim = 0
horPos = 0
depth = 0
for dir, dist in output:
    if dir == 'forward':
        horPos += dist
        depth += aim * dist
    elif dir == 'up':    aim -= dist
    elif dir == 'down':  aim += dist
print(horPos * depth)