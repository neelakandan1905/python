n=int(input())
var1=0
while(n>0):
  dig=n % 10
  var1+= dig
  n//=10
if(var1%3==0):
  print("Yes")
else:
  print("Not")
