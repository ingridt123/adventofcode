def readFile(filename, type, sepChar=""):
    if sepChar == "":
        output = [t for t in open(filename, "r").read().split()]
    elif sepChar == "\n":
        output = [t for t in open(filename, "r").read().splitlines()]
    if type == int:
        return [int(t) for t in output]
    return output