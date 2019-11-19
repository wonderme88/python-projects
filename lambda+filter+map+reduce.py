from functools import reduce

def is_even(n):
	return n%2==0

list1 = [3,2,6,8,4,6,2,9]

even1 = filter(is_even,list1)
print even1

# Using lambda instead of funcation
even2 = filter(lambda n: n%2==0,list1)
print even2


double = map( lambda n: n*2, even2)
print double

sum1 = reduce( lambda a,b : a+b, double)
print sum1
