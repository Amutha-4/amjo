def minOps(A, B): 
    M = len(A) 
    N = len(B)  
    if N != M: 
        return -1
  
    count = [0] * 256
  
    for i in xrange(N):      
        count[ord(B[i])] += 1
    for i in xrange(N):      
        count[ord(A[i])] -= 1
    for i in xrange(256):    
        if count[i]: 
            return -1
    res = 0
    i = N-1
    j = N-1    
    while i >= 0:
        while i>= 0 and A[i] != B[j]: 
            i -= 1
            res += 1
        if i >= 0: 
            i -= 1
            j -= 1
  return res 
A = "EACBD"
B = "EABCD"
print "Minimum number of operations required is " + str(minOps(A,B)) 
