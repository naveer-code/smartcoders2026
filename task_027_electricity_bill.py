u = float(input("Enter electricity units consumed: "))

if u <= 100:
    amt = u * 1.5
elif u <= 200:
    amt = (100 * 1.5) + ((u - 100) * 2.5)
elif u <= 300:
    amt = (100 * 1.5) + (100 * 2.5) + ((u - 200) * 4.0)
else:
    amt = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + ((u - 300) * 5.0)

print(f"Total Electricity Bill: {amt}")
