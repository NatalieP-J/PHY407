from numpy import array,empty,copy,matrix

A0 = array([[0,1,4,1],
           [3,4,-1,-1],
           [1,-4,1,5],
           [2,-2,1,3]], float)

v0 = array([-4,3,9,7],float)
v = copy(v0)
A = copy(A0)
N = len(v)

def pivot(A,v,m,N):
    div = A[m,m]

    pivot = m
    for k in range(m,N):
        if abs(A[k,m]) > abs(div):
            pivot = k
            div = A[k,m]

    A[m,:],A[pivot,:] = copy(A[pivot,:]), copy(A[m,:])
    v[m],v[pivot] = copy(v[pivot]),copy(v[m])
    return A,v,div


# Gaussian elimination
for m in range(N):

    A,v,div = pivot(A,v,m,N)

    # Divide by the diagonal element
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]


# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)

print v0, (matrix(A0)*matrix(x).T).T
