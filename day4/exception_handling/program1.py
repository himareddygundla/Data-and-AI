# print("step1")
# a=10
# b=20
# result=a/b
# print("step2")
# print("Result is:",result)

try:
    print("step1")
    a=int(input("Enter numerator: "))
    b=int(input("Enter denominator: "))
    result=a/b
    print("step2")
    print("Result is:",result)
except Exception as e:
    print("Error:Division by zero is not allowed")
finally:
    print("Execution completed")