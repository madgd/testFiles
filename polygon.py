import sys

n = int(sys.stdin.readline())

def judge(listOfedge):
    leng = len(listOfedge)
    data = [0 for i in range(leng)]
    total = 0
    for i in range(leng):
        total += int(listOfedge[i])
        print total
    for i in range(leng):
        if total - int(listOfedge[i]) * 2 <= 0:
            return False
    return True
edgeList = []
for i in range(n):
    rawdata = sys.stdin.readline()[:-1:].split(" ")
    if int(rawdata[0]) == 1:
        edgeList.append(rawdata[1])
    else:
        edgeList.remove(rawdata[1])
    print edgeList
    if judge(edgeList):
        print "Yes"
    else:
        print "No"
