import sys

def find(total, start, end):
    # print total
    # print 'haha'
    if total == 0:
        return True
    for i in xrange(start, end):
        if aset[i] != 0 or a[i] > total:
            pass
        elif a[i] == total:
            aset[i] = bagNumber
            return True
        else:
            if find(total - a[i], i + 1, end):
                aset[i] = bagNumber
                return True
    return False

n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
a = [int(i) for i in a]
while n:
    a.sort(reverse = True)
    # print a
    aset = [0] * n

    bagNumber = 0
    theMax = 20
    while 0 in aset:

        for i in xrange(n):
            #print theMax
            if aset[i] == 0:
                bagNumber += 1
                if find(theMax - a[i], i+1, n):
                    aset[i] = bagNumber
                    # print bagNumber
                    # print theMax
                    # print aset
                else:
                    bagNumber -= 1
        theMax -= 1

    # print theMax
    # print aset
    print bagNumber

    n = int(sys.stdin.readline())
    a = sys.stdin.readline().split()
    a = [int(i) for i in a]
