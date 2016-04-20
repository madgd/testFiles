# -*- coding:utf-8 -*-
#给定字符串，字符串中包含空格，在线性时间O(n)里对它做变形：
#1.把这个字符串由空格隔开的单词反续
#2.反转每个字符的大小写

def trans(s, n):
    # write code here
    out = []
    temp = ''
    for i in range(n):
        if s[i].isupper():
            temp = temp + s[i].lower()
        elif s[i].islower():
            temp = temp + s[i].upper()
        elif s[i] == ' ':
            out.append(temp)
            temp = ''
    for i in range(len(out)-1, -1, -1):
        temp = temp + ' ' + out[i]
    return temp

while True:
    s = str(raw_input())
    n = int(raw_input())
    print trans(s,n)
