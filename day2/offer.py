bill=int(input("enter total bill:"))
goldmem=input("are you a gold member:")
day=input("enter the day:")
if (bill>1000 and goldmem=="yes" and (day=="saturday" or "sunday")):
    print("you will get 20 percent offer")
else:
    print("no offer")