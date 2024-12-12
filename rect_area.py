class Rectangle:
    def __init__(self,Length,Breadth):
        self.L=Length
        self.B=Breadth
    def area(self):
        return self.L * self.B
    def perimeter(self):
        return 2*(self.L + self.B)


    def compare(self,other):

         if self.area()== other.area():
             print ("they have same area")
         else:
             print("they have different area")





rect1=Rectangle(Length=10,Breadth=5)
print("The area of the first rectangle is:", rect1.area())
print("The perimeter of a first rectangle is:", rect1.perimeter())

rect2=Rectangle(Length=10,Breadth=5)
print("The area of a second rectangle is:", rect2.area())
print("The perimeter of a second rectangle is", rect2.perimeter())
rect1.compare(rect2)