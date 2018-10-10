def word count (str):
counts=dict()
word=str.split()
for word in words:
  if word in counts:
    counts[word]+=1
  else:
    counts[word]=1:
return counts
print(word_count("the quike brownfox jumps over lazy dog:"))
