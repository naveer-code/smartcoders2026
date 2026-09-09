v = int(input("Enter integer: "))

if v > 0:
    tag = "Even" if (v % 2 == 0) else "Odd"
    print(f"Positive and {tag}")
elif v < 0:
    print("Negative")
else:
    print("Zero")
