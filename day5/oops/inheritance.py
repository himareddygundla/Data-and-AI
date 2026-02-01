# # Single inheritance
# # class Father:
# #     def drive(self):
# #         print("Father can drive")
# # class Son(Father):
# #     def play(self):
# #         print("Son can play")   
# # s1=Son()
# # s1.drive()  
# # s1.play()


# # Multi-Level inheritance
# # class Grandfather:
# #     def wisdom(self):
# #         print("Grandfather shares wisdom")
# # class Father(Grandfather):
# #     def drive(self):
# #         print("Father can drive")
# # class Son(Father):
# #     def play(self):
# #         print("Son can play")   
# # s1=Son()
# # s1.wisdom() 
# # s1.drive()
# # s1.play() 


# # Hierarchical Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
# d1=Dog()
# d1.speak()
# d1.bark()
# c1=Cat()
# c1.speak()
# c1.meow()


# class Mother:
#     def cook(self):
#         print("Mother can cook")
# class Daughter(Mother):
#     def dance(self):
#         print("Daughter can dance") 
# class Son(Mother):
#     def play(self):
#         print("Son can play")

# d1=Daughter()
# d1.cook()       
# s1=Son()
# s1.cook()


#Multiple Inheritance
# class Father:
#     def drive(self):
#         print("Father can drive")
# class Mother:
#     def cook(self):
#         print("Mother can cook")
# class Child(Father, Mother):
#     def play(self):
#         print("Child can play")

# c1=Child()
# c1.drive()
# c1.cook()
# c1.play()


# Hybrid inheritance
class A:
    def method_a(self):
        print("Method A from class A")
class B(A):
    def method_b(self):
        print("Method B from class B")
class C(A):
    def method_c(self):
        print("Method C from class C")
class D(B, C):
    def method_d(self):
        print("Method D from class D")
d1 = D()
d1.method_a()   
d1.method_b()
d1.method_c()
d1.method_d()



# Multiple Inheritance .....
class A:
    def display(self):
        print("Info from A")
        super().display()  

class B:
    def display(self):
        print("Info from B")

class C(A, B):
    pass

obj = C()
obj.display()