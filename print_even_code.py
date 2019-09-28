n= int(input())
if(1<=n & n<=1000):
  for i in range(1,n+1):
      if n % i==0:
          if i%2==0:
              print(i, end = ' ')
