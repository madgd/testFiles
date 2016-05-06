# -*- coding: utf-8 -*-
import sys

#计算lcs长度
def lcsLength(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for i in xrange(n)] for j in xrange(m)]
    c = [[0 for i in xrange(n+1)] for j in xrange(m+1)]

    for i in xrange(m):
        for j in xrange(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i][j] = 3 #
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 2 #
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = 1 #
    return c,b

#构造lcs
def printLcs(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == 3:
        printLcs(b, X, i-1, j-1)
        sys.stdout.write(X[i])
    elif b[i][j] == 2:
        printLcs(b, X, i-1, j)
    else:
        printLcs(b, X, i, j-1)

while True:
    X = raw_input()
    Y = raw_input()
    C, B = lcsLength(Y, X)
    #print C
    #print B
    print C[-1][-1]
    printLcs(B, Y, len(Y)-1, len(X)-1)
    print
