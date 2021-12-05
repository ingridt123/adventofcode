def getFilename(argv):
    filename = argv[0]
    filename = filename[:filename.index(".py")]

    if len(argv) > 1:
        filename += "-test"
        if len(argv) > 2:
            filename += argv[2]
        else:
            filename += "1"

    return filename + ".txt"


def readFile(filename, type, sepChar=""):
    if sepChar == "":
        output = [t for t in open(filename, "r").read().split()]
    elif sepChar == "\n":
        output = [t for t in open(filename, "r").read().splitlines()]
    if type == int:
        return [int(t) for t in output]
    return output