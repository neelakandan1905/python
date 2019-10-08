def norepeat(values, n): 

	for i in range(n):
		j = 0
		while(j < n):
			if (i != j & values[i] == values[j]): 
				break
			j += 1
		if (j == n): 
			return values[i] 

	return -1
a= int(input())
values= list(map(int,input().split()))
n = len(values)
print(norepeat(values, n))
