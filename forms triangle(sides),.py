def triangle(a, b, c):   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True
a,b,c=map(int,input().split())
if triangle (a, b, c): 
    print("yes")  
else: 
    print("no")
