import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar="\n")

rulesDict = dict()
index = -1
for o in output:
    if o == '':
        index = output.index(o) + 1
        break
    else:
        ruleNum = int(o[:o.index(':')])
        o = o[o.index(':')+1:]
        ruleList = []
        if '\"' in o:
            ruleList = [o[o.index('\"')+1:o.rindex('\"')]]
        else:
            while '|' in o:
                ruleList.append([int(x) for x in o[:o.index('|')].split()])
                o = o[o.index('|')+1:]
            ruleList.append([int(x) for x in o.split()])
        rulesDict[ruleNum] = ruleList
messages = output[index:]

# for each part of rule, expand until only a's and b's
# returns list of all possible combinations
def expandRule(rule, prevStr):
    # TODO: add memo
    if type(rule) == int:
        if len(rulesDict[rule]) == 1 and rulesDict[rule][0].isalpha():
            return rulesDict[rule][0]
        return expandRule(rulesDict[rule], prevStr)

    possibilities = []
    for r in rule:
        possibilities.append(expandRule(r))
    return possibilities

    # possibilities = []
    # for r in rule:
    #     possibilities += expandRule(r)


zeroRule = rulesDict[0][0]
print(zeroRule)
print(expandRule([4,4]), "")
print(expandRule([4,1,5]), "")

# print(rulesDict)
# print(messages)