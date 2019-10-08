import math
n,k=map(int,input().split())
x=(math.factorial(n))
y=(math.factorial(k))
z=(math.factorial(n-k))
b=y*z
print(int(x/b))
