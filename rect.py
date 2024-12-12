class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

r1=rectangle(5,3)
r2=rectangle(5,8)
print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r2.perimeter())