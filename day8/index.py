# import threading
# import time
# # def say_hello():
# #     print("hello world")

# # t=threading.Thread(target=say_hello)
# # t.start()

# # print("MAin Thread")

# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("Program finished")

# why we need a threading
# one task is waiting(like downloading,sleeping,input/output) and for program to stay responsive
# ex: downloading a file,showing progress,accepting user input

#passing arguments to thread

# import threading
# def greet(name):
#     print("Hello,{name}!")
# t=threading.Thread(target=greet,args=("Alice",))
# t.start()


import time
def greet(name):
    time.sleep(2)   
    print(f"Hello, {name}!")

greet("Alice")




# multiple threading
import threading
def worker(num):
    print(f"Worker {num} is running")
    time.sleep(1)
    print(f"Worker {num} has finished")
    
for i in range(5):
    t=threading.Thread(target=worker,args=(i,))
    t.start()
    

