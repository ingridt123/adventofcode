import sys
from utils import getFilename, readFile
import math
import functools
import operator

filename = getFilename(sys.argv)
output = readFile(filename, str)


### PART 1 ###

result1 = []
result1.append(int(output[0]))
result1.append([int(o) for o in output[1].split(",") if o != 'x'])

minWait = math.inf
minBus = -1
for r in result1[1]:
    wait = r - (result1[0] % r)
    if wait < minWait:
        minWait = wait
        minBus = r

print(minWait * minBus)                                             # 3385


### PART 2 ###

# find modulo inverse of a with respect to m using extended Euclid Algorithm
# source: https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
# see also https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def inv(a, m) : 
      
    m0 = m 
    x0 = 0
    x1 = 1
  
    if (m == 1) : 
        return 0
  
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m
        t = m 
  
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t 
      
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0 
  
    return x1 


result2 = [int(o) if o != 'x' else o for o in output[1].split(",")]

# if not 'x', need to depart at index after t
# t % result2[index] = (result2[index] - index) % result2[index] for all numbers

# let m = result2[index]
#     r = (result2[index] - index) % result2[index] = (r - index) % r
# so t % r = m
#    t ≡ m (mod r)
# use Chinese Remainder Theorem to solve for t
m = []
r = []
for index in range(len(result2)):
    if result2[index] != 'x':
        m.append(result2[index])
        r.append((result2[index] - index) % result2[index])

M = functools.reduce(operator.mul, m, 1)
y = [M // m_i for m_i in m]
z = [inv(y[i], m[i]) for i in range(len(m))]

print(sum([r[i] * y[i] * z[i] for i in range(len(m))]) % M)         # 600689120448303

