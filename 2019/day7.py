from itertools import permutations

text = open("day7.txt", "r").read().split(",")
text = [int(t) for t in text]
# text = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# text = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# text = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

posMode = 0     # position mode = value stored at address # in memory
imMode = 1      # immediate mode = #

phaseSettings = permutations([0,1,2,3,4])

def intcode(inputs):
    i = 0
    inputIndex = 0
    while i < len(text):
        # get values from current position
        opcode = text[i] % 100
        modes = []
        vals = []
        params = text[i] // 100
        paramNum = 0

        # set paramNum and parameters based on opcode
        if opcode in [1,2,7,8]:
            paramNum = 3
        elif opcode in [3,4]:
            paramNum = 1
        elif opcode in [5,6]:
            paramNum = 2
        for p in range(paramNum):
            modes.append(params % 10)
            if modes[p] == posMode:
                vals.append(text[text[i+p+1]])
            elif modes[p] == imMode:
                vals.append(text[i+p+1])
            params = params // 10
        # print(i, opcode, modes, vals)

        # perform operation based on opcode
        if opcode == 1:         # add
            text[text[i+3]] = vals[0] + vals[1]
            i += 4
        elif opcode == 2:      # multiply
            text[text[i+3]] = vals[0] * vals[1]
            i += 4
        elif opcode == 3:      # stores input
            text[text[i+1]] = inputs[inputIndex]
            inputIndex += 1
            i += 2
        elif opcode == 4:      # outputs
            # print(text[text[i+1]])
            return text[text[i+1]]
            # i += 2
        elif opcode == 5:       # jump if true
            if vals[0] != 0:
                i = vals[1]
            else:
                i += 3
        elif opcode == 6:       # jump if false
            if vals[0] == 0:
                i = vals[1]
            else:
                i += 3
        elif opcode == 7:       # less than
            if vals[0] < vals[1]:
                text[text[i+3]] = 1
            else:
                text[text[i+3]] = 0
            i += 4
        elif opcode == 8:       # equals
            if vals[0] == vals[1]:
                text[text[i+3]] = 1
            else:
                text[text[i+3]] = 0
            i += 4
        elif opcode == 99:
            break
        else:
            break

# PART 1
signals1 = []

for s in phaseSettings:
    prevOutput = 0
    for x in s:
        prevOutput = intcode([x, prevOutput])
    signals1.append(prevOutput)

print(max(signals1))


# PART 2