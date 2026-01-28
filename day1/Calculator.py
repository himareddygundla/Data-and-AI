def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter your choice (1-add, 2-subtract, 3-multiply, 4-division): "))

if c == 1:
    print(add(a, b))
elif c == 2:
    print(subtract(a, b))
elif c == 3:
    print(multiply(a, b))
elif c == 4:
    print(division(a, b))
else:
    print("Invalid choice")
