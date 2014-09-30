from numpy import array,empty,copy

# This code takes a set of simulatenous linear equations in the form of Ax = v
# (where A is a matrix, and x and v are vectors) and solves for x

# A function to perform partial pivoting for the Gaussian elimination
def pivot(A,v,m,N):
    # Start by assuming there is no need for partial pivoting
    div = A[m,m]
    pivot = m

    # Check subsequent rows to see if the mth column item in that row
    # is further from zero than the mth column item in the current row
    # If yes, update the div value and pivot number to that row
    
    for k in range(m,N):
        if abs(A[k,m]) > abs(div):
            pivot = k
            div = A[k,m]

    # Swap the rows in matrix A and vector v from the current to pivot row
    A[m,:],A[pivot,:] = copy(A[pivot,:]), copy(A[m,:])
    v[m],v[pivot] = copy(v[pivot]),copy(v[m])
    return A,v,div

# Function to perform Gaussian elimination that relies on pivot
def gausselim(A,v):
    N = len(v)

    for m in range(N):
        # Call pivot to pivot the matrix and vector if necessary
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
    return x

# Set matrix and resultant vector
A = array([[ 2,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]], float)
v = array([ -4, 3, 9, 7 ],float)

# Call gausselim to find x such that Ax = v 
x = gausselim(A,v)

print 'x =',x
