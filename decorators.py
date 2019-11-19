

def div(a,b):
	print (a/b)

#div(4,2)   ==> 2
#div(2,4)   ==> 0.5



def smart_div(func):
	def inner(a,b):
		if a<b:
			a,b = b,a   # swapping 
		return func(a,b)
	return inner

div = smart_div(div)
div(2,4)



