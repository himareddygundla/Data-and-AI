recharge=int(input("enter recharge price:"))
data=int(input("enter daily data:"))
if(recharge>399 and data>2):
    print("get bonus")
else:
    print("no bonus")