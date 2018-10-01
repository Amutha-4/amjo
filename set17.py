sum=0
temp=num
while temp>0:
  digit=temp%10
  sum+=digit**3
  temp
if num==sum:
  print(num,"is an aramstrong number")
else:
  print(num,"is not an aramstrong number")
