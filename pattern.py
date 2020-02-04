def pa(n):
    k=int(6)
    for i in range (0,k):
        for j in range (0,i):
            print(" ",end="")
        for l in range(0,k-i):
            print("*",end=" ")
        print("\r")
    for a in range (0,k):
        for b in range(0,k-1-a):
            print(end=" ")
        for c in range (0,a+1):
            print("*",end=" ")
        print("\r")
n=6
pa(n)
