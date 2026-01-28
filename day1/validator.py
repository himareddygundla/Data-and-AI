email = input("Enter email")
password = input("Enter password")
if "@" not in email:
    print("invalid email")
elif (len(password)<6):
    print("invalid password")
else:
    print("valid credentials")