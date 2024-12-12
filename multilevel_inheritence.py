class Animal():
    def Speak(self):
        print("A cat is a small, carnivorous mammal that is widely kept as a pet")
class Cat(Animal):
    def Bark(self):
        print("MEOWWWWW!!!!!Cats meow to communicate with humans, often to get attention, express hunger, or show affection.")
class Kitten(Cat):
    def meow(self):
        print("mariya loves kittens")



kitten = Kitten()
kitten.Speak()
kitten.Bark()
kitten.meow()
