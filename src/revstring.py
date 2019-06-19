

# This program is to reverse the string
def revStr(value):
	return value[::-1]


str1 = "my name is chanchal"
str2 = "birender"
str3 = "chanchal"

#print revStr(str1)


list = []

list.append(str1)
list.append(str2)
list.append(str3)

print (list)

for x in list:
	print revStr(x)


