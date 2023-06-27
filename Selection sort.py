a=input("Enter list:").split()
a=list(map(eval,a))
for i in range(0,len(a)):
	smallest=min(a[i:])
	sindex=a.index(smallest)
	a[i],a[sindex]=a[sindex],a[i]
print(a)