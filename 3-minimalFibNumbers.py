import sys

FibNumbers = [1, 1]

FibmOne = 1
FibmTwo = 1
for i in range(28):
    Fib = FibmOne + FibmTwo
    FibmTwo = FibmOne
    FibmOne = Fib
    FibNumbers.append(Fib)


#print len(FibNumbers)
#print FibNumbers

a = int(sys.stdin.readline())
while a:
    #print a
    n = 1
    for i in range(29, -1, -1):
        #print i
        if FibNumbers[i] > a:
            pass
        elif FibNumbers[i] == a:
            break;
        else:
            a = a - FibNumbers[i]
            n += 1
            #print n
    print n
    a = int(sys.stdin.readline())
