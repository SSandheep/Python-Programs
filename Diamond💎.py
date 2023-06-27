num=int(input("Enter no. of rows:"))
for i in range(1,num+1):
	print(" " *(num-i)+" *"*i)
for i in range(num-1,0,-1):
	print(" " *(num-i)+" *"*i)