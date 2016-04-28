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
