class rectangle:
    def __init__(self,len,b):
        self.length=len
        self.breadth=b
    def area (self):
        return(self.len*self.b)
    def perimeter(self):
        return(2*self.len+self.b)
r1.rectangle(5,3)
r2.rectangle(5,8)
print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r2.perimeter())