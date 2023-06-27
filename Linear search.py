a=[20,30,40,50,60,70,89]
print(a)
search=eval(input("enter a element to search:"))
for i in range(0,len(a),1):
	if search==a[i]:
		print("element found at",i)
		break
else:
	print("not found")

	