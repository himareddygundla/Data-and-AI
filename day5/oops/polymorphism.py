# Method overloading
class Demo: 
    def add(self,*args):
        if len(args)==2:
            print("Addition:",args[0]+args[1])
        elif len(args)==3:
            print("Addition:",args[0]+args[1]+args[2])
obj=Demo()
# obj.show(2)
# obj.show(2,3)
obj.add(1,2)
obj.add(2,3,4)


# Method overriding
class Animal:
    def sound(self):
        print("Some generic sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meow")
for animal in [Dog(),Cat()]:
    animal.sound()

