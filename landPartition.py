# -*- coding:utf-8 -*-

def getPartition(land, n, m):
    # write code here
    # return [0, 1]
    par = 0
    minWrong = 0
    landtotal = [m for i in range(n)]
    landspe = [0 for i in range(n)]
    for j in range(n):
        for i in range(m):
            landspe[j] = landspe[j] + land[i][j]
        minWrong = minWrong + m - landspe[j]
    temp = minWrong
    for i in range(n):
        temp = temp - m + 2 * landspe[i]
        if temp < minWrong:
            par = i + 1
            minWrong = temp
    return [par, par + 1]

testland = [[0,0,1,1],[0,0,0,0],[0,0,1,1]]
print getPartition(testland, 4, 3)


