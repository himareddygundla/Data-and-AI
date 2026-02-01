# class Student:
#     def hello(self):
#         print("Hello,I am a student")
# s1=Student()
# s1.hello()


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        # print("Hello,I am a student")
        print(f"Name:{self.name},Age:{self.age}")
name=input("Enter name:")
age=int(input("Enter age:"))
s1=Student(name,age)  
s1.display()      
