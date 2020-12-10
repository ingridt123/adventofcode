import sys
from utils import getFilename, readFile
import re

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar="\n")

credentials = []
c = {}
for o in output:
    if o == '':
        credentials.append(c)
        c = {}
    else:
        splitOutput = o.split()
        for s in splitOutput:
            index = s.index(":")
            key = s[:index]
            value = s[index+1:]
            c[key] = value

if c != {}:
    credentials.append(c)

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

### PART 1 ###
count1 = 0
for c in credentials:
    valid = True
    for r in requiredFields:
        if r not in c:
            valid = False
            break
    if valid:
        count1 += 1
print(count1)                       # 260

### PART 2 ###
count2 = 0
for c in credentials:
    valid = True
    for r in requiredFields:
        if r not in c:
            valid = False
            break
        else:
            value = c[r]
            if (r == 'byr' and not (1920 <= int(value) <= 2002)) or \
               (r == 'iyr' and not (2010 <= int(value) <= 2020)) or \
               (r == 'eyr' and not (2020 <= int(value) <= 2030)) or \
               (r == 'hgt' and ((value[-2:] != 'cm' and value[-2:] != 'in') or \
                               (value[-2:] == 'cm' and not (150 <= int(value[:-2]) <= 193)) or \
                               (value[-2:] == 'in' and not (59 <= int(value[:-2]) <= 76)))) or \
               (r == 'hcl' and re.fullmatch(r'^#[a-f0-9]{6}?$', value) == None) or \
               (r == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) or \
               (r == 'pid' and re.fullmatch(r'^\d{9}?$', value) == None):
                valid = False
                break
    if valid:
        count2 += 1
print(count2)                       # 153