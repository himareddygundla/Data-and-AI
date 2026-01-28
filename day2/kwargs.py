def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_data(name="hima",age=21)