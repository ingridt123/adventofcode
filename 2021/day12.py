from utils import getFilename, readFile

filename = 'day12.txt'
output = readFile(filename, str, sepChar='\n')
output = [o.split('-') for o in output]

### PART 1 ###
class Cave:
    def __init__(self, name):
        self.name = name
        self.adj = set()
        self.large = name.isupper()
        self.start = name == 'start'

    def add_adj(self, cave_name):
        self.adj.add(cave_name)

    def __repr__(self):
        return self.name + "--" + str(self.adj)

def find_all_paths1(cave, path, caves_dict):     # cave = , path = [start, b, A, c, A, end]
    if cave == 'end':
        return [path]

    paths = []
    for adj_cave in caves_dict[cave].adj:       # adj_cave = 'end'
        if caves_dict[adj_cave].large or adj_cave not in path:
            new_paths = find_all_paths1(adj_cave, path + [adj_cave], caves_dict)
            paths += new_paths
        # rest_of_paths = [[c,A,end]]

    return paths

caves = set([cave for o in output for cave in o])
caves_dict = dict()
for cave in caves:
    caves_dict[cave] = Cave(cave)
for cave1, cave2 in output:
    caves_dict[cave1].add_adj(cave2)
    caves_dict[cave2].add_adj(cave1)
# print(caves_dict)

print(len(find_all_paths1('start', ['start'], caves_dict)))


### PART 2 ###
def find_all_paths2(cave, path, small_revisited, caves_dict):
    if cave == 'end':
        return [path]

    paths = []
    for adj_cave in caves_dict[cave].adj:
        new_paths = []
        if caves_dict[adj_cave].large or adj_cave not in path:
            new_paths = find_all_paths2(adj_cave, path + [adj_cave], small_revisited, caves_dict)
        elif not small_revisited and not caves_dict[adj_cave].start:
            new_paths = find_all_paths2(adj_cave, path + [adj_cave], True, caves_dict)
        paths += new_paths

    return paths

print(len(find_all_paths2('start', ['start'], False, caves_dict)))