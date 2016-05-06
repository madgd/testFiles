# -*- coding: utf-8 -*-
#注意区分最长回文子序列和最长回文子串的区别:子序列考虑可以包含间隔,字串必须相连,没有间隔
#“character" 最长子序列为"carac"  最长子串为"ara"

#可以通过对给定字符串求逆序,再求LCS求出
import sys

def lpsLength(X):
    m = len(X)
    b = [[0 for i in xrange(m)] for j in xrange(m)]

    for i in xrange(m):
        b[i][i] = 1
    for i in xrange(1,m):
        for j in xrange(m-i):
            if X[j] == X[j+i]:
                b[j][j+i] = b[j+1][j+i-1] + 2 #两个字符相同,则为前后减去一位的子问题+2
            else:
                b[j][j+i] = max(b[j][j+i-1], b[j+1][j+i]) #两个字符不同,则为两个子问题的最大值
    return b

def printLps(X, b, i, j):
    if j < i: #没有输出
        return
    if i == j: #输出中心字符
        sys.stdout.write(X[i])
        strOut[0] += X[i]
        return

    if b[i][j] == b[i][j-1]:
        printLps(X, b, i, j-1)
    elif b[i][j] == b[i+1][j]:
        printLps(X, b, i+1, j)
    elif b[i][j] == b[i+1][j-1] + 2: #这里找到了需要输出的一对回文字符
        sys.stdout.write(X[i])
        strOut[0] += X[i]
        printLps(X, b, i+1, j-1)
        sys.stdout.write(X[j])
        strOut[0] += X[j]


while True:
    X = raw_input()
    #C, B = lcsLength(Y, X)
    #print C
    #print B
    B = lpsLength(X)
    strOut = ['']
    printLps(X, B, 0, len(X)-1)
    print
    print strOut[0]
