def sas( a, d, n) :
    sum = 0
    i = 0
    while i < n :
        sum +=  a
        a +=  d
        i += 1
    return sum

a,b,c=map(int,input().split())
print (sas(a, b, c))
