class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eating")
    
class Mammal(Animal):
    def walk(self):
        print("walking")
        
class Fish(Animal):
    def swim(self):
        print("Swimming")
        
m = Mammal()
m.eat()
m.walk()
print(m.age + 1)

f = Fish()
f.eat()
f.swim()
print(f.age +4)

print(isinstance(m, Mammal))