flag=0
for i in range(0,3):
    password=input("enter your password:")
    if (password=="1234"):
        print("correct")
        flag=1
        break
    elif(i<2):
        print(f"incorrect.try again.{3-i-1} attempts left")
if(flag==0):
    print("your account got locked")        
    
        