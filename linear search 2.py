a=[20,30,40,50]
print(a)
element=eval(input("Enter the element to be found"))
for i in a:
	if i==element:
		print("element found at",a.index(i))
else:
	print("element not found")