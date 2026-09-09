c_price = float(input("Enter cost price: "))
s_price = float(input("Enter selling price: "))

diff = s_price - c_price
if diff > 0:
    print(f"Profit: {diff}")
elif diff < 0:
    print(f"Loss: {abs(diff)}")
else:
    print("No Profit No Loss")
