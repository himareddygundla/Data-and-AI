import re

text="python is powerful"
result=re.search("powerful",text)
if result:
    print("Match found:",result.group())
        
text="my number is 1234567890 and 9876543210"
# numbers=re.findall("\d{10}",text)
# print(number)

for match in re.finditer("\d{10}",text):
    print("Match found at index:",match.start(),"to",match.end()) 
    
text="my phone number is 1234567890"
masked=re.sub("\d{6}","******",text)
print(masked)