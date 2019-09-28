N=int(input())
factorial=1
if(N==0):
    print("1")
elif(1<=N & N<=25):
    for i in range(1,N+1):
        factorial=factorial*i
    print(factorial)
