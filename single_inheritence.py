class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog is inheriting from Animal
    def bark(self):
        print("Dog barks")

# Creating an object of Dog
dog = Dog()
dog.speak()  # Inherited method from Animal
dog.bark()