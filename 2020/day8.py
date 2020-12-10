from utils import readFile

output = readFile("day8.txt", str, sepChar="\n")

def executeInstruction(output, index, acc):
    op = output[index][:3]
    num = int(output[index][4:])
    
    if op == "acc":
        acc += num
        index += 1
    elif op == "jmp":
        index += num
    else:
        index += 1

    return index, acc


### PART 1 ###

acc1 = 0
index = 0
visited = []

while True:
    if index in visited:
        break
    else:
        visited.append(index)

    index, acc1 = executeInstruction(output, index, acc1)

print(acc1)                 # 1594


### PART 2 ###

# iterate over every nop/jmp instruction
# if visits an instruction again, infinite so break
# otherwise, reaches last instruction
for i in range(len(output)):
    original = output[i]
    if output[i][:3] == "jmp":
        output[i] = "nop " + output[i][4:]
    elif output[i][:3] == "nop":
        output[i] = "jmp " + output[i][4:]
    else:
        continue

    acc2 = 0
    index = 0
    visited = []
    infinite = False
    while True:
        if index == len(output):        # reach instruction after last instruction
            break
        elif index in visited:          # visits an instruction again (loop)
            infinite = True
            break
        else:
            visited.append(index)

        index, acc2 = executeInstruction(output, index, acc2)

    if infinite:
        output[i] = original
    else:
        # print("index: " + str(i))
        break

print(acc2)             # 758