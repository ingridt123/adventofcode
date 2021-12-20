from utils import getFilename, readFile
from collections import Counter, defaultdict

filename = 'day8.txt'
output = readFile(filename, str, sepChar='\n')

output = [o.split() for o in output]

ALL_SEGMENTS = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
NUM_SEGMENTS = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}
SEGMENTS = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd' ,'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'}
}
SEGMENTS_REVERSE = {
    frozenset({'a', 'b', 'c', 'e', 'f', 'g'}): 0,
    frozenset({'c', 'f'}): 1,
    frozenset({'a', 'c', 'd', 'e', 'g'}): 2,
    frozenset({'a', 'c', 'd', 'f', 'g'}): 3,
    frozenset({'b', 'c', 'd', 'f'}): 4,
    frozenset({'a', 'b', 'd' ,'f', 'g'}): 5,
    frozenset({'a', 'b', 'd', 'e', 'f', 'g'}): 6,
    frozenset({'a', 'c', 'f'}): 7,
    frozenset({'a', 'b', 'c', 'd', 'e', 'f', 'g'}): 8,
    frozenset({'a', 'b', 'c', 'd', 'f', 'g'}): 9
}
UNIQUE_NUMS = [1,4,7,8]
NONUNIQUE_NUMS = [0,2,3,5,6,9]

### PART 1 ###
count = 0
outputs = [x for o in output for x in o[o.index('|')+1:]]
outputs_len = Counter(list(map(lambda x: len(x), outputs)))
for num in UNIQUE_NUMS:
    count += outputs_len[NUM_SEGMENTS[num]]
print(count)

### PART 2 ###
def clear_singles(all_possibilities):
    singles = set()
    cleared = set()
    while True:
        for segment in all_possibilities:
            if segment not in cleared and len(all_possibilities[segment]) == 1:
                singles.add(segment)

        if len(singles) == 0:
            return all_possibilities

        for s in singles:
            for segment in all_possibilities:
                if s != segment:
                    all_possibilities[segment].discard(list(all_possibilities[s])[0])
        cleared = cleared.union(singles)
        singles = set()

def check_all_singles(all_possibilities):
    return all(list(map(lambda x: len(x) == 1, all_possibilities.values())))

inputs = [o[:o.index('|')] for o in output]
outputs = [o[o.index('|')+1:] for o in output]
count = 0

for index in range(len(inputs)):
    input_lens = defaultdict(set)
    for i in inputs[index]:
        input_lens[len(i)].add(i)

    # dict matching signal wires (input) -> display segments (output)
    all_possibilities = dict()
    for segment in ALL_SEGMENTS:
        all_possibilities[segment] = ALL_SEGMENTS.copy()

    input_matches = dict()
    for num in NUM_SEGMENTS:
        input_matches[num] = input_lens[NUM_SEGMENTS[num]]

        if num in UNIQUE_NUMS:
            # input can only be segments corresponding to actual segment outputs
            for segment in input_matches[num]:
                all_possibilities[segment] = all_possibilities[segment].intersection(SEGMENTS[num])

    while not check_all_singles(input_matches):
        clear_singles(input_matches)
        for num in NONUNIQUE_NUMS:
            if len(input_matches[num]) != 1:
                for i in input_matches[num]:
                    

    # assign unique nums first
    # for num in UNIQUE_NUMS:
        # print(num, SEGMENTS[num], input_lens[NUM_SEGMENTS[num]][0])
        # input_matches[num] = input_lens[NUM_SEGMENTS[num]][0]
        # input_lens[NUM_SEGMENTS[num]] = []

    # while list(input_matches.keys) != UNIQUE_NUMS + NONUNIQUE_NUMS:
    #     num_possibilities =
    #     # for rest of nums, can only assign if all char still possible
    #     for num in NONUNIQUE_NUMS:


    while not check_all_singles(all_possibilities):
        


        clear_singles(all_possibilities)
    
    output_digits = []
    for o in outputs[index]:
        output_decode = set()
        for segment in o:
            output_decode.add(list(all_possibilities[segment])[0])
        output_digits.append(str(SEGMENTS_REVERSE[frozenset(output_decode)]))
    count += int(''.join(output_digits))

print(count)


# all_possibilities = {'d': 'a', 'e': 'b', 'a': 'c', 'f': 'd', 'g': 'e', 'b': 'f', 'c': 'g'}
# outputs[index] = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]