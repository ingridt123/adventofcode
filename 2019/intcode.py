def readFile(filename):
    return [int(t) for t in open(filename, "r").read().split(",")]

def compute(text, inputNum=0, i=0):
    posMode = 0     # position mode = value stored at address # in memory
    imMode = 1      # immediate mode = # itself
    relMode = 2     # relative mode = value stored at address (relative base + #) in memory
    
    relBase = 0
    output = []

    while i < len(text):
        # get data from current position
        opcode = text[i] % 100
        if opcode == 99:
            # day 11
            # return "HALT", text, i
            # day 13
            return output
            # print("HALT")
            # break

        modes = []
        indexes = []

        params = text[i] // 100
        paramNum = 0

        # set paramNum and parameters based on opcode
        if opcode in [1,2,7,8]:
            paramNum = 3            
        elif opcode in [3,4,9]:
            paramNum = 1
        elif opcode in [5,6]:
            paramNum = 2

        for p in range(paramNum):
            modes.append(params % 10)
            if modes[p] == posMode:
                text = checkIndex(i+1+p, text)
                indexes.append(text[i+1+p])
            elif modes[p] == imMode:
                indexes.append(i+1+p)
            elif modes[p] == relMode:
                text = checkIndex(i+1+p, text)
                indexes.append(relBase + text[i+1+p])
            text = checkIndex(indexes[p], text)
            params = params // 10
        # print(i, opcode, modes, indexes)

        # perform operation based on opcode
        if opcode == 1:         # add
            text[indexes[2]] = text[indexes[0]] + text[indexes[1]]
            i += 4
        elif opcode == 2:       # multiply
            text[indexes[2]] = text[indexes[0]] * text[indexes[1]]
            i += 4
        elif opcode == 3:       # stores input
            # text[indexes[0]] = int(input("Enter ID: "))
            text[indexes[0]] = inputNum
            i += 2
        elif opcode == 4:       # prints output
            # print("Outputting", text[indexes[0]])
            output.append(text[indexes[0]])
            # day 11
            # if len(output) == 2:
            #     return output, text, i
            i += 2
        elif opcode == 5:       # jump if true
            if text[indexes[0]] != 0:
                i = text[indexes[1]]
            else:
                i += 3
        elif opcode == 6:       # jump if false
            if text[indexes[0]] == 0:
                i = text[indexes[1]]
            else:
                i += 3
        elif opcode == 7:       # less than
            text[indexes[2]] = int(text[indexes[0]] < text[indexes[1]])
            i += 4
        elif opcode == 8:       # equals
            text[indexes[2]] = int(text[indexes[0]] == text[indexes[1]])
            i += 4
        elif opcode == 9:       # adjust relBase
            relBase += text[indexes[0]]
            i += 2
        else:
            print("INVALID")
            break

def checkIndex(index, text):
    if index >= 0 and index >= len(text):
        text += [0 for i in range(index - len(text) + 1)]
    return text

compute(readFile("day11.txt"))