places = {"Airport", "Railway Station", "Mall", "Hospital", "College", "Bus Stand"}

drivers = [
    {"name": "Ravi", "status": "available"},
    {"name": "Anil", "status": "available"},
    {"name": "Suresh", "status": "waiting"}
]

def calculate_cost(**kwargs):
    base_fare = kwargs.get("base_fare", 50)
    distance = kwargs.get("distance", 1)
    cost_per_km = kwargs.get("cost_per_km", 15)
    return base_fare + (distance * cost_per_km)

def calculate_eta(**kwargs):
    distance = kwargs.get("distance", 1)
    avg_speed = kwargs.get("avg_speed", 40)  
    eta = (distance / avg_speed) * 60  
    return round(eta)

print("Available Places:")
for p in places:
    print("-", p)

pickup = input("\nEnter Pickup Location: ")
drop = input("Enter Drop Location: ")

if pickup not in places or drop not in places:
    print("Invalid pickup or drop location!")
    exit()

assigned_driver = None
for d in drivers:
    if d["status"] == "available":
        assigned_driver = d
        d["status"] = "waiting"
        break

if not assigned_driver:
    print("No drivers available at the moment!")
    exit()

distance = int(input("Enter distance in km: "))

ride_status = "Waiting"

print("\n🚗 Driver Assigned!")
print("Driver Name   :", assigned_driver["name"])
print("Driver Status :", assigned_driver["status"])
print("Ride Status   :", ride_status)

ride_status = "Ride Started"
assigned_driver["status"] = "on trip"

eta = calculate_eta(distance=distance)

print("\n Ride Started")
print("Ride Status   :", ride_status)
print("Estimated Time:", eta, "minutes")

fare = calculate_cost(
    base_fare=50,
    distance=distance,
    cost_per_km=15
)

ride_status = "Completed"
assigned_driver["status"] = "available"

feedback = input("\nPlease give your feedback (Good / Average / Bad): ")

ride_details = {
    "pickup": pickup,
    "drop": drop,
    "driver": assigned_driver["name"],
    "distance": distance,
    "fare": fare,
    "ride_status": ride_status,
    "driver_status": assigned_driver["status"],
    "eta": eta,
    "feedback": feedback
}

invoice = (
    "UBER RIDE INVOICE",
    f"Pickup Location : {ride_details['pickup']}",
    f"Drop Location   : {ride_details['drop']}",
    f"Driver Name     : {ride_details['driver']}",
    f"Driver Status   : {ride_details['driver_status']}",
    f"Ride Status     : {ride_details['ride_status']}",
    f"Distance        : {ride_details['distance']} km",
    f"Estimated Time  : {ride_details['eta']} minutes",
    f"Total Fare      : ₹{ride_details['fare']}",
    f"User Feedback   : {ride_details['feedback']}"
)

print("\nFINAL INVOICE")
print("-" * 35)
for line in invoice:
    print(line)
print("-" * 35)
print("Thank you for riding with Uber!")
