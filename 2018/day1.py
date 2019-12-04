import methods
# input = [+1, -2, +3, +1, +1, -2]

# read input from txt file
input = methods.readFile("day1.txt")

# loop through input
freq = 0
freqs = [freq]
input = [int(x.replace('\n', '')) for x in input]
found = False
while found == False:
    for i in range(len(input)):
        freq += input[i]
    if freq in freqs:
            print("First frequency repeated: " + str(freq))
            found = True
            break
    else:
        freqs.append(freq)

print(freq)