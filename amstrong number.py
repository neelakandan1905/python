num = int(input("InputNumber"))
l=str(num)
length=len(l)
sum = 0
temp = num
while (temp > 0):
   digit = temp % 10
   sum += digit ** length
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
