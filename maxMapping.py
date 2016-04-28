'''
有 n 个字符串，每个字符串都是由 A-J 的大写字符构成。现在你将每个字符映射为一个 0-9 的数字，不同字符映射为不同的数字。这样每个字符串就可以看做一个整数，唯一的要求是这些整数必须是正整数且它们的字符串不能有前导零。现在问你怎样映射字符才能使得这些字符串表示的整数之和最大？

输入描述:
每组测试用例仅包含一组数据，每组数据第一行为一个正整数 n ， 接下来有 n 行，每行一个长度不超过 12 且仅包含大写字母 A-J 的字符串。 n 不大于 50，且至少存在一个字符不是任何字符串的首字母。
输出描述:
输出一个数，表示最大和是多少。

输入例子:
2
ABC
BCA
输出例子:
1875
'''
#统计每个字母出现的次数，例：如果A出现在百位，则加100个A
import sys

countDict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
notZero ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
n = int(sys.stdin.readline())

for i in range(n):
    base = 1
    data = sys.stdin.readline()
    for j in range(len(data)-1):
        countDict[data[-j-2]] += 1 * base
        base = base * 10
    notZero[data[-j-2]] = 1

items = countDict.items()
backitems=[[v[1],v[0]] for v in items]
backitems.sort()


setZero = False
assign = 1
total = 0
assignZero = ''
for i in backitems:
    if not setZero:
        if not notZero[i[1]]:
            assignZero = i[1]
            setZero = True
            break

for i in backitems:
    if i[1] != assignZero:
        total += countDict[i[1]] * assign
        assign += 1

print total
