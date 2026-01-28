list=[]
while True: 
    str=input("enter the item:")
    if(str!="done"):
        list.append(str)
    else:
        break
for i in list:
    print(i)