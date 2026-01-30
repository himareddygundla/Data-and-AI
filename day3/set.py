# myset={1,2,3,4,5,6}
# print(myset)

# uber={"Hyd","Mumbai","Bangalore","pondicherry","pune","delhi"}
# uber.add("gurgaon")
# print(uber)
# list_uber=list(uber)
# print(list_uber)

uber1={"Hyd","Mumbai","Bangalore","pune","delhi"}
uber2={"Calcutta","Hyd","delhi"}
print(uber1.union(uber2))
print(uber1.intersection(uber2))
print(uber1.difference(uber2))

uber1.add("gurugram")
print(uber1)
uber1.remove("gurugram")
print(uber1)