def round( n ):
  a = (n // 10) * 10
  b = a + 10
  if(1<=n& n<=10000):
    return (b if n - a > b - n else b)
n = int(input())
print(round(n))
