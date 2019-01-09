a=[]
N=int(input("Enter number of elements:"))
for i in range(1,N+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[N-1])
