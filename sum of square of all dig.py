a=int(input())
var1=0
while(a>0):
  dig=a % 10
  var1+= (dig**2)
  a//=10
print(var1)
