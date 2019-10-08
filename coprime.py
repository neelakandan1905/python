def gcd(a, b): 
	if (a == 0 or b == 0): return 0
	if (a == b): return a
	if (a > b):
		return gcd(a - b, b)
			
	return gcd(a, b - a) 
def coprime(a, b): 
	
	if ( gcd(a, b) == 1): 
		print("yes") 
	else: 
		print("no")
m,n =map(str,input().split())
s =len(m); x = len(n)
coprime(s, x)
