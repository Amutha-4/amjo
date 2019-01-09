A=[]
N=int(input("Enter number of elements:"))
for i in range(1,N+1):
    b=int(input("Enter element:"))
    A.append(b)
A.sort()
print("Largest element is:",A[N-1])a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])
