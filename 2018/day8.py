import methods

# read input from txt file
# input = methods.readFile("day8.txt")
input = methods.readFile("day8-test.txt")
input = [int(x) for x in input[0].split()]


def parse(data):
    child = 
    meta = 
    metaSum = 
    return 

    if child == 0:



def readTree(child, meta, list):
    print(list)
    if child != 0:
        sum = 0
        for i in range(child):
            sum += readTree(list[2], list[3], list[2:])
            print(sum)
    # return sum of metadata
    return sum(list[2:2+meta])
        
        

readTree(input[0], input[1], input)