import math_utils

def patient_billing(**args):
    result = ""
    for key, value in args.items():
        if key != "bills":
            result += f"{key}: {value}\n"
        else:
            total = 0
            print("Enter bill amounts:")
            for i in range(value):
                amt = int(input(f"Enter bill {i+1}: "))
                total = math_utils.add(total, amt)
            result += f"Total Bill: {total}\n"
    return result

n = int(input("Enter number of patients: "))
final_report = ""

for i in range(n):
    print(f"\nEnter details of patient {i+1}")

    name = input("Enter patient name: ")
    phone = input("Enter phone number: ")
    masked_phone = phone[:2] + "******" + phone[-2:]

    pid_msg = input("Enter patient ID message (format your:ID1234.info): ")
    patient_id = pid_msg.split(":")[1].split(".")[0]

    bills_count = int(input("Enter number of bills: "))

    final_report += f"\nPatient {i+1} Details:\n"
    final_report += patient_billing(
        Name=name,
        Phone=masked_phone,
        Patient_ID=patient_id,
        bills=bills_count
    )

print("\n--- HOSPITAL BILLING REPORT ---")
print(final_report)

# -------- SEARCH FEATURE --------
search_msg = input("Enter name to search: ")
if name.lower() in search_msg.lower():
    print("Patient name found")
else:
    print("Patient name not found")

print("Position:", search_msg.find(name))

# -------- CALCULATOR --------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

choice = int(input(
    "Choose operation:\n1.Add\n2.Sub\n3.Mul\n4.Div\n"
))

if choice == 1:
    print("Result:", math_utils.add(a, b))
elif choice == 2:
    print("Result:", math_utils.sub(a, b))
elif choice == 3:
    print("Result:", math_utils.mul(a, b))
elif choice == 4:
    print("Result:", math_utils.div(a, b))
else:
    print("Invalid choice")
