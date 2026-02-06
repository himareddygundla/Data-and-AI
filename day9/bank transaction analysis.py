import pandas as pd

# Create data
data = {
    "Transaction_id": [1, 2, 3, 4],
    "Type": ["deposit", "withdrawal", "deposit", "withdrawal"],
    "Amount": [1000, 20000, 300, 3330]
}

# Create DataFrame
df = pd.DataFrame(data)

# Total deposit and withdrawal
total_deposit = df[df["Type"] == "deposit"]["Amount"].sum()
total_withdrawal = df[df["Type"] == "withdrawal"]["Amount"].sum()

# Final balance
final_balance = total_deposit - total_withdrawal

# High value transactions
high_value = df[df["Amount"] > 5000]

print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", final_balance)
print("\nHigh Value Transactions:")
print(high_value)