# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @my_decorator
# def hello():
#     print("Hello World")

# hello()



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        result = func(*args, **kwargs)
        print("Function has finished")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b
print(add(3, 5))


# decorator with parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet():
    print("Hello!")
greet()