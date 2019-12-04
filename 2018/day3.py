import methods

# read input from txt file
input = methods.readFile("day3.txt")
input = [x.replace('\n', '') for x in input]

# 2D array representing the fabric
width = 1000
height = 1000
fabric = [['.' for col in range(width)] for row in range(height)]

# add to fabric
info = []
untouched = []
for i in range(len(input)):
    index0 = input[i].find(' ')
    index1 = input[i].find(' @ ') + 3
    index2 = input[i].find(': ')
    index3 = index2 + 2

    # 0 = id
    # 1 = from left
    # 2 = from top
    # 3 = width
    # 4 = height
    info.append([input[i][1:index0]] + input[i][index1:index2].split(',') + input[i][index3:].split('x'))
    info[i] = [int(x) for x in info[i]]

    overlap = False
    for ver in range(info[i][2], info[i][2]+info[i][4]):
        for hor in range(info[i][1], info[i][1]+info[i][3]):
            if fabric[ver][hor] == '.':
                fabric[ver][hor] = info[i][0]
            else:
                if fabric[ver][hor] in untouched:
                    untouched.remove(fabric[ver][hor])
                fabric[ver][hor] = 'X'
                overlap = True
    if overlap == False:
        untouched.append(info[i][0])

count = 0
for row in fabric:
    for cell in row:
        if cell == 'X':
            count += 1

print(count)
print(untouched)