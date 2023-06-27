a=0
b=1
n=eval(input("Enter the number of terms:"))
print("Fibonacci series:")
print(a,b)
for i in range(1,n,1):
	c=a+b
	print(c)
	a=b
	b=c