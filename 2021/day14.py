from utils import getFilename, readFile
from collections import Counter, defaultdict

filename = 'day14.txt'
output = readFile(filename, str, sepChar='\n')

template = output[0]
rules = dict()
for i in range(2, len(output)):
    temp = output[i].split()
    rules[temp[0]] = temp[2]

### PART 1 ###
for step in range(10):
    new_template = ''
    for i in range(len(template)-1):
        new_template += template[i]
        if template[i:i+2] in rules:
            new_template += rules[template[i:i+2]]
    new_template += template[-1]
    template = new_template

template_counts = Counter(template).most_common()
print(template_counts[0][1] - template_counts[-1][1])

### PART 2 ###
template = output[0]
template_dict = defaultdict(int)
for i in range(len(template)-1):
    template_dict[template[i:i+2]] += 1

for step in range(40):
    new_template_dict = defaultdict(int)
    for pair in template_dict:
        if pair in rules:
            new_template_dict[pair[0] + rules[pair]] += template_dict[pair]
            new_template_dict[rules[pair] + pair[1]] += template_dict[pair]
        else:
            new_template_dict[pair] += template_dict[pair]

    template_dict = new_template_dict

# print(template_dict)
letters_dict = defaultdict(int)
for pair in template_dict:
    letters_dict[pair[0]] += template_dict[pair]
    letters_dict[pair[1]] += template_dict[pair]
letters_dict[template[0]] += 1      # only two letters not double counted are first and last (same as original template)
letters_dict[template[-1]] += 1

max_occur = float('-inf')
min_occur = float('inf')
for letter in letters_dict:
    if letters_dict[letter] // 2 > max_occur:
        max_occur = letters_dict[letter] // 2
    if letters_dict[letter] // 2 < min_occur:
        min_occur = letters_dict[letter] // 2
# print(letters_dict)
print(max_occur - min_occur)