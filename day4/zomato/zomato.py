print("MENU:\n1. Pizza - ₹120 per item\n2. Burger - ₹80 per item\n3. Pasta - ₹100 per item\n4.Biryani - ₹250\n")

PRICE_PER_ITEM = 0
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    PRICE_PER_ITEM = 120 
elif choice == 2:
    PRICE_PER_ITEM = 80
elif choice == 3:
    PRICE_PER_ITEM = 100   
elif choice == 4:
    PRICE_PER_ITEM = 250 
else:
    print("Invalid choice! Please select a valid option.")
    exit()

try:
    items = int(input("How many items do you want to order? "))

    if items == 0:
        raise ZeroDivisionError("Zero items not allowed")

    total_bill = items * PRICE_PER_ITEM

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("You cannot order 0 items.")

else:
    print(f"Order placed successfully!")
    print(f"Total bill: ₹{total_bill}")

finally:
    print("Thank you for using Zomato!")