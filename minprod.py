a=[34,22,11,33,44]
b=[]
c=int(input("enter the no of elements"))
for j in range(c):
    ele=int(input())
    b.append(ele)
print(b)
n=len(a)
a.sort()
b.sort(reverse=True)
prod=0
for i in range(0,n):
    prod=prod+(a[i]*b[i])
print(prod)