def merge(A, p, q, r):
    L = A[p:q+1:]
    R = A[q+1:r+1:]
    L.append(2147483648)
    R.append(2147483648)
    i = 0
    j = 0
    for k in xrange(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        print p,r,q
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

A = [2,4,5,7,1,2,3,6]
mergeSort(A, 0, len(A)-1)
print A
