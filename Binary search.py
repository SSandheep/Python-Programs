a=[20,30,40,50,60,70,89]
print(a)
search=eval(input("enter a element to search:"))
start=0
stop=len(a)-1
while(start<=stop):
	mid=(start+stop)//2
	if(search==a[mid]):
		print("element found at",mid)
		break
	elif(search<a[mid]):
		stop=mid-1
	else:
		start=mid+1
else:
	print("not found")
