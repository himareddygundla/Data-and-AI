mydic={"key1":"value1","key2":"value2"}
print(type(mydic))
trip={
    "provider":"uber",
    "source":"pondicherry",
    "destination":"chennai airport",
    "fare":3500.00,
    "status":"completed"
}
print(trip["provider"])
print(trip.get("source"))
print(trip.keys())
print(trip.values())

for key,value in trip.items():
    print(f"Key:{key},Value:{value}")
    
trip.update({"status":"completed"})
print(trip)
trip.pop("status")
print(trip)

trip["fare"]=4000.0
print(trip)

for key in trip:
    print(key,"->",trip[key])