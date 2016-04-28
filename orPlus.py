'''
给定 x, k ，求满足 x + y = x | y 的第 k 小的正整数 y 。 | 是二进制的或(or)运算，例如 3 | 5 = 7。
比如当 x=5，k=1时返回 2，因为5+1=6 不等于 5|1=5，而 5+2=7 等于 5 | 2 = 7。

输入描述:
每组测试用例仅包含一组数据，每组数据为两个正整数 x , k。 满足 0 < x , k ≤ 2,000,000,000。
输出描述:
输出一个数y。

输入例子:
5 1
输出例子:
2
'''

#用二进制位运算处理，根据x确定必须是0的位，把k的每一位按原来的顺序插入到不是0的位置
import sys

[x, k] = sys.stdin.readline()[:-1:].split(" ")


xList = list(bin(int(x))[2::])
kList = list(bin(int(k))[2::])
cannotSetOne = []
for i in range(len(xList)):
	if xList[-i-1] == '1':
		cannotSetOne.append(i)

res = ''

j = 0
while kList:
	if j in cannotSetOne:
		res = '0' + res
	else:
		res = kList.pop() + res
	j += 1

print int(res, 2)
