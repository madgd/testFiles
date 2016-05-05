# -*- coding: utf-8 -*-
import sys

#计算最优分割
def MatrixChainOrder(p):
    n = len(p) - 1
    m = [[0 for i in xrange(n)] for j in xrange(n)]
    # print m
    s = [[0 for i in xrange(n)] for j in xrange(n)]
    #l is the chain length
    for l in xrange(2, n + 1):
        # i is the start position
        for i in xrange(n - l + 1):
            # j is the end position
            j = i + l - 1
            m[i][j] = 2147483647
            for k in xrange(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

#输出最优分割
def PrintOptimalParen(s, i, j):
    if i == j:
        sys.stdout.write("A"+str(i))
    else:
        sys.stdout.write("(")
        PrintOptimalParen(s, i, s[i][j])
        PrintOptimalParen(s, s[i][j]+1, j)
        sys.stdout.write(")")

#2个矩阵的乘法
def MatrixMultiply(A, B):
    if len(A[0]) != len(B):
        return 0
    else:
        Acolumns = len(A[0])
        Arows = len(A)
        Bcolumns = len(B[0])
        C = [[0 for i in xrange(Bcolumns)] for j in xrange(Arows)]
        for i in xrange(Arows):
            for j in xrange(Bcolumns):
                C[i][j] = 0
                for k in xrange(Acolumns):
                    C[i][j] += A[i][k] * B[k][j]
    return C

#按最优分割顺序进行矩阵链乘法
def MatrixChainMultiply(A, s, i, j):
    if i == j:
        return A[i]
    else:
        return MatrixMultiply(MatrixChainMultiply(A, s, i, s[i][j]), MatrixChainMultiply(A, s, s[i][j]+1, j))

#while True:
    #pin = list(raw_input().split(" "))
    #pin = [int(i) for i in pin]
A = []
A1 = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
A2 = [[1,1],[1,1],[1,1]]
A3 = [[1],[1]]
A4 = [[1,1,1,1]]
A = [A1, A2, A3, A4]
pin = [4,3,2,1,4]
# print pin
M, S = MatrixChainOrder(pin)
print M
print S
PrintOptimalParen(S,0,3)

print MatrixChainMultiply(A, S, 0, 3)
