def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in xrange(p, r):
        if A[j] < x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

A = [2,4,5,7,1,2,6,7]
quickSort(A, 0, len(A)-1)
print A
