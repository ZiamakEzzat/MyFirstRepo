def test():
    return 5

#add([10,20,30],[1,2,3]) ==> [11,22,33]
#x1+x2
def add(x1, x2):
	c=[]
	if len(x1) == len(x2):
		for a, b in zip(x1, x2):
			c.append(a+b)
	else:
		return [False]
	return c
	
#x1 - x2
def sub(x1, x2):
    
	c=[]
	if len(x1) == len(x2):
		for a, b in zip(x1, x2):
			c.append(a-b)
	else:
		return [False]
	return c
   

#print(add([10,20,30],[1,2,3]))

####

l = ['a','b','c']

print(l[0],l[1],l[2])
#print(add(x1,x2))