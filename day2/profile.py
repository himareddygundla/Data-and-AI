def profile(**data):
    for key,value in data.items():
        print(f"{key}: {value}")
        
name=input("enter name:")
age=int(input("enter the age:"))
phno=input("enter phone number:")
mail=input("enter the email:")
profile(Name=name,Age=age,PhnNo=phno,Email=mail)
