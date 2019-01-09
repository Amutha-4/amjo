def firstkdigits(N, k): 
  
    product = 1
      
    for i in range(N ): 
        product *= N
    while ((product // pow(10, k)) != 0): 
        product = product // 10
      
    return product 
  
# Driver Code 
N = 15
k = 4
print(firstkdigits(N, k)) 
