#generate a new line which everybody cant stay in his previous position,
#count how many possible lines in m
#n is the length of the line
n = int(raw_input())
def countPossibilities(n):
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
    return m

#recursion formula
def recursionSolution(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    aNminus2 = 0
    aNminus1 = 1
    i = 3
    while i <= n:
        aN = (i - 1) * (aNminus2 + aNminus1)
        aNminus2 = aNminus1
        aNminus1 = aN
        i = i + 1
    return aN

print recursionSolution(n)
