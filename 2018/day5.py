import methods

def main():
    # read input from txt file
    input = methods.readFile("day5.txt")[0]
    # input = "dabAcCaCBAcCcaDA"

    print(polymer(input))

    tempInput = input.lower()
    uniq = ''.join(set(tempInput))

    testLen = []
    for letter in uniq:
        testInput = input.replace(str(letter), '')
        testInput = testInput.replace(str(letter.upper()), '')
        testLen.append(polymer(testInput))

    print(min(testLen))


def polymer(input):
    changed = True
    while changed:
        changed = False
        temp = []
        prevIndex = 0
        i = 1
        while i < len(input):
            if (abs(ord(input[i-1]) - ord(input[i]))) == 32:
                temp.append(input[prevIndex:i-1])
                prevIndex = i+1
                changed = True
                i += 1
            i += 1
        temp.append(input[prevIndex:])
        input = ''.join(temp)

    # print(input)
    return len(input)

main()