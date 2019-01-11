def editDistance(str1, str2, M, N): 
    if M==0: 
         return N
    if n==0: 
        return M
    if str1[M-1]==str2[N-1]: 
        return editDistance(str1,str2,M-1,N-1)
    return 1 + min(editDistance(str1, str2, M, N-1),   
                   editDistance(str1, str2, M-1, N),   
                   editDistance(str1, str2, M-1, N-1)   
                   ) 
str1 = "sunday"
str2 = "saturday"
print editDistance(str1, str2, len(str1), len(str2)) 
  
