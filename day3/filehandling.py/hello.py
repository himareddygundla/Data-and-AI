file=open("notes.txt","w")
file.write("Welcome to python file handling!\n")
file.write("this is a sample file.\n")
file.close()

file=open("notes.txt","r")
content=file.read()
print(content)
file.close()

file=open("notes.txt","a")
file.write("This line is appended to the file.\n")
file.close()

with open("notes.txt","r") as file:
    content=file.read()
    print(content)
    
    
feedback=input("Please provide your feedback about our service:")
with open("feedback.txt","a") as file:
    file.write(feedback + "\n")
print("Thank you for your feedback!")


with open("data.txt","r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())
    
    
with open("data.txt","r") as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.strip())