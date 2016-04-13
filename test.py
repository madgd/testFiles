#generate a new line which everybody cant stay in his previous position,
#count how many possible lines in m
#n is the length of the line
n = int(raw_input())
m = 0
line = range(n)
from itertools import permutations
nPermutations = list(permutations(line, n))
def hasSame(i):
    for j in line:
        if i[j] == j:
            return True
    return False

for i in nPermutations:
    if not hasSame(i):
        #print i
        m = m + 1
print m
