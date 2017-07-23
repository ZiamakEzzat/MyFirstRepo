#int x = 10 

def help(x):
	print(x)
	print(type(x))


x = 10
y = 10.0
z = 'hello'
u = False

l = [x,y,z,u]
l2 = [x]
for i in l2:
	help(i)



#LOOPS

while False:
	print(x)
	x = x + 1
	if x > 15:
		break	


def foo():
	print('foo')

def bar():
	print('bar')

l3 = ['a', 'b', 'c', 2, 'e' , 'f', 'g', 'h']
l4 = [foo, bar, print]
print(l4)
for f in l4:
	f()

#for var in l3[:-1]:
#	print(var)

l51 = list(range(0,10))
l52 = list(range(13,17))
l53 = list(range(20,37,2))
l5 = [l51, l52, l53]
label = ['One','Two','Three']

for y,l in zip(label,l5):
	print('List '+y,l)

#print(zip(l5,l))
