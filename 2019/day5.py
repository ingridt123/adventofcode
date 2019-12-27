text = open("day5.txt", "r").read().split(",")
text = [int(t) for t in text]
# text = [1002,4,3,4,33]
# text = [3,9,8,9,10,9,4,9,99,-1,8]
# text = [3,9,7,9,10,9,4,9,99,-1,8]
# text = [3,3,1108,-1,8,3,4,3,99]
# text = [3,3,1107,-1,8,3,4,3,99]
# text = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# text = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
# text = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

posMode = 0     # position mode = value stored at address # in memory
imMode = 1      # immediate mode = #

i = 0
while i < len(text):
    # get values from current position
    opcode = text[i] % 100
    # print("opcode", opcode)
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
        # print(modes)
        if modes[p] == posMode:
            vals.append(text[text[i+p+1]])
        elif modes[p] == imMode:
            vals.append(text[i+p+1])
        params = params // 10
    # print("modes", modes)
    print(i, opcode, modes, vals)
    # print(text)

    # perform operation based on opcode
    if opcode == 1:         # add
        text[text[i+3]] = vals[0] + vals[1]
        i += 4
    elif opcode == 2:      # multiply
        text[text[i+3]] = vals[0] * vals[1]
        i += 4
    elif opcode == 3:      # stores input
        text[text[i+1]] = int(input("Enter ID: "))
        i += 2
    elif opcode == 4:      # outputs
        print(text[text[i+1]])
        i += 2
    elif opcode == 5:       # jump if true
        print(vals[1])
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
    print(i)
    # print(text)