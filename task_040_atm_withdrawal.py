acct_bal = float(input("Enter current balance: "))
amt_req = float(input("Enter withdrawal amount: "))
min_limit = 500.0

if amt_req <= 0:
    print("Invalid amount")
elif acct_bal - amt_req >= min_limit:
    print(f"Withdrawal approved. Remaining balance: {acct_bal - amt_req}")
else:
    print(f"Withdrawal rejected: Insufficient funds or violates minimum balance of {min_limit}")
