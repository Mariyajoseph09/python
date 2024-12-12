class Student:
    tutor = "Amalu"  # Class variable

    def __init__(self, N, A):
        self.name = N
        self.age = A

    def display(self):
        print("Student name:", self.name)
        print("Age is:", self.age)
        print("Tutor name:", Student.tutor)  # Correct way to access class variable

    def compare(self, other):
        if self.age == other.age:
            print(f"{self.name}'s age {self.age} and {other.name}'s age {other.age} have the same age.")
        else:
            print(f"{self.name} and {other.name} have different ages.")

# Creating student objects
s1 = Student("Mariya", 21)
s1.display()

s2 = Student("Sreerage", 21)
s2.display()

s3 = Student("Sinu", 25)
s3.display()

# Comparing ages between students
s1.compare(s2)
s2.compare(s3)
