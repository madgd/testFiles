#generate helix Matrix of N width
import sys
N = 5
if len(sys.argv) > 1:
    N =int(sys.argv[1])

#by recursion
#p:start number N:width m:start position of the Matrix A:Matrix array
#if N >= 3,generate the edges and the N-2 Matrix in the centre
def helix_recursion(p, N, m, A):
    if N == 1:
        A[m][m] = p
    elif N == 2:
        A[m][m] = p
        A[m][m + 1] = p + 1
        A[m + 1][m] = p + 1
        A[m + 1][m + 1] = p + 1
    else:
        i = m
        j = m
        for j in range(m, m + N):
            A[i][j] = p
            p = p + 1
        for i in range(m + 1, m + N):
            A[i][j] = p
            p = p + 1
        for j in range(m + N - 2, m - 1, -1):
            A[i][j] = p
            p = p + 1
        for i in range(m + N - 2, m, -1):
            A[i][j] = p
            p = p + 1
        helix(p, N - 2, m + 1, A)

#generate elements directly
#
#def calculate(n, i, j)

#by iteration
def helix_iteration(N, A):
    #increasing direction
    direction = 0
    #march steps
    #for 5 width, the steps are: 5 4 4 3 3 2 2 1 1,while the directions are
    #0 1 2 3 0 1 2 3 0
    #stepNow marks current step of the current edge,and stepMax marks the max steps
    stepNow = 1
    stepMax = N
    maxNum = N * N
    num = 1
    i = 0
    j = 0
    while num <= maxNum:
        A[i][j] = num
        #when stepNow meets stepMax, stepMax and direction changes
        if stepNow == stepMax:
            direction = direction + 1
            stepNow = 0
            if direction == 4:
                direction = 0
            if direction & 1:
                stepMax = stepMax -1
        #change marking position in Matrix A accroding to the direction
        if direction == 0:
            j = j + 1
        elif direction == 1:
            i = i + 1
        elif direction == 2:
            j = j - 1
        else:
            i = i - 1

        num = num + 1
        stepNow = stepNow + 1

outA = [[0 for i in range(N)] for j in range(N)]
helix_iteration(N, outA)
#helix_recursion(1, N, 0, outA)
print outA
