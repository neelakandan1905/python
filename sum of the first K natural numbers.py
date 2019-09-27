def findSum(k):
    sum=0
    x=1
    while(x<=k):
        sum=sum+x
        x=x+1
    return sum
k=int(input())
print(findSum(k))
