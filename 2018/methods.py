# read input from txt file
def readFile(fileName):
    f = open(fileName, "r")
    input = f.readlines()
    f.close()
    input = [x.replace('\n', '') for x in input]

    return input