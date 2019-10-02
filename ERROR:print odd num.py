n= input()
l=list(n)
c=0
for i in l:
  if int(i)%2!=0:
        print(i,end=" ")
  elif int(i)%2==0:
        c=c+1
if len(l)==c:
  print(-1)
