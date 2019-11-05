
f=int(input("Enter any number to find factorial: "))

fact =1
if f>0:
	for i in range(1,f+1):
		fact=fact*i

	print ("factorial of " , f, "is ", fact)

else:
	print("Enter a valid no")
	
