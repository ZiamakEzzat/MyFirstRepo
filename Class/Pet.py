class Pet:
    name = None


    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('Hello my name is ' + self.name)
        self.foo()

    def foo(self):
        print('foo')

class Complex():

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, c):
        r = self.r + c.r
        i = self.i + c.i
        return Complex(r,i) 



dog = Pet('dog')
cat = Pet('cat')

#dog.introduce()
#cat.introduce()

x = Complex(3,-1.4)
y = Complex(2, -5)


z = x.add(y)

print(x.r, x.i)
print(y.r, y.i)
print(z.r, z.i)
