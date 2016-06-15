# coding: utf-8
import sys
#分角向上和角向下两种三角形来考虑
#每次增加的三角形数可以看成一个数列，数列是一个差递增数列，num是数列当前项
#total是总的三角形数

while True:
    b = raw_input().split()
    n = int(b[0])
    #print a
    total = 0
    num = 0
    isOdd = n % 2
    for i in range(n + 1):
        num += i
        total += num
        if i % 2 != isOdd:
            total += num
    #print num
    print total
