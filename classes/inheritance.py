class Animal:
    def eat(self):
        print("eat")
        
class Mammal(Animal):
    def walk(self):
        print("walk")
        
class Fish(Animal):
    def swim(self):
        print("swim")
        

m = Mammal()
m.eat()
m.walk()

f = Fish()
f.eat()
f.swim()