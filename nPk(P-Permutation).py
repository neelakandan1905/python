import math
n,k=map(int,input().split())
x=math.factorial(n)
y=n-k
z=math.factorial(y)
print(int(x/z))
