from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance   

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"


class FixedAccount(BankAccount):
    def account_type(self):
        return "Fixed Account"


#  Customer Details
name = input("Enter customer name: ")
acc_no = input("Enter account number: ")
choice = input("Enter account type (S/F): ")
balance = float(input("Enter initial balance: "))

if choice.lower() == 's':
    account = SavingsAccount(name, acc_no, balance)
else:
    account = FixedAccount(name, acc_no, balance)

print("\nAccount Created Successfully!")
print("Account Type:", account.account_type())

while True:
    print("\n------ BANK MENU ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif option == '2':
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif option == '3':
        print("Current Balance:", account.get_balance())

    elif option == '4':
        print("Thank you for using our bank")
        break

    else:
        print("Invalid choice! Try again.")