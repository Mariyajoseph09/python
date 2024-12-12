class Animal:
    def speak(self):
        print("Josiya is a marapatty")
class Bird:
     def Sing(self):
         print("Srekku is a vayakkali")
class Sparrow(Animal,Bird):
    pass
sparrow= Sparrow()
sparrow.speak()
sparrow.Sing()