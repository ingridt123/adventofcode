from utils import readFile

output = readFile("day8.txt", str, sepChar="\n")

### PART 1 ###

acc1 = 0
index = 0
visited = []

while True:
    op = output[index][:3]
    num = int(output[index][4:])
    
    if index in visited:
        break
    else:
        visited.append(index)

    if op == "acc":
        acc1 += num
        index += 1
    elif op == "jmp":
        index += num
    else:
        index += 1

print(acc1)


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
        if index == len(output):
            break

        op = output[index][:3]
        num = int(output[index][4:])

        if index in visited:
            infinite = True
            break
        else:
            visited.append(index)

        if op == "acc":
            acc2 += num
            index += 1
        elif op == "jmp":
            index += num
        else:
            index += 1

    if infinite:
        output[i] = original
    else:
        # print("index: " + str(i))
        break

print(acc2)