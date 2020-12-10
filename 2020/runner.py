import os
import sys
import getopt

try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], 't:')
except getopt.GetoptError:
    print('usage: runner.py <day#> -t <test#>')
    sys.exit(2)

try:
    dayNum = args[0]
except IndexError:
    print('usage: runner.py <day#> -t <test#>')
    sys.exit(2)

dayFile = "day" + dayNum + ".py"
command = "python3 " + dayFile

for k,v in opts:
    if k == "-t":
        command += " " + k
        if len(v) != 0:
            command += " " + v

os.system(command)


# if __name__ == "__main__":
#     main(sys.argv[1:])


