a=eval(input("enter a value:"))
b=eval(input("enter b value:"))
c=eval(input("enter c value:"))
d=(b*b-4*a*c)
if (d==0):
	print("same and real roots")
elif(d>0):
	print("different real roots")
else:
	print("imaginary roots")
	