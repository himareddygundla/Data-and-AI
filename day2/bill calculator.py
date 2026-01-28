def trip_bills(**args):
    ans=""
    for key,value in args.items():
        if(key!="bills"):
            ans+=f"{key}:{value}\n"
        else:
            sum=0
            print("enter bills:\n")
            for i in range(value):
                sum+=int(input(f"enter bill {i+1}:"))
            ans+=f"Total bill:{sum}\n"
    return ans

n=int(input("enter no of people included:"))
result=""
for i in range(0,n):
    print(f"enter details of person {i+1}")
    nm=input("enter name:")
    num=input("enter phone number:")
    num=num[:2]+"******"+num[-2:]
    bill=int(input("enter no.of bills:"))
    result+=f"\nPerson {i+1} details:\n"
    result+=trip_bills(name=nm,phno=num,bills=bill)
print(result)