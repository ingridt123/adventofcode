import os
import sys
import getopt

try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], 'm:pc')
except getopt.GetoptError:
    print('usage: git.py <day#> -m <commitMsg> -p -c')
    sys.exit(2)

try:
    dayNum = int(args[0])
except IndexError:
    print('usage: git.py <day#> -m <commitMsg> -p -c')
    sys.exit(2)

dayFile = "day" + str(dayNum) + ".py"
dayTxt = "day" + str(dayNum) + ".txt"

commit = True
commitMsg = "Add day " + str(dayNum) + " for 2020"
push = True

for k,v in opts:
    if k == "-c":
        commit = False
        push = False
    elif k == "-m":
        commitMsg = v
    elif k == "-p":
        push = False

# Git commands
os.system("git add " + dayFile + " " + dayTxt)

if commit:
    os.system("git commit -m \"" + commitMsg + "\"")

if push:
    os.system("git push")